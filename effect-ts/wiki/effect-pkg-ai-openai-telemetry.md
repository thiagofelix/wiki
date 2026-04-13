---
title: OpenAiTelemetry (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiTelemetry (@effect/ai-openai)

Extends the GenAI OpenTelemetry semantic conventions with OpenAI-specific request and response attributes. Exposes a mutating `addGenAIAnnotations` helper for writing `gen_ai.openai.request.*` and `gen_ai.openai.response.*` fields to a `Tracer.Span`.

## Key Exports
- `OpenAiTelemetryAttributes` — combined GenAI + OpenAI prefixed attributes type
- `AllAttributes` — flat view of all attribute fields
- `RequestAttributes` — `responseFormat`, `serviceTier`
- `ResponseAttributes` — `serviceTier`, `systemFingerprint`
- `WellKnownResponseFormat` — `"json_object" | "json_schema" | "text"`
- `WellKnownServiceTier` — `"auto" | "default"`
- `OpenAiTelemetryAttributeOptions` — input shape for the annotator
- `addGenAIAnnotations` — dual helper mutating a `Span` with the attributes

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiTelemetry.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
