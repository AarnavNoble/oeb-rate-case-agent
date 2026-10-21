"""Rate-case research agent, run through Claude Code in headless mode (`claude -p`).

Claude Code supplies the tool-use loop and authenticates with the user's own Claude
login (no API key, no separate API billing). Our tools reach it over a stdio MCP server
(oeb.agent.mcp_server). The process runs isolated from the user's Claude Code setup:
no built-in tools, no settings/plugins/CLAUDE.md, no session persistence, and an empty
working directory.

    uv run python -m oeb.agent.agent "What is Toronto Hydro's proposed 2025 capital budget?"
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

from oeb.config import AGENT_MODEL, ROOT
from oeb.db import connect

SYSTEM_PROMPT = """\
You are a research assistant for Ontario Energy Board (OEB) rate cases. You answer questions \
about utility rate applications using only the filings available through your tools:
- EB-2023-0195: Toronto Hydro-Electric System Limited, 2025-2029 custom IR rate application.
- EB-2026-0164: Hydro One Networks Inc., 2028-2032 joint transmission and distribution application.

How to work:
- Search before answering. Try several phrasings, and read the page (fetch_page) before relying on \
a number. Use query_table for figures held in tables; check units and the year columns on the page.
- Every factual claim must end with a citation token copied exactly from a tool result, in the form \
[cite:<doc_id>:<page>]. Cite the specific page that supports the claim; several tokens are fine.
- Never cite a page you have not seen in a tool result. Never invent numbers, exhibits or pages.
- If the filings you can access do not contain the answer, say so plainly ("The filings available \
to me do not state ...") and describe what you did find. Do not guess.
- For comparisons across utilities, put the figures side by side, state each one's basis \
(years, nominal vs real, transmission vs distribution) and point out where they aren't comparable.

