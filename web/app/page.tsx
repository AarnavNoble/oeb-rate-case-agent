"use client";

import { useEffect, useState } from "react";
import { AskView } from "./components/AskView";
import { type Scope } from "./components/Composer";
import { FilingsView } from "./components/FilingsView";
import { Icon, Mark, type IconName } from "./components/Icon";
import { SearchView } from "./components/SearchView";
import { SourcePanel } from "./components/SourcePanel";
import { CASES, fmt, type CaseStats, type SourceRef } from "./lib";

type View = "ask" | "search" | "filings";

const NAV: { view: View; label: string; icon: IconName }[] = [
  { view: "ask", label: "Research", icon: "chat" },
  { view: "search", label: "Passage search", icon: "search" },
  { view: "filings", label: "Filings", icon: "files" },
];

const REPO = "https://github.com/AarnavNoble/oeb-rate-case-agent";

export default function Home() {
  const [view, setView] = useState<View>("ask");
  const [source, setSource] = useState<SourceRef | null>(null);
  const [scope, setScope] = useState<Scope>(null);
  const [corpus, setCorpus] = useState<CaseStats[] | null>(null);
  const [reset, setReset] = useState(0);
  function toggleTheme() {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem("theme", next);
    } catch {}
  }


  useEffect(() => {
    fetch("/api/corpus")
      .then((r) => (r.ok ? r.json() : null))
      .then(setCorpus)
      .catch(() => setCorpus(null));
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setSource(null);
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  return (
    <div className="flex min-h-screen">
      <aside className="sticky top-0 hidden h-screen w-[232px] shrink-0 flex-col border-r border-line bg-panel px-3 py-4 md:flex">
        <div className="flex items-center gap-2.5 px-2">
          <Mark />
          <div className="leading-tight">
            <p className="text-[14px] font-semibold tracking-tight">Rate Case Research</p>
            <p className="text-[11px] text-muted">Ontario Energy Board</p>
          </div>
        </div>

        <button
          onClick={() => {
            setView("ask");
            setSource(null);
            setReset((n) => n + 1);
          }}
          className="mt-5 flex items-center justify-center gap-1.5 rounded-lg bg-navy px-3 py-2 text-[13px] font-medium text-on-navy hover:bg-navy-hover"
        >
          <Icon name="plus" className="size-4" /> New question
        </button>

        <p className="eyebrow mt-6 px-2">Workbench</p>
        <nav className="mt-2 space-y-0.5">
          {NAV.map((n) => (
            <button
              key={n.view}
              onClick={() => setView(n.view)}
              aria-current={view === n.view ? "page" : undefined}
              className={`flex w-full items-center gap-2.5 rounded-lg px-2.5 py-1.5 text-[13px] transition-colors ${
                view === n.view ? "bg-tint font-medium text-navy" : "text-muted hover:bg-sunken hover:text-ink"
              }`}
            >
              <Icon name={n.icon} />
              {n.label}
            </button>
          ))}
        </nav>

        <p className="eyebrow mt-6 px-2">Cases</p>
        <ul className="mt-2 space-y-0.5">
          {Object.entries(CASES).map(([k, v]) => {
            const stats = corpus?.find((c) => c.case_number === k);
            return (
              <li key={k}>
                <button
                  onClick={() => setScope(scope === k ? null : k)}
                  className={`w-full rounded-lg px-2.5 py-1.5 text-left transition-colors ${scope === k ? "bg-tint" : "hover:bg-sunken"}`}
                >
                  <span className="flex items-center justify-between text-[13px]">
                    <span className={scope === k ? "font-medium text-navy" : ""}>{v.utility}</span>
                    {scope === k && <Icon name="check" className="size-3.5 text-navy" />}
                  </span>
                  <span className="block font-mono text-[10.5px] text-faint">
                    {k}
                    {stats ? ` · ${fmt.format(stats.pages)} pp` : ""}
                  </span>
                </button>
              </li>
            );
          })}
        </ul>

        <div className="mt-auto space-y-2 px-2 text-[11.5px] text-muted">
          <p className="flex items-start gap-1.5">
            <Icon name="shield" className="mt-px size-3.5 shrink-0 text-ok" />
            Answers are checked: every citation must be a page the agent retrieved, and cited figures are matched against the page.
          </p>
          <div className="flex items-center justify-between">
            <a href={REPO} target="_blank" rel="noreferrer" className="flex items-center gap-1 hover:text-ink">
              Source & evals <Icon name="external" className="size-3" />
            </a>
            <button onClick={toggleTheme} aria-label="Toggle dark theme" className="rounded-md p-1 hover:bg-sunken hover:text-ink">
              <Icon name="moon" className="size-3.5 dark:hidden" />
              <Icon name="sun" className="hidden size-3.5 dark:block" />
            </button>
          </div>
        </div>
      </aside>

      <div className="flex min-w-0 flex-1 flex-col">
        <header className="sticky top-0 z-20 flex h-14 items-center gap-2 border-b border-line bg-panel/95 px-3 backdrop-blur md:hidden">
          <Mark className="size-6" />
          <nav className="flex flex-1 gap-1 overflow-x-auto">
            {NAV.map((n) => (
              <button
                key={n.view}
                onClick={() => setView(n.view)}
                className={`flex shrink-0 items-center gap-1.5 rounded-md px-2.5 py-1.5 text-[12.5px] ${view === n.view ? "bg-tint font-medium text-navy" : "text-muted"}`}
              >
                <Icon name={n.icon} className="size-3.5" />
                {n.label}
              </button>
            ))}
          </nav>
        </header>

        <div className="flex min-w-0 flex-1">
          <main className="min-w-0 flex-1">
            <div className={view === "ask" ? "" : "hidden"}>
              <AskView corpus={corpus} active={source} onOpen={setSource} scope={scope} onScope={setScope} resetSignal={reset} />
            </div>
            {view === "search" && <SearchView active={source} onOpen={setSource} scope={scope} onScope={setScope} />}
            {view === "filings" && <FilingsView corpus={corpus} active={source} onOpen={setSource} scope={scope} onScope={setScope} />}
          </main>
          {source && <SourcePanel source={source} onClose={() => setSource(null)} onPage={(page) => setSource({ docId: source.docId, page })} onJump={(page) => setSource({ ...source, page })} />}
        </div>
      </div>
    </div>
  );
}
