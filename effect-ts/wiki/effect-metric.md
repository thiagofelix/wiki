---
title: Metric
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Metric

Concurrent, type-safe metrics system for observability. Supports Counters, Gauges, Frequencies, Histograms, and Summaries, each tagged with attributes and collected into snapshots for export. Metrics are updated from any `Effect` and integrate with fiber runtime statistics.

## Key Exports
- `Metric<Input, State>` — base type, input to update with, aggregate state
- `Counter` / `Gauge` / `Frequency` / `Histogram` / `Summary` — primitive types
- `counter` / `gauge` / `frequency` / `histogram` / `summary` — constructors
- `update` — update a metric with a value
- `value` — read the current state of a metric
- `withAttributes` — tag a metric with key-value attributes
- `tagged` / `taggedWithLabels` — attribute helpers
- `linearBoundaries` / `exponentialBoundaries` — histogram bucket builders
- `snapshot` — capture all registered metrics
- `trackAll` / `trackDuration` / `trackSuccess` — wrap effects to auto-update metrics

## Source
- `raw/effect-smol/packages/effect/src/Metric.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tracer]]
