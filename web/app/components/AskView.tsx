"use client";

import { useEffect, useRef, useState } from "react";
import { caseLabel, CASES, fmt, readSSE, type Citation, type Pipeline, type SourceRef, type ToolEvent } from "../lib";
import { Answer } from "./Answer";
import { Composer, type Scope } from "./Composer";
import { Icon } from "./Icon";

const EXAMPLES: { q: string; scope: Scope }[] = [
  { q: "Compare proposed distribution capital spending growth for Toronto Hydro (2025–2029) and Hydro One (2028–2032).", scope: null },
  { q: "What return on equity did Toronto Hydro use for its 2025 revenue requirement?", scope: "EB-2023-0195" },
  { q: "How does Hydro One justify its proposed vegetation management spending?", scope: "EB-2026-0164" },
  { q: "Why does Toronto Hydro's short-term debt rate differ from the OEB's deemed rate?", scope: "EB-2023-0195" },
];

type Turn = {
  id: number;
  question: string;
  scope: Scope;
  answer: string;
  steps: ToolEvent[];
  citations: Citation[] | null;
  error: string | null;
  status: "running" | "done" | "stopped";
  startedAt: number;
  durationMs?: number;
};

function describeStep(t: ToolEvent) {
  const i = t.input;
  if (t.name === "search") return { text: `“${String(i.query ?? "")}”`, meta: i.case_number ? caseLabel(String(i.case_number)) : "both cases" };
  if (t.name === "fetch_page") return { text: `page ${i.page}`, meta: String(i.doc_id ?? "") };
  if (t.name === "query_table") return { text: String(i.sql ?? "").replace(/\s+/g, " ").slice(0, 90), meta: undefined };
  return { text: "", meta: undefined };
}

/** The agent's tool calls, as they happen: the same three tools the MCP server exposes. */
function Trace({ steps, running }: { steps: ToolEvent[]; running: boolean }) {
  const [open, setOpen] = useState(false);
  if (!steps.length && !running) return null;
  const expanded = open || running;
  const count = (name: string) => steps.filter((s) => s.name === name).length;
  const summary = [
    [count("search"), "search", "searches"],
    [count("fetch_page"), "page read", "pages read"],
    [count("query_table"), "table query", "table queries"],
  ]
    .filter(([n]) => n)
    .map(([n, one, many]) => `${n} ${n === 1 ? one : many}`)
    .join(", ");
  return (
    <div className="mb-4 rounded-lg border border-line bg-surface/60">
      <button onClick={() => setOpen(!open)} aria-expanded={expanded} className="flex w-full items-center gap-2 px-3 py-2 text-left text-[13px] text-muted hover:text-text">
        <Icon name="chevron" className={`size-3.5 transition-transform ${expanded ? "rotate-90" : ""}`} />
        {running ? (
          <span className="flex items-center gap-2 text-text">
            <span className="size-1.5 animate-pulse rounded-full bg-amber" />
            Researching the record{steps.length ? `: ${summary}` : ""}
          </span>
        ) : (
          <span>Research trace: {summary || "no tool calls"}</span>
        )}
      </button>
      {expanded && steps.length > 0 && (
        <ol className="space-y-1 border-t border-line px-3 py-2.5">
          {steps.map((s, i) => {
            const d = describeStep(s);
            return (
              <li key={i} className="flex min-w-0 items-baseline gap-3 text-[12.5px]">
                <code className={`w-[86px] shrink-0 font-mono text-[11.5px] ${s.isError ? "text-serious" : "text-amber"}`}>{s.name}</code>
                <span className="truncate text-text/85">{d.text}</span>
                {d.meta && <span className="hidden shrink-0 truncate font-mono text-[11px] text-faint sm:inline">{d.meta}</span>}
                {!s.done && running && i === steps.length - 1 && <span className="size-1.5 shrink-0 animate-pulse rounded-full bg-amber" />}
              </li>
            );
          })}
        </ol>
      )}
    </div>
  );
}

function CopyButton({ text }: { text: string }) {
  const [done, setDone] = useState(false);
  return (
    <button
      onClick={() => {
        navigator.clipboard?.writeText(text).then(() => {
          setDone(true);
          setTimeout(() => setDone(false), 1200);
        });
      }}
      className="flex items-center gap-1.5 rounded-md px-2 py-1 text-[12.5px] text-faint hover:bg-raised hover:text-text"
    >
      <Icon name={done ? "check" : "copy"} className="size-3.5" />
      {done ? "Copied" : "Copy answer"}
    </button>
  );
}

