---
title: OpenAiLanguageModel (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiLanguageModel (@effect/ai-openai-compat)

LanguageModel implementation using OpenAI's Chat Completions API shape, compatible with proxy/OSS providers that implement the `/chat/completions` endpoint (Ollama, Groq, Together, LM Studio, etc.). Handles prompt conversion, tool calling, structured output, reasoning items, and streaming via `OpenAiClient.createResponseStream`.

## Key Exports
- `Config` — `Context.Service` carrying request parameters, `fileIdPrefixes`, `text.verbosity`, `strictJsonSchema`
- `model` — builds an `AiModel<"openai", LanguageModel, OpenAiClient>` from a model string
- `make` — effectful constructor producing a `LanguageModel.Service` with `generateText` and `streamText`
- `layer` — `Layer<LanguageModel, never, OpenAiClient>`
- `withConfigOverride` — dual helper overlaying config overrides on an Effect

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/OpenAiLanguageModel.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-compat-client]]
- [[effect-pkg-ai-openai-language-model]]
- [[effect-ai]]
