---
title: Metrics (@effect/opentelemetry)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Metrics (@effect/opentelemetry)

Bridge between Effect metrics and OpenTelemetry `MetricReader` instances. Constructs a `MetricProducer` that snapshots Effect metric registry values (supporting cumulative or delta temporality) and registers it with one or more readers such as `PeriodicExportingMetricReader`.

## Key Exports
- `TemporalityPreference` — `"cumulative" | "delta"`
- `makeProducer(temporality?)` — produces an OTel `MetricProducer` from Effect metrics
- `registerProducer(self, metricReader, options?)` — scoped acquire/release
- `layer(evaluate, options?)` — Layer wiring a reader factory to the Effect runtime

## Source
- `raw/effect-smol/packages/opentelemetry/src/Metrics.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-opentelemetry-resource]]
- [[effect-pkg-opentelemetry-nodesdk]]
