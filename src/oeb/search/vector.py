from psycopg import sql

from oeb.db import connect
from oeb.embed import embed_query
from oeb.search import HIT_COLUMNS, OVERFETCH, Filters, Hit, collapse_near_duplicates, row_to_hit


def search(query: str, k: int = 10, filters: Filters | None = None) -> list[Hit]:
    where, params = (filters or Filters()).sql()
    vec = embed_query(query)
    q = sql.SQL("""
        WITH nn AS (
            SELECT {cols}, c.text_hash, d.date_received, 1 - (c.embedding <=> %s) AS score
            FROM chunks c JOIN documents d USING (doc_id)
            WHERE c.embedding IS NOT NULL AND {where}
            ORDER BY c.embedding <=> %s
            LIMIT %s
        ), dedup AS (
            SELECT DISTINCT ON (text_hash) * FROM nn
            ORDER BY text_hash, score DESC, date_received DESC NULLS LAST, chunk_id DESC
        )
        SELECT * FROM dedup ORDER BY score DESC, chunk_id""").format(
        cols=sql.SQL(HIT_COLUMNS), where=sql.SQL(where))  # type: ignore[arg-type]
    with connect() as conn, conn.transaction():
        # filtered HNSW scans: keep scanning until enough rows survive the WHERE clause (pgvector >= 0.8)
        conn.execute("SET LOCAL hnsw.ef_search = 200")
        conn.execute("SET LOCAL hnsw.iterative_scan = relaxed_order")
        rows = conn.execute(q, [vec, *params, vec, k * OVERFETCH]).fetchall()
    return collapse_near_duplicates([row_to_hit(r, float(r["score"])) for r in rows], k)
