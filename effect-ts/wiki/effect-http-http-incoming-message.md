---
title: HttpIncomingMessage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpIncomingMessage (unstable)

Shared interface for inbound HTTP messages (both server requests and client responses). Exposes headers, remote address, and lazy body decoders (json, text, arrayBuffer, urlParamsBody, stream), plus Schema-based decoders for JSON bodies, URL-encoded bodies, and headers.

## Key Exports
- `HttpIncomingMessage` — shared interface with lazy body effects
- `TypeId` / `isHttpIncomingMessage` — guard
- `schemaBodyJson` — decode JSON via Schema
- `schemaBodyUrlParams` — decode URL-encoded body
- `schemaHeaders` — decode headers via Schema
- `MaxBodySize` — Context Reference bounding body size
- `inspect` — pretty-print helper

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpIncomingMessage.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client-response]]
- [[effect-http-http-server-request]]
