import time

from oeb import http


def test_breaker_doubles_cooldown_and_resets(tmp_path, monkeypatch):
    monkeypatch.setattr(http, "_LOCK_DIR", tmp_path)
    host = "example.test"

    http._record(host, ok=False)
    with open(tmp_path / host) as f:
        first = http._load(f)
    assert first["fails"] == 1
    assert 25 < first["cooldown_until"] - time.time() <= http.COOLDOWN_BASE_S

    http._record(host, ok=False)
    with open(tmp_path / host) as f:
        second = http._load(f)
    assert second["cooldown_until"] - time.time() > 55  # doubled

    for _ in range(20):
        http._record(host, ok=False)
    with open(tmp_path / host) as f:
        capped = http._load(f)
    assert capped["cooldown_until"] - time.time() <= http.COOLDOWN_MAX_S

    http._record(host, ok=True)
    with open(tmp_path / host) as f:
        reset = http._load(f)
    assert reset["fails"] == 0 and reset["cooldown_until"] == 0.0


def test_wait_turn_reads_legacy_float_state(tmp_path, monkeypatch):
    monkeypatch.setattr(http, "_LOCK_DIR", tmp_path)
    (tmp_path / "h").write_text("0.0")
    http._wait_turn("h")  # must not raise on the pre-breaker file format
    with open(tmp_path / "h") as f:
        assert http._load(f)["last"] > 0
