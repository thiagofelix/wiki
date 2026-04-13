---
title: HttpPlatform (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpPlatform (unstable)

Platform-specific service used by `HttpServerResponse` to generate efficient responses for static files. Knows how to stream a file from disk (`fileResponse`) or from a Web `FileLike` (`fileWebResponse`), compute ETags, and set Content-Type. Implementations are provided by platform packages (Node, Bun, Deno, Web).

## Key Exports
- `HttpPlatform` — Context Service with `fileResponse` / `fileWebResponse`
- `make` — build an `HttpPlatform` from primitive file handlers
- `layer` — (re-exported) platform-provided layer

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpPlatform.ts`

## Related
- [[effect-http]]
- [[effect-http-http-server-response]]
- [[effect-http-etag]]
