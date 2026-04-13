---
title: Telemetry (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Telemetry (unstable)

OpenTelemetry GenAI semantic convention support. Defines typed attribute shapes for GenAI request/response/token/usage/operation metadata and provides helpers to annotate `Tracer.Span`s with properly-prefixed `gen_ai.*` attributes. Also exposes a `SpanTransformer` hook used by `LanguageModel` to decorate spans.

## Key Exports
- `GenAITelemetryAttributes` — full typed attribute shape with `gen_ai.*` prefixes
- `AllAttributes` — unprefixed union of attribute groups
- `BaseAttributes`, `OperationAttributes`, `TokenAttributes`, `UsageAttributes`, `RequestAttributes`, `ResponseAttributes` — per-namespace attribute shapes
- `WellKnownSystem`, `WellKnownOperationName` — known enum values
- `addGenAIAnnotations` — applies a `GenAITelemetryAttributes` object to a `Span`
- `SpanTransformer` — function type `(span, options) => void` for custom decoration
- `CurrentSpanTransformer` — `Context.Reference` used by `LanguageModel` to pick up a custom transformer

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Telemetry.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
