"use client";

import { useEffect, useRef, useState } from "react";
import { caseLabel, CASES, fmt, readSSE, type CaseStats, type Citation, type SourceRef, type ToolEvent } from "../lib";
import { Answer } from "./Answer";
import { Composer, type Scope } from "./Composer";
import { Icon, Mark } from "./Icon";

const EXAMPLES = [
  "What return on equity did Toronto Hydro use for its 2025 revenue requirement?",
  "Why does Toronto Hydro's short-term debt rate differ from the OEB's deemed rate?",
  "How does Hydro One justify its proposed vegetation management spending?",
  "Compare proposed distribution capital spending growth for Toronto Hydro (2025–2029) and Hydro One (2028–2032).",
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
  if (t.name === "search")
    return { icon: "search" as const, text: `Searched “${String(i.query ?? "")}”`, meta: i.case_number ? caseLabel(String(i.case_number)) : undefined };
  if (t.name === "fetch_page") return { icon: "page" as const, text: `Read page ${i.page}`, meta: String(i.doc_id ?? "") };
  if (t.name === "query_table")
    return { icon: "table" as const, text: "Queried extracted tables", meta: String(i.sql ?? "").replace(/\s+/g, " ").slice(0, 70) };
  return { icon: "chevron" as const, text: t.name, meta: undefined };
}

