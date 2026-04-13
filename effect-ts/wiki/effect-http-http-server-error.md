---
title: HttpServerError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpServerError (unstable)

Tagged errors raised on the server side during request handling. Implements `Respondable` so errors can be converted to default HTTP responses (400 for parse errors, 499 for client abort, 500 for internals). `causeResponse` converts arbitrary `Cause` values into a response plus residual cause.

## Key Exports
- `HttpServerError` — top-level tagged error with reason discriminator
- `RequestError` / `RequestParseError` — request-level failures
- `ResponseError` — response construction failure
- `ServeError` — underlying server transport error
- `ClientAbort` — client disconnected
- `InternalError` — catch-all 500
- `causeResponse` — convert `Cause` to `[response, residualCause]`
- `causeResponseStripped` / `exitResponse` — helpers for handlers
- `isServerError` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpServerError.ts`

## Related
- [[effect-http]]
- [[effect-http-http-server-respondable]]
- [[effect-http-http-effect]]
