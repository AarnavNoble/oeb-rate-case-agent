export type Citation = {
  doc_id: string;
  page: number;
  case_number: string | null;
  exhibit: string | null;
  title: string | null;
  seen: boolean;
};

export type ToolEvent = { name: string; input: Record<string, unknown>; isError?: boolean; done?: boolean };

export type Hit = {
  chunk_id: number;
  doc_id: string;
  case_number: string;
  exhibit: string | null;
  title: string;
  page_start: number;
  page_end: number;
  heading: string | null;
  text: string;
  score: number;
  citation: string;
};

export type CaseStats = {
  case_number: string;
  applicant: string;
  documents: number;
  pages: number;
  first_filed: string | null;
  last_filed: string | null;
};

export type Doc = {
  doc_id: string;
  case_number: string;
  title: string;
  exhibit: string | null;
  doc_kind: string;
  doc_type: string | null;
  n_pages: number | null;
  date_received: string | null;
};

export type PageText = {
  doc_id: string;
  case_number: string;
  title: string;
  exhibit: string | null;
  record_number: string | null;
  date_received: string | null;
  n_pages: number | null;
  source_url: string;
  page_no: number;
  text: string;
  exhibit_ref: string | null;
};

/** What the source panel shows: a page, plus the claim it was cited for (if any). */
export type SourceRef = { docId: string; page: number; claim?: string; n?: number };

export const CASES: Record<string, { utility: string; period: string }> = {
  "EB-2023-0195": { utility: "Toronto Hydro", period: "2025–2029" },
  "EB-2026-0164": { utility: "Hydro One", period: "2028–2032" },
};

export const CITE_RE = /\[cite:([A-Za-z0-9_-]+):(\d+)\]/g;

export function pdfUrl(docId: string, page: number) {
  return `/api/pdf/${encodeURIComponent(docId)}#page=${page}`;
}

export function caseLabel(caseNumber: string | null | undefined) {
  return (caseNumber && CASES[caseNumber]?.utility) ?? caseNumber ?? "Unknown case";
}

export const fmt = new Intl.NumberFormat("en-CA");

export function fmtDate(d: string | null | undefined) {
  if (!d) return "—";
  return new Date(`${d}T00:00:00`).toLocaleDateString("en-CA", { year: "numeric", month: "short", day: "numeric" });
}

/** Minimal SSE parser over a fetch() body. */
export async function* readSSE(res: Response): AsyncGenerator<{ event: string; data: unknown }> {
  const reader = res.body!.pipeThrough(new TextDecoderStream()).getReader();
  let buf = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += value;
    let i: number;
    while ((i = buf.indexOf("\n\n")) >= 0) {
      const raw = buf.slice(0, i);
      buf = buf.slice(i + 2);
      let event = "message";
      const data: string[] = [];
      for (const line of raw.split("\n")) {
        if (line.startsWith("event:")) event = line.slice(6).trim();
        else if (line.startsWith("data:")) data.push(line.slice(5).trimStart());
      }
      if (data.length) yield { event, data: JSON.parse(data.join("\n")) };
    }
  }
}

const STOP = new Set(
  "the and for that with this from are was were has have had its their which will would been being into than then also such these those there they what when where while about over under only more most other some each both very can may per not but all any our out his her one two".split(
    " ",
  ),
);

function terms(s: string) {
  return (s.toLowerCase().match(/[a-z0-9$.%]+/g) ?? [])
    .map((t) => t.replace(/^[.]+|[.]+$/g, ""))
    .filter((t) => (t.length > 3 || /\d/.test(t)) && !STOP.has(t));
}

/**
 * Re-flow a PDF page's hard-wrapped lines into blocks (paragraphs, headings, table rows) and pick the
 * block that best matches the claim. Numbers count double: a cited figure is the strongest signal.
 * This is a display aid only: the agent cites pages, not passages.
 */
