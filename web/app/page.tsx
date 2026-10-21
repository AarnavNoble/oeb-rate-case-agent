"use client";

import { useRef, useState, type ReactNode } from "react";
import { CASES, CITE_RE, pdfUrl, readSSE, type Citation, type Hit, type ToolEvent } from "./lib";

const EXAMPLES = [
  "What return on equity did Toronto Hydro use for its 2025 revenue requirement?",
  "Why does Toronto Hydro's short-term debt rate differ from the OEB's deemed rate?",
  "Compare proposed distribution capital spending growth for Toronto Hydro (2025–2029) and Hydro One (2028–2032).",
];

type Mode = "ask" | "search";
type Open = { docId: string; page: number; label: string };

export default function Home() {
  const [mode, setMode] = useState<Mode>("ask");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [tools, setTools] = useState<ToolEvent[]>([]);
  const [citations, setCitations] = useState<Citation[] | null>(null);
  const [hits, setHits] = useState<Hit[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [open, setOpen] = useState<Open | null>(null);
  const abort = useRef<AbortController | null>(null);

  async function submit(q: string) {
    if (!q.trim() || busy) return;
    abort.current?.abort();
    const ctrl = new AbortController();
    abort.current = ctrl;
    setBusy(true);
    setError(null);
    setAnswer("");
    setTools([]);
    setCitations(null);
    setHits(null);
    try {
      if (mode === "search") {
        const res = await fetch(`/api/search?q=${encodeURIComponent(q)}&k=12`, { signal: ctrl.signal });
        if (!res.ok) throw new Error(`search failed: ${res.status}`);
        setHits(await res.json());
        return;
      }
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: q }),
        signal: ctrl.signal,
      });
      if (!res.ok || !res.body) throw new Error(`ask failed: ${res.status}`);
      for await (const { event, data } of readSSE(res)) {
        const d = data as Record<string, unknown>;
        if (event === "text") setAnswer((a) => a + (d.text as string));
        else if (event === "tool_use") setTools((t) => [...t, d as unknown as ToolEvent]);
        else if (event === "done") {
          if (d.answer) setAnswer(d.answer as string);
          setCitations((d.citations as Citation[]) ?? []);
          if (d.error) setError(d.error as string);
        }
      }
    } catch (e) {
      if ((e as Error).name !== "AbortError") setError(String(e));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="flex min-h-screen flex-col lg:flex-row">
      <main className={`w-full flex-1 px-4 py-8 sm:px-8 lg:max-w-3xl lg:px-12 ${open ? "" : "mx-auto"}`}>
        <header className="mb-6">
          <p className="text-xs font-semibold uppercase tracking-widest text-teal-700 dark:text-teal-400">
            Ontario Energy Board · rate cases
          </p>
          <h1 className="mt-1 text-2xl font-semibold tracking-tight">Rate-case research agent</h1>
          <p className="mt-2 text-sm text-neutral-600 dark:text-neutral-400">
            Answers come only from the filings, and every claim links to the page it came from.{" "}
            {Object.entries(CASES).map(([k, v], i) => (
              <span key={k}>
                {i > 0 && " · "}
                <span className="font-mono text-xs">{k}</span> {v}
              </span>
            ))}
          </p>
        </header>

        <form
          onSubmit={(e) => {
            e.preventDefault();
            submit(question);
          }}
          className="space-y-3"
        >
          <div className="flex gap-1 text-sm" role="tablist">
            {(["ask", "search"] as Mode[]).map((m) => (
              <button
                key={m}
                type="button"
                role="tab"
                aria-selected={mode === m}
                onClick={() => setMode(m)}
                className={`rounded-md px-3 py-1 ${mode === m ? "bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900" : "text-neutral-600 hover:bg-neutral-100 dark:text-neutral-400 dark:hover:bg-neutral-800"}`}
              >
                {m === "ask" ? "Ask the agent" : "Search only"}
              </button>
            ))}
          </div>
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) submit(question);
            }}
            rows={3}
            placeholder={mode === "ask" ? "Ask a question about the filings…" : "Search passages…"}
            className="w-full resize-y rounded-lg border border-neutral-300 bg-transparent p-3 text-sm outline-none focus:border-teal-600 dark:border-neutral-700"
          />
          <div className="flex flex-wrap items-center gap-2">
            <button
              type="submit"
              disabled={busy || !question.trim()}
              className="rounded-lg bg-teal-700 px-4 py-2 text-sm font-medium text-white disabled:opacity-40"
            >
              {busy ? "Working…" : mode === "ask" ? "Ask" : "Search"}
            </button>
            {busy && (
              <button type="button" onClick={() => abort.current?.abort()} className="text-sm text-neutral-500 underline">
                Stop
              </button>
            )}
          </div>
          {!answer && !hits && !busy && (
            <ul className="space-y-1 pt-2 text-sm">
              {EXAMPLES.map((ex) => (
                <li key={ex}>
                  <button type="button" onClick={() => setQuestion(ex)} className="text-left text-teal-700 hover:underline dark:text-teal-400">
                    {ex}
                  </button>
                </li>
              ))}
            </ul>
          )}
        </form>

        {tools.length > 0 && (
          <ol className="mt-6 space-y-1 border-l-2 border-neutral-200 pl-3 font-mono text-xs text-neutral-500 dark:border-neutral-800">
            {tools.map((t, i) => (
              <li key={i}>
                {t.name}({describeInput(t.input)})
              </li>
            ))}
          </ol>
        )}

        {error && (
          <p className="mt-6 rounded-md border border-red-300 bg-red-50 p-3 text-sm text-red-800 dark:border-red-900 dark:bg-red-950 dark:text-red-200">
            {error}
          </p>
        )}

        {answer && (
          <article className="prose-sm mt-6 whitespace-pre-wrap text-[15px] leading-7">
            {renderAnswer(answer, citations, setOpen)}
          </article>
        )}

        {citations && citations.length > 0 && (
          <p className="mt-4 text-xs text-neutral-500">
            {citations.length} citation{citations.length === 1 ? "" : "s"}
            {citations.some((c) => !c.seen) && (
              <span className="text-amber-700 dark:text-amber-400">
                {" "}· {citations.filter((c) => !c.seen).length} not backed by a page the agent read
              </span>
            )}
          </p>
        )}

        {hits && (
          <ul className="mt-6 space-y-4">
            {hits.length === 0 && <li className="text-sm text-neutral-500">No results.</li>}
            {hits.map((h) => (
              <li key={h.chunk_id} className="rounded-lg border border-neutral-200 p-3 dark:border-neutral-800">
                <button
                  onClick={() => setOpen({ docId: h.doc_id, page: h.page_start, label: h.citation })}
                  className="text-left text-sm font-medium text-teal-700 hover:underline dark:text-teal-400"
                >
                  {h.citation}
                </button>
                {h.heading && <p className="text-xs text-neutral-500">{h.heading}</p>}
                <p className="mt-1 line-clamp-4 text-sm text-neutral-700 dark:text-neutral-300">{h.text}</p>
              </li>
            ))}
          </ul>
        )}
      </main>

      {open && (
        <aside className="sticky top-0 flex h-[70vh] flex-col border-t border-neutral-200 lg:h-screen lg:flex-1 lg:border-l lg:border-t-0 dark:border-neutral-800">
          <div className="flex items-center justify-between gap-2 px-4 py-2 text-sm">
            <span className="truncate font-medium">{open.label}</span>
            <span className="flex shrink-0 gap-3">
              <a href={pdfUrl(open.docId, open.page)} target="_blank" rel="noreferrer" className="text-teal-700 hover:underline dark:text-teal-400">
                New tab
              </a>
              <button onClick={() => setOpen(null)} className="text-neutral-500 hover:underline">
                Close
              </button>
            </span>
          </div>
          {/* key forces a reload so #page= takes effect when switching citations */}
          <iframe key={`${open.docId}#${open.page}`} src={pdfUrl(open.docId, open.page)} title={open.label} className="flex-1 bg-neutral-100" />
        </aside>
      )}
    </div>
  );
}

