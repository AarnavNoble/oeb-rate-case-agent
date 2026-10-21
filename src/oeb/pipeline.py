"""Ingestion stages. Each stage is idempotent and keyed on documents.status, so
Temporal activities (and the plain CLI) can call them repeatedly.

status: listed -> downloaded -> parsed -> embedded   (or skipped_format / failed)"""

import json
import time

from psycopg import sql
from psycopg.types.json import Jsonb

from oeb.chunk import chunk_pages
from oeb.config import DATA_RAW
from oeb.db import connect
from oeb.embed import embed_passages
from oeb.http import download
from oeb.parse import parse_pdf, to_number
from oeb.sources import DocMeta, hydroone, rds, torontohydro

STAGES = ["listed", "downloaded", "parsed", "embedded"]


def _sources_for(case: str) -> list:
    if case in hydroone.CASES:
        return [hydroone]
    return [rds, torontohydro]  # torontohydro.list_case adds consolidated files for EB-2023-0195 only


def register_case(case: str) -> list[str]:
    """List every document in the case and upsert metadata. Returns doc_ids to process."""
    docs: list[DocMeta] = [d for src in _sources_for(case) for d in src.list_case(case)]
    with connect() as conn:
        for d in docs:
            r = d.row()
            r["status"] = "listed" if d.ext == "pdf" else "skipped_format"
            conn.execute(
                """INSERT INTO documents (doc_id, source, case_number, source_url, record_number, title,
                       exhibit, applicant, doc_type, doc_kind, date_received, ext, listed_size_bytes, status)
                   VALUES (%(doc_id)s, %(source)s, %(case_number)s, %(source_url)s, %(record_number)s,
                       %(title)s, %(exhibit)s, %(applicant)s, %(doc_type)s, %(doc_kind)s,
                       %(date_received)s, %(ext)s, %(size_bytes)s, %(status)s)
                   ON CONFLICT (doc_id) DO UPDATE SET
                       title = EXCLUDED.title, exhibit = EXCLUDED.exhibit, applicant = EXCLUDED.applicant,
                       doc_type = EXCLUDED.doc_type, doc_kind = EXCLUDED.doc_kind,
                       date_received = EXCLUDED.date_received, listed_size_bytes = EXCLUDED.listed_size_bytes""",
                r,
            )
        # keep chunk-level kinds in step if classification rules changed
        conn.execute("""UPDATE chunks c SET doc_kind = d.doc_kind FROM documents d
                        WHERE c.doc_id = d.doc_id AND d.case_number = %s AND c.doc_kind <> d.doc_kind""", (case,))
    return [d.doc_id for d in docs if d.ext == "pdf"]


def get_doc(doc_id: str) -> dict:
    with connect() as conn:
        row = conn.execute("SELECT * FROM documents WHERE doc_id = %s", (doc_id,)).fetchone()
    if row is None:
        raise KeyError(doc_id)
    return row


def done(doc: dict, stage: str) -> bool:
    return doc["status"] in STAGES and STAGES.index(doc["status"]) >= STAGES.index(stage)


def set_status(doc_id: str, status: str, stage: str, seconds: float, **cols) -> None:
    extra = sql.SQL("").join(
        sql.SQL(", {} = {}").format(sql.Identifier(k), sql.Placeholder(k)) for k in cols)
    query = sql.SQL(
        """UPDATE documents SET status = %(status)s, error = NULL, updated_at = now(),
               timings = timings || %(t)s{extra} WHERE doc_id = %(doc_id)s""").format(extra=extra)
    with connect() as conn:
        conn.execute(query, {"status": status, "t": Jsonb({stage: round(seconds, 2)}), "doc_id": doc_id, **cols})


def set_failed(doc_id: str, stage: str, err: str) -> None:
    with connect() as conn:
        conn.execute(
            "UPDATE documents SET error = %s, timings = timings || %s, updated_at = now() WHERE doc_id = %s",
            (f"{stage}: {err}"[:2000], Jsonb({f"{stage}_failed": True}), doc_id),
        )


def download_doc(doc_id: str, attempts: int = 4) -> dict:
    doc = get_doc(doc_id)
    if done(doc, "downloaded"):
        return {"doc_id": doc_id, "skipped": True}
    t0 = time.time()
    dest = DATA_RAW / doc["case_number"] / f"{doc_id}.{doc['ext']}"
    sha, n, fetched = download(doc["source_url"], dest, attempts=attempts,
                               expected_size=doc["listed_size_bytes"])
    set_status(doc_id, "downloaded", "download_s", time.time() - t0,
               local_path=str(dest), sha256=sha, size_bytes=n)
    return {"doc_id": doc_id, "bytes": n, "fetched": fetched}


class ParseError(Exception):
    """Non-retryable: the file itself can't be parsed."""


