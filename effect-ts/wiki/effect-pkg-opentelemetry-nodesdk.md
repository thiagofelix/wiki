---
title: NodeSdk (@effect/opentelemetry)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeSdk (@effect/opentelemetry)

Convenience Layer that combines `Resource`, `Tracer`, `Metrics`, and `Logger` configuration into a single `NodeTracerProvider`-backed stack suitable for Node.js applications. Accepts a `Configuration` describing span processors, metric readers, log record processors, resource attributes, and shutdown timeouts.

## Key Exports
- `Configuration` — span processors, tracer config, metric reader(s), temporality, log processors, logger config, resource, shutdownTimeout
- `layerTracerProvider(processor, config?)` — Layer for an `OtelTracerProvider` using `NodeTracerProvider`
- `layer(evaluate)` — combined Resource + Tracer + Metrics + Logger Layer (accepts LazyArg or Effect)

## Source
- `raw/effect-smol/packages/opentelemetry/src/NodeSdk.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-opentelemetry-websdk]]
- [[effect-pkg-opentelemetry-tracer]]
- [[effect-pkg-opentelemetry-metrics]]
- [[effect-pkg-opentelemetry-logger]]
