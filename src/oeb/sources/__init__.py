import re
from dataclasses import asdict, dataclass
from datetime import date


@dataclass
class DocMeta:
    doc_id: str
    source: str
    case_number: str
    source_url: str
    title: str
    ext: str
    record_number: str | None = None
    applicant: str | None = None
    doc_type: str | None = None
    date_received: date | None = None
    size_bytes: int | None = None

    @property
    def exhibit(self) -> str | None:
        return exhibit_from_title(self.title)

    @property
    def doc_kind(self) -> str:
        return classify_kind(self.doc_type, self.title)

    def row(self) -> dict:
        return asdict(self) | {"exhibit": self.exhibit, "doc_kind": self.doc_kind}


# 'THESL_Exhibit 2B_...', 'THESL_IRR Exhibit 2B_Part1of3', 'HONI_Appl_Ex B2_TSP', 'Ex A-01-01'
_TITLE_EXHIBIT = re.compile(r"(?:^|[_\s])(?:Exhibit|Exh|Ex)\.?\s*([0-9]{1,2}[A-Z]?|[A-Z][0-9]?)(?=[\s_\-–]|$)", re.I)


def exhibit_from_title(title: str) -> str | None:
    m = _TITLE_EXHIBIT.search(title)
    return m.group(1).upper() if m else None


# Ordered: a record tagged with several types takes the first (most leakage-prone) match.
_KIND_RULES: list[tuple[str, str]] = [
    ("Interrogatory Response", "ir_response"),
    ("Interrogatories to", "interrogatory"),
    ("Undertaking Response", "undertaking"),
    ("Settlement", "settlement"),
    ("Transcript", "transcript"),
    ("Argument", "argument"),
    ("Submission", "argument"),
    ("Decision", "decision"),
    ("Rate Order", "decision"),
    ("Intervenor Evidence", "intervenor_evidence"),
    ("Application and Evidence", "evidence"),
]


def classify_kind(doc_type: str | None, title: str) -> str:
    if doc_type:
        for needle, kind in _KIND_RULES:
            if needle.lower() in doc_type.lower():
                return kind
        return "other"
    # hydroone.com has no document type; the 2028-32 page only lists application evidence
    return "ir_response" if re.search(r"\bIRR?\b", title) else "evidence"
