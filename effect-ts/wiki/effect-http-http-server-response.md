---
title: HttpServerResponse (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpServerResponse (unstable)

Immutable outbound HTTP response: status, statusText, headers, cookies, and `HttpBody`. Provides constructors for text, JSON, HTML, empty, redirects, files, templates, and Schema-encoded bodies, plus combinators for setting headers, cookies, and status.

## Key Exports
- `HttpServerResponse` — response interface
- `Options` / `Options.WithContent` / `Options.WithContentType` — option bags
- `empty` / `text` / `json` / `unsafeJson` / `html` / `raw` — constructors
- `file` / `fileWeb` — platform file responses
- `redirect` — 30x response with Location header
- `stream` / `uint8Array` / `urlParams` — body constructors
- `schemaJson` — Schema-encoded JSON body
- `setHeader` / `setHeaders` / `setCookie` / `setStatus` — combinators
- `isHttpServerResponse` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpServerResponse.ts`

## Related
- [[effect-http]]
- [[effect-http-http-body]]
- [[effect-http-http-platform]]
