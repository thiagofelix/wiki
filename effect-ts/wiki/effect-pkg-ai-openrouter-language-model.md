---
title: OpenRouterLanguageModel (@effect/ai-openrouter)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenRouterLanguageModel (@effect/ai-openrouter)

LanguageModel implementation for OpenRouter's Chat Completions API. Converts Effect AI prompts into OpenRouter `ChatGenerationParams`, forwards tool calls and structured output using either the OpenAI or Anthropic structured-output codec depending on the underlying model family, and preserves reasoning detail metadata.

## Key Exports
- `Config` — `Context.Service` carrying request params with `strictJsonSchema` flag
- `ReasoningDetails` — extracted type for assistant `reasoning_details`
- `FileAnnotation` — extracted annotation type for file citations
- `model` — builds an `AiModel<"openrouter", LanguageModel, OpenRouterClient>`
- `make` — effectful constructor producing a `LanguageModel.Service` with `generateText` and `streamText`
- `layer` — `Layer<LanguageModel, never, OpenRouterClient>`
- `withConfigOverride` — dual helper for overlaying config overrides

## Source
- `raw/effect-smol/packages/ai/openrouter/src/OpenRouterLanguageModel.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openrouter-client]]
- [[effect-ai]]
