# OEB rate-case research agent

Ask a question about an Ontario Energy Board rate case and get an answer in which every claim
links to the page of the filing it came from. Built over two real proceedings:

| Case | Utility | Filing |
|---|---|---|
| [EB-2023-0195](https://www.rds.oeb.ca/CMWebDrawer/Record?q=CaseNumber:EB-2023-0195) | Toronto Hydro-Electric System Limited | 2025–2029 custom IR application, settled 2024 |
| EB-2026-0164 | Hydro One Networks Inc. | 2028–2032 joint transmission + distribution application, filed 2026-10-07 |

## The problem

A single rate case is hundreds of PDFs and tens of thousands of pages: pre-filed evidence,
interrogatories (written questions from intervenors and OEB staff) and the utility's responses,
undertakings, settlement proposals, decisions. Answering "what is the utility proposing and why"
means finding the right exhibit, tab, schedule and page, and quoting it exactly. This project
ingests whole cases, retrieves at page level, and answers with an agent that must cite pages it
actually read, or say the evidence isn't there.

## Architecture

```mermaid
flowchart LR
  subgraph Sources
    RDS["OEB Regulatory Document Search<br/>(WebDrawer JSON API)"]
    HO["hydroone.com<br/>(EB-2026-0164, not yet on RDS)"]
  end
  subgraph Temporal["Temporal: IngestCaseWorkflow → IngestDocWorkflow per document"]
    L[register_case] --> D["download<br/>queue: oeb-download (3 slots)"]
    D --> P["parse + chunk<br/>queue: oeb-cpu"]
    P --> E["embed<br/>queue: oeb-cpu"]
  end
  RDS --> L
  HO --> L
  D -->|"data/raw/{case}/ (cached, size-verified)"| P
  P --> PG[("Postgres 16 + pgvector<br/>documents · pages · tables · chunks<br/>GIN tsvector · HNSW")]
  E --> PG
  PG --> S["Retrievers<br/>full-text · vector · hybrid (RRF)"]
  S --> MCP["MCP server<br/>search · fetch_page · query_table"]
  MCP --> A["Agent: claude -p<br/>(Claude Code headless)"]
  A --> API["FastAPI<br/>/api/ask (SSE) · /api/search · /api/pdf"]
  API --> UI["Next.js UI<br/>streamed answer · citation → PDF page"]
  PG --> EV["evals/<br/>IR-based retrieval + agent eval"]
```

**Ingestion.** `oeb.sources.rds` lists a case through RDS's JSON search API (100 records per page; 1,000
times out server-side) and downloads each record from `/CMWebDrawer/Record/{uri}/File/document`. Every
request goes through one fetcher that spaces requests ≥1.1 s apart per host (shared across processes
with a file lock), sends a descriptive User-Agent, caches every response on disk, and verifies the byte
count. RDS truncates large files by exactly 80 KiB when it streams the whole file (with a 200 status),
but serves byte ranges intact and reports the true size in `Content-Range`. So files are fetched in
8 MiB ranges, each piece is length-checked, and the total must match both `Content-Range` and the size
RDS lists. PyMuPDF extracts text per page. Margin line numbers and the header block (`Exhibit 2B / Tab 1 /
Schedule 1 / Page n of m`, or `Section D1` in Exhibit 2B) are stripped from the text, and the header
becomes the page's exhibit reference. Appendix pages without a header inherit the preceding schedule's
reference. pdfplumber extracts tables only on pages with ruling lines. Chunks follow detected headings,
target 500–800 tokens, never cross an exhibit boundary, and keep their page range. Embeddings use
`BAAI/bge-small-en-v1.5` locally.

**Orchestration.** One child workflow per document runs download → parse/chunk → embed. Each activity
is idempotent on `documents.status`, so re-running a case skips finished documents. Network-bound and
CPU-bound activities use separate task queues with separate concurrency limits, so a slow RDS response
(RDS sometimes takes >4 minutes to first byte) never blocks parsing. Each host gets one request in
flight at a time, and a host-wide circuit breaker backs off when a server starts failing. Activities
heartbeat, so a restarted worker's work is retried within a minute. Because the download queue is FIFO,
`oeb.crawl --process` can run alongside the worker to fetch the documents the eval needs first; the
workflow's activities then find that work done and skip it.

