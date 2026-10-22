"""Agent eval on the held-out IR slice.

Leakage control is the same as for retrieval: the agent's tools only see
doc_kind='evidence' of the question's own case, and the question is given with
record locations stripped.

Metrics
- citation accuracy: share of questions where at least one citation is on a page of an
  exhibit the utility cited in its response
- answer correctness: Claude Opus 5.5 judge verdict vs the utility's actual response
- unverified-citation rate: citations to pages the agent never saw in a tool result

Runs are cached per IR in results/agent_runs/ so an interrupted eval resumes.
"""

import json
import random
import time
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from oeb.agent import agent
from oeb.agent.judge import JUDGE_MODEL, judge
from oeb.config import AGENT_MODEL

HERE = Path(__file__).parent
RESULTS = HERE / "results"
RUNS = RESULTS / "agent_runs"
SEED = 20261022


def _load_heldout() -> list[dict]:
    rows = [json.loads(line) for line in (HERE / "data" / "ir_eval.jsonl").read_text().splitlines()]
    return [r for r in rows if r["split"] == "heldout"]


def _unit_hit(row: dict, citations: list[dict], pages) -> bool | None:
    """Does any cited page sit in a section/tab/schedule the utility cited? None if the
    response only cites whole exhibits."""
    from oeb.irparse import unit_matches

    if not row["response_units"]:
        return None
    return any(unit_matches(g, u) for c in citations for u in pages.of(c["doc_id"], c["page"], c["page"])
               for g in row["response_units"])


def _run_one(row: dict) -> dict:
    path = RUNS / f"{row['ir_id']}.json"
    if path.exists():
        cached = json.loads(path.read_text())
        if cached["query"] == row["query"]:  # a rebuilt eval set can change the question
            return cached
    t0 = time.time()
    res = agent.run(row["query"], doc_kinds=["evidence"], cases=[row["case_number"]])
    cited_exhibits = sorted({c.exhibit for c in res.citations if c.exhibit})
    gold = set(row["response_exhibits"])
    rec = {
        "ir_id": row["ir_id"], "gold_exhibits": sorted(gold), "query": row["query"],
        "answer": res.answer, "answer_rendered": agent.render(res.answer, res.citations),
        "citations": [asdict(c) for c in res.citations], "cited_exhibits": cited_exhibits,
        "citation_hit": bool(gold & set(cited_exhibits)),
        "n_unverified": len(res.unverified_citations), "tool_calls": len(res.tool_calls),
        "num_turns": res.num_turns, "seconds": round(time.time() - t0, 1), "agent_error": res.error,
        "agent_cost_usd_equivalent": res.cost_usd_equivalent,
    }
    if res.error:
        rec["judge"] = {"verdict": "error", "rationale": res.error}
    else:
        rec["judge"] = judge(row["question"], row["response"], rec["answer_rendered"])
    RUNS.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rec, indent=2))
    return rec


