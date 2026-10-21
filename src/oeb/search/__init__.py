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


HIT_COLUMNS = """c.chunk_id, c.doc_id, c.case_number, c.exhibit, d.title, c.page_start, c.page_end,
                 c.heading, c.text"""


def row_to_hit(row: dict, score: float) -> Hit:
    return Hit(row["chunk_id"], row["doc_id"], row["case_number"], row["exhibit"], row["title"],
               row["page_start"], row["page_end"], row["heading"], row["text"], score)
