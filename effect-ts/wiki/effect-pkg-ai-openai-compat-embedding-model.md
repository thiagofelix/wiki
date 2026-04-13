---
title: OpenAiEmbeddingModel (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiEmbeddingModel (@effect/ai-openai-compat)

EmbeddingModel implementation for OpenAI-compatible embeddings endpoints. Accepts any model string (since compat providers expose their own model ids) and pairs the embedding service with an explicit `Dimensions` service for vector-storage sizing.

## Key Exports
- `Model` — `string` (compat providers expose arbitrary model ids)
- `Config` — `Context.Service` holding request parameters except `input`
- `model` — builds an `AiModel<"openai", EmbeddingModel | Dimensions, OpenAiClient>` with explicit `dimensions`
- `make` — effectful constructor returning an `EmbeddingModel.Service` with `embedMany`
- `layer` — `Layer<EmbeddingModel, never, OpenAiClient>`
- `withConfigOverride` — dual helper to override `Config`

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/OpenAiEmbeddingModel.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-compat-client]]
- [[effect-ai]]
