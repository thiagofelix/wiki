---
title: @effect/opentelemetry (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/opentelemetry (hub)

Effect integration with OpenTelemetry that bridges Effect's tracing, metrics, and logging subsystems to OTel providers. Ships Node and Web SDK bundles plus finer-grained Layers for each telemetry pillar so applications can mix-and-match exporters while sharing a single `Resource`.

## Modules
- [[effect-pkg-opentelemetry-resource]] — `Resource` service, env-var Layers, semantic attribute helpers
- [[effect-pkg-opentelemetry-tracer]] — Effect `Tracer` bridge over `Otel.Tracer`/`TracerProvider`
- [[effect-pkg-opentelemetry-metrics]] — `MetricProducer` + reader registration (cumulative/delta temporality)
- [[effect-pkg-opentelemetry-logger]] — Effect `Logger` emitting OTel log records with span/annotation context
- [[effect-pkg-opentelemetry-nodesdk]] — combined Node.js SDK Layer with `NodeTracerProvider`
- [[effect-pkg-opentelemetry-websdk]] — combined Browser SDK Layer with `WebTracerProvider`

## Source
- `raw/effect-smol/packages/opentelemetry/src/`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-vitest]]
