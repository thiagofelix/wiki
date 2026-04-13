---
title: WebSdk (@effect/opentelemetry)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# WebSdk (@effect/opentelemetry)

Browser counterpart of `NodeSdk` that assembles `Resource`, `Tracer`, `Metrics`, and `Logger` Layers on top of `WebTracerProvider` from `@opentelemetry/sdk-trace-web`. Provides a single `layer` entry point that takes a configuration record and wires everything together.

## Key Exports
- `Configuration` — span processors, tracer config, metric reader, log processors, required resource
- `layerTracerProvider(processor, config?)` — Layer creating a `WebTracerProvider`
- `layer(evaluate)` — combined Web SDK Layer (LazyArg or Effect variant)

## Source
- `raw/effect-smol/packages/opentelemetry/src/WebSdk.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-opentelemetry-nodesdk]]
- [[effect-pkg-opentelemetry-tracer]]
