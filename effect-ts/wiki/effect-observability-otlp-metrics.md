---
title: OtlpMetrics (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OtlpMetrics (unstable)

Periodic metrics snapshot exporter that encodes Effect's `Metric` registry into OTLP metrics messages. Supports both cumulative (default) and delta aggregation temporality, tracking previous state per metric for delta conversion of counters, histograms, frequency, and summary aggregations.

## Key Exports
- `make` — constructs the exporter; requires `HttpClient`, `OtlpSerialization`, `Scope`
- `layer` — layered form of `make`
- `AggregationTemporality` — `"cumulative" | "delta"` type
- `MetricsData` — top-level OTLP metrics envelope
- Snapshots Counter, Gauge, Histogram, Frequency, Summary metrics
- Handles counter reset semantics in delta mode
- Uses `Metric.snapshotUnsafe` to read registry
- Delta state maps per metric key

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/OtlpMetrics.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp-exporter]]
- [[effect-metric]]
- [[effect-observability-prometheus-metrics]]