**Retrieval.** Three retrievers return chunks with case/exhibit/page citations:
1. *Full-text*: Postgres `tsvector` with `ts_rank_cd`. This is BM25-*style*, not BM25: there is no IDF
   term, so query words found in more than 10% of chunks ("toronto", "hydro", "rate") are dropped
   before ranking (a document-frequency table refreshed after each ingest).
2. *Vector*: cosine over bge-small embeddings (HNSW, iterative scan for filtered queries).
3. *Hybrid*: reciprocal rank fusion (k=60) over the top 50 of each.

Utilities re-file updated exhibits, so 16% of Toronto Hydro's chunks are verbatim copies of
another chunk. All retrievers collapse exact copies (hash of normalized text, keeping the latest
filing) and near-copies (word 5-gram Jaccard ≥ 0.8), so re-filings don't crowd out other passages.

**Agent.** The agent runs through Claude Code in headless mode (`claude -p`, model `claude-sonnet-5-5`)
on the user's own Claude plan, not API billing. A guard (`oeb/agent/claude_cli.py`) strips API keys
and cloud-provider settings from the subprocess environment, requires `claude auth status` to report a
claude.ai login, and aborts any run whose init event reports an API key. The agent is isolated from
local Claude Code configuration: no built-in tools, no settings/plugins/CLAUDE.md, no session
persistence. Its only tools come from a stdio
MCP server:
- `search` (hybrid)
- `fetch_page`
- `query_table`: read-only SQL, run as a database role that can only SELECT two views

Every claim must carry a `[cite:doc_id:page]` token copied from a tool result. Tokens are then checked
against the pages the agent actually saw, and unverified ones are flagged in the UI.

## Evaluation

Ground truth comes from the case itself. In OEB proceedings, intervenors file interrogatories (IRs),
and the utility's written responses usually point to the evidence that answers them ("see Exhibit 2B,
Section E5.4"). `evals/build_ir_set.py` parses the utility's IR response documents into
(question, response, exhibits cited in the response) rows and keeps only rows with an explicit exhibit
reference.

**Leakage controls.** The IR responses are part of the corpus, and the questions themselves name
exhibits. So:
- Retrieval during eval is restricted to the utility's pre-filed **evidence**. IR responses,
  undertakings, settlement proposals, arguments and decisions (which quote IR answers) are excluded
  by a filter inside the SQL, which is equivalent to removing them from the index.
- Document type comes from the title as well as RDS's tag. Three Toronto Hydro IR-response updates
  are tagged "Application and Evidence" on RDS; before this fix they sat in the evidence index and
  inflated the scores.
- Queries are the question with every record location stripped: exhibit/tab/schedule/page/section
  references, IR numbers (`2B-SEC-45` encodes the exhibit) and case numbers.
- Gold labels are the locations cited in the *response*, not the question's "Reference:" line (both
  variants are reported). The agent eval also limits the agent's tools to the question's own case.
- An ablation reruns hybrid search with IR documents left in to show what the leak would do.

