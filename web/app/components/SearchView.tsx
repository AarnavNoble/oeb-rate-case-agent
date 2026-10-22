"use client";

import { useState, type ReactNode } from "react";
import { caseLabel, recordRef, type Hit, type SourceRef } from "../lib";
import { ScopeChips, type Scope } from "./Composer";
import { Icon } from "./Icon";

const RETRIEVERS = [
  ["hybrid", "Hybrid", "Full-text and vector results merged with reciprocal rank fusion. This is what the agent uses."],
  ["vector", "Vector", "Cosine similarity over bge-small embeddings. Finds passages with the same meaning in different words."],
  ["fts", "Full-text", "Postgres full-text ranking. Finds the exact terms, and drops words that appear in more than 10% of passages."],
] as const;

function highlight(text: string, q: string): ReactNode[] {
  const words = [...new Set(q.toLowerCase().match(/[a-z0-9]{4,}/g) ?? [])];
  if (!words.length) return [text];
  const re = new RegExp(`(${words.map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})`, "gi");
  return text.split(re).map((part, i) => (i % 2 ? <mark key={i} className="rounded-sm bg-amber-wash text-text">{part}</mark> : part));
}

export function PageHeader({ title, children }: { title: string; children?: ReactNode }) {
  return (
    <header className="max-w-[72ch]">
      <h1 className="text-[28px] font-semibold tracking-[-0.015em]">{title}</h1>
      {children && <div className="mt-2 text-[15px] leading-relaxed text-muted">{children}</div>}
    </header>
  );
}

export function SearchView({ active, onOpen, scope, onScope }: { active: SourceRef | null; onOpen: (s: SourceRef) => void; scope: Scope; onScope: (s: Scope) => void }) {
  const [q, setQ] = useState("");
  const [retriever, setRetriever] = useState<string>("hybrid");
  const [result, setResult] = useState<{ q: string; retriever: string; hits: Hit[]; ms: number } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function run(nextRetriever = retriever, nextScope = scope) {
    if (q.trim().length < 2) return;
    setBusy(true);
    setError(null);
    const t0 = performance.now();
    try {
      const params = new URLSearchParams({ q: q.trim(), k: "15", retriever: nextRetriever });
      if (nextScope) params.set("case", nextScope);
      const res = await fetch(`/api/search?${params}`);
      if (!res.ok) throw new Error(`Search failed (HTTP ${res.status}). Check that the API is running.`);
      setResult({ q: q.trim(), retriever: nextRetriever, hits: await res.json(), ms: performance.now() - t0 });
    } catch (e) {
      setError(String((e as Error).message ?? e));
    } finally {
      setBusy(false);
    }
  }

  const current = RETRIEVERS.find(([k]) => k === retriever)!;

  return (
    <div className="mx-auto w-full max-w-[960px] px-5 py-10 sm:px-8">
      <PageHeader title="Search passages">
        The three retrievers the agent is built on, with no language model involved. Compare what each one finds for the same question.
      </PageHeader>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          run();
        }}
        className="mt-7 rounded-xl border border-line-strong bg-surface p-2 focus-within:border-amber-line"
      >
        <div className="flex items-center gap-2">
          <Icon name="search" className="ml-2 size-4 shrink-0 text-faint" />
          <label htmlFor="search-q" className="sr-only">
            Search the filings
          </label>
          <input
            id="search-q"
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="vegetation management cycle length"
            className="h-10 w-full bg-transparent text-[15px] outline-none placeholder:text-faint focus-visible:outline-none"
          />
          <button type="submit" disabled={busy || q.trim().length < 2} className="h-9 shrink-0 rounded-lg bg-amber px-4 text-[13px] font-semibold text-on-amber hover:bg-amber-hover disabled:opacity-40">
            {busy ? "Searching" : "Search"}
          </button>
        </div>
        <div className="mt-2 flex flex-wrap items-center justify-between gap-2 border-t border-line px-1 pt-2">
          <div className="inline-flex rounded-md bg-ground p-0.5" role="radiogroup" aria-label="Retriever">
            {RETRIEVERS.map(([k, label]) => (
              <button
                key={k}
                type="button"
                role="radio"
                aria-checked={retriever === k}
                onClick={() => {
                  setRetriever(k);
                  if (result) run(k);
                }}
                className={`rounded-[5px] px-2.5 py-1 text-[12.5px] ${retriever === k ? "bg-raised font-medium text-text" : "text-muted hover:text-text"}`}
              >
                {label}
              </button>
            ))}
          </div>
          <ScopeChips
            scope={scope}
            onScope={(s) => {
              onScope(s);
              if (result) run(retriever, s);
            }}
          />
        </div>
      </form>
      <p className="mt-2 px-1 text-[12.5px] text-faint">{current[2]}</p>

      {error && (
        <p role="alert" className="mt-4 text-[13px] text-serious">
          {error}
        </p>
      )}

      {!result && !error && (
        <p className="mt-10 text-[14px] text-muted">
          Try a phrase a regulatory analyst would use, like &ldquo;station renewal backlog&rdquo; or &ldquo;deemed short-term debt rate&rdquo;.
        </p>
      )}

      {result && (
        <section className="mt-6" aria-label="Results">
          <p className="mb-2 px-1 text-[12.5px] text-muted">
            {result.hits.length} passages for &ldquo;{result.q}&rdquo; from the {RETRIEVERS.find(([k]) => k === result.retriever)?.[1].toLowerCase()} retriever,{" "}
            {Math.round(result.ms)} ms
          </p>
          {result.hits.length === 0 && <p className="rounded-xl border border-line bg-surface px-4 py-6 text-[14px] text-muted">No passages matched. Try fewer or broader words.</p>}
          <ol className="overflow-hidden rounded-xl border border-line bg-surface">
            {result.hits.map((h, i) => {
              const isActive = active?.docId === h.doc_id && active.page === h.page_start;
              return (
                <li key={h.chunk_id} className="border-b border-line last:border-0">
                  <button
                    onClick={() => onOpen({ docId: h.doc_id, page: h.page_start, claim: result.q })}
                    className={`grid w-full grid-cols-[2rem_1fr] gap-2 px-4 py-3.5 text-left transition-colors ${isActive ? "bg-amber-wash" : "hover:bg-raised"}`}
                  >
                    <span className="pt-0.5 font-mono text-[12px] text-faint">{i + 1}</span>
                    <span className="min-w-0">
                      <span className="flex flex-wrap items-baseline gap-x-2.5 gap-y-0.5">
                        <span className="text-[14px] font-medium">{caseLabel(h.case_number)}</span>
                        <span className="font-mono text-[12px] text-muted">
                          {recordRef(h.case_number, h.exhibit, h.page_start)}
                          {h.page_end !== h.page_start && `–${h.page_end}`}
                        </span>
                      </span>
                      {h.heading && <span className="mt-0.5 block truncate text-[12.5px] text-faint">{h.heading}</span>}
                      <span className="mt-1.5 line-clamp-3 text-[13.5px] leading-relaxed text-text/80">{highlight(h.text, result.q)}</span>
                    </span>
                  </button>
                </li>
              );
            })}
          </ol>
        </section>
      )}
    </div>
  );
}
