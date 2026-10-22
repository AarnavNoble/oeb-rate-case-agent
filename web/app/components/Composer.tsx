"use client";

import { useEffect, useRef } from "react";
import { CASES } from "../lib";
import { Icon } from "./Icon";

export type Scope = string | null; // a case number, or null for both

/** Segmented case filter: Both / Toronto Hydro / Hydro One. */
export function ScopeChips({ scope, onScope }: { scope: Scope; onScope: (s: Scope) => void }) {
  const options: [Scope, string][] = [[null, "Both cases"], ...Object.entries(CASES).map(([k, v]) => [k, v.utility] as [Scope, string])];
  return (
    <div className="inline-flex rounded-md border border-line bg-canvas p-0.5" role="radiogroup" aria-label="Case">
      {options.map(([value, label]) => (
        <button
          key={label}
          type="button"
          role="radio"
          aria-checked={scope === value}
          onClick={() => onScope(value)}
          title={value ?? "EB-2023-0195 and EB-2026-0164"}
          className={`rounded-[5px] px-2.5 py-1 text-[12px] transition-colors ${
            scope === value ? "bg-panel font-medium text-ink shadow-[0_1px_2px_rgba(0,0,0,0.08)]" : "text-muted hover:text-ink"
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

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit();
      }}
      className="rounded-lg border border-line-strong bg-panel transition-shadow focus-within:border-accent/50 focus-within:shadow-[0_0_0_3px_var(--tint)]"
    >
      <textarea
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
        className={`block w-full resize-none bg-transparent px-4 outline-none placeholder:text-faint ${compact ? "pb-1 pt-3 text-[14px]" : "pb-2 pt-4 text-[15.5px]"}`}
      />
      <div className="flex flex-wrap items-center justify-between gap-2 px-2.5 pb-2.5 pt-1">
        <ScopeChips scope={scope} onScope={onScope} />
        {busy ? (
          <button
            type="button"
            onClick={onStop}
            className="flex h-8 items-center gap-1.5 rounded-md border border-line-strong px-3 text-[12.5px] text-ink hover:bg-sunken"
          >
            <Icon name="stop" className="size-3.5" /> Stop
          </button>
        ) : (
          <button
            type="submit"
            disabled={!value.trim()}
            className="flex h-8 items-center gap-2 rounded-md bg-accent px-3.5 text-[13px] font-medium text-on-accent transition-colors hover:bg-accent-hover disabled:opacity-40"
          >
            Ask <span className="font-mono text-[11px] opacity-70">↵</span>
          </button>
        )}
      </div>
    </form>
  );
}
