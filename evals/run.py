"""Reproduce every reported number.

    uv run python -m evals.run                 # retrieval eval (+ agent eval if results are missing)
    uv run python -m evals.run --retrieval     # retrieval only
    uv run python -m evals.run --agent         # (re)run the agent eval on the held-out split

Retrieval: for each IR row, query = the intervenor's question with all record locations
stripped; search is restricted to doc_kind='evidence' (IR responses, undertakings,
settlement, argument and decisions are excluded: leakage control). A hit is relevant if
its chunk's exhibit is one the utility cited in its response (exhibit level), or if its
page header matches a section/tab/schedule the response cites (unit level). Random-chunk
and label-prior baselines calibrate both."""

import argparse
import json
import time
from pathlib import Path

from oeb.search import Filters, _shingles, fts, hybrid, vector

HERE = Path(__file__).parent
DATA = HERE / "data" / "ir_eval.jsonl"
RESULTS = HERE / "results"
RETRIEVERS = {"fts": fts.search, "vector": vector.search, "hybrid": hybrid.search}
K = 10


def load_rows(split: str | None = None) -> list[dict]:
    rows = [json.loads(line) for line in DATA.read_text().splitlines()]
    return [r for r in rows if split is None or r["split"] == split]


def first_relevant(hits: list, gold: set[str]) -> int | None:  # Hit or any object with .exhibit
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


class PageUnits:
    """Header-derived location units ('exhibit|section|tab|schedule') for evidence pages."""

    def __init__(self, case: str):
        from oeb.db import connect
        from oeb.irparse import ref_to_unit

        self.units: dict[tuple[str, int], str] = {}
        with connect() as conn:
            for r in conn.execute("""SELECT p.doc_id, p.page_no, p.exhibit_ref FROM pages p
                                     JOIN documents d USING (doc_id)
                                     WHERE d.case_number = %s AND d.doc_kind = 'evidence'
                                       AND p.exhibit_ref IS NOT NULL""", (case,)):
                unit = ref_to_unit(r["exhibit_ref"])
                if unit:
                    self.units[(r["doc_id"], r["page_no"])] = unit

    def of(self, doc_id: str, page_start: int, page_end: int) -> set[str]:
        return {u for p in range(page_start, page_end + 1) if (u := self.units.get((doc_id, p)))}


def first_relevant_unit(hits: list, gold_units: list[str], pages: PageUnits) -> int | None:
    from oeb.irparse import unit_matches

    for i, h in enumerate(hits, 1):
        if any(unit_matches(g, u) for g in gold_units for u in pages.of(h.doc_id, h.page_start, h.page_end)):
            return i
    return None


def baselines(rows: list[dict], pages: PageUnits, seeds: int = 20) -> dict:
    """Reference points for the metrics: random evidence chunks, and a label prior that
    always ranks exhibits by how often they are gold (it peeks at the labels, so it is an
    optimistic version of 'just guess the big exhibit')."""
    import random
    from collections import Counter

    from oeb.db import connect

    case = rows[0]["case_number"]
    with connect() as conn:
        chunks = [(r["doc_id"], r["exhibit"], r["page_start"], r["page_end"]) for r in conn.execute(
            "SELECT doc_id, exhibit, page_start, page_end FROM chunks WHERE case_number = %s AND doc_kind = 'evidence'",
            (case,))]

    class _H:  # minimal hit shape for first_relevant / first_relevant_unit
        def __init__(self, c):
            self.doc_id, self.exhibit, self.page_start, self.page_end = c

    rand_ex: list[dict] = []
    rand_unit: list[dict] = []
    fine_rows = [r for r in rows if r["response_units"]]
    for seed in range(seeds):
        rng = random.Random(seed)
        ex_ranks = []
        for row in rows:
            ex_ranks.append(first_relevant([_H(c) for c in rng.sample(chunks, K)], set(row["response_exhibits"])))
        rand_ex.append(metrics(ex_ranks))
        unit_ranks = [first_relevant_unit([_H(c) for c in rng.sample(chunks, K)], row["response_units"], pages)
                      for row in fine_rows]
        rand_unit.append(metrics(unit_ranks))

    def avg(ms: list[dict]) -> dict:
        return {k: (round(sum(m[k] for m in ms) / len(ms), 3) if k != "n" else ms[0]["n"]) for k in ms[0]}

    order = [e for e, _ in Counter(e for r in rows for e in r["response_exhibits"]).most_common()]
    prior_ranks = [next((i for i, e in enumerate(order[:K], 1) if e in set(r["response_exhibits"])), None)
                   for r in rows]
    return {"random_chunks": {"exhibit": avg(rand_ex), "unit": avg(rand_unit), "seeds": seeds},
            "exhibit_label_prior": {"exhibit": metrics(prior_ranks), "order": order[:5]}}


