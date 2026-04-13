---
title: AnthropicTelemetry (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicTelemetry (@effect/ai-anthropic)

Extends the base GenAI OpenTelemetry semantic conventions with Anthropic-specific request and response attributes. Provides a mutating `addGenAIAnnotations` helper that writes `gen_ai.anthropic.request.*` and `gen_ai.anthropic.response.*` fields onto a `Span`.

## Key Exports
- `AnthropicTelemetryAttributes` — combined GenAI + Anthropic-prefixed attribute type
- `AllAttributes` — flat union of all attributes for consumer APIs
- `RequestAttributes` — `extendedThinking`, `thinkingBudgetTokens`
- `ResponseAttributes` — `stopReason`, `cacheCreationInputTokens`, `cacheReadInputTokens`
- `AnthropicTelemetryAttributeOptions` — input shape accepted by the annotator
- `addGenAIAnnotations` — dual `(span, options) | (options)(span)` that mutates a `Tracer.Span`

## Source
- `raw/effect-smol/packages/ai/anthropic/src/AnthropicTelemetry.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
