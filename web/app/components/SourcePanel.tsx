"use client";

import { useEffect, useRef, useState } from "react";
import { caseLabel, claimFigures, figuresOn, fmtDate, pageBlocks, pdfUrl, type PageText, type SourceRef } from "../lib";
import { Icon } from "./Icon";

type View = "text" | "pdf";

/** Right-hand source viewer: the cited page's extracted text with the best-matching passage marked, or the PDF itself. */
export function SourcePanel({
  source,
  onClose,
  onPage,
  onJump,
}: {
  source: SourceRef;
  onClose: () => void;
  onPage: (page: number) => void;
  onJump: (page: number) => void;
}) {
  const [view, setView] = useState<View>("text");
  const [data, setData] = useState<{ key: string; page?: PageText; error?: string } | null>(null);
  const mark = useRef<HTMLParagraphElement>(null);
  const key = `${source.docId}:${source.page}`;

  useEffect(() => {
    const ctrl = new AbortController();
    fetch(`/api/page/${encodeURIComponent(source.docId)}/${source.page}`, { signal: ctrl.signal })
      .then(async (r) => (r.ok ? setData({ key, page: await r.json() }) : setData({ key, error: `Page not available (${r.status})` })))
      .catch((e) => e.name !== "AbortError" && setData({ key, error: String(e) }));
    return () => ctrl.abort();
  }, [key, source.docId, source.page]);

  const page = data?.key === key ? data.page : undefined;
  const error = data?.key === key ? data.error : undefined;
  const { blocks, best } = page ? pageBlocks(page.text, source.claim) : { blocks: [], best: -1 };

  useEffect(() => {
    mark.current?.scrollIntoView({ block: "center", behavior: "smooth" });
  }, [page, best]);

  // Support check for cited figures: if none of the claim's numbers are on the cited page, look on the
  // neighbouring pages (citations are sometimes off by a page or two when a passage spans pages).
  const figures = source.n ? claimFigures(source.claim) : [];
  const missing = !!page && figures.length > 0 && figuresOn(page.text, figures).length === 0;
  const [nearby, setNearby] = useState<{ key: string; page: number | null } | null>(null);
  useEffect(() => {
    if (!missing) return;
    const ctrl = new AbortController();
    const offsets = [1, -1, 2, -2].map((o) => source.page + o).filter((p) => p >= 1 && (!page?.n_pages || p <= page.n_pages));
    Promise.all(
      offsets.map((p) =>
        fetch(`/api/page/${encodeURIComponent(source.docId)}/${p}`, { signal: ctrl.signal })
          .then((r) => (r.ok ? r.json() : null))
          .then((d: PageText | null) => ({ p, hits: d ? figuresOn(d.text, figures).length : 0 })),
      ),
    )
      .then((rs) => {
        const top = rs.reduce((a, b) => (b.hits > a.hits ? b : a), { p: 0, hits: 0 });
        setNearby({ key, page: top.hits ? top.p : null });
      })
      .catch(() => {});
    return () => ctrl.abort();
    // figures derive from source.claim; key covers doc and page
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [missing, key, source.claim]);
  const found = nearby?.key === key ? nearby : null;

  return (
    <aside className="fixed inset-0 z-30 flex flex-col bg-panel lg:sticky lg:top-0 lg:z-auto lg:h-screen lg:w-[46%] lg:max-w-[720px] lg:shrink-0 lg:border-l lg:border-line">
      <header className="border-b border-line px-5 pb-3 pt-4">
        <div className="flex items-center justify-between gap-3">
          <div className="flex min-w-0 items-center gap-2 font-mono text-[11px] text-muted">
            {source.n && (
              <span className="flex size-[18px] shrink-0 items-center justify-center rounded-full bg-navy text-[10px] text-on-navy">{source.n}</span>
            )}
            <span className="truncate">
              {page ? `${page.case_number} · ${page.exhibit_ref ?? (page.exhibit ? `Exhibit ${page.exhibit}` : page.record_number ?? page.doc_id)}` : source.docId}
            </span>
          </div>
          <div className="flex shrink-0 items-center gap-1">
            <a
              href={pdfUrl(source.docId, source.page)}
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-1 rounded-md px-2 py-1 text-[12px] text-muted hover:bg-sunken hover:text-ink"
            >
              Open PDF <Icon name="external" className="size-3.5" />
            </a>
            <button onClick={onClose} aria-label="Close source" className="rounded-md p-1.5 text-muted hover:bg-sunken hover:text-ink">
              <Icon name="x" />
            </button>
          </div>
        </div>
        <h2 className="mt-2 text-[15px] font-semibold leading-snug tracking-tight">
          {page ? `${caseLabel(page.case_number)} · p. ${page.page_no}` : `Page ${source.page}`}
          {page?.n_pages ? <span className="font-normal text-faint"> of {page.n_pages}</span> : null}
        </h2>
        {page && (
          <p className="mt-0.5 truncate text-[12px] text-muted" title={page.title}>
            {page.title} · filed {fmtDate(page.date_received)}
          </p>
        )}
        <div className="mt-3 flex items-center justify-between">
          <div className="inline-flex rounded-md bg-sunken p-0.5 text-[12px]">
            {(["text", "pdf"] as View[]).map((v) => (
              <button
                key={v}
                onClick={() => setView(v)}
                className={`rounded px-2.5 py-1 ${view === v ? "bg-panel font-medium text-ink shadow-sm" : "text-muted hover:text-ink"}`}
              >
                {v === "text" ? "Extracted text" : "PDF page"}
              </button>
            ))}
          </div>
          <div className="flex items-center gap-1 font-mono text-[11px] text-muted">
            <button
              disabled={source.page <= 1}
              onClick={() => onPage(source.page - 1)}
              className="rounded px-1.5 py-1 hover:bg-sunken disabled:opacity-30"
              aria-label="Previous page"
            >
              ←
            </button>
            p. {source.page}
            <button
              disabled={!!page?.n_pages && source.page >= page.n_pages}
              onClick={() => onPage(source.page + 1)}
              className="rounded px-1.5 py-1 hover:bg-sunken disabled:opacity-30"
              aria-label="Next page"
            >
              →
            </button>
          </div>
        </div>
      </header>

      {view === "pdf" ? (
        // key forces a reload so #page= takes effect when switching citations
        <iframe key={key} src={pdfUrl(source.docId, source.page)} title={page?.title ?? source.docId} className="flex-1 bg-sunken" />
      ) : (
        <div className="flex-1 overflow-y-auto bg-canvas px-5 py-4">
          {error && <p className="text-sm text-warn">{error}</p>}
          {!page && !error && (
            <div className="space-y-2.5">
              {[92, 100, 84, 96, 70].map((w, i) => (
                <div key={i} className="h-2.5 animate-pulse rounded bg-line" style={{ width: `${w}%` }} />
              ))}
            </div>
          )}
          {page && (
            <>
              {missing && (
                <div className="mb-3 flex items-start gap-2 rounded-lg border border-warn/30 bg-warn-bg px-3 py-2 text-[12.5px] text-warn">
                  <Icon name="alert" className="mt-0.5 size-4 shrink-0" />
                  <span className="flex-1">
                    The figures in this claim ({figures.join(", ")}) are not on this page.
                    {found === null && " Checking nearby pages…"}
                    {found?.page && <> They appear on p. {found.page}.</>}
                    {found && !found.page && " They are not on the two pages either side either."}
                  </span>
                  {found?.page && (
                    <button onClick={() => onJump(found.page!)} className="shrink-0 rounded-md border border-warn/40 px-2 py-0.5 font-medium hover:bg-panel">
                      Go to p. {found.page}
                    </button>
                  )}
                </div>
              )}
              {best >= 0 && !missing && (
                <p className="mb-3 text-[11.5px] text-muted">
                  Highlighted: the passage on this page that best matches {source.n ? "the cited sentence" : "your search"} (by shared terms).
                </p>
              )}
              <div className="rounded-lg border border-line bg-panel py-2">
                {blocks.map((b, i) => (
                  <p
                    key={i}
                    ref={i === best ? mark : undefined}
                    className={`whitespace-pre-wrap px-4 py-1.5 text-[13px] leading-relaxed ${
                      i === best ? "border-l-2 border-navy bg-tint text-ink" : "border-l-2 border-transparent text-ink/80"
                    }`}
                  >
                    {b}
                  </p>
                ))}
                {!blocks.length && <p className="px-4 text-sm text-muted">No text was extracted from this page (it may be an image).</p>}
              </div>
            </>
          )}
        </div>
      )}
    </aside>
  );
}
