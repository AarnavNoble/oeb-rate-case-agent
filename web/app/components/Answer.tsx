import { Fragment, type ReactNode } from "react";
import { caseLabel, CITE_RE, recordRef, type Citation, type SourceRef } from "../lib";
import { Icon } from "./Icon";

type Source = { n: number; docId: string; page: number; citation?: Citation; claim: string };

const INLINE_RE = /(\*\*[^*]+\*\*|`[^`]+`|\[cite:[A-Za-z0-9_-]+:\d+\])/g;

/** The sentence a citation token supports: the text before it, back to the previous sentence end. */
function claimBefore(text: string) {
  const plain = text.replace(CITE_RE, "").replace(/\*\*/g, "").trim();
  const sentences = plain.split(/(?<=[.!?])\s+/).filter(Boolean);
  let claim = sentences.pop() ?? "";
  if (claim.length < 40 && sentences.length) claim = `${sentences.pop()} ${claim}`;
  return claim;
}

/** "THESL_JT3.1 to 3.42_TC_UndertakingResp_Day3of5_Consolidated_20240422" -> "JT3.1 to 3.42 TC UndertakingResp Day3of5 Consolidated" */
export function shortTitle(title: string) {
  return title.replace(/^(THESL|HONI)_/, "").replace(/_\d{8}$/, "").replace(/_/g, " ");
}

export function sourceLabel(c: Citation | undefined, docId: string, page: number) {
  if (!c?.case_number) return `${docId}, p. ${page}`;
  return c.exhibit ? recordRef(c.case_number, c.exhibit, page) : `${c.case_number}, ${shortTitle(c.title ?? docId)}, p. ${page}`;
}

/**
 * Renders the agent's markdown subset (paragraphs, **bold**, `code`, -/1. lists, # headings) and turns
 * [cite:doc:page] tokens into numbered markers, numbered by first appearance.
 */
export function Answer({
  text,
  citations,
  streaming,
  active,
  onOpen,
}: {
  text: string;
  citations: Citation[] | null;
  streaming: boolean;
  active: SourceRef | null;
  onOpen: (s: SourceRef) => void;
}) {
  const byKey = new Map((citations ?? []).map((c) => [`${c.doc_id}:${c.page}`, c]));
  const numbers = new Map<string, Source>();
  // hide a cite token that is still arriving
  const body = streaming ? text.replace(/\[(c(i(t(e(:[^\]]*)?)?)?)?)?$/, "") : text;

  function inline(src: string, key: string): ReactNode[] {
    const out: ReactNode[] = [];
    let last = 0;
    for (const m of src.matchAll(INLINE_RE)) {
      const idx = m.index ?? 0;
      out.push(src.slice(last, idx));
      const tok = m[0];
      if (tok.startsWith("**"))
        out.push(
          <strong key={`${key}-${idx}`} className="font-semibold text-text">
            {tok.slice(2, -2)}
          </strong>,
        );
      else if (tok.startsWith("`"))
        out.push(
          <code key={`${key}-${idx}`} className="rounded bg-raised px-1 py-0.5 font-mono text-[0.85em]">
            {tok.slice(1, -1)}
          </code>,
        );
      else {
        const [, docId, p] = tok.match(/\[cite:([A-Za-z0-9_-]+):(\d+)\]/)!;
        const page = Number(p);
        const k = `${docId}:${page}`;
        let entry = numbers.get(k);
        if (!entry) {
          entry = { n: numbers.size + 1, docId, page, citation: byKey.get(k), claim: claimBefore(src.slice(0, idx)) };
          numbers.set(k, entry);
        }
        const n = entry.n;
        const claim = claimBefore(src.slice(0, idx));
        const isActive = active?.docId === docId && active.page === page;
        const unverified = entry.citation && !entry.citation.seen;
        out.push(
          <button
            key={`${key}-${idx}`}
            onClick={() => onOpen({ docId, page, claim, n })}
            title={`${sourceLabel(entry.citation, docId, page)}${unverified ? ". The agent never retrieved this page." : ""}`}
            aria-label={`Source ${n}: ${sourceLabel(entry.citation, docId, page)}`}
            className={`mx-[2px] inline-flex h-[18px] min-w-[18px] -translate-y-px items-center justify-center rounded-[5px] px-1 align-middle font-mono text-[10.5px] font-medium leading-none transition-colors ${
              unverified
                ? "bg-serious/20 text-serious"
                : isActive
                  ? "bg-amber text-on-amber"
                  : "bg-amber-wash text-amber hover:bg-amber hover:text-on-amber"
            }`}
          >
            {n}
          </button>,
        );
      }
      last = idx + tok.length;
    }
    out.push(src.slice(last));
    return out;
  }

  const blocks: ReactNode[] = [];
  const bullet = /^\s*[-*•]\s+/;
  body
    .trim()
    .split(/\n{2,}/)
    .forEach((block, bi) => {
      const lines = block.split("\n").filter((l) => l.trim());
      if (!lines.length) return;
      const key = `b${bi}`;
      const list = (items: string[], k: string) => (
        <ul key={k} className="space-y-2 pl-4">
          {items.map((l, i) => (
            <li key={i} className="relative before:absolute before:-left-4 before:top-[0.7em] before:h-px before:w-2 before:bg-faint">
              {inline(l.replace(bullet, ""), `${k}-${i}`)}
            </li>
          ))}
        </ul>
      );
      if (lines.length >= 2 && lines.every((l) => l.trim().startsWith("|"))) {
        const cells = (l: string) => l.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
        const rows = lines.filter((l) => !/^\s*\|?\s*:?-{2,}/.test(l)).map(cells);
        const [head, ...body] = rows;
        blocks.push(
          <div key={key} className="overflow-x-auto rounded-lg border border-line">
            <table className="w-full text-left text-[13.5px] leading-snug">
              <thead className="bg-surface text-muted">
                <tr>
                  {head.map((c, i) => (
                    <th key={i} className="px-3 py-2 font-medium">
                      {inline(c, `${key}-h${i}`)}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {body.map((r, ri) => (
                  <tr key={ri} className="border-t border-line align-top">
                    {r.map((c, ci) => (
                      <td key={ci} className={`px-3 py-2 ${ci === 0 ? "text-muted" : "tabular-nums"}`}>
                        {inline(c, `${key}-${ri}-${ci}`)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>,
        );
      } else if (lines.every((l) => bullet.test(l))) blocks.push(list(lines, key));
      else if (lines.every((l) => /^\s*\d+[.)]\s+/.test(l))) {
        blocks.push(
          <ol key={key} className="list-decimal space-y-2 pl-5 marker:text-faint">
            {lines.map((l, i) => (
              <li key={i}>{inline(l.replace(/^\s*\d+[.)]\s+/, ""), `${key}-${i}`)}</li>
            ))}
          </ol>,
        );
      } else if (/^#{1,4}\s/.test(lines[0])) {
        blocks.push(
          <Fragment key={key}>
            <h3 className="pt-2 text-[15px] font-semibold text-text">{inline(lines[0].replace(/^#+\s*/, ""), key)}</h3>
            {lines.length > 1 && <p>{inline(lines.slice(1).join(" "), `${key}-r`)}</p>}
          </Fragment>,
        );
      } else {
        // a paragraph that runs into a list ("Intro:\n- a\n- b")
        const firstItem = lines.findIndex((l) => bullet.test(l));
        if (firstItem > 0 && lines.slice(firstItem).every((l) => bullet.test(l))) {
          blocks.push(<p key={`${key}-p`}>{inline(lines.slice(0, firstItem).join(" "), `${key}-p`)}</p>);
          blocks.push(list(lines.slice(firstItem), key));
        } else blocks.push(<p key={key}>{inline(lines.join(" "), key)}</p>);
      }
    });

  const sources = [...numbers.values()];
  const unverified = (citations ?? []).filter((c) => !c.seen).length;

  return (
    <div>
      <div className="max-w-[68ch] space-y-3.5 text-[15.5px] leading-[1.7] text-text/90">
        {blocks}
        {streaming && <span className="ml-0.5 inline-block h-4 w-[3px] animate-pulse rounded-full bg-amber align-middle" />}
      </div>

      {!streaming && sources.length > 0 && (
        <section className="mt-6 rounded-xl border border-line bg-surface" aria-label="Sources">
          <header className="flex flex-wrap items-center justify-between gap-2 border-b border-line px-4 py-2.5">
            <h3 className="text-[13px] font-medium">
              Sources <span className="text-faint">{sources.length}</span>
            </h3>
            {citations &&
              (unverified ? (
                <span className="flex items-center gap-1.5 text-[12.5px] text-serious">
                  <Icon name="alert" className="size-3.5" /> {unverified} cited page{unverified === 1 ? " was" : "s were"} never retrieved
                </span>
              ) : (
                <span className="flex items-center gap-1.5 text-[12.5px] text-good">
                  <Icon name="shield" className="size-3.5" /> Every cited page was retrieved by the agent
                </span>
              ))}
          </header>
          <ol>
            {sources.map((s) => {
              const isActive = active?.docId === s.docId && active.page === s.page;
              return (
                <li key={`${s.docId}:${s.page}`} className="border-b border-line last:border-0">
                  <button
                    onClick={() => onOpen({ docId: s.docId, page: s.page, claim: s.claim, n: s.n })}
                    className={`group flex w-full items-start gap-3 px-4 py-2.5 text-left transition-colors ${isActive ? "bg-amber-wash" : "hover:bg-raised"}`}
                  >
                    <span
                      className={`mt-px inline-flex h-[18px] min-w-[18px] items-center justify-center rounded-[5px] px-1 font-mono text-[10.5px] font-medium ${
                        s.citation && !s.citation.seen ? "bg-serious/20 text-serious" : isActive ? "bg-amber text-on-amber" : "bg-amber-wash text-amber"
                      }`}
                    >
                      {s.n}
                    </span>
                    <span className="min-w-0 flex-1">
                      <span className="block text-[13.5px] font-medium">
                        {caseLabel(s.citation?.case_number)}
                        <span className="ml-2 font-mono text-[12px] font-normal text-muted">{sourceLabel(s.citation, s.docId, s.page)}</span>
                      </span>
                      {s.citation?.title && <span className="block truncate text-[12.5px] text-faint">{s.citation.title}</span>}
                    </span>
                    <Icon name="chevron" className="mt-1 size-3.5 shrink-0 text-faint group-hover:text-text" />
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
