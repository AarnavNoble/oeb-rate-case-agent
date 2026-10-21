"""Split interrogatory-response documents into (question, response, cited exhibits).

Toronto Hydro IRR layout (EB-2023-0195):
    INTERROGATORY 5-STAFF-312
    References: Exhibit 5, Tab 1, Schedule 1, Page 7 ...
    Preamble: ...
    QUESTION (A) – (F): a) ... b) ...
    RESPONSE (A) – (F): ...
The IR id prefix ('5-') and the References block name the exhibit the *question* is
about; gold labels instead come from exhibits cited in the *response* body."""

import re
from dataclasses import dataclass, field

_IR_START = re.compile(
    r"^INTERROGATORY\s+([0-9]{1,2}[A-Z]?)\s*-\s*([A-Z][A-Za-z&.]*(?:\s?[A-Z]+)?)\s*-\s*(\d+[a-z]?)\b", re.M)
_REFERENCES = re.compile(r"^\s*References?\s*:", re.M | re.I)
_PREAMBLE = re.compile(r"^\s*Preamble\s*:", re.M | re.I)
_QUESTION = re.compile(r"^\s*QUESTIONS?\b[^\n]*:?", re.M)
_RESPONSE = re.compile(r"^\s*RESPONSES?\b(?!\s+TO\b)[^\n]*:?", re.M)
_SECTION_BANNER = re.compile(r"^\s*RESPONSES?\s+TO\s+[^\n]*INTERROGATOR[^\n]*$", re.M)
_EXHIBIT_MENTION = re.compile(r"\bExhibits?\s+([0-9]{1,2}[A-Z]?)\b")

# Everything that names a location in the record; removed from queries to avoid leakage.
_LOCATION = re.compile(
    r"\bExhibits?\s+[0-9]{1,2}[A-Z]?\b(?:[\s,]*(?:Tab|Schedule|Section|Page|Pages|Appendix|Attachment|Part|"
    r"Table|Figure|lines?|p\.|pp\.)\s*[A-Z0-9][\w.\-–]*(?:\s*(?:,|and|to|-|–)\s*\d[\w.]*)*)*"
    r"|\b(?:Tab|Schedule|Section|Pages?|Appendix|Attachment)\s+[A-Z]?\d[\w.\-–]*"
    r"|\b[0-9]{1,2}[A-Z]?-[A-Z][A-Za-z]*-\d+[a-z]?\b"
    r"|\bEB-\d{4}-\d{4}\b",
    re.I,
)


@dataclass
class IRRow:
    ir_id: str
    ir_exhibit: str              # exhibit the IR is filed under (question topic)
    intervenor: str
    doc_id: str
    page_start: int
    page_end: int
    references: str
    question: str                # preamble + questions, as filed
    response: str
    reference_exhibits: list[str] = field(default_factory=list)
    response_exhibits: list[str] = field(default_factory=list)
    response_units: list[str] = field(default_factory=list)  # finer refs, see unit_key()

    @property
    def query(self) -> str:
        return strip_locations(self.question)


def strip_locations(text: str) -> str:
    text = _LOCATION.sub(" ", text)
    return re.sub(r"[ \t]+", " ", re.sub(r"\s*\n\s*", "\n", text)).strip()


_UNIT_REF = re.compile(
    r"\bExhibit\s+([0-9]{1,2}[A-Z]?)\b[\s,]*(?:Section\s+([A-Z]{1,2}\d+)(?:\.\d+)*)?"
    r"[\s,]*(?:Tab\s+(\d+))?[\s,]*(?:Schedule\s+(\d+))?")


def unit_key(exhibit: str, section: str | None = None, tab: str | None = None, schedule: str | None = None) -> str:
    """Location below exhibit level: 'exhibit|section|tab|schedule', empty where absent.
    Sections keep only the top level (E5.4 -> E5), matching page headers."""
    return "|".join([exhibit.upper(), (section or "").upper(), tab or "", schedule or ""])


def ref_to_unit(ref: str) -> str | None:
    """Page header ref ('Exhibit 4, Tab 2, Schedule 14' / 'Exhibit 2B, Section E5') -> unit key."""
    m = _UNIT_REF.search(ref)
    return unit_key(*m.groups()) if m else None


