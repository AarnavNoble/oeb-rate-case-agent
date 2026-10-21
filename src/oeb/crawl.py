"""Priority crawl outside Temporal, running the same idempotent stages as the workflow.

Temporal's download queue is first-in-first-out, so when RDS is slow the documents an
eval needs can sit behind dozens of letters. This fetches chosen kinds first; with
--process it also parses and embeds them. The worker's own activities later find the
work done and skip it. Requests go through the same per-host in-flight lock, so RDS
still sees one request at a time.

    uv run python -m oeb.crawl EB-2023-0195 --kinds evidence,ir_response --process
"""

import argparse
import time

from oeb.db import connect
from oeb.pipeline import download_doc, embed_doc, parse_doc, register_case, set_failed

PRIORITY = ["evidence", "ir_response", "undertaking", "settlement", "decision", "argument",
            "interrogatory", "transcript", "intervenor_evidence", "other"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("case")
    ap.add_argument("--kinds", default=",".join(PRIORITY))
    ap.add_argument("--process", action="store_true", help="also parse and embed")
    args = ap.parse_args()
    kinds = args.kinds.split(",")
    statuses = ["listed", "downloaded", "parsed"] if args.process else ["listed"]

    register_case(args.case)
    with connect() as conn:
        rows = conn.execute(
            """SELECT doc_id, doc_kind FROM documents WHERE case_number = %s AND ext = 'pdf'
               AND status = ANY(%s) AND doc_kind = ANY(%s)""",
            (args.case, statuses, kinds),
        ).fetchall()
    rows.sort(key=lambda r: (kinds.index(r["doc_kind"]), r["doc_id"]))
    print(f"{len(rows)} to process", flush=True)

    t0 = time.time()
    for i, r in enumerate(rows, 1):
        doc_id, t = r["doc_id"], time.time()
        try:
            d = download_doc(doc_id)
            msg = f"{d.get('bytes', 0) / 1e6:.1f}MB"
            if args.process:
                p = parse_doc(doc_id)
                embed_doc(doc_id)
                msg += f", {p.get('pages', '-')} pages"
            print(f"[{i}/{len(rows)} {time.time() - t0:.0f}s] ok   {doc_id} {msg} {time.time() - t:.0f}s", flush=True)
        except Exception as e:  # record and move on; the workflow will retry it too
            set_failed(doc_id, "crawl", f"{type(e).__name__}: {e}")
            print(f"[{i}/{len(rows)} {time.time() - t0:.0f}s] FAIL {doc_id} {type(e).__name__}: {e}", flush=True)


if __name__ == "__main__":
    main()
