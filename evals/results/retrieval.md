Retrieval on 470 IR questions (EB-2023-0195), evidence-only index, k=10.

**Exhibit level**: a hit is any chunk from an exhibit the utility cited in its response.

| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 | Median latency |
|---|---|---|---|---|---|
| fts | 0.570 | 0.830 | 0.906 | 0.682 | 234 ms |
| vector | 0.679 | 0.879 | 0.917 | 0.760 | 53 ms |
| hybrid | 0.687 | 0.879 | 0.921 | 0.769 | 344 ms |
| _random chunks (20 seeds)_ | 0.340 | 0.746 | 0.844 | 0.507 |  |
| _label prior (always 2B, 1B, 4, ...)_ | 0.602 | 0.940 | 1.000 | 0.740 |  |

**Section/schedule level** (449 questions whose response cites a section, tab or schedule): a hit is a chunk on a page whose header matches it.

| Retriever | Recall@1 | Recall@5 | Recall@10 | MRR@10 |
|---|---|---|---|---|
| fts | 0.312 | 0.535 | 0.644 | 0.405 |
| vector | 0.463 | 0.677 | 0.748 | 0.551 |
| hybrid | 0.445 | 0.664 | 0.733 | 0.536 |
| _random chunks_ | 0.041 | 0.164 | 0.284 | 0.097 |

Secondary (exhibit level, gold = exhibit named in the question's reference line / IR number):

| Retriever | Recall@5 | MRR@10 |
|---|---|---|
| fts | 0.828 | 0.658 |
| vector | 0.887 | 0.780 |
| hybrid | 0.894 | 0.778 |

Leakage ablation: without the evidence-only filter, hybrid top-5 contains the utility's own answer to the question (matched by text, in any filing) for **65.7%** of questions.
