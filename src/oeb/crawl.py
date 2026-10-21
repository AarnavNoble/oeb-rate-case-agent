"""Download a case's PDFs outside Temporal (same idempotent stage as the workflow's
download activity). Useful because RDS has ~4 min time-to-first-byte per file.

    uv run python -m oeb.crawl EB-2023-0195 --kinds evidence,ir_response --concurrency 1
"""

import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from oeb.db import connect
from oeb.pipeline import download_doc, register_case, set_failed

PRIORITY = ["evidence", "ir_response", "undertaking", "settlement", "decision", "argument",
            "interrogatory", "transcript", "intervenor_evidence", "other"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("case")
    ap.add_argument("--kinds", default=",".join(PRIORITY))
    ap.add_argument("--concurrency", type=int, default=1)
    args = ap.parse_args()
    kinds = args.kinds.split(",")

    register_case(args.case)
    with connect() as conn:
        rows = conn.execute(
            """SELECT doc_id, doc_kind FROM documents
               WHERE case_number = %s AND ext = 'pdf' AND status = 'listed' AND doc_kind = ANY(%s)""",
            (args.case, kinds),
        ).fetchall()
    rows.sort(key=lambda r: (kinds.index(r["doc_kind"]), r["doc_id"]))
    print(f"{len(rows)} to download", flush=True)

    t0 = time.time()

    def one(doc_id: str) -> str:
        t = time.time()
        try:
            r = download_doc(doc_id)
            return f"ok   {doc_id} {r.get('bytes', 0) / 1e6:.1f}MB {time.time() - t:.0f}s"
        except Exception as e:
            set_failed(doc_id, "download", f"{type(e).__name__}: {e}")
            return f"FAIL {doc_id} {type(e).__name__}: {e}"

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futs = [pool.submit(one, r["doc_id"]) for r in rows]
        for i, f in enumerate(as_completed(futs), 1):
            print(f"[{i}/{len(rows)} {time.time() - t0:.0f}s] {f.result()}", flush=True)


if __name__ == "__main__":
    main()
