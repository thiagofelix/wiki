---
title: EmbeddingModel (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EmbeddingModel (unstable)

Provider-agnostic interface for text embedding models. Defines a service tag plus schema classes for embedding responses and usage, and builds a `RequestResolver` so individual `embed` calls can be batched into provider `embedMany` requests automatically.

## Key Exports
- `EmbeddingModel` — `Context.Service` tag for the embedding service
- `Dimensions` — service tag carrying the current embedding dimension count
- `EmbeddingUsage` — schema class capturing `inputTokens`
- `EmbedResponse` — schema class with `vector: number[]`
- `EmbedManyResponse` — schema class with `embeddings` + `usage`
- `EmbeddingRequest` — tagged Request used by the resolver
- `ProviderOptions` / `ProviderResponse` — provider adapter shapes
- `Service` — `embed`, `embedMany`, and `resolver`
- `make` — constructs a `Service` from a provider `embedMany` implementation, batching individual `embed` calls via a resolver

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/EmbeddingModel.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-model]]
