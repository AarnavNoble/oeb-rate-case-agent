from collections.abc import Iterator
from contextlib import contextmanager
from importlib import resources

import psycopg
from pgvector.psycopg import register_vector
from psycopg.rows import DictRow, dict_row

from oeb.config import DATABASE_URL


@contextmanager
def connect() -> Iterator[psycopg.Connection[DictRow]]:
    with psycopg.Connection[DictRow].connect(DATABASE_URL, row_factory=dict_row) as conn:
        register_vector(conn)
        yield conn


def init_schema() -> None:
    sql = resources.files("oeb").joinpath("schema.sql").read_text()
    with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
        conn.execute(sql)  # type: ignore[arg-type]


if __name__ == "__main__":
    init_schema()
    print("schema ok")
