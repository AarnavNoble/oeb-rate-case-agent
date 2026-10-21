"""Postgres full-text retriever. 'BM25-style', not BM25: ts_rank_cd scores term
frequency and proximity with length normalization, but has no IDF. We add the IDF
idea as a filter: query lexemes that occur in more than MAX_DF of all chunks
('toronto', 'hydro', 'rate', ...) are dropped, and the rest are OR-ed so long
natural-language questions still match. Verbatim copies from re-filed exhibits are
collapsed to the most recently filed one."""

from psycopg import sql

from oeb.db import connect
from oeb.search import HIT_COLUMNS, OVERFETCH, Filters, Hit, collapse_near_duplicates, row_to_hit

# 1 = divide rank by 1 + log(document length)
_NORMALIZATION = 1
MAX_DF = 0.10


def search(query: str, k: int = 10, filters: Filters | None = None) -> list[Hit]:
    where, params = (filters or Filters()).sql()
    q = sql.SQL("""
        WITH lex AS (
            SELECT unnest(tsvector_to_array(to_tsvector('english', %s))) AS word
        ), n AS (
            SELECT greatest(count(*), 1) AS total FROM chunks
        ), kept AS (
            SELECT lex.word FROM lex LEFT JOIN lexeme_df df USING (word), n
            WHERE coalesce(df.ndoc, 0) <= {max_df} * n.total
        ), q AS (
            -- fall back to all lexemes if every one is too common
            SELECT to_tsquery('english', coalesce(
                (SELECT string_agg(quote_literal(word), ' | ') FROM kept),
                (SELECT string_agg(quote_literal(word), ' | ') FROM lex))) AS tsq
        ), scored AS (
            SELECT DISTINCT ON (c.text_hash) {cols}, ts_rank_cd(c.tsv, q.tsq, {norm}) AS score
            FROM chunks c JOIN documents d USING (doc_id), q
            WHERE c.tsv @@ q.tsq AND {where}
            ORDER BY c.text_hash, score DESC, d.date_received DESC NULLS LAST, c.chunk_id DESC
        )
        SELECT * FROM scored ORDER BY score DESC, chunk_id LIMIT %s""").format(
        cols=sql.SQL(HIT_COLUMNS), norm=sql.Literal(_NORMALIZATION),  # type: ignore[arg-type]
        max_df=sql.Literal(MAX_DF), where=sql.SQL(where))  # type: ignore[arg-type]
    with connect() as conn:
        rows = conn.execute(q, [query, *params, k * OVERFETCH]).fetchall()
    return collapse_near_duplicates([row_to_hit(r, float(r["score"])) for r in rows], k)
