---
title: OpenAiLanguageModel (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiLanguageModel (@effect/ai-openai)

Implementation of `effect/unstable/ai/LanguageModel` backed by OpenAI's Responses API. Converts Effect AI prompts, tool definitions, and structured-output schemas into Responses payloads, handles file ID prefixes, reasoning items, and text verbosity, and streams responses through `OpenAiClient.createResponseStream`.

## Key Exports
- `Model` — union of Responses and shared model IDs from `Generated`
- `Config` — `Context.Service` with request overrides, `fileIdPrefixes`, `text.verbosity`, `strictJsonSchema`, etc.
- `model` — builds an `AiModel<"openai", LanguageModel, OpenAiClient>` from id + config
- `make` — effectful constructor producing a `LanguageModel.Service` with `generateText` and `streamText`
- `layer` — `Layer<LanguageModel, never, OpenAiClient>`
- `withConfigOverride` — dual helper overlaying config overrides on an Effect

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiLanguageModel.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-client]]
- [[effect-pkg-ai-openai-tool]]
- [[effect-ai]]