**Metrics.**
- Retrieval: recall@k and MRR@10 at two levels.
  - **Section/schedule level** is the headline. A hit is a chunk on a page whose header matches a
    section, tab or schedule the utility cited ("Exhibit 4, Tab 2, Schedule 14"; "Exhibit 2B,
    Section E5").
  - **Exhibit level** is reported for completeness but is weak here. There are about a dozen exhibits
    and the labels are skewed toward 2B, so a prior that always answers "2B, 1B, 3" beats every
    retriever.
  - Random-chunk and label-prior baselines are shown next to both.
- Agent (held-out, seeded 20-question slice; small, so the README reports counts alongside rates):
  - citation accuracy, at section/schedule and exhibit level: does it cite a page the utility cited?
  - answer correctness: a Claude Opus 5.5 judge compares the answer with the utility's actual response.
- Sample reviews:
  - 20 seeded IR rows for label quality (`evals/ir_sample_review.md`).
  - 20 judge verdicts for agreement (`evals/judge_review.md`).
  - These were reviewed by Claude, not a human. The sheets say so, and the numbers update if they are
    re-marked by hand (`uv run python -m evals.record_hand_checks`).

## Results

<!-- results:start -->
_Generated by `uv run python -m evals.run` on 2026-10-21._

**Corpus**

| Case | Records | PDFs | Ingested | Pages | Chunks | Tables | MB |
|---|---|---|---|---|---|---|---|
| EB-2023-0195 | 611 | 326 | 242 | 21,660 | 15,084 | 7,538 | 757 |
| EB-2026-0164 | 14 | 14 | 14 | 11,656 | 8,835 | 4,531 | 346 |

84 PDF(s) not ingested: `rds-826353` (listed); `rds-826356` (listed); `rds-826420` (listed); `rds-828245` (listed); `rds-828885` (listed); `rds-830166` (listed); `rds-830168` (listed); `rds-832711` (listed); `rds-832726` (listed); `rds-833550` (listed)

**Retrieval**

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

Eval set: 472 labelled IR questions from 938 parsed interrogatories (21 response documents).

**Agent**

Agent eval on 20 held-out IR questions (agent `claude-sonnet-5-5`, judge `claude-opus-5-5`), evidence-only tools, record locations stripped from questions.

| Metric | Value |
|---|---|
| Citation accuracy, section/schedule level (n=20) | 75.0% |
| Citation accuracy, exhibit level (cites an exhibit the utility cited) | 90.0% |
| Judge: correct | 35.0% |
| Judge: correct or partially correct | 75.0% |
| Verdicts (correct / partial / incorrect / abstained / error) | 7 / 8 / 1 / 4 / 0 |
| Citations to pages the agent never saw | 0.0% |
| Median tool calls / seconds per question | 6 / 26.7 |


**Sample reviews**

- IR eval-set rows passing the full review rubric (complete question, right response, every gold exhibit is an answer location): 8/20 = 40% (reviewed by Claude (claude-opus-5-5 in Claude Code), not a human)
- IR eval-set rows whose gold exhibits locate the answer to the queried question: 14/20 = 70% (reviewed by Claude (claude-opus-5-5 in Claude Code), not a human)
- Agreement with the LLM judge's verdicts: 19/20 = 95% (reviewed by Claude (claude-opus-5-5 in Claude Code), not a human)
<!-- results:end -->

### Reading the results

- **Section/schedule level is the number that matters.**
  - Vector search finds a page from the section or schedule Toronto Hydro cited in the top 5 for
    63% of questions, against 16% for random chunks.
  - Hybrid (62%) does not beat vector here. Full-text (51%) is clearly weaker and pulls the fusion
    down slightly. RRF only helps at exhibit level and on the question-reference variant.
- **Exhibit-level recall looks high but is weak evidence.** There are about a dozen exhibits and
  the labels are skewed toward 2B, so a label prior that always answers "2B, 1B, 4" gets recall@5
  0.94. Retrieval beats it only at rank 1.
- **The leakage control is necessary.** Without it, the utility's own answer to the question
  appears in the top 5 for most questions, so any retrieval number would mostly measure lookup.
- **Agent:**
  - 20 held-out questions, so each answer moves a rate by 5 points.
  - Every citation pointed to a page the agent had actually read.
  - It cited a section or schedule the utility cited for 15 of 20 questions.
  - The judge rated 15 of 20 answers correct or partially correct.
  - Some IR responses contain information created after the evidence was filed: `2B-SEC-69` asks
    for 2023 actuals. "Not in the evidence" is then the right answer, but the judge scores it as an
    abstention, not as correct. The 4 abstentions include cases like this as well as genuine misses
    (`1A-PP-2` was answerable from Exhibit 9).
- **Eval-set label quality (sample of 20, reviewed by Claude, not a human):**
  - 14 of 20 rows have gold exhibits that locate the answer to the question in the query (70%).
  - 8 of 20 pass the stricter rubric, which also requires the question to be complete.
  - The review found two parser bugs, so the retrieval numbers carry this label noise. It applies
    to every retriever and to the random baseline alike.
    - Multi-part IRs: later sub-questions and their answers land in the response field. The query
      is then only part (a), and a gold exhibit can come from a later part.
    - References to exhibits of *other* proceedings ("EB-2018-0165, Exhibit 9") are counted.
  - The judge review found 19 of 20 verdicts agreeable. This is weaker evidence than a human
    check, since the reviewer and the judge are both Claude models.
- **Cross-case comparisons:** six questions comparing Toronto Hydro and Hydro One (capital growth,
  ROE and capital structure, rate frameworks, bill impacts, ...) have no ground truth. They are
  answered in [`evals/results/comparisons.md`](evals/results/comparisons.md) for review.
  - Every answer cites both cases.
  - 1 of 62 citations was flagged by the citation check: the agent shortened a document ID, so it
    pointed at a document that does not exist.
- **Cost:** the agent eval used about $5 equivalent of Claude plan usage (Claude Code's estimate),
  with no API billing.

## Running it

Prerequisites: Docker, [uv](https://docs.astral.sh/uv/), Node 20+, the Temporal CLI
(`brew install temporal`), and [Claude Code](https://claude.com/claude-code) logged in (for the agent).

```bash
uv sync && npm --prefix web install
make up                                    # Postgres + Temporal dev server + worker + API + web UI
uv run python -m oeb.ingest EB-2023-0195   # in another shell; re-run any time, finished docs are skipped
uv run python -m oeb.ingest EB-2026-0164
uv run python -m evals.build_ir_set EB-2023-0195
uv run python -m evals.run                 # regenerates evals/results/* and the Results section above
```

- UI: http://localhost:3077
- API: http://localhost:8077/docs
- Temporal UI: http://localhost:8233

Raw PDFs are cached under `data/raw/` (git-ignored, ~1.25 GB for both cases).

`make check` runs ruff, pyright and pytest.

## Data and attribution

All filings are public records of the Ontario Energy Board's proceedings, retrieved from the
OEB's [Regulatory Document Search](https://www.oeb.ca/rds) and, for EB-2026-0164 (not yet posted
there), from [Hydro One's regulatory site](https://www.hydroone.com/about/regulatory/joint-rate-applications).
Source: Ontario Energy Board. Crown copyright and the filers' own rights apply to the documents.

This repository does not redistribute the PDFs. `data/raw/` is git-ignored, and the crawler fetches
them from the original sources. The eval set (`evals/data/ir_eval.jsonl`) and the hand-check sheets
quote interrogatory questions and Toronto Hydro's responses from the public record of EB-2023-0195,
for evaluation only.

The crawler:
- identifies itself in its User-Agent
- starts at most one request every 1.1 s per host
- keeps one download in flight by default
- backs off host-wide when a server starts failing
- never fetches the same file twice

## Built with Claude Code

This repo was built in a single Claude Code session. Claude Code:
- **Recon:** reverse-engineered the RDS WebDrawer JSON API from the public search form.
- **Code:** wrote the pipeline, retrievers, evals, agent and UI.
- **Debugging:** diagnosed problems from evidence rather than guessing:
  - RDS truncating large files by exactly 80 KiB, found by comparing on-disk bytes with the listed
    size and the PDF's `startxref`, then confirmed with a `Range` request that reports the true size
  - slow downloads blocking parsing, fixed by splitting the Temporal task queues and limiting
    in-flight requests per host instead of per worker
  - full-text search missing an obvious hit because `ts_rank_cd` has no IDF, fixed with the
    document-frequency filter
- **Eval integrity:** questioned its own numbers before reporting them:
  - found IR responses mis-tagged as evidence on RDS that were leaking answers into the index
  - showed that exhibit-level recall loses to a label prior, so added section/schedule-level
    relevance and baselines
  - fixed a leakage ablation that undercounted when the same answer was filed twice
- **Data source:** when RDS slowed to minutes per request, found that Toronto Hydro posts the same
  filings itself. 27 slow files became 2 fast ones.
- **Agent wiring:** set up the agent to run through Claude Code headless, with a guard that refuses to
  run on API billing.

A human made the calls on:
- which cases to use
- crawl politeness (≤1 request/s, backing off when the server struggles)
- running the agent on a Claude subscription instead of API billing
- having Claude do the sample reviews (eval-set labels and judge verdicts) in place of a human; the
  sheets are in `evals/` and record who reviewed them, so they can be re-marked by hand
