"use client";

import { useEffect, useMemo, useState } from "react";
import { CASES, fmt, fmtDate, type CaseStats, type Doc, type SourceRef } from "../lib";
import { type Scope } from "./Composer";
import { Icon } from "./Icon";
import { PageHeader } from "./SearchView";

const KIND_LABEL: Record<string, string> = {
  evidence: "Evidence",
  interrogatory: "Interrogatory",
  ir_response: "IR response",
  undertaking: "Undertaking",
  settlement: "Settlement",
  decision: "Decision",
  argument: "Argument",
  transcript: "Transcript",
  intervenor_evidence: "Intervenor evidence",
  other: "Other",
};

function monthYear(d: string | null) {
  return d ? new Date(`${d}T00:00:00`).toLocaleDateString("en-CA", { year: "numeric", month: "short" }) : "—";
}

export function FilingsView({ corpus, active, onOpen, scope, onScope }: { corpus: CaseStats[] | null; active: SourceRef | null; onOpen: (s: SourceRef) => void; scope: Scope; onScope: (s: Scope) => void }) {
  const [docs, setDocs] = useState<Doc[] | null>(null);
  const [kind, setKind] = useState<string | null>(null);
  const [filter, setFilter] = useState("");

  useEffect(() => {
    fetch("/api/documents")
      .then((r) => r.json())
      .then(setDocs)
      .catch(() => setDocs([]));
  }, []);

  const rows = useMemo(() => {
    const f = filter.trim().toLowerCase();
    return (docs ?? []).filter(
      (d) => (!scope || d.case_number === scope) && (!kind || d.doc_kind === kind) && (!f || `${d.title} ${d.exhibit ?? ""}`.toLowerCase().includes(f)),
    );
  }, [docs, scope, kind, filter]);

  const kinds = useMemo(() => {
    const counts = new Map<string, number>();
    for (const d of docs ?? []) if (!scope || d.case_number === scope) counts.set(d.doc_kind, (counts.get(d.doc_kind) ?? 0) + 1);
    return [...counts.entries()].sort((a, b) => b[1] - a[1]);
  }, [docs, scope]);

  return (
    <div className="mx-auto w-full max-w-[1000px] px-4 py-6 sm:px-6">
      <PageHeader eyebrow="Record" title="Filings" />

      <div className="mt-4 grid gap-3 sm:grid-cols-2">
        {(corpus ?? []).map((c) => {
          const meta = CASES[c.case_number];
          const selected = scope === c.case_number;
          return (
            <button
              key={c.case_number}
              onClick={() => onScope(selected ? null : c.case_number)}
              className={`rounded-xl border bg-panel p-4 text-left transition-colors ${selected ? "border-navy/50 ring-2 ring-tint-strong" : "border-line hover:border-line-strong"}`}
            >
              <div className="flex items-center justify-between">
                <span className="font-mono text-[11px] text-muted">{c.case_number}</span>
                <span className="rounded-full border border-line px-2 py-0.5 text-[10.5px] text-muted">{meta?.period} rates</span>
              </div>
              <p className="mt-2 text-[15px] font-semibold tracking-tight">{meta?.utility ?? c.applicant}</p>
              <p className="truncate text-[12px] text-muted">{c.applicant}</p>
              <dl className="mt-4 grid grid-cols-3 gap-2 border-t border-line pt-3">
                {[
                  ["Filings", fmt.format(c.documents)],
                  ["Pages", fmt.format(c.pages)],
                  ["Filed", c.first_filed === c.last_filed ? fmtDate(c.first_filed) : `${monthYear(c.first_filed)} – ${monthYear(c.last_filed)}`],
                ].map(([k, v]) => (
                  <div key={k} className="min-w-0">
                    <dt className="eyebrow">{k}</dt>
                    <dd className="mt-0.5 truncate text-[13px] font-medium tabular-nums" title={v}>
                      {v}
                    </dd>
                  </div>
                ))}
              </dl>
            </button>
          );
        })}
      </div>

      <div className="mt-6 flex flex-wrap items-center gap-2 rounded-xl border border-line bg-sunken/70 p-2">
        <label className="flex min-w-[220px] flex-1 items-center gap-2 rounded-lg border border-line-strong bg-panel px-3">
          <Icon name="search" className="size-4 text-faint" />
          <input value={filter} onChange={(e) => setFilter(e.target.value)} placeholder="Filter by title or exhibit" className="h-8 w-full bg-transparent text-[13px] outline-none placeholder:text-faint" />
        </label>
        <div className="flex flex-wrap gap-1">
          <button onClick={() => setKind(null)} className={`rounded-md px-2 py-1 text-[12px] ${kind === null ? "bg-panel font-medium text-ink shadow-sm" : "text-muted hover:text-ink"}`}>
            All
          </button>
          {kinds.map(([k, n]) => (
            <button key={k} onClick={() => setKind(kind === k ? null : k)} className={`rounded-md px-2 py-1 text-[12px] ${kind === k ? "bg-panel font-medium text-ink shadow-sm" : "text-muted hover:text-ink"}`}>
              {KIND_LABEL[k] ?? k} <span className="font-mono text-[10.5px] text-faint">{n}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="mt-3 overflow-x-auto rounded-xl border border-line bg-panel">
        <table className="w-full min-w-[680px] table-fixed text-left text-[12.5px]">
          <colgroup>
            <col />
            <col className="w-[72px]" />
            <col className="w-[132px]" />
            <col className="w-[72px]" />
            <col className="w-[112px]" />
            <col className="w-[72px]" />
          </colgroup>
          <thead>
            <tr className="border-b border-line bg-sunken/60 text-[11.5px] text-muted">
              <th className="px-4 py-2 font-normal">Name</th>
              <th className="px-3 py-2 font-normal">Exhibit</th>
              <th className="px-3 py-2 font-normal">Type</th>
              <th className="px-3 py-2 text-right font-normal">Pages</th>
              <th className="px-3 py-2 font-normal">Filed</th>
              <th className="px-3 py-2" />
            </tr>
          </thead>
          <tbody className="divide-y divide-line">
            {docs === null &&
              [0, 1, 2, 3].map((i) => (
                <tr key={i}>
                  <td colSpan={6} className="px-4 py-3">
                    <div className="h-2.5 w-2/3 animate-pulse rounded bg-line" />
                  </td>
                </tr>
              ))}
            {rows.map((d) => {
              const isActive = active?.docId === d.doc_id;
              return (
                <tr key={d.doc_id} className={isActive ? "bg-tint" : "hover:bg-sunken/50"}>
                  <td className="px-4 py-2">
                    <span className="block truncate font-medium" title={d.title}>
                      {d.title}
                    </span>
                    <span className="block truncate font-mono text-[10.5px] text-faint">
                      {CASES[d.case_number]?.utility} · {d.case_number}
                    </span>
                  </td>
                  <td className="px-3 py-2 font-mono text-[11.5px]">{d.exhibit ?? "—"}</td>
                  <td className="px-3 py-2">
                    <span className="rounded-full border border-line px-2 py-0.5 text-[11px] text-muted">{KIND_LABEL[d.doc_kind] ?? d.doc_kind}</span>
                  </td>
                  <td className="px-3 py-2 text-right tabular-nums">{d.n_pages ? fmt.format(d.n_pages) : "—"}</td>
                  <td className="whitespace-nowrap px-3 py-2 text-muted">{fmtDate(d.date_received)}</td>
                  <td className="px-3 py-2 text-right">
                    <button onClick={() => onOpen({ docId: d.doc_id, page: 1 })} className="rounded-md border border-line px-2 py-1 text-[11.5px] hover:border-line-strong hover:bg-sunken">
                      Open
                    </button>
                  </td>
                </tr>
              );
            })}
            {docs !== null && rows.length === 0 && (
              <tr>
                <td colSpan={6} className="px-4 py-6 text-center text-muted">
                  No filings match.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      <p className="mt-3 px-1 text-[11.5px] text-faint">
        Sources: Ontario Energy Board Regulatory Document Search (rds.oeb.ca), torontohydro.com and hydroone.com. Only PDFs are indexed; spreadsheets are listed at the source.
      </p>
    </div>
  );
}
