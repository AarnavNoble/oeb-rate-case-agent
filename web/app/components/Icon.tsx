const PATHS = {
  search: "M10.5 4a6.5 6.5 0 1 1 0 13 6.5 6.5 0 0 1 0-13zM20 20l-4.6-4.6",
  external: "M14 4h6v6M20 4l-9 9M18 14v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4",
  shield: "M12 3l7 3v5c0 4.5-3 8.2-7 10-4-1.8-7-5.5-7-10V6zM9 12l2 2 4-4",
  alert: "M12 4l9 16H3zM12 10v4M12 17h.01",
  x: "M6 6l12 12M18 6L6 18",
  chevron: "M9 6l6 6-6 6",
  copy: "M9 9h10v10H9zM5 15V5h10",
  check: "M5 12l4 4 10-10",
  page: "M7 3h10a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zM8.5 8h7M8.5 11.5h7M8.5 15h4",
  table: "M4 5h16v14H4zM4 10h16M4 14.5h16M10 5v14",
  stop: "M7 7h10v10H7z",
  moon: "M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z",
  sun: "M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4",
  arrowUp: "M12 19V5M6 11l6-6 6 6",
  left: "M15 6l-6 6 6 6",
  right: "M9 6l6 6-6 6",
} as const;

export type IconName = keyof typeof PATHS;

export function Icon({ name, className = "size-4" }: { name: IconName; className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={1.6} strokeLinecap="round" strokeLinejoin="round" className={className} aria-hidden>
      <path d={PATHS[name]} />
    </svg>
  );
}

/** Product mark: a filing sheet with an index tab, the way exhibits are separated in a paper record. */
export function Mark({ className = "size-6" }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" className={className} aria-hidden>
      <rect x="3.5" y="3.5" width="13" height="17" rx="2" fill="none" stroke="var(--text)" strokeWidth="1.6" />
      <path d="M6.5 8.5h7M6.5 12h7M6.5 15.5h4" stroke="var(--muted)" strokeWidth="1.6" strokeLinecap="round" />
      <rect x="16.5" y="6" width="4" height="6" rx="1" fill="var(--amber)" />
    </svg>
  );
}
