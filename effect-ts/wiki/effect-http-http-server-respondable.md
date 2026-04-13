---
title: HttpServerRespondable (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpServerRespondable (unstable)

Small interface for values that know how to turn themselves into an `HttpServerResponse`. Used by error classes and custom models so middleware can generically call `toResponse`, with sensible fallbacks for schema errors (400) and missing elements (404).

## Key Exports
- `Respondable` — interface with `[symbol]()` returning a response effect
- `symbol` — type id symbol
- `isRespondable` — guard
- `toResponse` — convert a known `Respondable` to a response
- `toResponseOrElse` — convert unknown values, falling back on common types
- `toResponseOrElseDefect` — variant that dies on unknown values

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpServerRespondable.ts`

## Related
- [[effect-http]]
- [[effect-http-http-server-response]]
- [[effect-http-http-server-error]]