def _evidence_doc_ids(case: str) -> set[str]:
    from oeb.db import connect

    with connect() as conn:
        return {r["doc_id"] for r in conn.execute(
            "SELECT doc_id FROM documents WHERE case_number = %s AND doc_kind = 'evidence'", (case,))}


def _containment(text: str, reference: set) -> float:
    """Share of the hit's word 5-grams that also occur in the reference text."""
    sh = _shingles(text)
    return len(sh & reference) / max(1, len(sh))


def run_retrieval() -> dict:
    rows = load_rows()
    case = rows[0]["case_number"]
    pages = PageUnits(case)
    fine_rows = {r["ir_id"] for r in rows if r["response_units"]}
    out: dict = {"n_rows": len(rows), "n_unit_rows": len(fine_rows), "k": K, "retrievers": {}}
    per_row: list[dict] = []
    ranks: dict[str, dict[str, list[int | None]]] = {
        name: {"response_gold": [], "unit_gold": [], "question_ref_gold": []} for name in RETRIEVERS}
    leak: list[bool] = []
    evidence_docs = _evidence_doc_ids(case)
    for row in rows:
        response_shingles = _shingles(row["response"])
        gold = set(row["response_exhibits"])
        ref_gold = set(row["reference_exhibits"]) | {row["ir_exhibit"]}
        rec = {"ir_id": row["ir_id"], "gold": sorted(gold), "gold_units": row["response_units"]}
        for name, fn in RETRIEVERS.items():
            t = time.time()
            hits = fn(row["query"], K, Filters(case_numbers=[row["case_number"]], doc_kinds=["evidence"]))
            rec[f"{name}_ms"] = round((time.time() - t) * 1000)
            r = first_relevant(hits, gold)
            ranks[name]["response_gold"].append(r)
            ranks[name]["question_ref_gold"].append(first_relevant(hits, ref_gold))
            ru = None
            if row["ir_id"] in fine_rows:
                ru = first_relevant_unit(hits, row["response_units"], pages)
                ranks[name]["unit_gold"].append(ru)
            rec[name] = {"rank": r, "unit_rank": ru,
                         "top5": [f"{h.exhibit}|{h.doc_id}|p{h.page_start}" for h in hits[:5]]}
        # ablation: same query, IR documents left in the index. A leak is any non-evidence hit
        # whose text is largely the utility's own response (matched by content, because the
        # same response can be filed in several documents and duplicates are collapsed).
        leaky = hybrid.search(row["query"], 5, Filters(case_numbers=[row["case_number"]]))
        leak.append(any(h.doc_id not in evidence_docs and _containment(h.text, response_shingles) >= 0.3
                        for h in leaky))
        per_row.append(rec)

    for name in RETRIEVERS:
        out["retrievers"][name] = {
            "response_gold": metrics(ranks[name]["response_gold"]),
            "unit_gold": metrics(ranks[name]["unit_gold"]),
            "question_ref_gold": metrics(ranks[name]["question_ref_gold"]),
            "median_latency_ms": sorted(r[f"{name}_ms"] for r in per_row)[len(per_row) // 2],
        }
    out["baselines"] = baselines(rows, pages)
    out["leakage_ablation"] = {
        "description": "hybrid top-5 over ALL documents (no leakage control): share of queries for which a "
                       "non-evidence hit is largely the utility's own response text (>=30% of its word "
                       "5-grams; unrelated chunks score <0.15)",
        "share": round(sum(leak) / len(leak), 3),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "retrieval.json").write_text(json.dumps(out, indent=2))
    (RESULTS / "retrieval_per_row.jsonl").write_text("\n".join(json.dumps(r) for r in per_row) + "\n")
    (RESULTS / "retrieval.md").write_text(retrieval_md(out))
    return out


def _row(label: str, m: dict, extra: str | None = None) -> str:
    cells = [label, *(f"{m[k]:.3f}" for k in ("recall@1", "recall@5", "recall@10", "mrr@10"))]
    return "| " + " | ".join(cells + ([extra] if extra is not None else [])) + " |"


def retrieval_md(out: dict) -> str:
    b = out["baselines"]
    rx, ru, pr = b["random_chunks"]["exhibit"], b["random_chunks"]["unit"], b["exhibit_label_prior"]["exhibit"]
    lines = [f"Retrieval on {out['n_rows']} IR questions (EB-2023-0195), evidence-only index, k={out['k']}.", "",
             "**Exhibit level**: a hit is any chunk from an exhibit the utility cited in its response.", "",
             "| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 | Median latency |",
             "|---|---|---|---|---|---|"]
    for name, r in out["retrievers"].items():
        lines.append(_row(name, r["response_gold"], f"{r['median_latency_ms']} ms"))
    prior = ", ".join(b["exhibit_label_prior"]["order"][:3])
    lines += [_row(f"_random chunks ({b['random_chunks']['seeds']} seeds)_", rx, ""),
              _row(f"_label prior (always {prior}, ...)_", pr, ""),
              "", f"**Section/schedule level** ({out['n_unit_rows']} questions whose response cites a section, tab or "
              "schedule): a hit is a chunk on a page whose header matches it.", "",
              "| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 |", "|---|---|---|---|---|"]
    for name, r in out["retrievers"].items():
        lines.append(_row(name, r["unit_gold"]))
    lines += [_row("_random chunks_", ru),
              "", "Secondary (exhibit level, gold = exhibit named in the question's reference line / IR number):", "",
              "| Retriever | Recall@5 | MRR@10 |", "|---|---|---|"]
    for name, r in out["retrievers"].items():
        m = r["question_ref_gold"]
        lines.append(f"| {name} | {m['recall@5']:.3f} | {m['mrr@10']:.3f} |")
    a = out["leakage_ablation"]
    lines += ["", f"Leakage ablation: without the evidence-only filter, hybrid top-5 contains the utility's own "
                  f"answer to the question (matched by text, in any filing) for **{a['share']:.1%}** of questions.", ""]
    return "\n".join(lines)


def corpus_stats() -> dict:
    from oeb.db import connect

    with connect() as conn:
        cases = conn.execute("""
            SELECT d.case_number,
                   count(*) AS records,
                   count(*) FILTER (WHERE d.ext = 'pdf') AS pdfs,
                   count(*) FILTER (WHERE d.status = 'embedded') AS ingested,
                   count(*) FILTER (WHERE d.ext = 'pdf' AND d.status <> 'embedded') AS not_ingested,
                   round(sum(d.size_bytes) FILTER (WHERE d.status = 'embedded') / 1e6) AS mb,
                   coalesce(sum(d.n_pages) FILTER (WHERE d.status = 'embedded'), 0) AS pages,
                   (SELECT count(*) FROM chunks c WHERE c.case_number = d.case_number) AS chunks,
                   (SELECT count(*) FROM extracted_tables t JOIN documents x USING (doc_id)
                     WHERE x.case_number = d.case_number) AS tables,
                   coalesce(sum((d.timings->'parse_stats'->>'empty_pages')::int), 0) AS empty_pages
            FROM documents d GROUP BY d.case_number ORDER BY d.case_number""").fetchall()
        failures = conn.execute("""
            SELECT case_number, doc_id, title, status, error FROM documents
            WHERE ext = 'pdf' AND status <> 'embedded' ORDER BY case_number, doc_id""").fetchall()
        timing = conn.execute("""
            SELECT round(sum((timings->>'download_s')::numeric) / 3600, 2) AS download_h,
                   round(sum((timings->>'parse_s')::numeric) / 3600, 2) AS parse_h,
                   round(sum((timings->>'embed_s')::numeric) / 3600, 2) AS embed_h
            FROM documents WHERE status = 'embedded'""").fetchone()
    out = {"cases": [dict(r) for r in cases], "not_ingested": [dict(r) for r in failures],
           "stage_hours_summed": dict(timing or {})}
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "corpus.json").write_text(json.dumps(out, indent=2, default=str))
    return out


