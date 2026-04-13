---
title: Tracer
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Tracer

Distributed tracing integration for Effect. Defines `Span`/`ExternalSpan`, a pluggable `Tracer` service that creates spans, and hooks into Effect's primitive evaluation. Spans carry status (Started/Ended), attributes, links, kind, and sampling.

## Key Exports
- `Tracer` — interface with `span(...)` factory and optional `context` hook
- `Span` / `ExternalSpan` / `AnySpan` — span models
- `SpanStatus` — Started or Ended with exit
- `SpanOptions` / `SpanOptionsNoTrace` / `TraceOptions` — configuration
- `ParentSpan` / `ParentSpanKey` — service tag for parent span propagation
- `SpanLink` / `SpanKind` — linking and classification
- `EffectPrimitive` — hook type for wrapping evaluation

## Source
- `raw/effect-smol/packages/effect/src/Tracer.ts`

## Related
- [[effect-ts-v4]]
- Works with Effect span combinators and Metric for observability