function HowItWorks({ pipeline, onNavigate }: { pipeline: Pipeline | null; onNavigate: (v: "evals" | "data") => void }) {
  const t = pipeline?.totals;
  const n = (v: number | undefined) => (v === undefined ? "…" : fmt.format(v));
  const docs = pipeline?.statuses.find((s) => s.status === "embedded")?.n;
  const steps = [
    ["Collect", <>{n(docs)} PDF filings from the OEB&apos;s document search and the utilities&apos; sites, downloaded by a Temporal workflow.</>],
    ["Index", <>{n(t?.pages)} pages split into {n(t?.chunks)} passages and {n(t?.tables)} tables, searchable by keyword and by meaning.</>],
    ["Research", <>The agent calls <code className="font-mono text-amber">search</code>, <code className="font-mono text-amber">fetch_page</code> and <code className="font-mono text-amber">query_table</code> until it has the evidence, or says it isn&apos;t there.</>],
    ["Cite", <>Every claim points to a case, exhibit and page you can open beside the answer.</>],
    ["Check", <>Cited pages must be ones the agent retrieved, and cited figures are matched against the page.</>],
  ] as const;
  return (
    <section className="mt-14 border-t border-line pt-8" aria-labelledby="how">
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <h2 id="how" className="text-[15px] font-semibold">
          How an answer is made
        </h2>
        <p className="text-[13px] text-muted">
          Measured on 470 real interrogatories:{" "}
          <button onClick={() => onNavigate("evals")} className="text-amber underline-offset-2 hover:underline">
            see the evaluation
          </button>
        </p>
      </div>
      <ol className="mt-5 grid gap-x-6 gap-y-5 sm:grid-cols-2 lg:grid-cols-5">
        {steps.map(([title, body], i) => (
          <li key={title} className="relative">
            <div className="flex items-center gap-2">
              <span className="flex size-6 items-center justify-center rounded-full border border-line-strong font-mono text-[11px] text-muted">{i + 1}</span>
              <h3 className="text-[14px] font-medium">{title}</h3>
            </div>
            <p className="mt-2 text-[13px] leading-relaxed text-muted">{body}</p>
          </li>
        ))}
      </ol>
    </section>
  );
}

