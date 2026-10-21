// Proxies /api/* to the FastAPI backend, streaming the body through (SSE for /api/ask, PDFs).
const API_URL = process.env.OEB_API_URL ?? "http://localhost:8077";

async function proxy(req: Request, ctx: RouteContext<"/api/[...path]">) {
  const { path } = await ctx.params;
  const incoming = new URL(req.url);
  const target = `${API_URL}/api/${path.map(encodeURIComponent).join("/")}${incoming.search}`;
  const upstream = await fetch(target, {
    method: req.method,
    headers: { "content-type": req.headers.get("content-type") ?? "application/json" },
    body: req.method === "GET" ? undefined : await req.text(),
    signal: req.signal,
  });
  const headers = new Headers();
  for (const h of ["content-type", "content-disposition", "cache-control"]) {
    const v = upstream.headers.get(h);
    if (v) headers.set(h, v);
  }
  return new Response(upstream.body, { status: upstream.status, headers });
}

export { proxy as GET, proxy as POST };