function describeInput(input: Record<string, unknown>) {
  if (typeof input.query === "string") return JSON.stringify(input.query);
  if (typeof input.doc_id === "string") return `${input.doc_id}, p.${input.page}`;
  if (typeof input.sql === "string") return input.sql.replace(/\s+/g, " ").slice(0, 80) + "…";
  return "";
}

function renderAnswer(text: string, citations: Citation[] | null, onOpen: (o: Open) => void): ReactNode[] {
  const byKey = new Map((citations ?? []).map((c) => [`${c.doc_id}:${c.page}`, c]));
  const out: ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(CITE_RE)) {
    out.push(text.slice(last, m.index));
    const docId = m[1];
    const page = Number(m[2]);
    const c = byKey.get(`${docId}:${page}`);
    const label = c?.case_number
      ? `${c.case_number} · ${c.exhibit ? `Ex. ${c.exhibit}` : c.title} · p.${page}`
      : `${docId} · p.${page}`;
    const unverified = c && !c.seen;
    out.push(
      <button
        key={`${m.index}`}
        onClick={() => onOpen({ docId, page, label })}
        title={unverified ? "The agent did not read this page — treat with caution" : c?.title ?? docId}
        className={`mx-0.5 inline-flex items-center rounded px-1.5 py-0.5 align-baseline font-mono text-[11px] leading-none ${unverified ? "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-200" : "bg-teal-50 text-teal-800 hover:bg-teal-100 dark:bg-teal-950 dark:text-teal-200"}`}
      >
        {label}
      </button>,
    );
    last = (m.index ?? 0) + m[0].length;
  }
  out.push(text.slice(last));
  return out;
}
