"use client";

import { useEffect, useRef, useState } from "react";
import { caseLabel, claimFigures, figuresOn, pageBlocks, pdfUrl, type PageText, type SourceRef } from "../lib";
import { Icon } from "./Icon";

type View = "text" | "pdf";

/**
 * The page header every OEB filing carries in its top-right corner (Filed date, case number, exhibit
 * reference, page). Reproducing it here makes a citation look like what it points to.
 */
function FilingHeader({ page }: { page: PageText }) {
  const ref = page.exhibit_ref ?? (page.exhibit ? `Exhibit ${page.exhibit}` : null);
  return (
    <dl className="shrink-0 text-right font-mono text-[11px] leading-[1.55] text-muted">
      <div>
        <dt className="inline">Filed: </dt>
        <dd className="inline text-text">{page.date_received ?? "n/a"}</dd>
      </div>
      <dd className="text-text">{page.case_number}</dd>
      {ref && <dd>{ref}</dd>}
      <dd>
        Page {page.page_no}
        {page.n_pages ? ` of ${page.n_pages}` : ""}
      </dd>
    </dl>
  );
}

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
      .then(async (r) => (r.ok ? setData({ key, page: await r.json() }) : setData({ key, error: `This page isn't in the index (HTTP ${r.status}).` })))
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
  const figuresOk = !!page && figures.length > 0 && !missing;

  return (
    <aside
      aria-label="Source"
      className="fixed inset-0 z-30 flex flex-col bg-surface lg:static lg:z-auto lg:w-[46%] lg:max-w-[720px] lg:shrink-0 lg:border-l lg:border-line"
    >
      <header className="border-b border-line px-5 pb-3 pt-4">
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              {source.n && (
                <span className="inline-flex h-[18px] min-w-[18px] items-center justify-center rounded-[5px] bg-amber px-1 font-mono text-[10.5px] font-medium text-on-amber">
                  {source.n}
                </span>
              )}
              <h2 className="text-[16px] font-semibold">{page ? caseLabel(page.case_number) : "Loading page"}</h2>
            </div>
            {page && (
              <p className="mt-1 line-clamp-2 text-[12.5px] text-muted" title={page.title}>
                {page.title}
              </p>
            )}
          </div>
          {page ? <FilingHeader page={page} /> : <span className="h-14 w-36 animate-pulse rounded bg-raised" />}
        </div>

        <div className="mt-3 flex items-center justify-between gap-2">
          <div className="inline-flex rounded-md bg-ground p-0.5 text-[12.5px]" role="tablist">
            {(["text", "pdf"] as View[]).map((v) => (
              <button
                key={v}
                role="tab"
                aria-selected={view === v}
                onClick={() => setView(v)}
                className={`rounded-[5px] px-2.5 py-1 ${view === v ? "bg-raised font-medium text-text" : "text-muted hover:text-text"}`}
              >
                {v === "text" ? "Page text" : "PDF"}
              </button>
            ))}
          </div>
          <div className="flex items-center gap-0.5 text-muted">
            <button disabled={source.page <= 1} onClick={() => onPage(source.page - 1)} className="rounded-md p-1.5 hover:bg-raised disabled:opacity-30" aria-label="Previous page">
              <Icon name="left" className="size-4" />
            </button>
            <button
              disabled={!!page?.n_pages && source.page >= page.n_pages}
              onClick={() => onPage(source.page + 1)}
              className="rounded-md p-1.5 hover:bg-raised disabled:opacity-30"
              aria-label="Next page"
            >
              <Icon name="right" className="size-4" />
            </button>
            <a href={pdfUrl(source.docId, source.page)} target="_blank" rel="noreferrer" className="ml-1 flex items-center gap-1 rounded-md px-2 py-1 text-[12.5px] hover:bg-raised hover:text-text">
              Open PDF <Icon name="external" className="size-3.5" />
            </a>
            <button onClick={onClose} aria-label="Close source" className="rounded-md p-1.5 hover:bg-raised hover:text-text">
              <Icon name="x" />
            </button>
          </div>
        </div>
      </header>

      {page && missing && (
        <div className="flex items-start gap-2.5 border-b border-line bg-serious/10 px-5 py-2.5 text-[13px]">
          <Icon name="alert" className="mt-0.5 size-4 shrink-0 text-serious" />
          <p className="flex-1">
            <span className="font-medium text-serious">Figures not on this page.</span>{" "}
            <span className="text-muted">
              The claim cites {figures.join(", ")}.{found === null && " Checking the pages either side."}
              {found?.page && ` They are on page ${found.page}.`}
              {found && !found.page && " They aren't on the two pages either side either."}
            </span>
          </p>
          {found?.page && (
            <button onClick={() => onJump(found.page!)} className="shrink-0 rounded-md bg-amber px-2.5 py-1 text-[12.5px] font-semibold text-on-amber hover:bg-amber-hover">
              Go to page {found.page}
            </button>
          )}
        </div>
      )}
      {figuresOk && (
        <div className="flex items-center gap-2 border-b border-line px-5 py-2 text-[12.5px] text-muted">
          <Icon name="check" className="size-4 text-good" />
          The figures in this claim ({figures.join(", ")}) appear on this page.
        </div>
      )}

      {view === "pdf" ? (
        // key forces a reload so #page= takes effect when switching citations
        <iframe key={key} src={pdfUrl(source.docId, source.page)} title={page?.title ?? source.docId} className="flex-1 bg-ground" />
      ) : (
        <div className="flex-1 overflow-y-auto bg-ground px-5 py-5">
          {error && <p className="text-[13px] text-serious">{error}</p>}
          {!page && !error && (
            <div className="space-y-2.5">
              {[92, 100, 84, 96, 70].map((w, i) => (
                <div key={i} className="h-2.5 animate-pulse rounded bg-raised" style={{ width: `${w}%` }} />
              ))}
            </div>
          )}
          {page && (
            <article className="mx-auto max-w-[640px] rounded-lg border border-line bg-surface py-4">
              {blocks.map((b, i) => (
                <p
                  key={i}
                  ref={i === best ? mark : undefined}
                  className={`whitespace-pre-wrap border-l-2 px-5 py-1 text-[13.5px] leading-relaxed ${
                    i === best ? "border-amber bg-amber-wash text-text" : "border-transparent text-text/75"
                  }`}
                >
                  {b}
                </p>
              ))}
              {!blocks.length && <p className="px-5 text-[13px] text-muted">No text was extracted from this page. It may be a scanned image.</p>}
            </article>
          )}
          {page && best >= 0 && (
            <p className="mx-auto mt-3 max-w-[640px] text-[12px] text-faint">
              The marked passage shares the most terms with {source.n ? "the cited sentence" : "your search"}. The agent cites pages, not passages.
            </p>
          )}
        </div>
      )}
    </aside>
  );
}
