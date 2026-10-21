"""Reciprocal rank fusion of the full-text and vector retrievers."""

from oeb.search import Filters, Hit, fts, vector

RRF_K = 60
CANDIDATES = 50


def rrf(rankings: dict[str, list[Hit]], k: int = 10, rrf_k: int = RRF_K) -> list[Hit]:
    fused: dict[int, Hit] = {}
    scores: dict[int, float] = {}
    for name, hits in rankings.items():
        for rank, h in enumerate(hits, 1):
            hit = fused.setdefault(h.chunk_id, h)
            hit.ranks[name] = rank
            scores[h.chunk_id] = scores.get(h.chunk_id, 0.0) + 1.0 / (rrf_k + rank)
    ordered = sorted(fused, key=lambda cid: (-scores[cid], cid))[:k]
    out = []
    for cid in ordered:
        h = fused[cid]
        h.score = scores[cid]
        out.append(h)
    return out


def search(query: str, k: int = 10, filters: Filters | None = None) -> list[Hit]:
    return rrf({"fts": fts.search(query, CANDIDATES, filters),
                "vector": vector.search(query, CANDIDATES, filters)}, k)
