---
title: HttpTraceContext (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpTraceContext (unstable)

Parses and serializes distributed tracing headers (W3C `traceparent`, B3 single-header, and X-B3 multi-header variants) into and out of an Effect `Tracer.ExternalSpan`. Used by the HTTP tracer middleware to propagate spans across services.

## Key Exports
- `FromHeaders` — function type parsing headers into an optional span
- `fromHeaders` — try all supported formats in order
- `toHeaders` — serialize a span into tracing headers (b3 + traceparent)
- `w3c` / `b3` / `xb3` — individual format parsers

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpTraceContext.ts`

## Related
- [[effect-http]]
- [[effect-http-http-middleware]]
- [[effect-tracer]]
