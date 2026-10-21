import pymupdf
import pytest

from oeb.chunk import MAX_TOKENS, chunk_pages
from oeb.parse import Line, Page, carry_forward_refs, parse_exhibit_ref, parse_pdf, to_number
from oeb.sources import classify_kind, exhibit_from_title


@pytest.mark.parametrize(("title", "expected"), [
    ("THESL_Exhibit 2B_Asset Management Process_Part2of3_20231117", "2B"),
    ("THESL_Exhibit 1B - Application Overview_20231117", "1B"),
    ("THESL_Exhibit 8 _Rate Design_20231117", "8"),
    ("THESL_IRR Exhibit 2B_Part1of3_20240311", "2B"),
    ("HONI_Appl_Ex B2_TSP_20261007", "B2"),
    ("HONI_Appl_Ex A-01-01_Exhibit List_20261007", "A"),
    ("THESL_2025-2029 Rate Application_Cover Letter_20231117", None),
])
def test_exhibit_from_title(title, expected):
    assert exhibit_from_title(title) == expected


def test_classify_kind_prefers_leaky_type():
    assert classify_kind("Application and Evidence", "x") == "evidence"
    assert classify_kind("Application and Evidence; Interrogatory Response from Applicant", "x") == "ir_response"
    assert classify_kind("Correspondence", "x") == "other"
    assert classify_kind(None, "HONI_Appl_Ex B3_DSP_20261007") == "evidence"
    # mis-tagged on RDS: title wins
    assert classify_kind("Application and Evidence", "THESL_IRR Exhibit 2B_Part3of3_Updated_20240507") == "ir_response"
    assert classify_kind("Application and Evidence", "THESL_2025-2029 Rate Application_IR_Responses_20240311") \
        == "ir_response"
    assert classify_kind("Application and Evidence", "THESL_Exhibit 2B_Capital Expenditure Plan_Part3of3") \
        == "evidence"


def test_parse_exhibit_ref():
    assert parse_exhibit_ref("Toronto Hydro EB-2023-0195 Exhibit 5 Tab 1 Schedule 1 ORIGINAL Page 1 of 7") == (
        "5", "Exhibit 5, Tab 1, Schedule 1")
    assert parse_exhibit_ref("Interrogatory Responses 5-Staff-312") == (None, None)
    assert parse_exhibit_ref("Toronto Hydro EB-2023-0195 Exhibit 2B Section D1 ORIGINAL") == (
        "2B", "Exhibit 2B, Section D1")


def test_carry_forward_refs():
    assert carry_forward_refs([None, "Exhibit 4, Tab 1, Schedule 1", None, None, "Exhibit 4, Tab 2, Schedule 1"]) == [
        None, "Exhibit 4, Tab 1, Schedule 1", "Exhibit 4, Tab 1, Schedule 1", "Exhibit 4, Tab 1, Schedule 1",
        "Exhibit 4, Tab 2, Schedule 1"]


@pytest.mark.parametrize(("s", "v"), [("9.30%", 9.3), ("(1,234)", -1234.0), ("$ 12.5", 12.5), ("2018", 2018.0),
                                      ("n/a", None), ("", None)])
def test_to_number(s, v):
    assert to_number(s) == v


def _page(no, exhibit, n_lines, heading_every=0):
    lines = []
    for i in range(n_lines):
        if heading_every and i % heading_every == 0:
            lines.append(Line(f"{i}. SECTION HEADING {i}", True))
        else:
            lines.append(Line("The utility proposes capital expenditures for distribution renewal. " * 2, False))
    return Page(no, lines, "", None, exhibit)


def test_chunks_respect_max_and_exhibit_boundaries():
    pages = [_page(i, "2B", 30, heading_every=12) for i in range(1, 6)] + [_page(6, "4", 30)]
    chunks = chunk_pages(pages)
    assert chunks
    assert all(c.n_tokens <= MAX_TOKENS + 5 for c in chunks)
    assert all(c.page_start <= c.page_end for c in chunks)
    assert {c.exhibit for c in chunks if c.page_start == 6} == {"4"}
    assert not any(c.exhibit == "2B" and c.page_end == 6 for c in chunks)


def test_parse_pdf_strips_header_and_line_numbers(tmp_path):
    path = tmp_path / "x.pdf"
    doc = pymupdf.open()
    page = doc.new_page(width=612, height=792)
    for i, t in enumerate(["Toronto Hydro-Electric System Limited", "EB-2023-0195", "Exhibit 2B",
                           "Tab 1", "Schedule 1", "Page 1 of 1"]):
        page.insert_text((400, 40 + 11 * i), t, fontsize=9)
    for i, t in enumerate(["CAPITAL PLAN OVERVIEW", "Toronto Hydro plans to invest in renewal."]):
        page.insert_text((70, 200 + 20 * i), str(i + 1), fontsize=9)  # margin line number
        page.insert_text((100, 200 + 20 * i), t, fontsize=11)
    doc.save(path)

    parsed = parse_pdf(str(path))
    p = parsed.pages[0]
    assert p.exhibit == "2B"
    assert p.exhibit_ref == "Exhibit 2B, Tab 1, Schedule 1"
    assert p.text.splitlines() == ["CAPITAL PLAN OVERVIEW", "Toronto Hydro plans to invest in renewal."]
