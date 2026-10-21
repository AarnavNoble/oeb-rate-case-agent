export type Citation = {
  doc_id: string;
  page: number;
  case_number: string | null;
  exhibit: string | null;
  title: string | null;
  seen: boolean;
};

export type ToolEvent = { name: string; input: Record<string, unknown> };

export type Hit = {
  chunk_id: number;
  doc_id: string;
  case_number: string;
  exhibit: string | null;
  title: string;
  page_start: number;
  page_end: number;
  heading: string | null;
  text: string;
  score: number;
  citation: string;
};

export const CASES: Record<string, string> = {
  "EB-2023-0195": "Toronto Hydro 2025–2029",
  "EB-2026-0164": "Hydro One 2028–2032",
};

export const CITE_RE = /\[cite:([A-Za-z0-9_-]+):(\d+)\]/g;

export function pdfUrl(docId: string, page: number) {
  return `/api/pdf/${encodeURIComponent(docId)}#page=${page}`;
}

/** Minimal SSE parser over a fetch() body. */
export async function* readSSE(res: Response): AsyncGenerator<{ event: string; data: unknown }> {
  const reader = res.body!.pipeThrough(new TextDecoderStream()).getReader();
  let buf = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += value;
    let i: number;
    while ((i = buf.indexOf("\n\n")) >= 0) {
      const raw = buf.slice(0, i);
      buf = buf.slice(i + 2);
      let event = "message";
      const data: string[] = [];
      for (const line of raw.split("\n")) {
        if (line.startsWith("event:")) event = line.slice(6).trim();
        else if (line.startsWith("data:")) data.push(line.slice(5).trimStart());
      }
      if (data.length) yield { event, data: JSON.parse(data.join("\n")) };
    }
  }
}