def parse_doc(doc_id: str) -> dict:
    """Pages, tables and (unembedded) chunks, written in one transaction."""
    doc = get_doc(doc_id)
    if done(doc, "parsed"):
        return {"doc_id": doc_id, "skipped": True}
    if not done(doc, "downloaded"):
        raise RuntimeError(f"{doc_id} not downloaded")
    t0 = time.time()
    try:
        parsed = parse_pdf(doc["local_path"], title_exhibit=doc["exhibit"])
    except Exception as e:
        set_failed(doc_id, "parse", f"{type(e).__name__}: {e}")
        raise ParseError(f"{doc_id}: {type(e).__name__}: {e}") from e
    t_parse = time.time() - t0
    chunks = chunk_pages(parsed.pages)
    empty_pages = sum(1 for p in parsed.pages if not p.lines)

    with connect() as conn, conn.transaction():
        conn.execute("DELETE FROM pages WHERE doc_id = %s", (doc_id,))
        conn.execute("DELETE FROM extracted_tables WHERE doc_id = %s", (doc_id,))
        conn.execute("DELETE FROM chunks WHERE doc_id = %s", (doc_id,))
        with conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO pages (doc_id, page_no, text, exhibit_ref) VALUES (%s, %s, %s, %s)",
                [(doc_id, p.page_no, p.text, p.exhibit_ref) for p in parsed.pages],
            )
            for t in parsed.tables:
                table_id = cur.execute(
                    """INSERT INTO extracted_tables (doc_id, page_no, table_idx, header, rows)
                       VALUES (%s, %s, %s, %s, %s) RETURNING table_id""",
                    (doc_id, t.page_no, t.table_idx, Jsonb(t.header), Jsonb(t.rows)),
                ).fetchone()["table_id"]  # type: ignore[index]
                cur.executemany(
                    """INSERT INTO table_cells (table_id, row_idx, col_idx, col_name, value_text, value_num)
                       VALUES (%s, %s, %s, %s, %s, %s)""",
                    [(table_id, ri, ci, t.header[ci] if ci < len(t.header) else None, v, to_number(v))
                     for ri, row in enumerate(t.rows) for ci, v in enumerate(row) if v],
                )
            cur.executemany(
                """INSERT INTO chunks (doc_id, case_number, exhibit, doc_kind, page_start, page_end,
                       heading, text, n_tokens) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                [(doc_id, doc["case_number"], c.exhibit, doc["doc_kind"], c.page_start, c.page_end,
                  c.heading, c.text, c.n_tokens) for c in chunks],
            )
    stats = {"pages": len(parsed.pages), "empty_pages": empty_pages, "tables": len(parsed.tables),
             "table_errors": len(parsed.table_errors), "chunks": len(chunks), "parse_only_s": round(t_parse, 2)}
    set_status(doc_id, "parsed", "parse_s", time.time() - t0, n_pages=len(parsed.pages))
    with connect() as conn:
        conn.execute("UPDATE documents SET timings = timings || %s WHERE doc_id = %s",
                     (Jsonb({"parse_stats": stats, "table_error_samples": parsed.table_errors[:5]}), doc_id))
    return {"doc_id": doc_id, **stats}


def embed_doc(doc_id: str, batch: int = 64) -> dict:
    doc = get_doc(doc_id)
    if done(doc, "embedded"):
        return {"doc_id": doc_id, "skipped": True}
    if not done(doc, "parsed"):
        raise RuntimeError(f"{doc_id} not parsed")
    t0 = time.time()
    with connect() as conn:
        rows = conn.execute(
            "SELECT chunk_id, heading, text FROM chunks WHERE doc_id = %s AND embedding IS NULL ORDER BY chunk_id",
            (doc_id,),
        ).fetchall()
    for i in range(0, len(rows), batch):
        part = rows[i:i + batch]
        vecs = embed_passages([r["text"] for r in part])
        with connect() as conn, conn.cursor() as cur:
            cur.executemany("UPDATE chunks SET embedding = %s WHERE chunk_id = %s",
                            [(v, r["chunk_id"]) for v, r in zip(vecs, part, strict=True)])
    set_status(doc_id, "embedded", "embed_s", time.time() - t0)
    return {"doc_id": doc_id, "chunks": len(rows)}


def refresh_search_stats() -> dict:
    t0 = time.time()
    with connect() as conn:
        conn.execute("REFRESH MATERIALIZED VIEW lexeme_df")
        n = conn.execute("SELECT count(*) AS n FROM lexeme_df").fetchone()
    return {"lexemes": n["n"] if n else 0, "seconds": round(time.time() - t0, 1)}


if __name__ == "__main__":
    import sys

    ids = register_case(sys.argv[1])
    print(json.dumps({"case": sys.argv[1], "pdfs": len(ids)}))
