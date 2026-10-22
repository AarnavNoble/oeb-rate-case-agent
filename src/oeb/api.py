"""HTTP API for the web UI.

    GET  /api/search?q=...&case=...&retriever=hybrid|fts|vector   (no LLM)
    POST /api/ask {"question": ..., "case": ...}                 (SSE stream of agent events)
    GET  /api/pdf/{doc_id}                                       (cached PDF; open with #page=N)
    GET  /api/page/{doc_id}/{page}                               (extracted page text + document metadata)
    GET  /api/corpus                                             (per-case document and page counts)
    GET  /api/documents?case=...                                 (ingested filings)
"""

import json
from collections.abc import Iterator
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

from oeb.agent import agent
from oeb.config import DATA_RAW
from oeb.db import connect
from oeb.search import Filters, fts, hybrid, vector

app = FastAPI(title="OEB rate-case research agent")
RETRIEVERS = {"hybrid": hybrid.search, "fts": fts.search, "vector": vector.search}


@app.get("/api/health")
def health() -> dict:
    with connect() as conn:
        row = conn.execute("""SELECT count(*) FILTER (WHERE status = 'embedded') AS documents,
                                     (SELECT count(*) FROM chunks) AS chunks FROM documents""").fetchone()
    return {"ok": True, **(row or {})}


@app.get("/api/corpus")
def corpus() -> list[dict]:
    with connect() as conn:
        return conn.execute("""
            SELECT d.case_number, min(d.applicant) AS applicant,
                   count(*) FILTER (WHERE d.status = 'embedded') AS documents,
                   coalesce(sum(d.n_pages) FILTER (WHERE d.status = 'embedded'), 0) AS pages,
                   min(d.date_received) AS first_filed, max(d.date_received) AS last_filed
            FROM documents d GROUP BY d.case_number ORDER BY d.case_number""").fetchall()


@app.get("/api/documents")
def documents(case: str | None = None) -> list[dict]:
    with connect() as conn:
        return conn.execute("""
            SELECT doc_id, case_number, title, exhibit, doc_kind, doc_type, n_pages, date_received
            FROM documents WHERE status = 'embedded' AND (%(case)s::text IS NULL OR case_number = %(case)s)
            ORDER BY case_number, date_received NULLS LAST, title""", {"case": case}).fetchall()


@app.get("/api/page/{doc_id}/{page}")
def page(doc_id: str, page: int) -> dict:
    with connect() as conn:
        row = conn.execute("""
            SELECT d.doc_id, d.case_number, d.title, d.exhibit, d.record_number, d.date_received,
                   d.n_pages, d.source_url, p.page_no, p.text, p.exhibit_ref
            FROM documents d JOIN pages p USING (doc_id)
            WHERE d.doc_id = %s AND p.page_no = %s""", (doc_id, page)).fetchone()
    if row is None:
        raise HTTPException(404, "page not found")
    return row


@app.get("/api/search")
def search(q: str = Query(min_length=2), case: str | None = None, retriever: str = "hybrid",
           k: int = Query(10, ge=1, le=50)) -> list[dict]:
    if retriever not in RETRIEVERS:
        raise HTTPException(400, f"retriever must be one of {sorted(RETRIEVERS)}")
    hits = RETRIEVERS[retriever](q, k, Filters(case_numbers=[case] if case else None))
    return [{**asdict(h), "citation": h.citation, "text": h.text[:1500]} for h in hits]


class AskRequest(BaseModel):
    question: str
    case: str | None = None


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


@app.post("/api/ask")
def ask(req: AskRequest) -> StreamingResponse:
    if not req.question.strip():
        raise HTTPException(400, "empty question")

    def events() -> Iterator[str]:
        try:
            for ev in agent.run_stream(req.question, cases=[req.case] if req.case else None):
                if ev["type"] == "done":
                    res = ev["result"]
                    yield _sse("done", {
                        "answer": res.answer, "error": res.error,
                        "citations": [asdict(c) for c in res.citations],
                        "tool_calls": len(res.tool_calls), "num_turns": res.num_turns,
                        "duration_ms": res.duration_ms})
                else:
                    yield _sse(ev["type"], {k: v for k, v in ev.items() if k != "type"})
        except Exception as e:  # surface failures to the UI instead of dropping the stream
            yield _sse("done", {"answer": "", "error": f"{type(e).__name__}: {e}", "citations": []})

    # sync generator: Starlette iterates it in a threadpool, so the subprocess read doesn't block the loop
    return StreamingResponse(events(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


@app.get("/api/pdf/{doc_id}")
def pdf(doc_id: str) -> FileResponse:
    with connect() as conn:
        row = conn.execute("SELECT local_path, title FROM documents WHERE doc_id = %s", (doc_id,)).fetchone()
    if row is None or not row["local_path"]:
        raise HTTPException(404, "document not downloaded")
    path = Path(row["local_path"]).resolve()
    if not path.is_relative_to(DATA_RAW.resolve()) or not path.exists():
        raise HTTPException(404, "file missing")
    return FileResponse(path, media_type="application/pdf",
                        headers={"Content-Disposition": f'inline; filename="{doc_id}.pdf"'})
