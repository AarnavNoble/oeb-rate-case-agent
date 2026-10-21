"""Running Claude Code headless on the user's own Claude plan, never on API billing.

Guards, applied to every agent and judge run:
1. credentials and provider switches that would bill an API or cloud account are
   removed from the subprocess environment;
2. `claude auth status` must report a claude.ai (subscription) login, checked once;
3. the run's init event must report apiKeySource == "none"; otherwise it is aborted
   before the model answers.
"""

import functools
import json
import os
import shutil
import subprocess

_BILLED_ENV = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK",
               "CLAUDE_CODE_USE_VERTEX", "CLAUDE_CODE_USE_FOUNDRY", "ANTHROPIC_BASE_URL")


class BillingGuardError(RuntimeError):
    pass


def claude_bin() -> str:
    path = shutil.which("claude")
    if not path:
        raise RuntimeError("Claude Code CLI not found on PATH")
    return path


def plan_env(extra: dict[str, str] | None = None) -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if k not in _BILLED_ENV}
    return {**env, **(extra or {})}


@functools.lru_cache(maxsize=1)
def verify_plan_auth() -> str:
    """Raises unless Claude Code is logged in with a claude.ai subscription account."""
    proc = subprocess.run([claude_bin(), "auth", "status"], env=plan_env(), capture_output=True, text=True,
                          timeout=60)
    try:
        status = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise BillingGuardError(f"could not read `claude auth status`: {proc.stdout[:200]} {proc.stderr[:200]}") from e
    if not status.get("loggedIn") or status.get("authMethod") != "claude.ai" \
            or status.get("apiProvider") != "firstParty":
        raise BillingGuardError(
            f"refusing to run: Claude Code auth is {status.get('authMethod')!r} via {status.get('apiProvider')!r}, "
            "not a claude.ai plan login")
    return status["authMethod"]


def check_init_event(event: dict) -> None:
    if event.get("type") == "system" and event.get("subtype") == "init" and event.get("apiKeySource") != "none":
        raise BillingGuardError(f"refusing to run: Claude Code is using an API key ({event.get('apiKeySource')!r})")
