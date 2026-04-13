---
title: Logger (@effect/opentelemetry)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Logger (@effect/opentelemetry)

Effect `Logger` implementation that forwards log events to an OpenTelemetry `LoggerProvider`. Captures the fiber id, trace/span ids from `Tracer.ParentSpan`, log annotations, and log spans as attributes, and maps `LogLevel` to OTel severity numbers.

## Key Exports
- `OtelLoggerProvider` — Context service holding an `Otel.LoggerProvider`
- `make` — Effect producing a `Logger.Logger` backed by an OTel logger
- `layer({ mergeWithExisting })` — Layer installing the logger
- `layerLoggerProvider(processor, config?)` — Layer that constructs an `Otel.LoggerProvider` from a `Resource`

## Source
- `raw/effect-smol/packages/opentelemetry/src/Logger.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-opentelemetry-resource]]
- [[effect-pkg-opentelemetry-tracer]]
