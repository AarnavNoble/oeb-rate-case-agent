"use client";

import { useEffect, useRef } from "react";
import { CASES } from "../lib";
import { Icon } from "./Icon";

export type Scope = string | null; // a case number, or null for both

/** Segmented case filter: both cases, or one. */
export function ScopeChips({ scope, onScope }: { scope: Scope; onScope: (s: Scope) => void }) {
  const options: [Scope, string][] = [[null, "Both cases"], ...Object.entries(CASES).map(([k, v]) => [k, v.utility] as [Scope, string])];
  return (
    <div className="inline-flex rounded-md bg-ground p-0.5" role="radiogroup" aria-label="Which case to search">
      {options.map(([value, label]) => (
        <button
          key={label}
          type="button"
          role="radio"
          aria-checked={scope === value}
          onClick={() => onScope(value)}
          title={value ?? "EB-2023-0195 and EB-2026-0164"}
          className={`rounded-[5px] px-2.5 py-1 text-[12.5px] transition-colors ${
            scope === value ? "bg-raised font-medium text-text" : "text-muted hover:text-text"
          }`}
        >
          {label}
        </button>
      ))}
    </div>
  );
}

export function Composer({
  value,
  onChange,
  onSubmit,
  onStop,
  busy,
  scope,
  onScope,
  placeholder,
  autoFocus,
  compact,
}: {
  value: string;
  onChange: (v: string) => void;
  onSubmit: () => void;
  onStop: () => void;
  busy: boolean;
  scope: Scope;
  onScope: (s: Scope) => void;
  placeholder: string;
  autoFocus?: boolean;
  compact?: boolean;
}) {
  const ref = useRef<HTMLTextAreaElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, 220)}px`;
  }, [value]);

  // "/" focuses the question box from anywhere, unless the person is already typing
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const t = e.target as HTMLElement;
      if (e.key === "/" && !/^(INPUT|TEXTAREA)$/.test(t.tagName) && !t.isContentEditable) {
        e.preventDefault();
        ref.current?.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit();
      }}
      className="rounded-xl border border-line-strong bg-surface transition-colors focus-within:border-amber-line"
    >
      <label htmlFor="question" className="sr-only">
        Question
      </label>
      <textarea
        id="question"
        ref={ref}
        value={value}
        autoFocus={autoFocus}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
            e.preventDefault();
            onSubmit();
          }
        }}
        rows={compact ? 1 : 2}
        placeholder={placeholder}
        className={`block w-full resize-none bg-transparent px-4 outline-none placeholder:text-faint focus-visible:outline-none ${compact ? "pb-1 pt-3 text-[14.5px]" : "pb-2 pt-4 text-[16px]"}`}
      />
      <div className="flex flex-wrap items-center justify-between gap-2 px-2.5 pb-2.5 pt-1">
        <ScopeChips scope={scope} onScope={onScope} />
        <div className="flex items-center gap-3">
          {!compact && <span className="hidden text-[12px] text-faint sm:inline">Enter to ask, Shift+Enter for a new line</span>}
          {busy ? (
            <button type="button" onClick={onStop} className="flex h-8 items-center gap-1.5 rounded-lg border border-line-strong px-3 text-[13px] hover:bg-raised">
              <Icon name="stop" className="size-3.5" /> Stop
            </button>
          ) : (
            <button
              type="submit"
              disabled={!value.trim()}
              className="flex h-8 items-center gap-1.5 rounded-lg bg-amber px-3.5 text-[13px] font-semibold text-on-amber transition-colors hover:bg-amber-hover disabled:opacity-40"
            >
              Ask
              <Icon name="arrowUp" className="size-3.5" />
            </button>
          )}
        </div>
      </div>
    </form>
  );
}
