"""Agent tools: hybrid search, page fetch, read-only SQL over extracted tables.

Every result carries a cite token `[cite:<doc_id>:<page>]` the model copies into its
answer; tokens are later checked against the pages the agent actually saw."""

import json
import re
from dataclasses import dataclass, field

import psycopg
from psycopg import sql
from psycopg.rows import DictRow, dict_row

from oeb.config import AGENT_DATABASE_URL
from oeb.db import connect
from oeb.search import Filters, hybrid

CASES = {"EB-2023-0195": "Toronto Hydro 2025-2029 rate application",
         "EB-2026-0164": "Hydro One 2028-2032 joint rate application"}

TOOL_DEFS = [
    {
        "name": "search",
        "description": (
            "Hybrid (full-text + vector) search over regulatory filings. Returns up to k passages, each with a "
            "cite token, case, exhibit, page range and text. Use specific terms (program names, dollar items, "
            "years). Run several searches with different wording when the first results miss."),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "What to look for."},
                "case_number": {"type": "string", "enum": list(CASES),
                                "description": "Restrict to one case. Omit to search all cases."},
                "k": {"type": "integer", "minimum": 1, "maximum": 15, "description": "Results to return (default 8)."},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "fetch_page",
        "description": (
            "Full text of one PDF page (1-based page number) plus the tables extracted from it. Use it to read "
            "around a search hit or to check a number before citing it."),
        "input_schema": {
            "type": "object",
            "properties": {"doc_id": {"type": "string"}, "page": {"type": "integer", "minimum": 1}},
            "required": ["doc_id", "page"],
            "additionalProperties": False,
        },
    },
    {
        "name": "query_table",
        "description": (
            "Read-only SQL (PostgreSQL SELECT) over tables extracted from the filings. Views:\n"
            "  agent_tables(table_id, doc_id, case_number, exhibit, doc_kind, title, page_no, header jsonb, "
            "rows jsonb)\n"
            "  agent_table_cells(table_id, doc_id, case_number, exhibit, doc_kind, page_no, row_idx, col_idx, "
            "col_name, value_text, value_num)\n"
            "value_num is the parsed number (parentheses = negative, % and $ stripped); units come from the "
            "table header or caption, so read the page before citing. At most 50 rows are returned."),
        "input_schema": {
            "type": "object",
            "properties": {"sql": {"type": "string"}},
            "required": ["sql"],
            "additionalProperties": False,
        },
    },
]

MAX_ROWS = 50
_SELECT_ONLY = re.compile(r"^\s*(?:with|select)\b", re.I)
_FORBIDDEN = re.compile(r";\s*\S|\b(?:insert|update|delete|drop|alter|create|grant|copy|call|do|set|reset)\b", re.I)


@dataclass
class ToolContext:
    """Per-run state: allowed document kinds (eval leakage control), allowed cases,
    and what was seen."""
    doc_kinds: list[str] | None = None
    cases: list[str] | None = None
    seen_pages: set[tuple[str, int]] = field(default_factory=set)

    def _see(self, doc_id: str, start: int, end: int) -> None:
        for p in range(start, end + 1):
            self.seen_pages.add((doc_id, p))


def cite_token(doc_id: str, page: int) -> str:
    return f"[cite:{doc_id}:{page}]"


def run_tool(ctx: ToolContext, name: str, args: dict) -> str:
    if name == "search":
        return _search(ctx, args)
    if name == "fetch_page":
        return _fetch_page(ctx, args)
    if name == "query_table":
        return _query_table(ctx, args)
    raise ValueError(f"unknown tool {name}")


def _search(ctx: ToolContext, args: dict) -> str:
    query = args.get("query")
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    case = args.get("case_number")
    if ctx.cases and case and case not in ctx.cases:
        raise ValueError(f"only these cases are available in this session: {', '.join(ctx.cases)}")
    k = int(args.get("k") or 8)
    hits = hybrid.search(query, max(1, min(k, 15)),
                         Filters(case_numbers=[case] if case else ctx.cases, doc_kinds=ctx.doc_kinds))
    out = []
    for h in hits:
        ctx._see(h.doc_id, h.page_start, h.page_end)
        out.append({
            "cite": cite_token(h.doc_id, h.page_start),
            "doc_id": h.doc_id, "case_number": h.case_number, "exhibit": h.exhibit, "title": h.title,
            "pages": [h.page_start, h.page_end], "heading": h.heading, "text": h.text[:2500],
        })
    return json.dumps(out) if out else "No results."


