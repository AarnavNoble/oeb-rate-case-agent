"use client";

import { useEffect, useMemo, useState } from "react";
import { CASES, fmt, fmtDate, type Doc, type Pipeline, type SourceRef } from "../lib";
import { ScopeChips, type Scope } from "./Composer";
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

const SOURCE_LABEL: Record<string, string> = {
  "rds.oeb.ca": "OEB Regulatory Document Search",
  "torontohydro.com": "torontohydro.com",
  "hydroone.com": "hydroone.com",
};

/** The ingestion run as a sequence: what each Temporal stage did and how long it took in total. */
function PipelineSummary({ pipeline }: { pipeline: Pipeline }) {
  const embedded = pipeline.statuses.find((s) => s.status === "embedded")?.n ?? 0;
  const skipped = pipeline.statuses.find((s) => s.status === "skipped_format")?.n ?? 0;
  const h = pipeline.corpus.stage_hours_summed;
  const stages = [
    {
      name: "Download",
      stat: `${fmt.format(embedded)} PDFs`,
      time: `${h.download_h} h`,
      body: (
        <>
          From {pipeline.sources.map((s) => `${SOURCE_LABEL[s.source] ?? s.source} (${s.n})`).join(", ")}. One request at a time per host, at least 1.1 s apart,
          with byte-range downloads checked against the size the server lists. {fmt.format(skipped)} spreadsheets and Word files were listed but not
          downloaded.
        </>
      ),
    },
    {
      name: "Parse",
      stat: `${fmt.format(pipeline.totals.pages)} pages`,
      time: `${h.parse_h} h`,
      body: <>Text per page with PyMuPDF, page headers turned into exhibit references, and {fmt.format(pipeline.totals.tables)} tables extracted with pdfplumber.</>,
    },
    {
      name: "Chunk and embed",
      stat: `${fmt.format(pipeline.totals.chunks)} passages`,
      time: `${h.embed_h} h`,
      body: <>Split at headings into 500–800 token passages that keep their page range, embedded locally with bge-small, and indexed for full-text and vector search.</>,
    },
  ];
  return (
    <section aria-labelledby="pipeline" className="mt-8">
      <h2 id="pipeline" className="text-[17px] font-semibold">
        Ingestion pipeline
      </h2>
      <p className="mt-1 text-[14px] text-muted">
        A Temporal workflow per case, with one child workflow per document. Each stage is idempotent: re-running a case skips every finished document.
        Times are summed across documents.
      </p>
      <ol className="mt-5 grid gap-px overflow-hidden rounded-xl border border-line bg-line md:grid-cols-3">
        {stages.map((s, i) => (
          <li key={s.name} className="bg-surface p-4">
            <div className="flex items-center gap-2">
              <span className="flex size-6 items-center justify-center rounded-full border border-line-strong font-mono text-[11px] text-muted">{i + 1}</span>
              <h3 className="text-[14px] font-medium">{s.name}</h3>
              <span className="ml-auto font-mono text-[12px] text-faint">{s.time}</span>
            </div>
            <p className="mt-3 text-[22px] font-semibold tabular-nums">{s.stat}</p>
            <p className="mt-1 text-[13px] leading-relaxed text-muted">{s.body}</p>
          </li>
        ))}
      </ol>
    </section>
  );
}

