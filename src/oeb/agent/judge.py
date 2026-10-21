"""LLM judge (run through Claude Code headless, like the agent): compares the agent's
answer with the utility's actual interrogatory response."""

import json
import os
import shutil
import subprocess
import tempfile

JUDGE_MODEL = os.environ.get("OEB_JUDGE_MODEL", "claude-opus-5-5")

SYSTEM = """\
You grade answers to interrogatories (written questions) from an Ontario Energy Board rate case. \
You get the question, the utility's own written response (the reference), and a candidate answer \
written by a research assistant that could only read the utility's pre-filed evidence.

Grade whether the candidate's substance agrees with the reference:
- correct: covers the reference's main points and contains nothing that contradicts it. Different \
wording, extra correct context, or citing evidence instead of restating it is fine.
- partially_correct: gets some main points right but misses or misstates others, or is too vague \
to confirm the key figures/positions.
- incorrect: contradicts the reference on a main point (wrong number, wrong position).
- abstained: the candidate says the evidence doesn't answer the question and gives no substantive answer.

Judge only against the reference. If the reference itself only points elsewhere ("see the \
response to 2B-SEC-12"), grade on whatever substance it does contain. Be strict about numbers.\
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["correct", "partially_correct", "incorrect", "abstained"]},
        "rationale": {"type": "string", "description": "One to three sentences."},
    },
    "required": ["verdict", "rationale"],
    "additionalProperties": False,
}


def judge(question: str, reference: str, candidate: str, model: str = JUDGE_MODEL) -> dict:
    prompt = (f"<question>\n{question}\n</question>\n\n<reference_response>\n{reference}\n</reference_response>\n\n"
              f"<candidate_answer>\n{candidate}\n</candidate_answer>\n\nGrade the candidate.")
    claude = shutil.which("claude")
    if not claude:
        raise RuntimeError("Claude Code CLI not found on PATH")
    env = {**os.environ}
    env.pop("ANTHROPIC_API_KEY", None)  # use the Claude Code login
    with tempfile.TemporaryDirectory(prefix="oeb-judge-") as cwd:
        proc = subprocess.run(
            [claude, "-p", prompt, "--model", model, "--system-prompt", SYSTEM, "--tools", "",
             "--strict-mcp-config", "--setting-sources", "", "--no-session-persistence",
             "--output-format", "json", "--json-schema", json.dumps(SCHEMA)],
            cwd=cwd, env=env, capture_output=True, text=True, timeout=600)
    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"judge failed (exit {proc.returncode}): {proc.stderr[-800:]}") from e
    if out.get("is_error") or not out.get("structured_output"):
        raise RuntimeError(f"judge error: {out.get('subtype')} {str(out.get('result'))[:300]}")
    return {**out["structured_output"], "model": model, "cost_usd_equivalent": out.get("total_cost_usd")}
