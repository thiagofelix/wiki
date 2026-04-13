---
title: Tracer (@effect/opentelemetry)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Tracer (@effect/opentelemetry)

Effect `Tracer` implementation backed by an OpenTelemetry `Otel.Tracer`. Converts Effect spans into OTel spans, propagates parent span context, exposes external-span constructors for incoming trace contexts, and records attributes, exceptions, and exit values on span close.

## Key Exports
- `OtelTracer` — Context service holding an `Otel.Tracer`
- `OtelTracerProvider` — service holding an `Otel.TracerProvider`
- `OtelTraceFlags` / `OtelTraceState` — propagation context services
- `make` — Effect producing an Effect `Tracer.Tracer`
- `makeExternalSpan(options)` — build an `ExternalSpan` from trace/span ids
- `layer` — Layer providing the tracer on top of `OtelTracer`
- `OtelSpan` — internal class adapting Effect span lifecycle to OTel

## Source
- `raw/effect-smol/packages/opentelemetry/src/Tracer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-opentelemetry-nodesdk]]
- [[effect-pkg-opentelemetry-websdk]]
