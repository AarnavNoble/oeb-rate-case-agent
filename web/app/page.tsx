"use client";

import { useEffect, useState } from "react";
import { AskView } from "./components/AskView";
import { type Scope } from "./components/Composer";
import { FilingsView } from "./components/FilingsView";
import { Icon, Mark } from "./components/Icon";
import { SearchView } from "./components/SearchView";
import { SourcePanel } from "./components/SourcePanel";
import { type CaseStats, type SourceRef } from "./lib";

type View = "ask" | "search" | "filings";

const NAV: { view: View; label: string }[] = [
  { view: "ask", label: "Ask" },
  { view: "search", label: "Search passages" },
  { view: "filings", label: "Filings" },
];

const REPO = "https://github.com/AarnavNoble/oeb-rate-case-agent";

export default function Home() {
  const [view, setView] = useState<View>("ask");
  const [source, setSource] = useState<SourceRef | null>(null);
  const [scope, setScope] = useState<Scope>(null);
  const [corpus, setCorpus] = useState<CaseStats[] | null>(null);
  const [reset, setReset] = useState(0);

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

  function toggleTheme() {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem("theme", next);
    } catch {}
  }

  return (
    <div className="flex h-screen flex-col">
      <header className="z-20 shrink-0 border-b border-line bg-panel">
        <div className="flex h-14 items-center gap-4 px-4 sm:px-6">
          <button
            onClick={() => {
              setView("ask");
              setSource(null);
              setReset((n) => n + 1);
            }}
            className="flex items-center gap-2.5"
            title="New question"
          >
            <Mark className="size-8 text-[17px]" />
            <span className="hidden font-serif text-[18px] font-semibold tracking-tight sm:inline">Rate Case Research</span>
          </button>
          <nav className="ml-2 flex h-full items-stretch gap-1 overflow-x-auto sm:ml-6">
            {NAV.map((n) => (
              <button
                key={n.view}
                onClick={() => setView(n.view)}
                aria-current={view === n.view ? "page" : undefined}
                className={`relative shrink-0 px-2.5 text-[13.5px] transition-colors ${
                  view === n.view
                    ? "font-medium text-ink after:absolute after:inset-x-2.5 after:bottom-0 after:h-[2px] after:rounded-full after:bg-accent"
                    : "text-muted hover:text-ink"
                }`}
              >
                {n.label}
              </button>
            ))}
          </nav>
          <div className="ml-auto flex items-center gap-1 text-muted">
            <span className="mr-2 hidden items-center gap-1.5 text-[12px] lg:flex">
              <Icon name="shield" className="size-3.5 text-ok" />
              Citations checked against the pages the agent retrieved
            </span>
            <a href={REPO} target="_blank" rel="noreferrer" className="flex items-center gap-1 rounded-md px-2 py-1.5 text-[12.5px] hover:bg-sunken hover:text-ink">
              Code & evals <Icon name="external" className="size-3" />
            </a>
            <button onClick={toggleTheme} aria-label="Toggle dark theme" className="rounded-md p-2 hover:bg-sunken hover:text-ink">
              <Icon name="moon" className="size-4 dark:hidden" />
              <Icon name="sun" className="hidden size-4 dark:block" />
            </button>
          </div>
        </div>
      </header>

      <div className="flex min-h-0 flex-1">
        <main className="min-w-0 flex-1 overflow-y-auto">
          <div className={view === "ask" ? "h-full" : "hidden"}>
            <AskView
              corpus={corpus}
              active={source}
              onOpen={setSource}
              scope={scope}
              onScope={setScope}
              resetSignal={reset}
              onBrowse={(s) => {
                setScope(s);
                setView("filings");
              }}
            />
          </div>
          {view === "search" && <SearchView active={source} onOpen={setSource} scope={scope} onScope={setScope} />}
          {view === "filings" && <FilingsView corpus={corpus} active={source} onOpen={setSource} scope={scope} onScope={setScope} />}
        </main>
        {source && (
          <SourcePanel
            source={source}
            onClose={() => setSource(null)}
            onPage={(page) => setSource({ docId: source.docId, page })}
            onJump={(page) => setSource({ ...source, page })}
          />
        )}
      </div>
    </div>
  );
}
