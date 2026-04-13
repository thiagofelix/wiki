---
title: Otlp (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Otlp (unstable)

Top-level OTLP layer that wires together logger, metrics, and tracer exporters against a single base URL. Provides JSON and Protobuf variants and forwards options to each sub-layer. Handles OpenTelemetry Protocol over HTTP for Effect's logging, metric, and tracing subsystems.

## Key Exports
- `layer` — merges OtlpLogger, OtlpMetrics, and OtlpTracer layers; requires `OtlpSerialization`
- `layerJson` — same as `layer` with JSON serialization provided
- `layerProtobuf` — same as `layer` with Protobuf serialization provided
- Accepts `baseUrl`, `resource`, `headers`, `maxBatchSize`, `tracerContext`
- Separate export intervals for logs, metrics, traces
- `metricsTemporality` option: `"cumulative" | "delta"`
- `shutdownTimeout` for graceful flush

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/Otlp.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp-logger]]
- [[effect-observability-otlp-metrics]]
- [[effect-observability-otlp-tracer]]
- [[effect-ts-v4]]