def corpus_md(c: dict) -> str:
    lines = ["| Case | Records | PDFs | Ingested | Pages | Chunks | Tables | MB |", "|---|---|---|---|---|---|---|---|"]
    for r in c["cases"]:
        lines.append(f"| {r['case_number']} | {r['records']} | {r['pdfs']} | {r['ingested']} | {r['pages']:,} | "
                     f"{r['chunks']:,} | {r['tables']:,} | {r['mb']} |")
    if c["not_ingested"]:
        lines += ["", f"{len(c['not_ingested'])} PDF(s) not ingested: "
                  + "; ".join(f"`{f['doc_id']}` ({f['status']}{': ' + f['error'][:80] if f['error'] else ''})"
                              for f in c["not_ingested"][:10])]
    return "\n".join(lines)


README = HERE.parent / "README.md"
START, END = "<!-- results:start -->", "<!-- results:end -->"


def update_readme() -> None:
    """Regenerate the README results block from evals/results/*.json so numbers can't drift."""
    if not README.exists() or START not in README.read_text():
        return
    parts = [f"_Generated by `uv run python -m evals.run` on {time.strftime('%Y-%m-%d')}._", "",
             "**Corpus**", "", corpus_md(json.loads((RESULTS / "corpus.json").read_text()))]
    if (RESULTS / "retrieval.json").exists():
        parts += ["", "**Retrieval**", "", retrieval_md(json.loads((RESULTS / "retrieval.json").read_text()))]
    build = HERE / "data" / "ir_build_stats.json"
    if build.exists():
        b = json.loads(build.read_text())
        parts += [f"Eval set: {b['labelled_rows']} labelled IR questions from {b['unique_irs']} parsed "
                  f"interrogatories ({b['ir_documents_parsed']} response documents)."]
    if (RESULTS / "agent.json").exists():
        from evals.agent_eval import agent_md
        parts += ["", "**Agent**", "", agent_md(json.loads((RESULTS / "agent.json").read_text()))]
    for name in ("hand_checks.json",):
        p = RESULTS / name
        h = json.loads(p.read_text()) if p.exists() else {}
        if h:
            parts += ["", "**Sample reviews**", "", *[f"- {k}: {v}" for k, v in h.items()]]
    text = README.read_text()
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{START}\n{chr(10).join(parts)}\n{END}{tail}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retrieval", action="store_true")
    ap.add_argument("--agent", action="store_true")
    args = ap.parse_args()
    run_all = not (args.retrieval or args.agent)
    print(corpus_md(corpus_stats()))
    if args.retrieval or run_all:
        print(retrieval_md(run_retrieval()))
    if args.agent or (run_all and not (RESULTS / "agent.json").exists()):
        from evals.agent_eval import run_agent_eval
        run_agent_eval()
    update_readme()


if __name__ == "__main__":
    main()
