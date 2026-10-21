"""Backfill pages.exhibit_ref with the current header rules, without re-parsing,
re-chunking or re-embedding.

    uv run python -m oeb.reheader EB-2023-0195
"""

import sys
import time

from oeb.db import connect
from oeb.parse import page_refs


def reheader(case: str) -> dict:
    with connect() as conn:
        docs = conn.execute("""SELECT doc_id, local_path FROM documents WHERE case_number = %s
                               AND status IN ('parsed', 'embedded') ORDER BY doc_id""", (case,)).fetchall()
    changed = 0
    t0 = time.time()
    for d in docs:
        refs = page_refs(d["local_path"])
        with connect() as conn, conn.cursor() as cur:
            cur.executemany("UPDATE pages SET exhibit_ref = %s WHERE doc_id = %s AND page_no = %s "
                            "AND exhibit_ref IS DISTINCT FROM %s",
                            [(r, d["doc_id"], i, r) for i, r in enumerate(refs, 1)])
            changed += cur.rowcount if cur.rowcount > 0 else 0
    return {"case": case, "documents": len(docs), "seconds": round(time.time() - t0)}


if __name__ == "__main__":
    print(reheader(sys.argv[1]))
