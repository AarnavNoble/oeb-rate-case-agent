"""PDF -> per-page clean text (+ header exhibit ref, heading-marked lines) and tables.

OEB filings carry a top-right header block (utility, case, 'Exhibit 2B / Tab 1 /
Schedule 1', 'Page n of m') and margin line numbers; both are removed from body text.
PyMuPDF handles text; pdfplumber extracts tables only on pages with ruling lines."""

import itertools
import re
import statistics
from dataclasses import dataclass, field

import pdfplumber
import pymupdf

_LINE_NO = re.compile(r"\d{1,2}")
_HEADING_NUM = re.compile(r"^(?:[A-Z]?\d+(?:\.\d+)*\.?|[A-Z]\.|[IVX]+\.)\s+\S")
_EXHIBIT_REF = re.compile(
    r"Exhibit\s+([0-9]{1,2}[A-Z]?|[A-Z][0-9]?)\b"
    r"(?:[\s,]*Tab\s+(\d+))?(?:[\s,]*Schedule\s+(\d+))?", re.I)


@dataclass
class Line:
    text: str
    heading: bool


@dataclass
class Page:
    page_no: int
    lines: list[Line]
    header: str
    exhibit_ref: str | None
    exhibit: str | None

    @property
    def text(self) -> str:
        return "\n".join(ln.text for ln in self.lines)


@dataclass
class Table:
    page_no: int
    table_idx: int
    header: list[str]
    rows: list[list[str]]


@dataclass
class ParsedDoc:
    pages: list[Page]
    tables: list[Table] = field(default_factory=list)
    table_errors: list[str] = field(default_factory=list)


def parse_exhibit_ref(text: str) -> tuple[str | None, str | None]:
    """'Exhibit 2B Tab 1 Schedule 1' -> ('2B', 'Exhibit 2B, Tab 1, Schedule 1')"""
    m = _EXHIBIT_REF.search(text)
    if not m:
        return None, None
    ex = m.group(1).upper()
    parts = [f"Exhibit {ex}"]
    if m.group(2):
        parts.append(f"Tab {m.group(2)}")
    if m.group(3):
        parts.append(f"Schedule {m.group(3)}")
    return ex, ", ".join(parts)


def _page_lines(page: pymupdf.Page) -> tuple[list[tuple[str, float, bool]], str]:
    """Returns body lines as (text, font_size, all_bold) plus the header text."""
    w, h = page.rect.width, page.rect.height
    header_parts: list[str] = []
    body: list[tuple[str, float, bool]] = []
    layout: dict = page.get_text("dict", sort=True)  # type: ignore[assignment]
    for block in layout["blocks"]:
        for line in block.get("lines", []):
            spans = []
            for s in line["spans"]:
                t = s["text"]
                x0, y0, _, y1 = s["bbox"]
                if not t.strip():
                    continue
                if _LINE_NO.fullmatch(t.strip()) and x0 < 0.14 * w:
                    continue  # margin line number
                if y1 < 0.17 * h and x0 > 0.5 * w:
                    header_parts.append(t.strip())
                    continue
                if y0 > h - 0.06 * h and len(t.strip()) < 40:
                    continue  # footer ('Panel 3', page stamps)
                spans.append(s)
            if not spans:
                continue
            text = " ".join(_join_spans(spans).split())
            if not text:
                continue
            size = max(s["size"] for s in spans)
            bold = all(s["flags"] & 16 or "Bold" in s["font"] for s in spans)
            body.append((text, size, bold))
    return body, " ".join(header_parts)


def _join_spans(spans: list[dict]) -> str:
    """Concatenate spans, inserting a space where the PDF positions words apart
    without an explicit space character ('1.' + 'CAPITAL' -> '1. CAPITAL')."""
    out = spans[0]["text"]
    for prev, s in itertools.pairwise(spans):
        gap = s["bbox"][0] - prev["bbox"][2]
        if gap > 0.15 * s["size"] and not out.endswith(" ") and not s["text"].startswith(" "):
            out += " "
        out += s["text"]
    return out


def _is_heading(text: str, size: float, bold: bool, body_size: float) -> bool:
    if len(text) > 110 or text.endswith((".", ",", ";")) or len(text) < 3:
        return False
    letters = [c for c in text if c.isalpha()]
    if len(letters) < 3:
        return False
    if size >= body_size + 1.5:
        return True
    caps = sum(c.isupper() for c in letters) / len(letters) > 0.85 and len(text.split()) >= 2
    return (bold and (caps or _HEADING_NUM.match(text) is not None or len(text.split()) <= 8)) or (
        caps and _HEADING_NUM.match(text) is not None)


def parse_pdf(path: str, title_exhibit: str | None = None, tables: bool = True) -> ParsedDoc:
    doc = pymupdf.open(path)
    raw: list[tuple[int, list[tuple[str, float, bool]], str]] = []
    sizes: list[float] = []
    ruled_pages: list[int] = []
    for i, page in enumerate(doc.pages()):
        body, header = _page_lines(page)
        raw.append((i + 1, body, header))
        sizes.extend(sz for _, sz, _ in body)
        if tables and _has_ruling(page):
            ruled_pages.append(i + 1)
    doc.close()
    body_size = statistics.median(sizes) if sizes else 11.0

    pages: list[Page] = []
    for page_no, body, header in raw:
        ex, ref = parse_exhibit_ref(header)
        lines = [Line(t, _is_heading(t, sz, b, body_size)) for t, sz, b in body]
        pages.append(Page(page_no, lines, header, ref, ex or title_exhibit))

    out = ParsedDoc(pages)
    if ruled_pages:
        _extract_tables(path, ruled_pages, out)
    return out


def _has_ruling(page: pymupdf.Page) -> bool:
    n = 0
    for d in page.get_drawings():
        for item in d["items"]:
            if item[0] in ("l", "re"):
                n += 1
        if n >= 12:
            return True
    return False


def _clean(cell: str | None) -> str:
    return " ".join((cell or "").split())


def _extract_tables(path: str, page_nos: list[int], out: ParsedDoc) -> None:
    try:
        pdf = pdfplumber.open(path)
    except Exception as e:  # pdfminer is stricter than MuPDF; keep the text, record the loss
        out.table_errors.append(f"open: {type(e).__name__}: {e}"[:300])
        return
    with pdf:
        for page_no in page_nos:
            try:
                found = pdf.pages[page_no - 1].extract_tables()
            except Exception as e:  # malformed page streams; recorded, not fatal
                out.table_errors.append(f"p{page_no}: {type(e).__name__}: {e}"[:300])
                continue
            for idx, t in enumerate(found):
                rows = [[_clean(c) for c in r] for r in t if any(_clean(c) for c in r)]
                if rows:
                    width = max(len(r) for r in rows)
                    rows = [r + [""] * (width - len(r)) for r in rows]
                    keep = [j for j in range(width) if any(r[j] for r in rows)]
                    rows = [[r[j] for j in keep] for r in rows]
                if len(rows) < 2 or max(len(r) for r in rows) < 2:
                    continue
                out.tables.append(Table(page_no, idx, rows[0], rows[1:]))
            pdf.pages[page_no - 1].flush_cache()


_NUM = re.compile(r"^\(?-?\$?\s*-?[\d,]*\.?\d+\s*%?\)?$")


def to_number(s: str) -> float | None:
    s = s.strip()
    if not s or not _NUM.match(s):
        return None
    neg = s.startswith("(") and s.endswith(")") or s.startswith("-") or "$-" in s or "$ -" in s
    v = re.sub(r"[^\d.]", "", s)
    try:
        f = float(v)
    except ValueError:
        return None
    return -f if neg else f
