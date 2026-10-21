"""Toronto Hydro's own posting of EB-2023-0195 (2025-2029 rate application).

RDS serves this case slowly (minutes to first byte per request), so two consolidated
files are taken from torontohydro.com instead of ~30 separate RDS records: all
interrogatory responses in one PDF, and the full Exhibit 2B distribution system plan.
Everything else for the case still comes from RDS."""

import re
from html import unescape

import httpx

from oeb.config import DATA_RAW, USER_AGENT
from oeb.http import _wait_turn
from oeb.sources import DocMeta

HOST = "https://www.torontohydro.com"
PAGE = f"{HOST}/regulatory-information/2025-distribution-rate-application"
CASE = "EB-2023-0195"
# slug -> title used for classification (doc kind and exhibit come from the title)
WANTED = {
    "consolidated-interrogatory-responses": "THESL_Consolidated Interrogatory Responses (torontohydro.com)",
    "exhibit-2b-distribution-system-plan": "THESL_Exhibit 2B_Distribution System Plan (torontohydro.com)",
}
_LINK = re.compile(r'href="(?:https://www\.torontohydro\.com)?/documents/d/guest/([a-z0-9\-]+)"')


def _page_html() -> str:
    cache = DATA_RAW / CASE / "_listing" / "torontohydro_2025_application.html"
    if cache.exists():
        return cache.read_text()
    _wait_turn("www.torontohydro.com")
    r = httpx.get(PAGE, headers={"User-Agent": USER_AGENT}, timeout=60, follow_redirects=True)
    r.raise_for_status()
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(r.text)
    return r.text


def list_case(case: str) -> list[DocMeta]:
    if case != CASE:
        return []
    slugs = {unescape(m) for m in _LINK.findall(_page_html())}
    return [DocMeta(doc_id=f"th-{slug}", source="torontohydro.com", case_number=case,
                    source_url=f"{HOST}/documents/d/guest/{slug}", title=title, ext="pdf",
                    applicant="Toronto Hydro-Electric System Limited")
            for slug, title in WANTED.items() if slug in slugs]