export function pageBlocks(text: string, claim?: string): { blocks: string[]; best: number } {
  const blocks: string[] = [];
  let cur = "";
  for (const raw of text.split("\n")) {
    const line = raw.trim();
    if (!line) {
      if (cur) blocks.push(cur);
      cur = "";
      continue;
    }
    if (!cur) cur = line;
    else if (/[.:;?!]$/.test(cur) || /^(\d+(\.\d+)+|[A-Z][A-Z\s&,-]{6,}$|Table \d|Figure \d|•|-\s)/.test(line)) {
      blocks.push(cur);
      cur = line;
    } else cur += (cur.endsWith("-") ? "" : " ") + line;
  }
  if (cur) blocks.push(cur);
  if (!claim) return { blocks, best: -1 };
  const want = new Set(terms(claim));
  let best = -1;
  let bestScore = 1.5;
  blocks.forEach((b, i) => {
    const got = new Set(terms(b));
    let score = 0;
    for (const t of want) if (got.has(t)) score += /\d/.test(t) ? 2 : 1;
    if (score > bestScore) {
      best = i;
      bestScore = score;
    }
  });
  return { blocks, best };
}

/** Figures in a claim worth checking against the page: "9.36%", "$220.9M", "5,899.1" (not bare years or list numbers). */
export function claimFigures(claim: string | undefined): string[] {
  const out = new Set<string>();
  for (const m of (claim ?? "").matchAll(/\$?\d[\d,]*(\.\d+)?/g)) {
    const n = m[0].replace(/[$,]/g, "");
    if (/^(19|20)\d\d$/.test(n) || n.replace(".", "").length < 3) continue;
    out.add(n);
  }
  return [...out];
}

export function figuresOn(text: string, figures: string[]) {
  const flat = text.replace(/(\d),(\d)/g, "$1$2");
  return figures.filter((f) => new RegExp(`(^|[^\\d.])${f.replace(".", "\\.")}(?![\\d])`).test(flat));
}

export type RetrieverScores = { n: number; "recall@1": number; "recall@5": number; "recall@10": number; "mrr@10": number };

export type AgentRun = {
  ir_id: string;
  query: string;
  gold_exhibits: string[];
  cited_exhibits: string[];
  citation_hit: boolean;
  section_hit: boolean | null;
  verdict: "correct" | "partially_correct" | "incorrect" | "abstained" | "error";
  rationale: string;
  n_unverified: number;
  seconds: number;
};

export type Evals = {
  retrieval: {
    n_rows: number;
    n_unit_rows: number;
    retrievers: Record<string, { response_gold: RetrieverScores; unit_gold: RetrieverScores; median_latency_ms: number }>;
    baselines: { random_chunks: { unit: RetrieverScores } };
    leakage_ablation: { share: number };
  };
  agent: {
    n: number;
    agent_model: string;
    judge_model: string;
    citation_accuracy: number;
    citation_unit_accuracy: number;
    correct_or_partial_rate: number;
    unverified_citation_rate: number;
    verdicts: Record<string, number>;
    median_seconds: number;
    median_tool_calls: number;
  };
  hand_checks: Record<string, string>;
  runs: AgentRun[];
};

export type Pipeline = {
  statuses: { status: string; n: number }[];
  sources: { source: string; n: number }[];
  totals: { pages: number; chunks: number; tables: number };
  corpus: {
    cases: { case_number: string; records: number; pdfs: number; ingested: number; mb: string; pages: number; chunks: number; tables: number }[];
    stage_hours_summed: { download_h: string; parse_h: string; embed_h: string };
  };
};

/** "EB-2023-0195, Exhibit 2B, p. 89": the way a filing cites itself. */
export function recordRef(caseNumber: string | null | undefined, exhibit: string | null | undefined, page: number) {
  return [caseNumber, exhibit ? `Exhibit ${exhibit}` : null, `p. ${page}`].filter(Boolean).join(", ");
}