function Steps({ steps, running }: { steps: ToolEvent[]; running: boolean }) {
  const [open, setOpen] = useState(false);
  if (!steps.length && !running) return null;
  const expanded = open || running;
  const reads = steps.filter((s) => s.name === "fetch_page").length;
  const searches = steps.filter((s) => s.name === "search").length;
  return (
    <div className="mb-3 text-[12.5px]">
      <button onClick={() => setOpen(!open)} className="flex items-center gap-1.5 text-muted hover:text-ink">
        <Icon name="chevron" className={`size-3.5 transition-transform ${expanded ? "rotate-90" : ""}`} />
        {running ? (
          <span className="flex items-center gap-2">
            Researching the filings
            <span className="flex gap-0.5">
              {[0, 1, 2].map((d) => (
                <span key={d} className="size-1 animate-bounce rounded-full bg-muted" style={{ animationDelay: `${d * 120}ms` }} />
              ))}
            </span>
          </span>
        ) : (
          <span>
            {searches} search{searches === 1 ? "" : "es"} · {reads} full page{reads === 1 ? "" : "s"} opened
          </span>
        )}
      </button>
      {expanded && steps.length > 0 && (
        <ol className="ml-[7px] mt-2 space-y-1.5 border-l border-line pl-4">
          {steps.map((s, i) => {
            const d = describeStep(s);
            return (
              <li key={i} className="flex min-w-0 items-center gap-2 text-muted">
                <Icon name={d.icon} className={`size-3.5 shrink-0 ${s.isError ? "text-warn" : "text-faint"}`} />
                <span className="truncate text-ink/85">{d.text}</span>
                {d.meta && <span className="truncate font-mono text-[10.5px] text-faint">{d.meta}</span>}
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
      aria-label="Copy answer"
      className="rounded-md p-1.5 text-faint hover:bg-sunken hover:text-ink"
    >
      <Icon name={done ? "check" : "copy"} className="size-3.5" />
    </button>
  );
}

export function AskView({
  corpus,
  active,
  onOpen,
  scope,
  onScope,
  resetSignal,
}: {
  corpus: CaseStats[] | null;
  active: SourceRef | null;
  onOpen: (s: SourceRef) => void;
  scope: Scope;
  onScope: (s: Scope) => void;
  resetSignal: number;
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

  async function ask(q: string) {
    if (!q.trim() || busy) return;
    const ctrl = new AbortController();
    abort.current = ctrl;
    const id = Date.now();
    setTurns((ts) => [...ts, { id, question: q.trim(), scope, answer: "", steps: [], citations: null, error: null, status: "running", startedAt: id }]);
    setDraft("");
    try {
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: q.trim(), case: scope }),
        signal: ctrl.signal,
      });
      if (!res.ok || !res.body) throw new Error(`The agent request failed (${res.status}).`);
      for await (const { event, data } of readSSE(res)) {
        const d = data as Record<string, unknown>;
        if (event === "text") patch(id, (t) => ({ answer: t.answer + (d.text as string) }));
        else if (event === "tool_use") patch(id, (t) => ({ steps: [...t.steps, d as unknown as ToolEvent] }));
        else if (event === "tool_result")
          patch(id, (t) => {
            const steps = [...t.steps];
            const last = steps.findLastIndex((s) => !s.done);
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

  const totals = corpus && {
    docs: corpus.reduce((a, c) => a + c.documents, 0),
    pages: corpus.reduce((a, c) => a + c.pages, 0),
  };

  if (!turns.length)
    return (
      <div className="flex min-h-[calc(100vh-3.5rem)] flex-col items-center justify-center px-4 py-12 lg:min-h-screen">
        <div className="w-full max-w-[680px]">
          <div className="mb-7 flex flex-col items-center text-center">
            <Mark className="size-10" />
            <h1 className="mt-4 text-[26px] font-semibold tracking-tight">Ask the rate-case record</h1>
            <p className="mt-2 max-w-md text-[13.5px] leading-relaxed text-muted">
              Answers come only from Ontario Energy Board filings, and every claim links to the page it came from.
            </p>
            {totals && (
              <p className="mt-3 font-mono text-[11px] text-faint">
                {corpus!.length} cases · {fmt.format(totals.docs)} filings · {fmt.format(totals.pages)} pages indexed
              </p>
            )}
          </div>
          <Composer
            value={draft}
            onChange={setDraft}
            onSubmit={() => ask(draft)}
            onStop={() => abort.current?.abort()}
            busy={false}
            scope={scope}
            onScope={onScope}
            placeholder="Ask about a filing, an interrogatory, or how the two cases compare…"
            autoFocus
          />
          <div className="mt-6">
            <p className="mb-2 flex items-center gap-1.5 text-[12px] text-muted">
              <Icon name="bulb" className="size-3.5" /> Need ideas?
            </p>
            <div className="grid gap-2 sm:grid-cols-2">
              {EXAMPLES.map((ex) => (
                <button
                  key={ex}
                  onClick={() => ask(ex)}
                  className="rounded-lg border border-line bg-panel px-3 py-2.5 text-left text-[13px] leading-snug text-ink/85 transition-colors hover:border-line-strong hover:bg-sunken"
                >
                  {ex}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>
    );

  return (
    <div className="flex min-h-[calc(100vh-3.5rem)] flex-col lg:min-h-screen">
      <div className="mx-auto w-full max-w-[760px] flex-1 px-4 pb-8 pt-8 sm:px-6">
        <div className="space-y-10">
          {turns.map((t) => (
            <section key={t.id}>
              <div className="flex justify-end">
                <div className="max-w-[85%] rounded-2xl rounded-br-md bg-sunken px-4 py-2.5 text-[14px] leading-relaxed">{t.question}</div>
              </div>
              <p className="mt-5 font-mono text-[10.5px] text-faint">
                {new Date(t.startedAt).toLocaleTimeString("en-CA", { hour: "numeric", minute: "2-digit" })}
                {" · "}
                {t.scope ? `${CASES[t.scope]?.utility} · ${t.scope}` : "Both cases"}
                {t.durationMs ? ` · ${Math.round(t.durationMs / 1000)} s` : ""}
              </p>
              <div className="mt-2 flex gap-3">
                <Mark className="size-7 shrink-0" />
                <div className="min-w-0 flex-1 pt-0.5">
                  <Steps steps={t.steps} running={t.status === "running"} />
                  {t.answer && <Answer text={t.answer} citations={t.citations} streaming={t.status === "running"} active={active} onOpen={onOpen} />}
                  {t.status === "stopped" && <p className="mt-2 text-[13px] text-muted">Stopped.</p>}
                  {t.error && (
                    <div className="mt-3 flex gap-2 rounded-lg border border-warn/30 bg-warn-bg px-3 py-2 text-[13px] text-warn">
                      <Icon name="alert" className="mt-0.5 size-4 shrink-0" />
                      <span className="break-words">{t.error}</span>
                    </div>
                  )}
                  {t.status === "done" && t.answer && (
                    <div className="mt-2 flex items-center gap-0.5">
                      <CopyButton text={t.answer} />
                    </div>
                  )}
                </div>
              </div>
            </section>
          ))}
        </div>
        <div ref={bottom} />
      </div>
      <div className="sticky bottom-0 bg-gradient-to-t from-canvas via-canvas to-canvas/0 px-4 pb-4 pt-6 sm:px-6">
        <div className="mx-auto max-w-[760px]">
          <Composer
            value={draft}
            onChange={setDraft}
            onSubmit={() => ask(draft)}
            onStop={() => abort.current?.abort()}
            busy={busy}
            scope={scope}
            onScope={onScope}
            placeholder="Ask a follow-up (each question is answered from the filings on its own)…"
          />
        </div>
      </div>
    </div>
  );
}
