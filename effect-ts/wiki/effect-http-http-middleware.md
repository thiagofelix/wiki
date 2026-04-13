---
title: HttpMiddleware (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpMiddleware (unstable)

Composable server-side middleware applied to handler effects producing `HttpServerResponse`. Supplies built-in logger, tracer, CORS, search-param parsing, XML body handling, and timeouts, plus utilities to disable logging/tracing per request.

## Key Exports
- `HttpMiddleware` — function type wrapping a handler effect
- `make` — identity helper for typing custom middleware
- `logger` — request/response logger middleware
- `tracer` — OpenTelemetry-style tracing middleware
- `cors` — CORS handling
- `searchParamsParser` — eagerly decode URL search params
- `xmlParser` — XML body decoder
- `withLoggerDisabled` — opt-out for a single effect
- `TracerDisabledWhen` — Context Reference predicate to skip tracing

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpMiddleware.ts`

## Related
- [[effect-http]]
- [[effect-http-http-router]]
- [[effect-http-http-server]]