def _fetch_page(ctx: ToolContext, args: dict) -> str:
    doc_id, page = args.get("doc_id"), args.get("page")
    if not isinstance(doc_id, str) or not isinstance(page, int):
        raise ValueError("doc_id (string) and page (integer) are required")
    with connect() as conn:
        doc = conn.execute("SELECT case_number, exhibit, title, doc_kind, n_pages FROM documents WHERE doc_id = %s",
                           (doc_id,)).fetchone()
        if doc is None:
            raise ValueError(f"unknown doc_id {doc_id}")
        if (ctx.doc_kinds and doc["doc_kind"] not in ctx.doc_kinds) or (
                ctx.cases and doc["case_number"] not in ctx.cases):
            raise ValueError(f"{doc_id} is not available in this session")
        row = conn.execute("SELECT text, exhibit_ref FROM pages WHERE doc_id = %s AND page_no = %s",
                           (doc_id, page)).fetchone()
        if row is None:
            raise ValueError(f"{doc_id} has {doc['n_pages']} pages; page {page} not found")
        tables = conn.execute("SELECT header, rows FROM extracted_tables WHERE doc_id = %s AND page_no = %s "
                              "ORDER BY table_idx", (doc_id, page)).fetchall()
    ctx._see(doc_id, page, page)
    return json.dumps({
        "cite": cite_token(doc_id, page), "case_number": doc["case_number"], "exhibit": doc["exhibit"],
        "exhibit_ref": row["exhibit_ref"], "title": doc["title"], "page": page, "n_pages": doc["n_pages"],
        "text": row["text"][:12000],
        "tables": [{"header": t["header"], "rows": t["rows"][:60]} for t in tables],
    })


def _query_table(ctx: ToolContext, args: dict) -> str:
    query = args.get("sql")
    if not isinstance(query, str) or not _SELECT_ONLY.match(query) or _FORBIDDEN.search(query.rstrip().rstrip(";")):
        raise ValueError("only a single SELECT (or WITH ... SELECT) statement over agent_tables / "
                         "agent_table_cells is allowed")
    body = query.rstrip().rstrip(";")
    # Wrap so the row cap and the doc_kind restriction can't be bypassed by the inner query.
    wrapped = sql.SQL("SELECT * FROM ({inner}) AS q LIMIT {limit}").format(
        inner=sql.SQL(body), limit=sql.Literal(MAX_ROWS))  # type: ignore[arg-type]
    try:
        # agent_ro can SELECT only the agent_* views; everything is rolled back afterwards
        with psycopg.Connection[DictRow].connect(AGENT_DATABASE_URL, row_factory=dict_row) as conn:
            conn.execute("SET statement_timeout = '5s'")
            if ctx.doc_kinds or ctx.cases:
                # temp views shadow the public ones (pg_temp is searched first), restricting kinds/cases
                cond = sql.SQL(" AND ").join([
                    *([sql.SQL("doc_kind = ANY({})").format(sql.Literal(ctx.doc_kinds))] if ctx.doc_kinds else []),
                    *([sql.SQL("case_number = ANY({})").format(sql.Literal(ctx.cases))] if ctx.cases else []),
                ])
                for view in ("agent_tables", "agent_table_cells"):
                    conn.execute(sql.SQL("CREATE TEMP VIEW {v} AS SELECT * FROM {pv} WHERE {c}").format(
                        v=sql.Identifier(view), pv=sql.Identifier("public", view), c=cond))
            rows = conn.execute(wrapped).fetchall()
            conn.rollback()
    except psycopg.Error as e:
        raise ValueError(f"SQL error: {str(e).strip()[:500]}") from e
    return json.dumps(rows, default=str)
