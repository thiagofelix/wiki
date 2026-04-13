---
title: effect/unstable/observability (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/observability (hub)

OpenTelemetry and Prometheus exporters for Effect's logging, metrics, and tracing. Provides an OTLP over HTTP stack (JSON or Protobuf) built on top of a shared batching exporter, plus a text-format Prometheus endpoint for pull-based scraping. All modules are marked `@since 4.0.0` and live under `unstable/` pending stabilization.

## Entries
- [[effect-observability-otlp]] — top-level layer combining logger/metrics/tracer
- [[effect-observability-otlp-exporter]] — shared batching HTTP exporter
- [[effect-observability-otlp-logger]] — Effect `Logger` emitting OTLP log records
- [[effect-observability-otlp-metrics]] — metric registry snapshotter (cumulative/delta)
- [[effect-observability-otlp-tracer]] — span exporter implementing `Tracer`
- [[effect-observability-otlp-resource]] — `Resource` model + attribute helpers
- [[effect-observability-otlp-serialization]] — JSON/Protobuf body encoder service
- [[effect-observability-prometheus-metrics]] — Prometheus text-format exporter and HTTP route
- [[effect-observability-internal]] — internal protobuf encoders

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/`

## Related
- [[effect-ts-v4]]
- [[effect-metric]]
- [[effect-tracer]]
- [[effect-logger]]
