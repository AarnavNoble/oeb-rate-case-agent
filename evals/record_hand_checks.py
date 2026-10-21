"""Turn the review sheets into numbers for the README.

Mark `verdict:` / `label-for-query:` lines in evals/ir_sample_review.md and `agree:` lines
in evals/judge_review.md, then run

    uv run python -m evals.record_hand_checks

which writes evals/results/hand_checks.json and refreshes the README results block. The
reported reviewer comes from the sheet's "Reviewed by" line, so marks made by Claude are
never labelled as human checks.
"""

import json
import re
from pathlib import Path

from evals.run import RESULTS, update_readme

HERE = Path(__file__).parent


def _reviewer(text: str) -> str:
    m = re.search(r"\*\*Reviewed by ([^*]+)\*\*", text)
    return m.group(1).strip() if m else "hand-checked"


def _tally(text: str, field: str, positive: str) -> tuple[int, int, int]:
    marks = re.findall(rf"^{field}:[ \t]*(.*)$", text, re.M)
    filled = [m.strip().lower() for m in marks if m.strip()]
    return sum(1 for m in filled if m.startswith(positive)), len(filled), len(marks)


def _fmt(ok: int, n: int, total: int, who: str) -> str:
    pending = f", {total - n} of {total} not yet marked" if n < total else ""
    return f"{ok}/{n} = {ok / n:.0%} (reviewed by {who}{pending})"


def main() -> None:
    out: dict[str, str] = {}
    ir = (HERE / "ir_sample_review.md").read_text() if (HERE / "ir_sample_review.md").exists() else ""
    who = _reviewer(ir)
    ok, n, total = _tally(ir, "verdict", "correct")
    if n:
        out["IR eval-set rows passing the full review rubric (complete question, right response, every gold "
            "exhibit is an answer location)"] = _fmt(ok, n, total, who)
    ok, n, total = _tally(ir, "label-for-query", "yes")
    if n:
        out["IR eval-set rows whose gold exhibits locate the answer to the queried question"] = _fmt(ok, n, total, who)
    jr = (HERE / "judge_review.md").read_text() if (HERE / "judge_review.md").exists() else ""
    ok, n, total = _tally(jr, "agree", "yes")
    if n:
        out["Agreement with the LLM judge's verdicts"] = _fmt(ok, n, total, _reviewer(jr))
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "hand_checks.json").write_text(json.dumps(out, indent=2))
    update_readme()
    print(json.dumps(out, indent=2) if out else "No marks found yet.")


if __name__ == "__main__":
    main()
