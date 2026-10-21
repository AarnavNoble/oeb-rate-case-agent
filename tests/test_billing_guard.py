import json
import subprocess

import pytest

from oeb.agent import claude_cli


def test_plan_env_strips_billing_credentials(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    monkeypatch.setenv("CLAUDE_CODE_USE_BEDROCK", "1")
    env = claude_cli.plan_env({"MCP_TIMEOUT": "1"})
    assert "ANTHROPIC_API_KEY" not in env and "CLAUDE_CODE_USE_BEDROCK" not in env
    assert env["MCP_TIMEOUT"] == "1"


def test_init_event_with_api_key_is_refused():
    claude_cli.check_init_event({"type": "system", "subtype": "init", "apiKeySource": "none"})
    with pytest.raises(claude_cli.BillingGuardError):
        claude_cli.check_init_event({"type": "system", "subtype": "init", "apiKeySource": "ANTHROPIC_API_KEY"})


@pytest.mark.parametrize(("status", "ok"), [
    ({"loggedIn": True, "authMethod": "claude.ai", "apiProvider": "firstParty"}, True),
    ({"loggedIn": True, "authMethod": "api_key", "apiProvider": "firstParty"}, False),
    ({"loggedIn": True, "authMethod": "claude.ai", "apiProvider": "bedrock"}, False),
    ({"loggedIn": False}, False),
])
def test_verify_plan_auth(monkeypatch, status, ok):
    claude_cli.verify_plan_auth.cache_clear()
    monkeypatch.setattr(claude_cli, "claude_bin", lambda: "claude")
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: subprocess.CompletedProcess(a, 0, json.dumps(status), ""))
    if ok:
        assert claude_cli.verify_plan_auth() == "claude.ai"
    else:
        with pytest.raises(claude_cli.BillingGuardError):
            claude_cli.verify_plan_auth()
    claude_cli.verify_plan_auth.cache_clear()
