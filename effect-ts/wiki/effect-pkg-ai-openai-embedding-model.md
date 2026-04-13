---
title: OpenAiEmbeddingModel (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiEmbeddingModel (@effect/ai-openai)

Implementation of `effect/unstable/ai/EmbeddingModel` backed by OpenAI's embeddings endpoint (`text-embedding-3-*`, `ada-002`). Bundles model selection with an explicit `Dimensions` service so downstream consumers can allocate vector storage without probing.

## Key Exports
- `Model` — union of known embedding model ids
- `Config` — `Context.Service` with request parameters except `input`
- `model` — creates an `AiModel<"openai", EmbeddingModel | Dimensions, OpenAiClient>` merging the config layer with `Dimensions`
- `make` — effectful constructor producing an `EmbeddingModel.Service` with `embedMany`
- `layer` — `Layer<EmbeddingModel, never, OpenAiClient>`
- `withConfigOverride` — dual helper to override the `Config` service

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiEmbeddingModel.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-client]]
- [[effect-ai]]
