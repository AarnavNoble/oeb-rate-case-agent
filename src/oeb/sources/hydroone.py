"""Hydro One's own posting of the 2028-2032 Joint Rate Application (EB-2026-0164).
As of 2026-10-21 OEB RDS has no records for this case, so the evidence comes from hydroone.com."""

import re
from datetime import date
from pathlib import PurePosixPath
from urllib.parse import unquote

import httpx

from oeb.config import DATA_RAW, USER_AGENT
from oeb.http import _wait_turn
from oeb.sources import DocMeta

HOST = "https://www.hydroone.com"
PAGE = f"{HOST}/about/regulatory/joint-rate-applications"
CASES = {"EB-2026-0164": "2028-32"}

_LINK = re.compile(
    r'href="(/abouthydroone/RegulatoryInformation/JointRateApplications/Documents/([^/"]+)/[^"]+\.pdf)"', re.I)


def _page_html(case: str) -> str:
    cache = DATA_RAW / case / "_listing" / "hydroone_jra.html"
    if cache.exists():
        return cache.read_text()
    _wait_turn("www.hydroone.com")
    r = httpx.get(PAGE, headers={"User-Agent": USER_AGENT}, timeout=60, follow_redirects=True)
    r.raise_for_status()
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(r.text)
    return r.text


def list_case(case: str) -> list[DocMeta]:
    folder = CASES[case]
    seen: dict[str, DocMeta] = {}
    for path, fold in _LINK.findall(_page_html(case)):
        if fold != folder or path in seen:
            continue
        name = PurePosixPath(unquote(path)).stem  # HONI_Appl_Ex B2_TSP_20261007
        m = re.search(r"_(\d{8})$", name)
        seen[path] = DocMeta(
            doc_id="ho-" + re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower(),
            source="hydroone.com",
            case_number=case,
            source_url=HOST + path,
            title=name,
            ext="pdf",
            applicant="Hydro One Networks Inc.",
            doc_type=None,
            date_received=date(int(m[1][:4]), int(m[1][4:6]), int(m[1][6:])) if m else None,
        )
    return list(seen.values())
