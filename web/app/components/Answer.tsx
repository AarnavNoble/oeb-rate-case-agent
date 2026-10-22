import { Fragment, type ReactNode } from "react";
import { caseLabel, CITE_RE, type Citation, type SourceRef } from "../lib";
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
function shortTitle(title: string) {
  return title.replace(/^(THESL|HONI)_/, "").replace(/_\d{8}$/, "").replace(/_/g, " ");
}

export function sourceLabel(c: Citation | undefined, docId: string, page: number) {
  if (!c?.case_number) return `${docId} · p. ${page}`;
  return `${caseLabel(c.case_number)} · ${c.exhibit ? `Ex. ${c.exhibit}` : shortTitle(c.title ?? docId)} · p. ${page}`;
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
      if (tok.startsWith("**")) out.push(<strong key={`${key}-${idx}`} className="font-semibold">{tok.slice(2, -2)}</strong>);
      else if (tok.startsWith("`"))
        out.push(
          <code key={`${key}-${idx}`} className="rounded bg-sunken px-1 py-0.5 font-mono text-[0.85em]">
            {tok.slice(1, -1)}
          </code>,
        );
      else {
        const [, docId, p] = tok.match(/\[cite:([A-Za-z0-9_-]+):(\d+)\]/)!;
        const page = Number(p);
        const k = `${docId}:${page}`;
        let s = numbers.get(k);
        if (!s) {
          s = { n: numbers.size + 1, docId, page, citation: byKey.get(k), claim: claimBefore(src.slice(0, idx)) };
          numbers.set(k, s);
        }
        const entry = s;
        const claim = claimBefore(src.slice(0, idx));
        const isActive = active?.docId === docId && active.page === page;
        const unverified = entry.citation && !entry.citation.seen;
        out.push(
          <button
            key={`${key}-${idx}`}
            onClick={() => onOpen({ docId, page, claim, n: entry.n })}
            title={`${sourceLabel(entry.citation, docId, page)}${unverified ? " — the agent never retrieved this page" : ""}`}
            className={`relative -top-px mx-[1px] inline-flex size-[18px] items-center justify-center rounded-full align-middle font-mono text-[10px] font-medium leading-none transition-colors ${
              unverified
                ? "bg-warn-bg text-warn ring-1 ring-warn/40"
                : isActive
                  ? "bg-navy text-on-navy"
                  : "bg-tint text-navy ring-1 ring-tint-strong hover:bg-navy hover:text-on-navy"
            }`}
          >
            {entry.n}
          </button>,
        );
      }
      last = idx + tok.length;
    }
    out.push(src.slice(last));
    return out;
  }

  const blocks: ReactNode[] = [];
  body
    .trim()
    .split(/\n{2,}/)
    .forEach((block, bi) => {
      const lines = block.split("\n").filter((l) => l.trim());
      if (!lines.length) return;
      const key = `b${bi}`;
      if (lines.every((l) => /^\s*[-*•]\s+/.test(l))) {
        blocks.push(
          <ul key={key} className="list-disc space-y-1.5 pl-5 marker:text-faint">
            {lines.map((l, i) => (
              <li key={i}>{inline(l.replace(/^\s*[-*•]\s+/, ""), `${key}-${i}`)}</li>
            ))}
          </ul>,
        );
      } else if (lines.every((l) => /^\s*\d+[.)]\s+/.test(l))) {
        blocks.push(
          <ol key={key} className="list-decimal space-y-1.5 pl-5 marker:font-mono marker:text-xs marker:text-faint">
            {lines.map((l, i) => (
              <li key={i}>{inline(l.replace(/^\s*\d+[.)]\s+/, ""), `${key}-${i}`)}</li>
            ))}
          </ol>,
        );
      } else if (/^#{1,4}\s/.test(lines[0])) {
        blocks.push(
          <Fragment key={key}>
            <h3 className="pt-1 text-[15px] font-semibold tracking-tight">{inline(lines[0].replace(/^#+\s*/, ""), key)}</h3>
            {lines.length > 1 && <p>{inline(lines.slice(1).join(" "), `${key}-r`)}</p>}
          </Fragment>,
        );
      } else {
        // a paragraph that runs into a list ("Intro:\n- a\n- b")
        const firstItem = lines.findIndex((l) => /^\s*[-*•]\s+/.test(l));
        if (firstItem > 0 && lines.slice(firstItem).every((l) => /^\s*[-*•]\s+/.test(l))) {
          blocks.push(<p key={`${key}-p`}>{inline(lines.slice(0, firstItem).join(" "), `${key}-p`)}</p>);
          blocks.push(
            <ul key={key} className="list-disc space-y-1.5 pl-5 marker:text-faint">
              {lines.slice(firstItem).map((l, i) => (
                <li key={i}>{inline(l.replace(/^\s*[-*•]\s+/, ""), `${key}-${i}`)}</li>
              ))}
            </ul>,
          );
        } else blocks.push(<p key={key}>{inline(lines.join(" "), key)}</p>);
      }
    });

  const sources = [...numbers.values()];
  const unverified = (citations ?? []).filter((c) => !c.seen).length;

  return (
    <div>
      <div className="space-y-3 text-[14.5px] leading-[1.7] text-ink">
        {blocks}
        {streaming && <span className="ml-0.5 inline-block h-4 w-[7px] animate-pulse rounded-[1px] bg-navy align-middle" />}
      </div>

      {!streaming && sources.length > 0 && (
        <div className="mt-5 overflow-hidden rounded-lg border border-line bg-panel">
          <div className="flex items-center justify-between border-b border-line px-3 py-2">
            <span className="eyebrow">Sources · {sources.length}</span>
            {citations &&
              (unverified ? (
                <span className="flex items-center gap-1 text-[11.5px] text-warn">
                  <Icon name="alert" className="size-3.5" /> {unverified} not on a page the agent retrieved
                </span>
              ) : (
                <span className="flex items-center gap-1 text-[11.5px] text-ok">
                  <Icon name="shield" className="size-3.5" /> Every citation is a page the agent retrieved
                </span>
              ))}
          </div>
          <ol className="divide-y divide-line">
            {sources.map((s) => {
              const isActive = active?.docId === s.docId && active.page === s.page;
              return (
                <li key={`${s.docId}:${s.page}`}>
                  <button
                    onClick={() => onOpen({ docId: s.docId, page: s.page, claim: s.claim, n: s.n })}
                    className={`group flex w-full items-center gap-3 px-3 py-2 text-left text-[13px] transition-colors ${isActive ? "bg-tint" : "hover:bg-sunken"}`}
                  >
                    <span
                      className={`flex size-[18px] shrink-0 items-center justify-center rounded-full font-mono text-[10px] ${
                        s.citation && !s.citation.seen ? "bg-warn-bg text-warn" : isActive ? "bg-navy text-on-navy" : "bg-tint text-navy"
                      }`}
                    >
                      {s.n}
                    </span>
                    <span className="min-w-0 flex-1">
                      <span className="font-medium">{sourceLabel(s.citation, s.docId, s.page)}</span>
                      {s.citation?.title && <span className="block truncate text-[12px] text-muted">{s.citation.title}</span>}
                    </span>
                    <Icon name="chevron" className="size-3.5 shrink-0 text-faint group-hover:text-ink" />
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
