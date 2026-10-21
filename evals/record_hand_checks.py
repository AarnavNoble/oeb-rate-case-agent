"""Turn the hand-check sheets into numbers for the README.

Fill in `verdict:` lines in evals/ir_sample_review.md (correct / wrong (...)) and
`agree:` lines in evals/judge_review.md (yes / no (...)), then run

    uv run python -m evals.record_hand_checks

which writes evals/results/hand_checks.json and refreshes the README results block.
"""

import json
import re
from pathlib import Path

from evals.run import RESULTS, update_readme

HERE = Path(__file__).parent


def _tally(path: Path, field: str, positive: str) -> tuple[int, int, int]:
    marks = re.findall(rf"^{field}:[ \t]*(.*)$", path.read_text(), re.M) if path.exists() else []
    filled = [m.strip().lower() for m in marks if m.strip()]
    return sum(1 for m in filled if m.startswith(positive)), len(filled), len(marks)


def main() -> None:
    out: dict[str, str] = {}
    ok, n, total = _tally(HERE / "ir_sample_review.md", "verdict", "correct")
    if n:
        out["IR eval-set parsing precision (hand-checked sample)"] = f"{ok}/{n} = {ok / n:.0%}" + (
            f" ({total - n} of {total} not yet marked)" if n < total else "")
    ok, n, total = _tally(HERE / "judge_review.md", "agree", "yes")
    if n:
        out["Human agreement with the LLM judge (hand-checked sample)"] = f"{ok}/{n} = {ok / n:.0%}" + (
            f" ({total - n} of {total} not yet marked)" if n < total else "")
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "hand_checks.json").write_text(json.dumps(out, indent=2))
    update_readme()
    print(json.dumps(out, indent=2) if out else "No marks found yet.")


if __name__ == "__main__":
    main()
