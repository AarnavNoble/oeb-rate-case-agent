"use client";

import { useEffect, useState } from "react";
import { type AgentRun, type Evals } from "../lib";
import { Icon } from "./Icon";
import { PageHeader } from "./SearchView";

const RETRIEVER_LABEL: Record<string, string> = { vector: "Vector", hybrid: "Hybrid (RRF)", fts: "Full-text" };

const VERDICT: Record<AgentRun["verdict"], { label: string; glyph: string; fill: string; ink: string }> = {
  correct: { label: "Correct", glyph: "✓", fill: "bg-good", ink: "text-ground" },
  partially_correct: { label: "Partly correct", glyph: "◐", fill: "bg-warning", ink: "text-ground" },
  incorrect: { label: "Incorrect", glyph: "✕", fill: "bg-serious", ink: "text-ground" },
  abstained: { label: "Said the evidence wasn't there", glyph: "–", fill: "bg-neutral", ink: "text-ground" },
  error: { label: "Error", glyph: "!", fill: "bg-serious", ink: "text-ground" },
};

const pct = (x: number) => `${Math.round(x * 100)}%`;

function Section({ title, lead, children }: { title: string; lead: React.ReactNode; children: React.ReactNode }) {
  return (
    <section className="border-t border-line pt-8">
      <div className="grid gap-x-10 gap-y-4 lg:grid-cols-[300px_1fr]">
        <div>
          <h2 className="text-[17px] font-semibold">{title}</h2>
          <div className="mt-2 text-[14px] leading-relaxed text-muted">{lead}</div>
        </div>
        <div className="min-w-0">{children}</div>
      </div>
    </section>
  );
}