def run_agent_eval(limit: int | None = None) -> dict:
    from evals.run import PageUnits

    rows = _load_heldout()[:limit] if limit else _load_heldout()
    pages = PageUnits(rows[0]["case_number"])
    recs = []
    for i, row in enumerate(rows, 1):
        rec = _run_one(row)
        rec["citation_unit_hit"] = _unit_hit(row, rec["citations"], pages)
        recs.append(rec)
        print(f"[{i}/{len(rows)}] {rec['ir_id']}: cite_hit={rec['citation_hit']} "
              f"verdict={rec['judge']['verdict']} ({rec['seconds']}s)", flush=True)

    n = len(recs)
    verdicts = Counter(r["judge"]["verdict"] for r in recs)
    n_cites = sum(len(r["citations"]) for r in recs)
    out = {
        "n": n, "agent_model": AGENT_MODEL, "judge_model": JUDGE_MODEL,
        "citation_accuracy": round(sum(r["citation_hit"] for r in recs) / n, 3),
        "citation_unit_accuracy": round(sum(1 for r in recs if r["citation_unit_hit"])
                                        / max(1, sum(1 for r in recs if r["citation_unit_hit"] is not None)), 3),
        "n_unit": sum(1 for r in recs if r["citation_unit_hit"] is not None),
        "answers_with_citations": round(sum(1 for r in recs if r["citations"]) / n, 3),
        "unverified_citation_rate": round(sum(r["n_unverified"] for r in recs) / max(1, n_cites), 3),
        "verdicts": dict(verdicts),
        "correct_rate": round(verdicts["correct"] / n, 3),
        "correct_or_partial_rate": round((verdicts["correct"] + verdicts["partially_correct"]) / n, 3),
        "median_seconds": sorted(r["seconds"] for r in recs)[n // 2],
        "median_tool_calls": sorted(r["tool_calls"] for r in recs)[n // 2],
        "cost_usd_equivalent_total": round(sum((r.get("agent_cost_usd_equivalent") or 0)
                                               + (r["judge"].get("cost_usd_equivalent") or 0) for r in recs), 2),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "agent.json").write_text(json.dumps(out, indent=2))
    (RESULTS / "agent.md").write_text(agent_md(out))
    write_judge_review(recs)
    return out


def agent_md(o: dict) -> str:
    v = o["verdicts"]
    return "\n".join([
        f"Agent eval on {o['n']} held-out IR questions (agent `{o['agent_model']}`, judge `{o['judge_model']}`), "
        "evidence-only tools, record locations stripped from questions.", "",
        "| Metric | Value |", "|---|---|",
        f"| Citation accuracy, section/schedule level (n={o['n_unit']}) | {o['citation_unit_accuracy']:.1%} |",
        f"| Citation accuracy, exhibit level (cites an exhibit the utility cited) | {o['citation_accuracy']:.1%} |",
        f"| Judge: correct | {o['correct_rate']:.1%} |",
        f"| Judge: correct or partially correct | {o['correct_or_partial_rate']:.1%} |",
        f"| Verdicts (correct / partial / incorrect / abstained / error) | {v.get('correct', 0)} / "
        f"{v.get('partially_correct', 0)} / {v.get('incorrect', 0)} / {v.get('abstained', 0)} / {v.get('error', 0)} |",
        f"| Citations to pages the agent never saw | {o['unverified_citation_rate']:.1%} |",
        f"| Median tool calls / seconds per question | {o['median_tool_calls']} / {o['median_seconds']} |", ""])


def write_judge_review(recs: list[dict], n: int = 20) -> None:
    sample = random.Random(SEED).sample(sorted(recs, key=lambda r: r["ir_id"]), min(n, len(recs)))
    rows = [json.loads(line) for line in (HERE / "data" / "ir_eval.jsonl").read_text().splitlines()]
    by_id = {r["ir_id"]: r for r in rows}
    lines = ["# Judge verdicts: hand-check sample", "",
             f"Seeded sample (seed {SEED}) of {len(sample)} judge verdicts. For each, read the utility's response "
             "and the agent's answer, decide the verdict yourself, and mark `agree: yes` or "
             "`agree: no (<your verdict>)`.",
             ""]
    for i, r in enumerate(sample, 1):
        row = by_id[r["ir_id"]]
        lines += [f"## {i}. {r['ir_id']}: judge says **{r['judge']['verdict']}**", "",
                  f"> {r['judge']['rationale']}", "", "**Question**", "", "```", row["question"][:2000], "```", "",
                  "**Utility's response (reference)**", "", "```", row["response"][:3000], "```", "",
                  "**Agent answer**", "", "```", r["answer_rendered"][:3000], "```", "", "agree: ", ""]
    (HERE / "judge_review.md").write_text("\n".join(lines))


if __name__ == "__main__":
    import sys
    print(json.dumps(run_agent_eval(int(sys.argv[1]) if len(sys.argv) > 1 else None), indent=2))
