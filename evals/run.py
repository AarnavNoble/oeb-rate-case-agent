"""Reproduce every reported number.

    uv run python -m evals.run                 # retrieval eval (+ agent eval if results are missing)
    uv run python -m evals.run --retrieval     # retrieval only
    uv run python -m evals.run --agent         # (re)run the agent eval on the held-out split

Retrieval: for each IR row, query = the intervenor's question with all record locations
stripped; search is restricted to doc_kind='evidence' (IR responses, undertakings,
settlement, argument and decisions are excluded: leakage control). A hit is relevant if
its chunk's exhibit is one the utility cited in its response."""

import argparse
import json
import time
from pathlib import Path

from oeb.search import Filters, Hit, fts, hybrid, vector

HERE = Path(__file__).parent
DATA = HERE / "data" / "ir_eval.jsonl"
RESULTS = HERE / "results"
RETRIEVERS = {"fts": fts.search, "vector": vector.search, "hybrid": hybrid.search}
K = 10


def load_rows(split: str | None = None) -> list[dict]:
    rows = [json.loads(line) for line in DATA.read_text().splitlines()]
    return [r for r in rows if split is None or r["split"] == split]


def first_relevant(hits: list[Hit], gold: set[str]) -> int | None:
    for i, h in enumerate(hits, 1):
        if h.exhibit in gold:
            return i
    return None


def metrics(ranks: list[int | None]) -> dict:
    n = len(ranks)
    return {
        "n": n,
        "recall@1": round(sum(1 for r in ranks if r and r <= 1) / n, 3),
        "recall@5": round(sum(1 for r in ranks if r and r <= 5) / n, 3),
        "recall@10": round(sum(1 for r in ranks if r and r <= 10) / n, 3),
        "mrr@10": round(sum(1 / r for r in ranks if r) / n, 3),
    }


def run_retrieval() -> dict:
    rows = load_rows()
    evidence_only = Filters(doc_kinds=["evidence"])
    out: dict = {"n_rows": len(rows), "k": K, "retrievers": {}}
    per_row: list[dict] = []
    ranks: dict[str, dict[str, list[int | None]]] = {
        name: {"response_gold": [], "question_ref_gold": []} for name in RETRIEVERS}
    leak: list[bool] = []
    for row in rows:
        gold = set(row["response_exhibits"])
        ref_gold = set(row["reference_exhibits"]) | {row["ir_exhibit"]}
        rec = {"ir_id": row["ir_id"], "gold": sorted(gold)}
        for name, fn in RETRIEVERS.items():
            t = time.time()
            hits = fn(row["query"], K, Filters(case_numbers=[row["case_number"]], doc_kinds=evidence_only.doc_kinds))
            rec[f"{name}_ms"] = round((time.time() - t) * 1000)
            r = first_relevant(hits, gold)
            ranks[name]["response_gold"].append(r)
            ranks[name]["question_ref_gold"].append(first_relevant(hits, ref_gold))
            rec[name] = {"rank": r, "top5": [f"{h.exhibit}|{h.doc_id}|p{h.page_start}" for h in hits[:5]]}
        # ablation: same query, IR documents left in the index
        leaky = hybrid.search(row["query"], 5, Filters(case_numbers=[row["case_number"]]))
        leak.append(any(h.doc_id == row["doc_id"] and h.page_start <= row["page_end"]
                        and h.page_end >= row["page_start"] for h in leaky))
        per_row.append(rec)

    for name in RETRIEVERS:
        out["retrievers"][name] = {
            "response_gold": metrics(ranks[name]["response_gold"]),
            "question_ref_gold": metrics(ranks[name]["question_ref_gold"]),
            "median_latency_ms": sorted(r[f"{name}_ms"] for r in per_row)[len(per_row) // 2],
        }
    out["leakage_ablation"] = {
        "description": "hybrid top-5 over ALL documents (no leakage control): share of queries whose own "
                       "IR response pages are retrieved",
        "share": round(sum(leak) / len(leak), 3),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "retrieval.json").write_text(json.dumps(out, indent=2))
    (RESULTS / "retrieval_per_row.jsonl").write_text("\n".join(json.dumps(r) for r in per_row) + "\n")
    (RESULTS / "retrieval.md").write_text(retrieval_md(out))
    return out


def retrieval_md(out: dict) -> str:
    lines = [f"Retrieval on {out['n_rows']} IR questions (EB-2023-0195), evidence-only index, exhibit-level relevance.",
             "", "| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 | Median latency |",
             "|---|---|---|---|---|---|"]
    for name, r in out["retrievers"].items():
        m = r["response_gold"]
        lines.append(f"| {name} | {m['recall@1']:.3f} | {m['recall@5']:.3f} | {m['recall@10']:.3f} | "
                     f"{m['mrr@10']:.3f} | {r['median_latency_ms']} ms |")
    lines += ["", "Secondary (gold = exhibit named in the question's reference line / IR number):", "",
              "| Retriever | Recall@5 | MRR@10 |", "|---|---|---|"]
    for name, r in out["retrievers"].items():
        m = r["question_ref_gold"]
        lines.append(f"| {name} | {m['recall@5']:.3f} | {m['mrr@10']:.3f} |")
    a = out["leakage_ablation"]
    lines += ["", f"Leakage ablation: without the evidence-only filter, hybrid top-5 contains the query's own "
                  f"IR response for **{a['share']:.1%}** of questions.", ""]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retrieval", action="store_true")
    ap.add_argument("--agent", action="store_true")
    args = ap.parse_args()
    run_all = not (args.retrieval or args.agent)
    if args.retrieval or run_all:
        print(retrieval_md(run_retrieval()))
    if args.agent or (run_all and not (RESULTS / "agent.json").exists()):
        from evals.agent_eval import run_agent_eval
        run_agent_eval()


if __name__ == "__main__":
    main()
