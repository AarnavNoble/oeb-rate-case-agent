"""Polite HTTP: one request per MIN_REQUEST_INTERVAL_S per host, a host-wide circuit
breaker on failures, descriptive UA, retry on 429/5xx, and an on-disk cache so nothing
is fetched twice."""

import fcntl
import hashlib
import json
import time
from pathlib import Path
from urllib.parse import urlparse

import httpx

from oeb.config import DATA_RAW, MIN_REQUEST_INTERVAL_S, USER_AGENT

_LOCK_DIR = DATA_RAW / ".ratelimit"


class FetchError(Exception):
    pass


COOLDOWN_BASE_S = 30.0
COOLDOWN_MAX_S = 600.0  # below the download activity's 15 min start-to-close timeout


def _load(f) -> dict:
    f.seek(0)
    raw = f.read().strip()
    try:
        state = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        state = {}
    return state if isinstance(state, dict) else {"last": float(state)}


def _store(f, state: dict) -> None:
    f.seek(0)
    f.truncate()
    f.write(json.dumps(state))


def _wait_turn(host: str) -> None:
    """Cross-process rate limit and circuit breaker: a lock file per host holds the last
    request time and a cooldown. Temporal runs many activities (each with its own retry
    backoff) at once, so per-request backoff alone still lets a failing host get a steady
    stream of requests; the shared cooldown stops that."""
    _LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(_LOCK_DIR / host, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        state = _load(f)
        resume_at = max(state.get("last", 0.0) + MIN_REQUEST_INTERVAL_S, state.get("cooldown_until", 0.0))
        delay = resume_at - time.time()
        if delay > 0:
            time.sleep(delay)
        state["last"] = time.time()
        _store(f, state)
        # lock released on close


def _record(host: str, ok: bool) -> None:
    """Success resets the breaker; each failure doubles the host-wide cooldown."""
    _LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(_LOCK_DIR / host, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        state = _load(f)
        if ok:
            state["fails"] = 0
            state["cooldown_until"] = 0.0
        else:
            fails = state.get("fails", 0) + 1
            state["fails"] = fails
            state["cooldown_until"] = time.time() + min(COOLDOWN_MAX_S, COOLDOWN_BASE_S * 2 ** (fails - 1))
        _store(f, state)


def _client(timeout: float) -> httpx.Client:
    return httpx.Client(headers={"User-Agent": USER_AGENT}, timeout=timeout, follow_redirects=True)


def get_json(url: str, cache_path: Path, timeout: float = 180.0, attempts: int = 4) -> dict:
    if cache_path.exists():
        return json.loads(cache_path.read_text())
    host = urlparse(url).netloc
    last_err: Exception | None = None
    for i in range(attempts):
        _wait_turn(host)
        try:
            with _client(timeout) as c:
                r = c.get(url)
            if r.status_code == 429 or r.status_code >= 500:
                raise FetchError(f"HTTP {r.status_code}")
            r.raise_for_status()
            data = r.json()
            _record(host, ok=True)
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(json.dumps(data))
            return data
        except (httpx.HTTPError, FetchError) as e:
            last_err = e
            _record(host, ok=False)
            time.sleep(min(60, 5 * 2**i))
    raise FetchError(f"{url}: {last_err}")


def download(url: str, dest: Path, timeout: float = 600.0, attempts: int = 4,
             expected_size: int | None = None) -> tuple[str, int, bool]:
    """Stream url to dest. Returns (sha256, bytes, fetched). fetched=False means cache hit.
    The byte count must match Content-Length and expected_size (the source's listed size)
    when known; RDS has served a body 80 KiB short with a 200 status."""
    if dest.exists():
        if expected_size is None or dest.stat().st_size == expected_size:
            return _sha256(dest), dest.stat().st_size, False
        dest.unlink()  # cached file from before integrity checks; refetch
    host = urlparse(url).netloc
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    last_err: Exception | None = None
    for i in range(attempts):
        _wait_turn(host)
        try:
            h = hashlib.sha256()
            n = 0
            with _client(timeout) as c, c.stream("GET", url) as r:
                if r.status_code == 429 or r.status_code >= 500:
                    raise FetchError(f"HTTP {r.status_code}")
                r.raise_for_status()
                declared = int(r.headers["content-length"]) if "content-length" in r.headers else None
                with open(tmp, "wb") as f:
                    for block in r.iter_bytes(1 << 20):
                        f.write(block)
                        h.update(block)
                        n += len(block)
            for want, what in ((declared, "Content-Length"), (expected_size, "listed size")):
                if want is not None and n != want:
                    raise FetchError(f"truncated body: got {n} bytes, {what} {want}")
            tmp.rename(dest)
            _record(host, ok=True)
            return h.hexdigest(), n, True
        except (httpx.HTTPError, FetchError) as e:
            last_err = e
            _record(host, ok=False)
            tmp.unlink(missing_ok=True)
            time.sleep(min(60, 5 * 2**i))
    raise FetchError(f"{url}: {last_err}")


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()
