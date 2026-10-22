Retrieval on 472 IR questions (EB-2023-0195), evidence-only index, k=10.

**Exhibit level**: a hit is any chunk from an exhibit the utility cited in its response.

| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 | Median latency |
|---|---|---|---|---|---|
| fts | 0.547 | 0.816 | 0.892 | 0.660 | 133 ms |
| vector | 0.646 | 0.854 | 0.913 | 0.733 | 48 ms |
| hybrid | 0.648 | 0.858 | 0.900 | 0.733 | 247 ms |
| _random chunks (20 seeds)_ | 0.339 | 0.748 | 0.845 | 0.508 |  |
| _label prior (always 2B, 1B, 4, ...)_ | 0.604 | 0.941 | 1.000 | 0.741 |  |

**Section/schedule level** (449 questions whose response cites a section, tab or schedule): a hit is a chunk on a page whose header matches it.

| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 |
|---|---|---|---|---|
| fts | 0.287 | 0.503 | 0.604 | 0.379 |
| vector | 0.425 | 0.628 | 0.719 | 0.514 |
| hybrid | 0.401 | 0.619 | 0.695 | 0.492 |
| _random chunks_ | 0.038 | 0.161 | 0.289 | 0.096 |

Secondary (exhibit level, gold = exhibit named in the question's reference line / IR number):

| Retriever | Recall@5 | MRR@10 |
|---|---|---|
| fts | 0.811 | 0.649 |
| vector | 0.858 | 0.745 |
| hybrid | 0.871 | 0.750 |

Leakage ablation: without the evidence-only filter, hybrid top-5 contains the utility's own answer to the question (matched by text, in any filing) for **60.4%** of questions.
