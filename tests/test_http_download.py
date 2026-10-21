import hashlib

import httpx
import pytest

from oeb import http

BODY = bytes(range(256)) * 1000  # 256,000 bytes


@pytest.fixture(autouse=True)
def fast(tmp_path, monkeypatch):
    monkeypatch.setattr(http, "_LOCK_DIR", tmp_path / "rl")
    monkeypatch.setattr(http, "MIN_REQUEST_INTERVAL_S", 0)
    monkeypatch.setattr(http, "RANGE_CHUNK", 100_000)
    monkeypatch.setattr(http.time, "sleep", lambda s: None)


def _serve(monkeypatch, handler):
    monkeypatch.setattr(http, "_client", lambda timeout: httpx.Client(transport=httpx.MockTransport(handler)))


def _ranged(truncate_first: bool = False):
    calls = {"n": 0}

    def handler(req: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        start, end = map(int, req.headers["range"].removeprefix("bytes=").split("-"))
        end = min(end, len(BODY) - 1)
        chunk = BODY[start:end + 1]
        if truncate_first and calls["n"] == 1:
            chunk = chunk[:-500]  # like RDS: fewer bytes than the headers promise
        return httpx.Response(206, content=chunk, headers={
            "content-range": f"bytes {start}-{end}/{len(BODY)}", "content-length": str(end - start + 1)})
    return handler, calls


def test_ranged_download_assembles_file(tmp_path, monkeypatch):
    handler, calls = _ranged()
    _serve(monkeypatch, handler)
    sha, n, fetched = http.download("https://x.test/f", tmp_path / "f.pdf", expected_size=len(BODY))
    assert (n, fetched, calls["n"]) == (len(BODY), True, 3)
    assert (tmp_path / "f.pdf").read_bytes() == BODY
    assert sha == hashlib.sha256(BODY).hexdigest()


def test_truncated_range_is_retried(tmp_path, monkeypatch):
    handler, calls = _ranged(truncate_first=True)
    _serve(monkeypatch, handler)
    http.download("https://x.test/f", tmp_path / "f.pdf", expected_size=len(BODY))
    assert (tmp_path / "f.pdf").read_bytes() == BODY
    assert calls["n"] == 4  # first range retried once


def test_server_ignoring_range_gets_full_download(tmp_path, monkeypatch):
    _serve(monkeypatch, lambda req: httpx.Response(200, content=BODY))
    _, n, _ = http.download("https://x.test/f", tmp_path / "f.pdf", expected_size=len(BODY))
    assert n == len(BODY)


def test_listed_size_mismatch_fails_and_leaves_nothing(tmp_path, monkeypatch):
    _serve(monkeypatch, lambda req: httpx.Response(200, content=BODY[:-81920]))
    with pytest.raises(http.FetchError):
        http.download("https://x.test/f", tmp_path / "f.pdf", expected_size=len(BODY))
    assert not (tmp_path / "f.pdf").exists() and not (tmp_path / "f.pdf.part").exists()
