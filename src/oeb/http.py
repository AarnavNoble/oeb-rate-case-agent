"""Polite HTTP: one request per MIN_REQUEST_INTERVAL_S per host, a host-wide circuit
breaker on failures, descriptive UA, retry on 429/5xx, and an on-disk cache so nothing
is fetched twice."""

import contextlib
import fcntl
import hashlib
import json
import re
import time
from collections.abc import Iterator
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


@contextlib.contextmanager
def _in_flight(host: str) -> Iterator[None]:
    """At most one request in flight per host, across threads and processes. Lets the
    worker run several download slots (cache hits, other hosts) while each server still
    sees one connection at a time."""
    _LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(_LOCK_DIR / f"{host}.inflight", "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield


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


RANGE_CHUNK = 8 << 20
_CONTENT_RANGE = re.compile(r"bytes (\d+)-(\d+)/(\d+)")


def download(url: str, dest: Path, timeout: float = 600.0, attempts: int = 4,
             expected_size: int | None = None) -> tuple[str, int, bool]:
    """Fetch url to dest in RANGE_CHUNK byte ranges. Returns (sha256, bytes, fetched);
    fetched=False means cache hit.

    RDS truncates large files by exactly 80 KiB when streaming a whole file (with a 200
    status), but serves byte ranges intact and reports the true size in Content-Range.
    So we fetch ranges, check every piece's length, and require the total to match both
    Content-Range and expected_size (the source's listed size). Servers that ignore Range
    get a single full download with the same checks."""
    if dest.exists():
        if expected_size is None or dest.stat().st_size == expected_size:
            return _sha256(dest), dest.stat().st_size, False
        dest.unlink()  # cached file from before integrity checks; refetch
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with open(tmp, "wb") as f:
            total = _fetch_ranges(url, f, timeout, attempts)
        if expected_size is not None and total != expected_size:
            raise FetchError(f"size mismatch: got {total} bytes, listed size {expected_size}")
        tmp.rename(dest)
    finally:
        tmp.unlink(missing_ok=True)
    return _sha256(dest), total, True


def _fetch_ranges(url: str, f, timeout: float, attempts: int) -> int:
    host = urlparse(url).netloc
    start, total = 0, None
    while total is None or start < total:
        end = start + RANGE_CHUNK - 1
        last_err: Exception | None = None
        for i in range(attempts):
            try:
                f.seek(start)
                f.truncate()
                n = 0
                with _in_flight(host):
                    _wait_turn(host)
                    with _client(timeout) as c, c.stream("GET", url,
                                                         headers={"Range": f"bytes={start}-{end}"}) as r:
                        status = r.status_code
                        if r.status_code == 429 or r.status_code >= 500:
                            raise FetchError(f"HTTP {r.status_code}")
                        r.raise_for_status()
                        declared = int(r.headers["content-length"]) if "content-length" in r.headers else None
                        if r.status_code == 206:
                            m = _CONTENT_RANGE.fullmatch(r.headers.get("content-range", "").strip())
                            if not m or int(m.group(1)) != start:
                                raise FetchError(f"bad Content-Range: {r.headers.get('content-range')!r}")
                            want, total = int(m.group(2)) - start + 1, int(m.group(3))
                        elif start == 0:  # server ignored Range: whole file in one response
                            want = declared
                        else:
                            raise FetchError(f"server stopped honouring Range at byte {start}")
                        for block in r.iter_bytes(1 << 20):
                            f.write(block)
                            n += len(block)
                if want is not None and n != want:
                    raise FetchError(f"truncated body: got {n} bytes, expected {want}")
                if status != 206:
                    total = n
                _record(host, ok=True)
                break
            except (httpx.HTTPError, FetchError) as e:
                last_err = e
                _record(host, ok=False)
                time.sleep(min(60, 5 * 2**i))
        else:
            raise FetchError(f"{url} bytes {start}-{end}: {last_err}")
        start += n
    return start


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()
