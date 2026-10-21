"""stdio MCP server exposing the agent tools to Claude Code (`claude -p`).

Env:
  OEB_DOC_KINDS  comma-separated doc kinds the tools may return (eval leakage control)
  OEB_CASES      comma-separated case numbers the tools may return
  OEB_SEEN_LOG   JSONL file; every page the agent sees is appended, for citation checking
"""

import json
import os
from typing import Literal

from mcp.server.mcpserver import MCPServer

from oeb.agent.tools import TOOL_DEFS, ToolContext, run_tool

_DESC = {t["name"]: t["description"] for t in TOOL_DEFS}
_kinds = os.environ.get("OEB_DOC_KINDS")
_cases = os.environ.get("OEB_CASES")
_ctx = ToolContext(doc_kinds=_kinds.split(",") if _kinds else None, cases=_cases.split(",") if _cases else None)
_seen_log = os.environ.get("OEB_SEEN_LOG")

server = MCPServer("oeb", instructions="Ontario Energy Board rate-case filings: search, read pages, query tables.")


def _call(name: str, args: dict) -> str:
    before = set(_ctx.seen_pages)
    out = run_tool(_ctx, name, args)
    if _seen_log:
        with open(_seen_log, "a") as f:
            for doc_id, page in sorted(_ctx.seen_pages - before):
                f.write(json.dumps({"doc_id": doc_id, "page": page, "tool": name}) + "\n")
    return out


@server.tool(description=_DESC["search"])
def search(query: str, case_number: Literal["EB-2023-0195", "EB-2026-0164"] | None = None, k: int = 8) -> str:
    return _call("search", {"query": query, "case_number": case_number, "k": k})


@server.tool(description=_DESC["fetch_page"])
def fetch_page(doc_id: str, page: int) -> str:
    return _call("fetch_page", {"doc_id": doc_id, "page": page})


@server.tool(description=_DESC["query_table"])
def query_table(sql: str) -> str:
    return _call("query_table", {"sql": sql})


if __name__ == "__main__":
    server.run("stdio")
