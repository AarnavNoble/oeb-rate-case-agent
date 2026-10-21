"""Three retrievers over `chunks`, all returning Hits with document/page citations.

Filters are applied inside the SQL, so restricting doc_kinds is equivalent to
removing the other documents from the index (used for the eval leakage control)."""

from dataclasses import dataclass, field


@dataclass
class Filters:
    case_numbers: list[str] | None = None
    doc_kinds: list[str] | None = None
    exclude_doc_kinds: list[str] | None = None

    def sql(self, alias: str = "c") -> tuple[str, list]:
        clauses, params = [], []
        if self.case_numbers:
            clauses.append(f"{alias}.case_number = ANY(%s)")
            params.append(self.case_numbers)
        if self.doc_kinds:
            clauses.append(f"{alias}.doc_kind = ANY(%s)")
            params.append(self.doc_kinds)
        if self.exclude_doc_kinds:
            clauses.append(f"NOT ({alias}.doc_kind = ANY(%s))")
            params.append(self.exclude_doc_kinds)
        return (" AND ".join(clauses) or "TRUE"), params


@dataclass
class Hit:
    chunk_id: int
    doc_id: str
    case_number: str
    exhibit: str | None
    title: str
    page_start: int
    page_end: int
    heading: str | None
    text: str
    score: float
    ranks: dict[str, int] = field(default_factory=dict)

    @property
    def citation(self) -> str:
        pages = f"p.{self.page_start}" if self.page_start == self.page_end else f"pp.{self.page_start}-{self.page_end}"
        ex = f"Exhibit {self.exhibit}" if self.exhibit else self.title
        return f"{self.case_number} / {ex} / {pages}"


NEAR_DUP_JACCARD = 0.8
OVERFETCH = 4  # SQL fetches k * OVERFETCH so k remain after collapsing duplicates


def _shingles(text: str, n: int = 5) -> set[tuple[str, ...]]:
    words = text.lower().split()
    return {tuple(words[i:i + n]) for i in range(max(1, len(words) - n + 1))}


def collapse_near_duplicates(hits: list[Hit], k: int, threshold: float = NEAR_DUP_JACCARD) -> list[Hit]:
    """Keep hits in rank order, dropping any whose word 5-grams overlap a kept hit by
    >= threshold (Jaccard). Re-filed exhibit versions differ only in headers/markers."""
    kept: list[tuple[Hit, set]] = []
    for h in hits:
        sh = _shingles(h.text)
        if any(len(sh & s) / max(1, len(sh | s)) >= threshold for _, s in kept):
            continue
        kept.append((h, sh))
        if len(kept) == k:
            break
    return [h for h, _ in kept]


HIT_COLUMNS ="""c.chunk_id, c.doc_id, c.case_number, c.exhibit, d.title, c.page_start, c.page_end,
                 c.heading, c.text"""


def row_to_hit(row: dict, score: float) -> Hit:
    return Hit(row["chunk_id"], row["doc_id"], row["case_number"], row["exhibit"], row["title"],
               row["page_start"], row["page_end"], row["heading"], row["text"], score)
