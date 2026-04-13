---
title: OtlpExporter (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OtlpExporter (unstable)

Shared batching HTTP exporter used by the OTLP logger, metrics, and tracer modules. Buffers data and flushes at a configurable interval or when the batch reaches `maxBatchSize`. Retries transient errors with backoff, honors `Retry-After` on 429 responses, and disables itself for 60 seconds after a failure cause.

## Key Exports
- `make` — constructs an exporter returning `{ push }`; requires `HttpClient` and `Scope`
- `url`, `headers`, `label` options for request configuration
- `exportInterval` controls periodic flush frequency
- `maxBatchSize` supports `"disabled"` for unbatched mode
- `body: (data: Array<any>) => HttpBody` pluggable encoder
- `shutdownTimeout` finalizer for flush on scope close
- Built-in retry policy with `retry-after` header handling
- `runExport` runs on interval via `Effect.forkIn`

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/OtlpExporter.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp]]
- [[effect-http-http-client]]
- [[effect-ts-v4]]
