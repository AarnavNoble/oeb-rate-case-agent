"""LLM judge (run through Claude Code headless on the user's plan, like the agent):
compares the agent's answer with the utility's actual interrogatory response."""

import json
import os
import subprocess
import tempfile

from oeb.agent.claude_cli import check_init_event, claude_bin, plan_env, verify_plan_auth

JUDGE_MODEL = os.environ.get("OEB_JUDGE_MODEL", "claude-opus-5-5")

SYSTEM = """\
You grade answers to interrogatories (written questions) from an Ontario Energy Board rate case. \
You get the question, the utility's own written response (the reference), and a candidate answer \
written by a research assistant that could only read the utility's pre-filed evidence.

Grade whether the candidate's substance agrees with the reference:
- correct: covers the reference's main points and contains nothing that contradicts it. Different \
wording, extra correct context, or citing evidence instead of restating it is fine.
- partially_correct: gets some main points right but misses or misstates others, or is too vague \
to confirm the key figures/positions.
- incorrect: contradicts the reference on a main point (wrong number, wrong position).
- abstained: the candidate says the evidence doesn't answer the question and gives no substantive answer.

Judge only against the reference. If the reference itself only points elsewhere ("see the \
response to 2B-SEC-12"), grade on whatever substance it does contain. Be strict about numbers.\
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["correct", "partially_correct", "incorrect", "abstained"]},
        "rationale": {"type": "string", "description": "One to three sentences."},
    },
    "required": ["verdict", "rationale"],
    "additionalProperties": False,
}


def judge(question: str, reference: str, candidate: str, model: str = JUDGE_MODEL) -> dict:
    prompt = (f"<question>\n{question}\n</question>\n\n<reference_response>\n{reference}\n</reference_response>\n\n"
              f"<candidate_answer>\n{candidate}\n</candidate_answer>\n\nGrade the candidate.")
    verify_plan_auth()  # claude.ai plan login only, never API billing
    with tempfile.TemporaryDirectory(prefix="oeb-judge-") as cwd:
        proc = subprocess.run(
            [claude_bin(), "-p", prompt, "--model", model, "--system-prompt", SYSTEM, "--tools", "",
             "--strict-mcp-config", "--setting-sources", "", "--no-session-persistence",
             "--output-format", "stream-json", "--verbose", "--json-schema", json.dumps(SCHEMA)],
            cwd=cwd, env=plan_env(), capture_output=True, text=True, timeout=600)
    events = []
    for line in proc.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    for ev in events:
        check_init_event(ev)  # raises if this run used an API key
    result = next((ev for ev in reversed(events) if ev.get("type") == "result"), None)
    if result is None:
        raise RuntimeError(f"judge failed (exit {proc.returncode}): {proc.stderr[-800:]}")
    if result.get("is_error") or not result.get("structured_output"):
        raise RuntimeError(f"judge error: {result.get('subtype')} {str(result.get('result'))[:300]}")
    return {**result["structured_output"], "model": model, "cost_usd_equivalent": result.get("total_cost_usd")}
