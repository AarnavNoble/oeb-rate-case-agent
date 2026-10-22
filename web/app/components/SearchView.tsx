"use client";

import { useState, type ReactNode } from "react";
import { caseLabel, type Hit, type SourceRef } from "../lib";
import { ScopeChips, type Scope } from "./Composer";
import { Icon } from "./Icon";

const RETRIEVERS = [
  ["hybrid", "Hybrid (RRF)"],
  ["vector", "Vector"],
  ["fts", "Full-text"],
] as const;

function highlight(text: string, q: string): ReactNode[] {
  const words = [...new Set(q.toLowerCase().match(/[a-z0-9]{4,}/g) ?? [])];
  if (!words.length) return [text];
  const re = new RegExp(`(${words.map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})`, "gi");
  return text.split(re).map((part, i) => (i % 2 ? <mark key={i} className="rounded-sm bg-tint text-navy">{part}</mark> : part));
}

export function PageHeader({ eyebrow, title, children }: { eyebrow: string; title: string; children?: ReactNode }) {
  return (
    <div className="flex items-center gap-3 rounded-xl border border-line bg-panel px-4 py-3">
      <span className="flex size-9 items-center justify-center rounded-lg border border-line bg-sunken text-muted">
        <Icon name={eyebrow === "Search" ? "search" : "files"} />
      </span>
      <div className="min-w-0 flex-1">
        <p className="eyebrow">{eyebrow}</p>
        <h1 className="text-[17px] font-semibold tracking-tight">{title}</h1>
      </div>
      {children}
    </div>
  );
}

export function SearchView({ active, onOpen, scope, onScope }: { active: SourceRef | null; onOpen: (s: SourceRef) => void; scope: Scope; onScope: (s: Scope) => void }) {
  const [q, setQ] = useState("");
  const [retriever, setRetriever] = useState<string>("hybrid");
  const [result, setResult] = useState<{ q: string; hits: Hit[]; ms: number } | null>(null);
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
      if (!res.ok) throw new Error(`Search failed (${res.status})`);
      setResult({ q: q.trim(), hits: await res.json(), ms: performance.now() - t0 });
    } catch (e) {
      setError(String((e as Error).message ?? e));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="mx-auto w-full max-w-[900px] px-4 py-6 sm:px-6">
      <PageHeader eyebrow="Search" title="Passage search" />
      <p className="mt-3 px-1 text-[12.5px] text-muted">
        Searches the same index the agent uses, with no language model involved. Useful for checking what retrieval finds for a question.
      </p>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          run();
        }}
        className="mt-4 flex flex-wrap items-center gap-2 rounded-xl border border-line bg-sunken/70 p-2"
      >
        <label className="flex min-w-[240px] flex-1 items-center gap-2 rounded-lg border border-line-strong bg-panel px-3 focus-within:border-navy/40">
          <Icon name="search" className="size-4 text-faint" />
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="e.g. vegetation management cycle"
            className="h-9 w-full bg-transparent text-[13.5px] outline-none placeholder:text-faint"
          />
        </label>
        <div className="inline-flex rounded-lg border border-line bg-panel p-0.5 text-[12px]">
          {RETRIEVERS.map(([k, label]) => (
            <button
              key={k}
              type="button"
              onClick={() => {
                setRetriever(k);
                if (result) run(k);
              }}
              className={`rounded-md px-2.5 py-1.5 ${retriever === k ? "bg-navy text-on-navy" : "text-muted hover:text-ink"}`}
            >
              {label}
            </button>
          ))}
        </div>
        <button type="submit" disabled={busy || q.trim().length < 2} className="h-9 rounded-lg bg-navy px-4 text-[13px] font-medium text-on-navy hover:bg-navy-hover disabled:opacity-40">
          {busy ? "Searching…" : "Search"}
        </button>
      </form>
      <div className="mt-3 px-1">
        <ScopeChips
          scope={scope}
          onScope={(s) => {
            onScope(s);
            if (result) run(retriever, s);
          }}
        />
      </div>

      {error && <p className="mt-4 text-[13px] text-warn">{error}</p>}

      {result && (
        <div className="mt-5 overflow-hidden rounded-xl border border-line bg-panel">
          <div className="grid grid-cols-[2.5rem_1fr_auto] items-center gap-3 border-b border-line bg-sunken/60 px-4 py-2 text-[11.5px] text-muted">
            <span className="font-mono">#</span>
            <span>
              {result.hits.length} passages for “{result.q}”
            </span>
            <span className="font-mono">{Math.round(result.ms)} ms</span>
          </div>
          {result.hits.length === 0 && <p className="px-4 py-6 text-[13px] text-muted">No passages matched.</p>}
          <ol className="divide-y divide-line">
            {result.hits.map((h, i) => {
              const isActive = active?.docId === h.doc_id && active.page === h.page_start;
              return (
                <li key={h.chunk_id}>
                  <button
                    onClick={() => onOpen({ docId: h.doc_id, page: h.page_start, claim: result.q })}
                    className={`grid w-full grid-cols-[2.5rem_1fr] gap-3 px-4 py-3 text-left transition-colors ${isActive ? "bg-tint" : "hover:bg-sunken/60"}`}
                  >
                    <span className="pt-0.5 font-mono text-[11px] text-faint">{String(i + 1).padStart(2, "0")}</span>
                    <span className="min-w-0">
                      <span className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
                        <span className="text-[13px] font-medium">
                          {caseLabel(h.case_number)} · {h.exhibit ? `Ex. ${h.exhibit}` : h.title} · p. {h.page_start}
                          {h.page_end !== h.page_start && `–${h.page_end}`}
                        </span>
                        <span className="font-mono text-[10.5px] text-faint">{h.case_number}</span>
                      </span>
                      {h.heading && <span className="mt-0.5 block truncate text-[12px] font-medium text-muted">{h.heading}</span>}
                      <span className="mt-1 line-clamp-3 text-[12.5px] leading-relaxed text-ink/80">{highlight(h.text, result.q)}</span>
                    </span>
                  </button>
                </li>
              );
            })}
          </ol>
        </div>
      )}
    </div>
  );
}
