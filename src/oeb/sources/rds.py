"""OEB Regulatory Document Search (Content Manager WebDrawer) JSON API."""

from datetime import date

from oeb.config import DATA_RAW
from oeb.http import get_json
from oeb.sources import DocMeta

BASE = "https://www.rds.oeb.ca/CMWebDrawer"
PAGE_SIZE = 100  # pageSize=1000 times out server-side
PROPS = ",".join([
    "RecordTitle", "RecordNumber", "RecordDateRegistered", "RecordExtension",
    "RecordDocumentSize", "CaseNumber", "Applicant", "SIDocumentType", "fDateReceived",
])


def _val(rec: dict, key: str):
    v = rec.get(key)
    return v.get("Value") if isinstance(v, dict) else v


def _field(rec: dict, key: str) -> str | None:
    f = (rec.get("Fields") or {}).get(key) or {}
    return f.get("StringValue") or f.get("Value") or None


def list_case(case: str) -> list[DocMeta]:
    docs: list[DocMeta] = []
    start = 1
    while True:
        url = (f"{BASE}/Record?q=CaseNumber:{case}&format=json&pageSize={PAGE_SIZE}&start={start}"
               f"&sortBy=recRegisteredOn&properties={PROPS}&propertyValue=both")
        page = get_json(url, DATA_RAW / case / "_listing" / f"rds_{start:05d}.json")
        if page.get("ResponseStatus", {}).get("ErrorCode"):
            raise RuntimeError(f"RDS error for {case}: {page['ResponseStatus']}")
        for rec in page["Results"]:
            docs.append(_to_meta(case, rec))
        if not page.get("HasMoreItems") or not page["Results"]:
            break
        start += PAGE_SIZE
    return docs


def _to_meta(case: str, rec: dict) -> DocMeta:
    uri = rec["Uri"]
    received = _field(rec, "fDateReceived")
    return DocMeta(
        doc_id=f"rds-{uri}",
        source="rds.oeb.ca",
        case_number=case,
        source_url=f"{BASE}/Record/{uri}/File/document",
        title=_val(rec, "RecordTitle") or "",
        ext=(_val(rec, "RecordExtension") or "").lower(),
        record_number=_val(rec, "RecordNumber"),
        applicant=_field(rec, "Applicant"),
        doc_type=_field(rec, "SIDocumentType"),
        date_received=date.fromisoformat(received) if received else None,
        size_bytes=_val(rec, "RecordDocumentSize"),
    )
