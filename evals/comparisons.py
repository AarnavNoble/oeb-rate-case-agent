"""Run the cross-case comparison questions (no ground truth: reviewed by hand).

    uv run python -m evals.comparisons

Writes evals/results/comparisons.md with each rendered answer and its citation checks.
"""

import json
from pathlib import Path

from oeb.agent import agent

HERE = Path(__file__).parent


def main() -> None:
    qs = [json.loads(line) for line in (HERE / "data" / "comparison_questions.jsonl").read_text().splitlines()]
    out = ["# Cross-case comparison questions", "",
           "Answers from the agent over both cases (all document kinds). No ground truth: review by hand.", ""]
    for q in qs:
        res = agent.run(q["question"])
        cases = sorted({c.case_number for c in res.citations if c.case_number})
        out += [f"## {q['id']}. {q['question']}", "",
                f"_Tool calls: {len(res.tool_calls)}, citations: {len(res.citations)} "
                f"({len(res.unverified_citations)} unverified), cases cited: {', '.join(cases) or 'none'}_", "",
                agent.render(res.answer, res.citations) if not res.error else f"**Error:** {res.error}", ""]
        print(f"{q['id']}: {len(res.citations)} citations, cases {cases}", flush=True)
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / "comparisons.md").write_text("\n".join(out))


if __name__ == "__main__":
    main()
