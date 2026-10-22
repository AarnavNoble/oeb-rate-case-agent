"use client";

import { useEffect, useState } from "react";
import { AskView } from "./components/AskView";
import { type Scope } from "./components/Composer";
import { EvalView } from "./components/EvalView";
import { FilingsView } from "./components/FilingsView";
import { Icon, Mark } from "./components/Icon";
import { SearchView } from "./components/SearchView";
import { SourcePanel } from "./components/SourcePanel";
import { type Pipeline, type SourceRef } from "./lib";

type View = "ask" | "search" | "evals" | "data";

// Each view has its own URL hash, so a view can be linked to and the back button works.
const NAV: { view: View; label: string; hash: string }[] = [
  { view: "ask", label: "Ask", hash: "" },
  { view: "search", label: "Search", hash: "#search" },
  { view: "evals", label: "Evaluation", hash: "#evaluation" },
  { view: "data", label: "Data", hash: "#data" },
];

const REPO = "https://github.com/AarnavNoble/oeb-rate-case-agent";

function viewFromHash(): View {
  if (typeof window === "undefined") return "ask";
  return NAV.find((n) => n.hash && n.hash === window.location.hash)?.view ?? "ask";
}

export default function Home() {
  const [view, setViewState] = useState<View>("ask");
  const [source, setSource] = useState<SourceRef | null>(null);
  const [scope, setScope] = useState<Scope>(null);
  const [pipeline, setPipeline] = useState<Pipeline | null>(null);
  const [reset, setReset] = useState(0);

  function setView(v: View) {
    const hash = NAV.find((n) => n.view === v)!.hash;
    history.pushState(null, "", hash || window.location.pathname);
    setViewState(v);
  }

  useEffect(() => {
    const sync = () => setViewState(viewFromHash());
    sync();
    window.addEventListener("popstate", sync);
    return () => window.removeEventListener("popstate", sync);
  }, []);

  useEffect(() => {
    fetch("/api/pipeline")
      .then((r) => (r.ok ? r.json() : null))
      .then(setPipeline)
      .catch(() => setPipeline(null));
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setSource(null);
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  function toggleTheme() {
    const next = document.documentElement.dataset.theme === "light" ? "dark" : "light";
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem("theme", next);
    } catch {}
  }

  return (
    <div className="flex h-screen flex-col">
      <header className="z-20 shrink-0 border-b border-line bg-ground">
        <div className="flex h-14 items-center gap-2 px-4 sm:gap-6 sm:px-6">
          <button
            onClick={() => {
              setView("ask");
              setSource(null);
              setReset((n) => n + 1);
            }}
            className="flex shrink-0 items-center gap-2 rounded-md"
            aria-label="Rate Case Research, start a new question"
          >
            <Mark className="size-6" />
            <span className="hidden text-[14.5px] font-semibold md:inline">Rate Case Research</span>
          </button>
          <nav aria-label="Main" className="flex h-full min-w-0 items-stretch gap-0.5 overflow-x-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden">
            {NAV.map((n) => (
              <button
                key={n.view}
                onClick={() => setView(n.view)}
                aria-current={view === n.view ? "page" : undefined}
                className={`relative shrink-0 px-3 text-[13.5px] transition-colors ${
                  view === n.view
                    ? "font-medium text-text after:absolute after:inset-x-3 after:bottom-[-1px] after:h-[2px] after:rounded-full after:bg-amber"
                    : "text-muted hover:text-text"
                }`}
              >
                {n.label}
              </button>
            ))}
          </nav>
          <div className="ml-auto flex shrink-0 items-center gap-1 text-muted">
            <a href={REPO} target="_blank" rel="noreferrer" className="hidden items-center gap-1 rounded-md px-2 py-1.5 text-[13px] hover:bg-surface hover:text-text sm:flex">
              Source code <Icon name="external" className="size-3.5" />
            </a>
            <button onClick={toggleTheme} aria-label="Switch between dark and light theme" className="rounded-md p-2 hover:bg-surface hover:text-text">
              <Icon name="sun" className="size-4 light:hidden" />
              <Icon name="moon" className="hidden size-4 light:block" />
            </button>
          </div>
        </div>
      </header>

      <div className="flex min-h-0 flex-1">
        <main className="min-w-0 flex-1 overflow-y-auto">
          <div className={view === "ask" ? "h-full" : "hidden"}>
            <AskView
              pipeline={pipeline}
              active={source}
              onOpen={setSource}
              scope={scope}
              onScope={setScope}
              resetSignal={reset}
              onNavigate={(v) => setView(v)}
            />
          </div>
          {view === "search" && <SearchView active={source} onOpen={setSource} scope={scope} onScope={setScope} />}
          {view === "evals" && <EvalView />}
          {view === "data" && <FilingsView pipeline={pipeline} active={source} onOpen={setSource} scope={scope} onScope={setScope} />}
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
