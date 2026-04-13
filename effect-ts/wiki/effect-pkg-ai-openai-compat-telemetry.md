---
title: OpenAiTelemetry (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiTelemetry (@effect/ai-openai-compat)

Extends GenAI OpenTelemetry attributes with OpenAI-compat specific request/response fields. Mirrors `@effect/ai-openai/OpenAiTelemetry` with the same attribute names so traces produced by compat providers stay interchangeable.

## Key Exports
- `OpenAiTelemetryAttributes` — combined GenAI + prefixed attributes
- `AllAttributes` — flat attribute view
- `RequestAttributes` — `responseFormat`, `serviceTier`
- `ResponseAttributes` — `serviceTier`, `systemFingerprint`
- `WellKnownResponseFormat`, `WellKnownServiceTier` — enumerated literal types
- `OpenAiTelemetryAttributeOptions` — annotator input shape
- `addGenAIAnnotations` — dual helper that mutates a `Tracer.Span`

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/OpenAiTelemetry.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-telemetry]]
- [[effect-ai]]
