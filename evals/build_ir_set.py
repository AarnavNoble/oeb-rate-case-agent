"""Build the IR eval set from the utility's interrogatory responses.

    uv run python -m evals.build_ir_set EB-2023-0195

Writes evals/data/ir_eval.jsonl (rows whose *response* cites an evidence exhibit),
evals/data/ir_build_stats.json, and evals/ir_sample_review.md (seeded 20-row sample
for the hand check)."""

import json
import random
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from oeb.db import connect
from oeb.irparse import IRRow, split_irs

OUT = Path(__file__).parent / "data"
SEED = 20261021
HELDOUT_N = 20


def valid_exhibits(conn, case: str) -> set[str]:
    rows = conn.execute(
        "SELECT DISTINCT exhibit FROM chunks WHERE case_number = %s AND doc_kind = 'evidence' AND exhibit IS NOT NULL",
        (case,)).fetchall()
    return {r["exhibit"] for r in rows}


def build(case: str) -> dict:
    with connect() as conn:
        valid = valid_exhibits(conn, case)
        docs = conn.execute(
            """SELECT doc_id, title, date_received FROM documents
               WHERE case_number = %s AND doc_kind = 'ir_response' AND n_pages IS NOT NULL
                 -- the utility's own responses (some are mis-tagged 'Application and Evidence' on RDS)
                 AND coalesce(doc_type, '') NOT ILIKE '%%from Intervenor%%'
               ORDER BY date_received, doc_id""", (case,)).fetchall()
        all_rows: list[tuple[IRRow, str]] = []
        for d in docs:
            pages = [(r["page_no"], r["text"]) for r in conn.execute(
                "SELECT page_no, text FROM pages WHERE doc_id = %s ORDER BY page_no", (d["doc_id"],))]
            for row in split_irs(d["doc_id"], pages, valid):
                all_rows.append((row, str(d["date_received"])))

    # re-filed / updated responses: keep the latest filing of each IR
    latest: dict[str, tuple[IRRow, str]] = {}
    for row, filed in all_rows:
        if row.ir_id not in latest or filed >= latest[row.ir_id][1]:
            latest[row.ir_id] = (row, filed)
    unique = [r for r, _ in latest.values()]
    labelled = [r for r in unique if r.response_exhibits and len(r.query) >= 40]

    rng = random.Random(SEED)
    ids = sorted(r.ir_id for r in labelled)
    heldout = set(rng.sample(ids, min(HELDOUT_N, len(ids))))
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "ir_eval.jsonl", "w") as f:
        for r in sorted(labelled, key=lambda r: r.ir_id):
            rec = asdict(r) | {"case_number": case, "query": r.query,
                               "split": "heldout" if r.ir_id in heldout else "dev"}
            f.write(json.dumps(rec) + "\n")

    stats = {
        "case": case,
        "ir_documents_parsed": len(docs),
        "ir_blocks_found": len(all_rows),
        "unique_irs": len(unique),
        "with_response_exhibit_ref": sum(1 for r in unique if r.response_exhibits),
        "labelled_rows": len(labelled),
        "heldout_rows": len(heldout),
        "valid_evidence_exhibits": sorted(valid),
        "gold_exhibit_counts": Counter(e for r in labelled for e in r.response_exhibits).most_common(),
        "gold_equals_ir_exhibit_share": round(
            sum(1 for r in labelled if r.response_exhibits == [r.ir_exhibit]) / max(1, len(labelled)), 3),
        "intervenors": Counter(r.intervenor for r in labelled).most_common(),
    }
    (OUT / "ir_build_stats.json").write_text(json.dumps(stats, indent=2))
    write_review_sample(labelled)
    return stats


def write_review_sample(rows: list[IRRow], n: int = 20) -> None:
    sample = random.Random(SEED + 1).sample(sorted(rows, key=lambda r: r.ir_id), min(n, len(rows)))
    lines = ["# IR eval set: hand-check sample", "",
             f"Seeded random sample (seed {SEED + 1}) of {len(sample)} labelled rows.",
             "A row is **correct** if (1) the question is the intervenor's question, complete and not mixed",
             "with another IR, (2) the response is Toronto Hydro's response to it, and (3) every gold exhibit",
             "is cited in the response as a place where the answer/evidence is found.", "",
             "Mark each `verdict:` as `correct` or `wrong (<reason>)`.", ""]
    for i, r in enumerate(sample, 1):
        lines += [f"## {i}. {r.ir_id}  (doc `{r.doc_id}`, pp. {r.page_start}-{r.page_end})", "",
                  f"- gold (response) exhibits: **{', '.join(r.response_exhibits)}**",
                  f"- reference-line exhibits: {', '.join(r.reference_exhibits) or '-'}",
                  f"- PDF: `/pdf/{r.doc_id}#page={r.page_start}`", "",
                  "**Question (as filed)**", "", "```", r.question[:2500], "```", "",
                  "**Query used for retrieval (locations stripped)**", "", "```", r.query[:1500], "```", "",
                  "**Response**", "", "```", r.response[:3000], "```", "",
                  "verdict: ", ""]
    (Path(__file__).parent / "ir_sample_review.md").write_text("\n".join(lines))


if __name__ == "__main__":
    print(json.dumps(build(sys.argv[1] if len(sys.argv) > 1 else "EB-2023-0195"), indent=2))
