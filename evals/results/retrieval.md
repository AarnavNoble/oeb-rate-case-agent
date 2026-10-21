Retrieval on 472 IR questions (EB-2023-0195), evidence-only index, k=10.

**Exhibit level**: a hit is any chunk from an exhibit the utility cited in its response.

| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 | Median latency |
|---|---|---|---|---|---|
| fts | 0.547 | 0.828 | 0.896 | 0.665 | 115 ms |
| vector | 0.646 | 0.856 | 0.913 | 0.733 | 52 ms |
| hybrid | 0.650 | 0.858 | 0.896 | 0.733 | 247 ms |
| _random chunks (20 seeds)_ | 0.339 | 0.748 | 0.845 | 0.508 |  |
| _label prior (always 2B, 1B, 4, ...)_ | 0.604 | 0.941 | 1.000 | 0.741 |  |

**Section/schedule level** (449 questions whose response cites a section, tab or schedule): a hit is a chunk on a page whose header matches it.

| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 |
|---|---|---|---|---|
| fts | 0.281 | 0.506 | 0.606 | 0.377 |
| vector | 0.425 | 0.628 | 0.717 | 0.514 |
| hybrid | 0.396 | 0.617 | 0.697 | 0.489 |
| _random chunks_ | 0.038 | 0.161 | 0.289 | 0.096 |

Secondary (exhibit level, gold = exhibit named in the question's reference line / IR number):

| Retriever | Recall@5 | MRR@10 |
|---|---|---|
| fts | 0.820 | 0.658 |
| vector | 0.858 | 0.745 |
| hybrid | 0.875 | 0.750 |

Leakage ablation: without the evidence-only filter, hybrid top-5 contains the utility's own answer to the question (matched by text, in any filing) for **60.6%** of questions.