Answer in plain prose with short paragraphs or a compact table. Lead with the direct answer.\
"""

CITE = re.compile(r"\[cite:([A-Za-z0-9_\-]+):(\d+)\]")
TOOL_NAMES = ["mcp__oeb__search", "mcp__oeb__fetch_page", "mcp__oeb__query_table"]


@dataclass
class Citation:
    doc_id: str
    page: int
    case_number: str | None = None
    exhibit: str | None = None
    title: str | None = None
    seen: bool = False


@dataclass
class AgentResult:
    answer: str
    citations: list[Citation] = field(default_factory=list)
    tool_calls: list[dict] = field(default_factory=list)
    num_turns: int | None = None
    duration_ms: int | None = None
    usage: dict = field(default_factory=dict)
    cost_usd_equivalent: float | None = None   # Claude Code's estimate; billed to the plan, not the API
    error: str | None = None

    @property
    def unverified_citations(self) -> list[Citation]:
        return [c for c in self.citations if not c.seen]


def _claude_bin() -> str:
    path = shutil.which("claude")
    if not path:
        raise RuntimeError("Claude Code CLI not found on PATH (needed for the agent)")
    return path


def _command(question: str, mcp_config: Path, model: str) -> list[str]:
    return [
        _claude_bin(), "-p", question,
        "--model", model,
        "--system-prompt", SYSTEM_PROMPT,
        "--tools", "",                       # no built-in tools (Bash, Read, WebFetch, ...)
        "--mcp-config", str(mcp_config), "--strict-mcp-config",
        "--allowedTools", ",".join(TOOL_NAMES),
        "--setting-sources", "",             # ignore user/project/local settings (hooks, plugins)
        "--no-session-persistence",
        "--output-format", "stream-json", "--verbose", "--include-partial-messages",
    ]


def run_stream(question: str, doc_kinds: list[str] | None = None, model: str = AGENT_MODEL,
               cases: list[str] | None = None) -> Iterator[dict]:
    """Yields events: {"type": "text", "text"}, {"type": "tool_use", "name", "input"},
    {"type": "tool_result", "is_error", "preview"}, and finally {"type": "done", "result": AgentResult}."""
    with tempfile.TemporaryDirectory(prefix="oeb-agent-") as tmp:
        tmpdir = Path(tmp)
        seen_log = tmpdir / "seen.jsonl"
        seen_log.touch()
        env = {"PYTHONPATH": str(ROOT / "src"), "OEB_SEEN_LOG": str(seen_log)}
        if doc_kinds:
            env["OEB_DOC_KINDS"] = ",".join(doc_kinds)
        if cases:
            env["OEB_CASES"] = ",".join(cases)
        mcp_config = tmpdir / "mcp.json"
        mcp_config.write_text(json.dumps({"mcpServers": {"oeb": {
            "command": str(ROOT / ".venv" / "bin" / "python"),
            "args": ["-m", "oeb.agent.mcp_server"], "env": env}}}))
        workdir = tmpdir / "cwd"  # empty dir: no project CLAUDE.md is discovered
        workdir.mkdir()
        proc_env = {**os.environ, "MCP_TIMEOUT": "120000"}  # MCP server loads the embedding model
        proc_env.pop("ANTHROPIC_API_KEY", None)  # use the Claude Code login, never an API key

        proc = subprocess.Popen(_command(question, mcp_config, model), cwd=workdir, env=proc_env,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        assert proc.stdout is not None
        tool_calls: list[dict] = []
        final: dict | None = None
        streamed_text = []
        for line in proc.stdout:
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            kind = ev.get("type")
            if kind == "stream_event":
                inner = ev.get("event", {})
                delta = inner.get("delta", {}) if inner.get("type") == "content_block_delta" else {}
                if delta.get("type") == "text_delta":
                    streamed_text.append(delta["text"])
                    yield {"type": "text", "text": delta["text"]}
            elif kind == "assistant":
                for block in ev.get("message", {}).get("content", []):
                    if block.get("type") == "tool_use":
                        call = {"name": block["name"].removeprefix("mcp__oeb__"), "input": block.get("input", {})}
                        tool_calls.append(call)
                        yield {"type": "tool_use", **call}
            elif kind == "user":
                for block in ev.get("message", {}).get("content", []):
                    if isinstance(block, dict) and block.get("type") == "tool_result":
                        content = block.get("content")
                        text = content if isinstance(content, str) else json.dumps(content)
                        yield {"type": "tool_result", "is_error": bool(block.get("is_error")), "preview": text[:300]}
            elif kind == "result":
                final = ev
        proc.wait()
        stderr = proc.stderr.read() if proc.stderr else ""
        seen = {(r["doc_id"], r["page"]) for r in map(json.loads, seen_log.read_text().splitlines())}

    error = None
    if final is None:
        error = f"claude exited {proc.returncode} without a result: {stderr.strip()[-1500:]}"
        answer = "".join(streamed_text)
    else:
        answer = final.get("result") or "".join(streamed_text)
        if final.get("is_error") or final.get("subtype") != "success":
            error = f"{final.get('subtype')}: {answer[:500]}"
    result = AgentResult(
        answer=answer, citations=resolve_citations(answer, seen), tool_calls=tool_calls,
        num_turns=(final or {}).get("num_turns"), duration_ms=(final or {}).get("duration_ms"),
        usage=(final or {}).get("usage") or {}, cost_usd_equivalent=(final or {}).get("total_cost_usd"),
        error=error)
    yield {"type": "done", "result": result}


def run(question: str, doc_kinds: list[str] | None = None, model: str = AGENT_MODEL,
        cases: list[str] | None = None) -> AgentResult:
    for ev in run_stream(question, doc_kinds, model, cases):
        if ev["type"] == "done":
            return ev["result"]
    raise RuntimeError("agent produced no result")


def resolve_citations(answer: str, seen: set[tuple[str, int]]) -> list[Citation]:
    pairs = list(dict.fromkeys((d, int(p)) for d, p in CITE.findall(answer)))
    if not pairs:
        return []
    with connect() as conn:
        meta = {r["doc_id"]: r for r in conn.execute(
            "SELECT doc_id, case_number, exhibit, title FROM documents WHERE doc_id = ANY(%s)",
            ([d for d, _ in pairs],))}
    out = []
    for doc_id, page in pairs:
        m = meta.get(doc_id) or {}
        out.append(Citation(doc_id, page, m.get("case_number"), m.get("exhibit"), m.get("title"),
                            seen=(doc_id, page) in seen))
    return out


def render(answer: str, citations: list[Citation]) -> str:
    """Replace cite tokens with human-readable 'case / Exhibit X / p.N' labels."""
    lookup = {(c.doc_id, c.page): c for c in citations}

    def label(m: re.Match) -> str:
        c = lookup.get((m.group(1), int(m.group(2))))
        if c is None or c.case_number is None:
            return f"[{m.group(1)} p.{m.group(2)} (unknown document)]"
        ex = f"Exhibit {c.exhibit}" if c.exhibit else c.title
        flag = "" if c.seen else " (UNVERIFIED)"
        return f"[{c.case_number} / {ex} / p.{c.page}{flag}]"

    return CITE.sub(label, answer)


if __name__ == "__main__":
    q = " ".join(sys.argv[1:])
    res: AgentResult | None = None
    for event in run_stream(q):
        if event["type"] == "text":
            print(event["text"], end="", flush=True)
        elif event["type"] == "tool_use":
            print(f"\n  -> {event['name']}({json.dumps(event['input'])[:120]})", file=sys.stderr, flush=True)
        elif event["type"] == "done":
            res = event["result"]
    assert res is not None
    print("\n\n" + render(res.answer, res.citations))
    if res.error:
        print(f"\nERROR: {res.error}", file=sys.stderr)
    print(f"\n[{len(res.citations)} citations, {len(res.unverified_citations)} unverified, "
          f"{len(res.tool_calls)} tool calls, {res.num_turns} turns]", file=sys.stderr)