export function AskView({
  pipeline,
  active,
  onOpen,
  scope,
  onScope,
  resetSignal,
  onNavigate,
}: {
  pipeline: Pipeline | null;
  active: SourceRef | null;
  onOpen: (s: SourceRef) => void;
  scope: Scope;
  onScope: (s: Scope) => void;
  resetSignal: number;
  onNavigate: (v: "evals" | "data") => void;
}) {
  const [turns, setTurns] = useState<Turn[]>([]);
  const [draft, setDraft] = useState("");
  const abort = useRef<AbortController | null>(null);
  const bottom = useRef<HTMLDivElement>(null);
  const busy = turns.at(-1)?.status === "running";

  useEffect(() => {
    abort.current?.abort();
    setTurns([]);
  }, [resetSignal]);

  const lastSteps = turns.at(-1)?.steps.length;
  const lastStatus = turns.at(-1)?.status;
  useEffect(() => {
    bottom.current?.scrollIntoView({ block: "end", behavior: "smooth" });
  }, [turns.length, lastSteps, lastStatus]);

  function patch(id: number, f: (t: Turn) => Partial<Turn>) {
    setTurns((ts) => ts.map((t) => (t.id === id ? { ...t, ...f(t) } : t)));
  }

  async function ask(q: string, s: Scope = scope) {
    if (!q.trim() || busy) return;
    const ctrl = new AbortController();
    abort.current = ctrl;
    const id = Date.now();
    setTurns((ts) => [...ts, { id, question: q.trim(), scope: s, answer: "", steps: [], citations: null, error: null, status: "running", startedAt: id }]);
    setDraft("");
    try {
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: q.trim(), case: s }),
        signal: ctrl.signal,
      });
      if (!res.ok || !res.body) throw new Error(`The agent couldn't start (HTTP ${res.status}). Check that the API is running.`);
      for await (const { event, data } of readSSE(res)) {
        const d = data as Record<string, unknown>;
        if (event === "text") patch(id, (t) => ({ answer: t.answer + (d.text as string) }));
        else if (event === "tool_use") patch(id, (t) => ({ steps: [...t.steps, d as unknown as ToolEvent] }));
        else if (event === "tool_result")
          patch(id, (t) => {
            const steps = [...t.steps];
            const last = steps.findLastIndex((x) => !x.done);
            if (last >= 0) steps[last] = { ...steps[last], done: true, isError: Boolean(d.is_error) };
            return { steps };
          });
        else if (event === "done")
          patch(id, (t) => ({
            answer: (d.answer as string) || t.answer,
            citations: (d.citations as Citation[]) ?? [],
            error: (d.error as string) ?? null,
            status: "done",
            durationMs: Date.now() - t.startedAt,
          }));
      }
      patch(id, (t) => (t.status === "running" ? { status: "done", durationMs: Date.now() - t.startedAt } : {}));
    } catch (e) {
      if ((e as Error).name === "AbortError") patch(id, () => ({ status: "stopped" }));
      else patch(id, () => ({ status: "done", error: String((e as Error).message ?? e) }));
    }
  }

  if (!turns.length)
    return (
      <div className="mx-auto w-full max-w-[1080px] px-5 pb-16 pt-12 sm:px-8 lg:pt-20">
        <div className="max-w-[760px]">
          <h1 className="text-[34px] font-semibold leading-[1.15] tracking-[-0.015em] text-balance sm:text-[42px]">
            Ask two Ontario rate cases a question. Get the answer with the page it came from.
          </h1>
          <p className="mt-4 max-w-[60ch] text-[16px] leading-relaxed text-muted">
            The agent reads Toronto Hydro&apos;s 2025–2029 and Hydro One&apos;s 2028–2032 applications to the Ontario Energy Board: evidence,
            interrogatory responses, settlements and decisions.
          </p>
          <div className="mt-8">
            <Composer
              value={draft}
              onChange={setDraft}
              onSubmit={() => ask(draft)}
              onStop={() => abort.current?.abort()}
              busy={false}
              scope={scope}
              onScope={onScope}
              placeholder="Ask about spending, rates, a program, or how the two utilities compare"
              autoFocus
            />
          </div>
          <div className="mt-6">
            <h2 className="text-[13px] text-muted">Questions that work well</h2>
            <ul className="mt-2 grid gap-2 sm:grid-cols-2">
              {EXAMPLES.map((ex) => (
                <li key={ex.q}>
                  <button
                    onClick={() => {
                      onScope(ex.scope);
                      ask(ex.q, ex.scope);
                    }}
                    className="h-full w-full rounded-lg border border-line bg-surface/50 px-3.5 py-3 text-left text-[13.5px] leading-snug text-text/85 transition-colors hover:border-line-strong hover:bg-surface hover:text-text"
                  >
                    {ex.q}
                    <span className="mt-1.5 block text-[12px] text-faint">{ex.scope ? CASES[ex.scope]?.utility : "Both cases"}</span>
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </div>
        <HowItWorks pipeline={pipeline} onNavigate={onNavigate} />
      </div>
    );

  return (
    <div className="flex min-h-full flex-col">
      <div className="mx-auto w-full max-w-[820px] flex-1 px-5 pb-10 pt-10 sm:px-8">
        <div className="space-y-16">
          {turns.map((t) => (
            <section key={t.id} aria-label={t.question}>
              <h2 className="text-[22px] font-semibold leading-snug tracking-[-0.01em]">{t.question}</h2>
              <p className="mt-1.5 text-[12.5px] text-faint">
                {t.scope ? `${CASES[t.scope]?.utility} (${t.scope})` : "Both cases"}
                {t.durationMs ? `, answered in ${Math.round(t.durationMs / 1000)} s` : ""}
              </p>
              <div className="mt-5">
                <Trace steps={t.steps} running={t.status === "running"} />
                {t.answer && <Answer text={t.answer} citations={t.citations} streaming={t.status === "running"} active={active} onOpen={onOpen} />}
                {t.status === "stopped" && <p className="mt-2 text-[13px] text-muted">Stopped. Ask again to restart.</p>}
                {t.error && (
                  <div role="alert" className="mt-3 flex gap-2 rounded-lg border border-serious/40 bg-serious/10 px-3 py-2 text-[13px]">
                    <Icon name="alert" className="mt-0.5 size-4 shrink-0 text-serious" />
                    <span className="break-words">{t.error}</span>
                  </div>
                )}
                {t.status === "done" && t.answer && (
                  <div className="mt-3">
                    <CopyButton text={t.answer} />
                  </div>
                )}
              </div>
            </section>
          ))}
        </div>
        <div ref={bottom} />
      </div>
      <div className="sticky bottom-0 border-t border-line bg-ground/90 px-5 py-3 backdrop-blur sm:px-8">
        <div className="mx-auto max-w-[820px]">
          <Composer
            value={draft}
            onChange={setDraft}
            onSubmit={() => ask(draft)}
            onStop={() => abort.current?.abort()}
            busy={busy}
            scope={scope}
            onScope={onScope}
            placeholder="Ask another question. Each one is answered from the filings on its own."
            compact
          />
        </div>
      </div>
    </div>
  );
}
