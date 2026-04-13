---
title: HttpServerRequest (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpServerRequest (unstable)

Server-side `HttpIncomingMessage` extended with request URL, originalUrl, method, cookies, and multipart access (buffered and streamed). Accessed as a Context tag from handlers and middleware, providing schema-based decoders for params, body, and upgrades to Socket for WebSockets.

## Key Exports
- `HttpServerRequest` — Context tag + interface
- `TypeId` / `isServerRequest` — guard
- `schemaBodyJson` / `schemaBodyUrlParams` / `schemaHeaders` — decoders
- `schemaSearchParams` / `schemaCookies` — decoders
- `toURL` — parse request into a URL object
- `upgrade` — Effect yielding a `Socket` for WebSocket upgrades
- `MaxBodySize` — re-exported fiber ref
- `multipart` / `multipartStream` — access to multipart form data

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpServerRequest.ts`

## Related
- [[effect-http]]
- [[effect-http-http-incoming-message]]
- [[effect-http-multipart]]
- [[effect-http-http-router]]
