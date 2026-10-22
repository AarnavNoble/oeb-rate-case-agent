"use client";

import { useEffect, useRef } from "react";
import { CASES } from "../lib";
import { Icon } from "./Icon";

export type Scope = string | null; // a case number, or null for both

export function ScopeChips({ scope, onScope }: { scope: Scope; onScope: (s: Scope) => void }) {
  const options: [Scope, string][] = [[null, "Both cases"], ...Object.entries(CASES).map(([k, v]) => [k, v.utility] as [Scope, string])];
  return (
    <div className="flex flex-wrap gap-1.5">
      {options.map(([value, label]) => (
        <button
          key={label}
          type="button"
          onClick={() => onScope(value)}
          aria-pressed={scope === value}
          className={`flex items-center gap-1.5 rounded-full border px-2.5 py-[3px] text-[12px] transition-colors ${
            scope === value ? "border-tint-strong bg-tint text-navy" : "border-line bg-panel text-muted hover:border-line-strong hover:text-ink"
          }`}
        >
          <Icon name="files" className="size-3.5" />
          {label}
          {value && <span className="font-mono text-[10.5px] opacity-70">{value}</span>}
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
}) {
  const ref = useRef<HTMLTextAreaElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, 220)}px`;
  }, [value]);

  return (
    <div className="w-full">
      <div className="mb-2">
        <ScopeChips scope={scope} onScope={onScope} />
      </div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit();
        }}
        className="overflow-hidden rounded-xl border border-line-strong bg-panel shadow-[0_1px_2px_rgba(16,24,40,0.04),0_4px_16px_-6px_rgba(16,24,40,0.08)] focus-within:border-navy/40"
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
          rows={1}
          placeholder={placeholder}
          className="block w-full resize-none bg-transparent px-4 pb-2 pt-3.5 text-[14.5px] outline-none placeholder:text-faint"
        />
        <div className="flex items-center justify-between gap-2 border-t border-line bg-sunken/60 px-2.5 py-2">
          <span className="pl-1 text-[11.5px] text-faint">
            Answers cite filing pages · <kbd className="font-mono">Enter</kbd> to send, <kbd className="font-mono">Shift+Enter</kbd> for a new line
          </span>
          {busy ? (
            <button
              type="button"
              onClick={onStop}
              aria-label="Stop"
              className="flex size-8 items-center justify-center rounded-lg border border-line-strong bg-panel text-ink hover:bg-sunken"
            >
              <Icon name="stop" className="size-3.5" />
            </button>
          ) : (
            <button
              type="submit"
              disabled={!value.trim()}
              aria-label="Send"
              className="flex size-8 items-center justify-center rounded-lg bg-navy text-on-navy transition-colors hover:bg-navy-hover disabled:opacity-35"
            >
              <Icon name="arrowUp" />
            </button>
          )}
        </div>
      </form>
    </div>
  );
}
