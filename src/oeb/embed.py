import threading
from functools import lru_cache

import numpy as np
import torch
from sentence_transformers import SentenceTransformer

from oeb.config import EMBED_MODEL, EMBED_QUERY_PREFIX


@lru_cache(maxsize=1)
def model() -> SentenceTransformer:
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    return SentenceTransformer(EMBED_MODEL, device=device)


_lock = threading.Lock()  # activities run in threads; one model, one encode at a time


def embed_passages(texts: list[str], batch_size: int = 32) -> np.ndarray:
    with _lock:
        return model().encode(texts, batch_size=batch_size, normalize_embeddings=True,
                              convert_to_numpy=True, show_progress_bar=False)


def embed_query(text: str) -> np.ndarray:
    return model().encode(EMBED_QUERY_PREFIX + text, normalize_embeddings=True, convert_to_numpy=True)
