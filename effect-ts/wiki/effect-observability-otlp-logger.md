---
title: OtlpLogger (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OtlpLogger (unstable)

Effect `Logger` that emits structured log records to an OTLP `/v1/logs` endpoint. Builds OTLP `LogRecord` values from Effect log options, merging fiber annotations, log spans, and errors. Uses `OtlpExporter` for batching and `OtlpResource` for service identity.

## Key Exports
- `make` — constructs an OTLP `Logger.Logger<unknown, void>`
- `layer` — `Logger.layer` wrapping `make`, merges with existing loggers by default
- Options: `url`, `resource`, `headers`, `exportInterval`, `maxBatchSize`
- `excludeLogSpans` omits `logSpan.*` attributes
- `mergeWithExisting` controls logger composition
- Maps `LogLevel` to OTLP severity numbers
- Attaches current span `traceId`/`spanId` when present
- Exports `LogsData`, `ILogRecord`-compatible shapes

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/OtlpLogger.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp-exporter]]
- [[effect-observability-otlp-resource]]
- [[effect-logger]]
