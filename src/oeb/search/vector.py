from psycopg import sql

from oeb.db import connect
from oeb.embed import embed_query
from oeb.search import HIT_COLUMNS, Filters, Hit, row_to_hit


def search(query: str, k: int = 10, filters: Filters | None = None) -> list[Hit]:
    where, params = (filters or Filters()).sql()
    vec = embed_query(query)
    q = sql.SQL("""
        SELECT {cols}, 1 - (c.embedding <=> %s) AS score
        FROM chunks c JOIN documents d USING (doc_id)
        WHERE c.embedding IS NOT NULL AND {where}
        ORDER BY c.embedding <=> %s
        LIMIT %s""").format(cols=sql.SQL(HIT_COLUMNS), where=sql.SQL(where))  # type: ignore[arg-type]
    with connect() as conn, conn.transaction():
        # filtered HNSW scans: keep scanning until k rows survive the WHERE clause (pgvector >= 0.8)
        conn.execute("SET LOCAL hnsw.ef_search = 200")
        conn.execute("SET LOCAL hnsw.iterative_scan = relaxed_order")
        rows = conn.execute(q, [vec, *params, vec, k]).fetchall()
    return [row_to_hit(r, float(r["score"])) for r in rows]
