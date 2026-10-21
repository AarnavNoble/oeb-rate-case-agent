from oeb.irparse import ref_to_unit, split_irs, strip_locations, unit_matches
from oeb.search import Hit, collapse_near_duplicates
from oeb.search.hybrid import rrf

VALID = {"1A", "1B", "2B", "4", "5"}

PAGE_1 = """RESPONSES TO SCHOOL ENERGY COALITION INTERROGATORIES
INTERROGATORY 2B-SEC-45
Reference:
Exhibit 2B, Section E5.1, Page 3
Please explain the increase in stations renewal spending between 2025 and 2029.
RESPONSE:
The increase is driven by end-of-life transformers, as described in Exhibit 2B, Section E6.2.
See also Exhibit 4, Tab 2, Schedule 1 and Exhibit K1.2.
"""
PAGE_2 = """RESPONSES TO ONTARIO ENERGY BOARD STAFF INTERROGATORIES
INTERROGATORY 1B-STAFF-7
References:
Exhibit 1B, Tab 2, Schedule 1
Preamble:
Toronto Hydro forecasts customer growth.
QUESTION (A) – (B):
a) Please provide the forecast by class.
RESPONSE (A):
Please see the response to interrogatory 1B-SEC-5.
"""


def test_split_irs_labels_from_response():
    rows = split_irs("doc", [(1, PAGE_1), (2, PAGE_2)], VALID)
    assert [r.ir_id for r in rows] == ["2B-SEC-45", "1B-STAFF-7"]
    a, b = rows
    assert a.reference_exhibits == ["2B"]
    assert a.response_exhibits == ["2B", "4"]  # K1.2 is a hearing exhibit, not evidence
    assert a.question.startswith("Please explain the increase")
    assert (a.page_start, a.page_end) == (1, 1)
    assert b.question.startswith("Toronto Hydro forecasts customer growth.")
    assert "a) Please provide the forecast by class." in b.question
    assert b.response_exhibits == []
    assert (b.page_start, b.page_end) == (2, 2)


def test_units_and_matching():
    rows = split_irs("doc", [(1, PAGE_1)], VALID)
    assert rows[0].response_units == ["2B|E6||", "4||2|1"]
    assert ref_to_unit("Exhibit 4, Tab 2, Schedule 1") == "4||2|1"
    assert ref_to_unit("Exhibit 2B, Section E6") == "2B|E6||"
    assert unit_matches("2B|E6||", "2B|E6||")
    assert not unit_matches("2B|E6||", "2B|E5||")
    assert unit_matches("4||2|", "4||2|14")      # tab-only gold matches any schedule in the tab
    assert not unit_matches("4||2|1", "4||2|14")


def test_query_has_no_location_leakage():
    q = strip_locations("Per Exhibit 2B, Section E5.1, Page 3 and Tab 2, Schedule 1 (see 2B-SEC-45, EB-2023-0195), "
                        "explain the stations renewal increase.")
    for leak in ("2B", "E5.1", "Schedule", "SEC-45", "EB-2023"):
        assert leak not in q
    assert "stations renewal increase" in q


def _hit(cid: int) -> Hit:
    return Hit(cid, "d", "EB", None, "t", 1, 1, None, "x", 0.0)


def test_collapse_near_duplicates_keeps_first_version():
    base = "Table 11 below presents the 2025 forecast versus 2029 forecast PP&E NBV values by asset class " * 3
    hits = [Hit(1, "a", "EB", "2A", "t", 18, 19, None, base, 0.9),
            Hit(2, "b", "EB", "2A", "t", 18, 19, None, base + " Updated", 0.8),
            Hit(3, "c", "EB", "4", "t", 5, 5, None, "Operating expenses for vegetation management", 0.7)]
    assert [h.chunk_id for h in collapse_near_duplicates(hits, k=3)] == [1, 3]
    assert [h.chunk_id for h in collapse_near_duplicates(hits, k=1)] == [1]


def test_rrf_rewards_agreement():
    fused = rrf({"fts": [_hit(1), _hit(2), _hit(3)], "vector": [_hit(3), _hit(4), _hit(1)]}, k=4)
    assert [h.chunk_id for h in fused][:2] == [1, 3]
    assert fused[0].ranks == {"fts": 1, "vector": 3}
