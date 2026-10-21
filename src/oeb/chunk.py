"""Heading-aware chunking: split at detected headings, pack sections into
MIN..MAX token chunks, never cross an exhibit change, keep page ranges."""

from dataclasses import dataclass
from functools import lru_cache

import tiktoken

from oeb.parse import Page

MIN_TOKENS = 500
MAX_TOKENS = 800
OVERLAP_TOKENS = 60


@lru_cache(maxsize=1)
def _enc() -> tiktoken.Encoding:
    return tiktoken.get_encoding("cl100k_base")


def n_tokens(text: str) -> int:
    return len(_enc().encode(text, disallowed_special=()))


@dataclass
class Chunk:
    page_start: int
    page_end: int
    exhibit: str | None
    heading: str | None
    text: str
    n_tokens: int


@dataclass
class _Line:
    page_no: int
    text: str
    tokens: int
    heading: bool


@dataclass
class _Section:
    exhibit: str | None
    heading: str | None
    lines: list[_Line]

    @property
    def tokens(self) -> int:
        return sum(ln.tokens for ln in self.lines)


def _sections(pages: list[Page]) -> list[_Section]:
    out: list[_Section] = []
    cur: _Section | None = None
    for p in pages:
        for ln in p.lines:
            line = _Line(p.page_no, ln.text, n_tokens(ln.text) + 1, ln.heading)
            new_exhibit = cur is not None and p.exhibit != cur.exhibit
            if cur is None or new_exhibit or (ln.heading and not _only_headings(cur)):
                cur = _Section(p.exhibit, ln.text if ln.heading else None, [])
                out.append(cur)
            elif ln.heading and cur.heading:
                cur.heading = f"{cur.heading} / {ln.text}"[:200]  # stacked headings
            elif ln.heading:
                cur.heading = ln.text
            cur.lines.append(line)
    return out


def _only_headings(s: _Section) -> bool:
    return all(ln.heading for ln in s.lines)


def _render(lines: list[_Line]) -> str:
    parts: list[str] = []
    for ln in lines:
        if ln.heading:
            parts.append(("\n" if parts else "") + ln.text + "\n")
        else:
            parts.append(ln.text + " ")
    return "".join(parts).strip()


def _make(lines: list[_Line], exhibit: str | None, heading: str | None) -> Chunk:
    text = _render(lines)
    return Chunk(lines[0].page_no, lines[-1].page_no, exhibit, heading, text, n_tokens(text))


def chunk_pages(pages: list[Page]) -> list[Chunk]:
    chunks: list[Chunk] = []
    buf: list[_Line] = []
    buf_tokens = 0
    buf_exhibit: str | None = None
    buf_heading: str | None = None

    def flush() -> None:
        nonlocal buf, buf_tokens, buf_heading
        if buf:
            prev = chunks[-1] if chunks else None
            if (prev and buf_tokens < MIN_TOKENS // 4 and prev.exhibit == buf_exhibit
                    and prev.n_tokens + buf_tokens <= MAX_TOKENS):
                # fold a small tail into the previous chunk rather than emit a fragment
                merged = prev.text + "\n" + _render(buf)
                chunks[-1] = Chunk(prev.page_start, buf[-1].page_no, prev.exhibit, prev.heading,
                                   merged, n_tokens(merged))
            else:
                chunks.append(_make(buf, buf_exhibit, buf_heading))
        buf, buf_tokens, buf_heading = [], 0, None

    for sec in _sections(pages):
        if buf and sec.exhibit != buf_exhibit:
            flush()
        if sec.tokens > MAX_TOKENS:
            flush()
            chunks.extend(_split_long(sec))
            continue
        if buf and buf_tokens + sec.tokens > MAX_TOKENS:
            flush()
        if not buf:
            buf_exhibit, buf_heading = sec.exhibit, sec.heading
        buf.extend(sec.lines)
        buf_tokens += sec.tokens
        if buf_tokens >= MIN_TOKENS:
            flush()
    flush()
    return [c for c in chunks if c.text]


def _split_long(sec: _Section) -> list[Chunk]:
    """Sliding window over lines: ~MAX_TOKENS-OVERLAP per step, OVERLAP tokens repeated."""
    target = (MIN_TOKENS + MAX_TOKENS) // 2
    out: list[Chunk] = []
    i = 0
    lines = sec.lines
    while i < len(lines):
        j, tok = i, 0
        while j < len(lines) and (tok + lines[j].tokens <= target or j == i):
            tok += lines[j].tokens
            j += 1
        # don't leave a tiny tail; absorb it if it still fits under MAX
        rest = sum(ln.tokens for ln in lines[j:])
        if 0 < rest < MIN_TOKENS // 2 and tok + rest <= MAX_TOKENS:
            j = len(lines)
        window = lines[i:j]
        if sec.heading and not window[0].heading:
            window = [_Line(window[0].page_no, sec.heading, 0, True), *window]
        out.append(_make(window, sec.exhibit, sec.heading))
        if j >= len(lines):
            break
        # step back for overlap
        k, back = j, 0
        while k > i + 1 and back < OVERLAP_TOKENS:
            k -= 1
            back += lines[k].tokens
        i = k
    return out