function RetrievalChart({ evals }: { evals: Evals }) {
  const [hover, setHover] = useState<string | null>(null);
  const [table, setTable] = useState(false);
  const r = evals.retrieval;
  const rows = Object.entries(r.retrievers)
    .map(([k, v]) => ({ key: k, label: RETRIEVER_LABEL[k] ?? k, s: v.unit_gold, ms: v.median_latency_ms }))
    .sort((a, b) => b.s["recall@5"] - a.s["recall@5"]);
  const random = r.baselines.random_chunks.unit;

  return (
    <div>
      <div className="mb-3 flex items-center justify-between">
        <p className="text-[13px] text-muted">Recall@5: share of {r.n_unit_rows} questions where the cited section is in the top 5 passages</p>
        <button onClick={() => setTable(!table)} className="rounded-md px-2 py-1 text-[12.5px] text-muted hover:bg-raised hover:text-text">
          {table ? "Show chart" : "Show table"}
        </button>
      </div>
      {table ? (
        <table className="w-full text-left text-[13px]">
          <thead className="text-muted">
            <tr className="border-b border-line">
              <th className="py-2 font-normal">Retriever</th>
              {["Recall@1", "Recall@5", "Recall@10", "MRR@10", "Median latency"].map((h) => (
                <th key={h} className="py-2 text-right font-normal">
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="font-mono tabular-nums">
            {rows.map((x) => (
              <tr key={x.key} className="border-b border-line">
                <td className="py-2 font-sans">{x.label}</td>
                <td className="py-2 text-right">{x.s["recall@1"].toFixed(3)}</td>
                <td className="py-2 text-right font-medium text-text">{x.s["recall@5"].toFixed(3)}</td>
                <td className="py-2 text-right">{x.s["recall@10"].toFixed(3)}</td>
                <td className="py-2 text-right">{x.s["mrr@10"].toFixed(3)}</td>
                <td className="py-2 text-right">{x.ms} ms</td>
              </tr>
            ))}
            <tr>
              <td className="py-2 font-sans text-muted">Random passages</td>
              <td className="py-2 text-right text-muted">{random["recall@1"].toFixed(3)}</td>
              <td className="py-2 text-right text-muted">{random["recall@5"].toFixed(3)}</td>
              <td className="py-2 text-right text-muted">{random["recall@10"].toFixed(3)}</td>
              <td className="py-2 text-right text-muted">{random["mrr@10"].toFixed(3)}</td>
              <td className="py-2 text-right text-muted">–</td>
            </tr>
          </tbody>
        </table>
      ) : (
        <div className="relative space-y-2.5" onMouseLeave={() => setHover(null)}>
          {/* the random baseline runs through every row as a reference line */}
          <div className="pointer-events-none absolute inset-y-0 left-[132px] right-[56px]">
            <div className="absolute inset-y-[-6px] border-l border-dashed border-faint" style={{ left: `${random["recall@5"] * 100}%` }} />
          </div>
          {rows.map((x) => (
            <div key={x.key} className="relative grid grid-cols-[120px_1fr_44px] items-center gap-3" onMouseEnter={() => setHover(x.key)}>
              <span className="text-[13.5px]">{x.label}</span>
              <div className="h-7 rounded-r-[4px] bg-raised/60">
                <div className="h-full rounded-r-[4px] bg-data" style={{ width: `${x.s["recall@5"] * 100}%` }} />
              </div>
              <span className="text-right font-mono text-[13px] tabular-nums">{x.s["recall@5"].toFixed(2)}</span>
              {hover === x.key && (
                <div className="absolute left-[132px] top-full z-10 mt-1 rounded-md border border-line-strong bg-raised px-3 py-2 text-[12px] shadow-lg">
                  <p className="font-medium">{x.label}</p>
                  <p className="mt-0.5 font-mono text-muted">
                    R@1 {x.s["recall@1"].toFixed(2)}, R@5 {x.s["recall@5"].toFixed(2)}, R@10 {x.s["recall@10"].toFixed(2)}, MRR {x.s["mrr@10"].toFixed(2)}
                  </p>
                </div>
              )}
            </div>
          ))}
          <div className="grid grid-cols-[120px_1fr_44px] items-center gap-3">
            <span className="text-[13.5px] text-muted">Random passages</span>
            <div className="h-7 rounded-r-[4px] bg-raised/60">
              <div className="h-full rounded-r-[4px] bg-neutral" style={{ width: `${random["recall@5"] * 100}%` }} />
            </div>
            <span className="text-right font-mono text-[13px] tabular-nums text-muted">{random["recall@5"].toFixed(2)}</span>
          </div>
        </div>
      )}
    </div>
  );
}

function AgentGrid({ runs }: { runs: AgentRun[] }) {
  const [sel, setSel] = useState<AgentRun | null>(runs[0] ?? null);
  return (
    <div className="grid gap-5 xl:grid-cols-[auto_1fr]">
      <div>
        <div className="grid w-max grid-cols-5 gap-1.5" role="listbox" aria-label="Held-out questions">
          {runs.map((r) => {
            const v = VERDICT[r.verdict] ?? VERDICT.error;
            const isSel = sel?.ir_id === r.ir_id;
            return (
              <button
                key={r.ir_id}
                role="option"
                aria-selected={isSel}
                onClick={() => setSel(r)}
                title={`${r.ir_id}: ${v.label}${r.section_hit ? ", cited the utility's section" : ", missed the utility's section"}`}
                className={`relative flex size-11 items-center justify-center rounded-md text-[15px] font-semibold ${v.fill} ${v.ink} ${
                  isSel ? "ring-2 ring-text ring-offset-2 ring-offset-ground" : "opacity-90 hover:opacity-100"
                }`}
              >
                {v.glyph}
                <span
                  className={`absolute bottom-1 right-1 size-2 rounded-full border border-ground ${r.section_hit ? "bg-ground" : "bg-transparent"}`}
                  aria-hidden
                />
              </button>
            );
          })}
        </div>
        <ul className="mt-4 space-y-1.5 text-[12.5px] text-muted">
          {(["correct", "partially_correct", "abstained"] as const).map((k) => (
            <li key={k} className="flex items-center gap-2">
              <span className={`flex size-4 items-center justify-center rounded-[4px] text-[10px] font-bold ${VERDICT[k].fill} ${VERDICT[k].ink}`}>{VERDICT[k].glyph}</span>
              {VERDICT[k].label} ({runs.filter((r) => r.verdict === k).length})
            </li>
          ))}
          <li className="flex items-center gap-2">
            <span className="relative size-4 rounded-[4px] bg-raised">
              <span className="absolute bottom-0.5 right-0.5 size-2 rounded-full bg-text" />
            </span>
            Dot: cited the section the utility cited ({runs.filter((r) => r.section_hit).length})
          </li>
        </ul>
      </div>
      {sel && (
        <div className="min-w-0 rounded-xl border border-line bg-surface p-4">
          <div className="flex flex-wrap items-center gap-x-3 gap-y-1">
            <span className="font-mono text-[12.5px] text-muted">{sel.ir_id}</span>
            <span className={`rounded-md px-1.5 py-0.5 text-[12px] font-medium ${VERDICT[sel.verdict].fill} ${VERDICT[sel.verdict].ink}`}>{VERDICT[sel.verdict].label}</span>
            <span className={`text-[12.5px] ${sel.section_hit ? "text-good" : "text-serious"}`}>
              {sel.section_hit ? "Cited the utility's section" : "Missed the utility's section"}
            </span>
          </div>
          <p className="mt-3 line-clamp-5 whitespace-pre-line text-[13.5px] leading-relaxed">{sel.query.replace(/\n(?![a-z]\))/g, " ")}</p>
          <dl className="mt-3 grid grid-cols-2 gap-3 text-[12.5px]">
            <div>
              <dt className="text-faint">Utility cited</dt>
              <dd className="font-mono">Exhibit {sel.gold_exhibits.join(", ")}</dd>
            </div>
            <div>
              <dt className="text-faint">Agent cited</dt>
              <dd className="font-mono">{sel.cited_exhibits.length ? `Exhibit ${sel.cited_exhibits.join(", ")}` : "nothing"}</dd>
            </div>
          </dl>
          <p className="mt-3 border-t border-line pt-3 text-[13px] leading-relaxed text-muted">
            <span className="text-text">Judge: </span>
            {sel.rationale}
          </p>
        </div>
      )}
    </div>
  );
}

export function EvalView() {
  const [evals, setEvals] = useState<Evals | null>(null);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    fetch("/api/evals")
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`))))
      .then(setEvals)
      .catch((e) => setError(`Couldn't load the eval results (${e.message}). Run uv run python -m evals.run, then reload.`));
  }, []);

  return (
    <div className="mx-auto w-full max-w-[1080px] px-5 py-10 sm:px-8">
      <PageHeader title="Evaluation">
        Ground truth comes from the case itself. When an intervenor files an interrogatory, the utility&apos;s written response names the evidence
        that answers it. The system gets the same question, without the response, and is scored on whether it finds that evidence.
      </PageHeader>

      {error && (
        <p role="alert" className="mt-6 text-[14px] text-serious">
          {error}
        </p>
      )}
      {!evals && !error && <div className="mt-8 h-64 animate-pulse rounded-xl bg-surface" />}

      {evals && (
        <div className="mt-10 space-y-10">
          <Section
            title="Retrieval"
            lead={
              <>
                {evals.retrieval.n_rows} interrogatory questions from Toronto Hydro&apos;s case, {evals.retrieval.n_unit_rows} of them answered from a
                specific section. A hit means a top-5 passage comes from the exact section or schedule the utility cited. Random passages set the floor.
              </>
            }
          >
            <RetrievalChart evals={evals} />
          </Section>

          <Section
            title="Leakage control"
            lead="The utility's answers are in the corpus too. Left in, retrieval finds the answer instead of the evidence, and the score means nothing."
          >
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="rounded-xl border border-line bg-surface p-4">
                <p className="text-[13px] text-muted">Without the control</p>
                <p className="mt-1 text-[32px] font-semibold tabular-nums text-serious">{pct(evals.retrieval.leakage_ablation.share)}</p>
                <p className="text-[13px] text-muted">of questions have the utility&apos;s own answer in the top 5 passages</p>
              </div>
              <div className="rounded-xl border border-line bg-surface p-4">
                <p className="text-[13px] text-muted">With the control</p>
                <p className="mt-1 text-[32px] font-semibold text-good">Evidence only</p>
                <p className="text-[13px] text-muted">
                  Interrogatory responses, settlements and decisions are filtered out of retrieval, and exhibit references are stripped from each
                  question before it is asked
                </p>
              </div>
            </div>
          </Section>

          <Section
            title="Agent"
            lead={
              <>
                {evals.agent.n} held-out questions, answered by {evals.agent.agent_model} with only the evidence filings available. A separate judge (
                {evals.agent.judge_model}) compared each answer with the utility&apos;s real response.
              </>
            }
          >
            <dl className="mb-6 grid grid-cols-2 gap-4 sm:grid-cols-4">
              {[
                [`${Math.round(evals.agent.citation_unit_accuracy * evals.agent.n)}/${evals.agent.n}`, "cited the section the utility cited"],
                [`${Math.round(evals.agent.citation_accuracy * evals.agent.n)}/${evals.agent.n}`, "cited the exhibit the utility cited"],
                [`${Math.round(evals.agent.correct_or_partial_rate * evals.agent.n)}/${evals.agent.n}`, "judged correct or partly correct"],
                [String(Math.round(evals.agent.unverified_citation_rate * 100)), "citations to pages the agent never retrieved"],
              ].map(([v, l]) => (
                <div key={l}>
                  <dt className="sr-only">{l}</dt>
                  <dd className="text-[26px] font-semibold tabular-nums">{v}</dd>
                  <dd className="text-[12.5px] leading-snug text-muted">{l}</dd>
                </div>
              ))}
            </dl>
            <AgentGrid runs={evals.runs} />
            <p className="mt-4 text-[12.5px] leading-relaxed text-faint">
              Most answers are partly correct because interrogatories have several parts and the judge gives full credit only when every part matches.
              Select a square to read the question and the judge&apos;s reasoning.
            </p>
          </Section>

          <Section title="Checking the checks" lead="Spot checks of the eval labels and the judge. These were reviewed by Claude, not by a person, and are labelled that way in the repo.">
            <ul className="space-y-3">
              {Object.entries(evals.hand_checks).map(([k, v]) => (
                <li key={k} className="flex gap-3 text-[14px]">
                  <span className="w-16 shrink-0 font-mono tabular-nums text-text">{v.split(" ")[0]}</span>
                  <span className="text-muted">{k}</span>
                </li>
              ))}
            </ul>
          </Section>

          <p className="flex items-center gap-2 border-t border-line pt-6 text-[13px] text-muted">
            <Icon name="check" className="size-4 text-good" />
            Reproduce the retrieval numbers with <code className="rounded bg-surface px-1.5 py-0.5 font-mono text-[12.5px] text-text">uv run python -m evals.run</code>
          </p>
        </div>
      )}
    </div>
  );
}