export function FilingsView({
  pipeline,
  active,
  onOpen,
  scope,
  onScope,
}: {
  pipeline: Pipeline | null;
  active: SourceRef | null;
  onOpen: (s: SourceRef) => void;
  scope: Scope;
  onScope: (s: Scope) => void;
}) {
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
    <div className="mx-auto w-full max-w-[1080px] px-5 py-10 sm:px-8">
      <PageHeader title="Data">Every filing the agent can read, and how it got into the index. All of it is real, public record.</PageHeader>

      <div className="mt-8 grid gap-4 sm:grid-cols-2">
        {(pipeline?.corpus.cases ?? []).map((c) => {
          const meta = CASES[c.case_number];
          return (
            <div key={c.case_number} className="rounded-xl border border-line bg-surface p-4">
              <div className="flex items-baseline justify-between gap-2">
                <h3 className="text-[17px] font-semibold">{meta?.utility}</h3>
                <span className="font-mono text-[12px] text-muted">{c.case_number}</span>
              </div>
              <p className="text-[13px] text-muted">{meta?.period} rate application</p>
              <dl className="mt-4 grid grid-cols-3 gap-3 border-t border-line pt-3">
                {[
                  [fmt.format(c.ingested), "PDFs indexed"],
                  [fmt.format(c.pages), "pages"],
                  [`${fmt.format(Number(c.mb))} MB`, "downloaded"],
                ].map(([v, l]) => (
                  <div key={l}>
                    <dd className="text-[17px] font-semibold tabular-nums">{v}</dd>
                    <dt className="text-[12.5px] text-muted">{l}</dt>
                  </div>
                ))}
              </dl>
            </div>
          );
        })}
      </div>

      {pipeline && <PipelineSummary pipeline={pipeline} />}

      <section aria-labelledby="filings" className="mt-12">
        <h2 id="filings" className="text-[17px] font-semibold">
          Filings
        </h2>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <label className="flex min-w-[220px] flex-1 items-center gap-2 rounded-lg border border-line-strong bg-surface px-3 focus-within:border-amber-line">
            <Icon name="search" className="size-4 text-faint" />
            <span className="sr-only">Filter filings</span>
            <input
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
              placeholder="Filter by title or exhibit"
              className="h-9 w-full bg-transparent text-[13.5px] outline-none placeholder:text-faint focus-visible:outline-none"
            />
          </label>
          <ScopeChips scope={scope} onScope={onScope} />
        </div>
        <div className="mt-2 flex flex-wrap gap-1">
          <button
            onClick={() => setKind(null)}
            aria-pressed={kind === null}
            className={`rounded-md px-2 py-1 text-[12.5px] ${kind === null ? "bg-raised font-medium text-text" : "text-muted hover:text-text"}`}
          >
            All types
          </button>
          {kinds.map(([k, n]) => (
            <button
              key={k}
              onClick={() => setKind(kind === k ? null : k)}
              aria-pressed={kind === k}
              className={`rounded-md px-2 py-1 text-[12.5px] ${kind === k ? "bg-raised font-medium text-text" : "text-muted hover:text-text"}`}
            >
              {KIND_LABEL[k] ?? k} <span className="text-faint">{n}</span>
            </button>
          ))}
        </div>

        <div className="mt-3 overflow-x-auto rounded-xl border border-line bg-surface">
          <table className="w-full min-w-[680px] table-fixed text-left text-[13px]">
            <colgroup>
              <col />
              <col className="w-[80px]" />
              <col className="w-[140px]" />
              <col className="w-[76px]" />
              <col className="w-[116px]" />
              <col className="w-[76px]" />
            </colgroup>
            <thead>
              <tr className="border-b border-line text-[12.5px] text-muted">
                <th className="px-4 py-2.5 font-normal">Filing</th>
                <th className="px-3 py-2.5 font-normal">Exhibit</th>
                <th className="px-3 py-2.5 font-normal">Type</th>
                <th className="px-3 py-2.5 text-right font-normal">Pages</th>
                <th className="px-3 py-2.5 font-normal">Filed</th>
                <th className="px-3 py-2.5">
                  <span className="sr-only">Open</span>
                </th>
              </tr>
            </thead>
            <tbody>
              {docs === null &&
                [0, 1, 2, 3].map((i) => (
                  <tr key={i}>
                    <td colSpan={6} className="px-4 py-3">
                      <div className="h-2.5 w-2/3 animate-pulse rounded bg-raised" />
                    </td>
                  </tr>
                ))}
              {rows.map((d) => {
                const isActive = active?.docId === d.doc_id;
                return (
                  <tr key={d.doc_id} className={`border-b border-line last:border-0 ${isActive ? "bg-amber-wash" : "hover:bg-raised/60"}`}>
                    <td className="px-4 py-2.5">
                      <span className="block truncate font-medium" title={d.title}>
                        {d.title}
                      </span>
                      <span className="block truncate text-[12px] text-faint">
                        {CASES[d.case_number]?.utility}, {d.case_number}
                      </span>
                    </td>
                    <td className="px-3 py-2.5 font-mono text-[12px]">{d.exhibit ?? <span className="text-faint">none</span>}</td>
                    <td className="px-3 py-2.5 text-muted">{KIND_LABEL[d.doc_kind] ?? d.doc_kind}</td>
                    <td className="px-3 py-2.5 text-right tabular-nums">{d.n_pages ? fmt.format(d.n_pages) : "–"}</td>
                    <td className="whitespace-nowrap px-3 py-2.5 text-muted">{fmtDate(d.date_received)}</td>
                    <td className="px-3 py-2.5 text-right">
                      <button onClick={() => onOpen({ docId: d.doc_id, page: 1 })} className="rounded-md px-2 py-1 text-[12.5px] text-amber hover:bg-amber-wash">
                        Open
                      </button>
                    </td>
                  </tr>
                );
              })}
              {docs !== null && rows.length === 0 && (
                <tr>
                  <td colSpan={6} className="px-4 py-6 text-center text-muted">
                    No filings match that filter.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
