---
title: OtlpTracer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OtlpTracer (unstable)

Effect `Tracer` implementation that exports spans in OTLP format. Builds spans via `Tracer.make`, pushes completed spans through `OtlpExporter`, and supports an optional `context` callback for propagating trace context through effect primitives.

## Key Exports
- `make` — constructs a `Tracer.Tracer`; requires `OtlpSerialization`, `HttpClient`, `Scope`
- `layer` — layered form over `Tracer.Tracer`
- `TraceData` — `{ resourceSpans }` envelope type
- Options: `url`, `resource`, `headers`, `exportInterval`, `maxBatchSize`, `context`
- Only sampled spans are exported
- `makeOtlpSpan` builds OTLP `ISpan` from internal span impl
- Default `exportInterval` 5s, `maxBatchSize` 1000

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/OtlpTracer.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp-exporter]]
- [[effect-tracer]]