def unit_matches(gold: str, page_unit: str) -> bool:
    """A gold unit matches a page if every field the gold reference specifies is equal."""
    return all(g == "" or g == p for g, p in zip(gold.split("|"), page_unit.split("|"), strict=True))


def _units(text: str, valid: set[str]) -> list[str]:
    seen: list[str] = []
    for m in _UNIT_REF.finditer(text):
        ex, section, tab, schedule = m.groups()
        if ex.upper() not in valid or not (section or tab):
            continue  # exhibit-only references carry no finer location
        key = unit_key(ex, section, tab, schedule)
        if key not in seen:
            seen.append(key)
    return seen


def _exhibits(text: str, valid: set[str]) -> list[str]:
    seen: list[str] = []
    for m in _EXHIBIT_MENTION.finditer(text):
        ex = m.group(1).upper()
        if ex in valid and ex not in seen:
            seen.append(ex)
    return seen


_CITATION_LINE = re.compile(
    r"Exhibit|EB-\d|\bPages?\b|\bTab\b|Schedule|Appendix|Attachment|Interrogator|Undertaking"
    r"|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}"
    r"|\b[0-9]{1,2}[A-Z]?-[A-Z]+-\d+", re.I)
_QUESTION_LINE = re.compile(r"^\s*(?:Please\b|[a-z]\)|\([a-z]\))|\?", re.I)


def _split_unlabelled_refs(head: str, start: int) -> tuple[str, int]:
    """No 'Preamble:'/'QUESTION' label: reference lines run until the first line
    that has no citation token or reads as a question, which starts the question."""
    pos = start
    for line in head[start:].splitlines(keepends=True):
        if line.strip() and (not _CITATION_LINE.search(line) or _QUESTION_LINE.search(line)):
            break
        pos += len(line)
    return head[start:pos].strip(), pos


def split_irs(doc_id: str, pages: list[tuple[int, str]], valid_exhibits: set[str]) -> list[IRRow]:
    """pages: [(page_no, text)] for one IRR document."""
    text_parts, offsets = [], []
    pos = 0
    for page_no, t in pages:
        offsets.append((pos, page_no))
        text_parts.append(t + "\n")
        pos += len(t) + 1
    full = "".join(text_parts)

    def page_at(i: int) -> int:
        p = offsets[0][1]
        for start, page_no in offsets:
            if start > i:
                break
            p = page_no
        return p

    starts = list(_IR_START.finditer(full))
    rows: list[IRRow] = []
    for k, m in enumerate(starts):
        end = starts[k + 1].start() if k + 1 < len(starts) else len(full)
        block = full[m.end():end]
        banner = _SECTION_BANNER.search(block)  # next section's 'RESPONSES TO ...' banner
        if banner:
            block = block[:banner.start()]
        block_end = m.end() + len(block.rstrip())
        resp = _RESPONSE.search(block)
        if not resp:
            continue
        head, response = block[:resp.start()], block[resp.start():]
        refs = ""
        rm = _REFERENCES.search(head)
        body_start = 0
        if rm:
            nxt = _PREAMBLE.search(head, rm.end()) or _QUESTION.search(head, rm.end())
            if nxt:
                refs, body_start = head[rm.end():nxt.start()].strip(), nxt.start()
            else:
                refs, body_start = _split_unlabelled_refs(head, rm.end())
        question = head[body_start:].strip()
        question = _PREAMBLE.sub("", question, count=1)
        question = _QUESTION.sub("", question).strip()
        response = _RESPONSE.sub("", response).strip()
        ex, who, num = m.group(1).upper(), m.group(2).upper(), m.group(3)
        rows.append(IRRow(
            ir_id=f"{ex}-{who}-{num}", ir_exhibit=ex, intervenor=who, doc_id=doc_id,
            page_start=page_at(m.start()), page_end=page_at(max(m.start(), block_end - 1)),
            references=refs, question=question, response=response,
            reference_exhibits=_exhibits(refs, valid_exhibits),
            response_exhibits=_exhibits(response, valid_exhibits),
            response_units=_units(response, valid_exhibits),
        ))
    return rows
