---
title: PrometheusMetrics (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PrometheusMetrics (unstable)

Prometheus exposition-format exporter for Effect's `Metric` registry. Formats the entire registry into the Prometheus text format with optional prefix and metric-name mapper, plus an HTTP route layer that serves metrics at a chosen path for scraping.

## Key Exports
- `format` — `Effect<string>` that produces Prometheus text from current context
- `formatUnsafe` — sync variant taking a services context
- `FormatOptions` — `{ prefix, metricNameMapper }`
- `MetricNameMapper` — `(name: string) => string` transform
- `HttpOptions` — extends `FormatOptions` with `path`
- HTTP route layer integration via `HttpRouter` and `HttpServerResponse`
- Sanitizes metric names per Prometheus rules
- Supports Counter, Gauge, Histogram, Summary, Frequency

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/PrometheusMetrics.ts`

## Related
- [[effect-observability]]
- [[effect-metric]]
- [[effect-unstable-http-router]]
