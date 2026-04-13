---
title: Model (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Model (unstable)

Represents a provider+model pairing as a `Layer`/`Effect` hybrid. A `Model` constructs an AI service `Layer` and automatically provides `ProviderName` and `ModelName` context tags alongside it, enabling interchangeable, identifiable provider implementations.

## Key Exports
- `Model<Provider, Provides, Requires>` — interface combining `Layer` and `Effect.Yieldable`
- `ProviderName` — `Context.Service<ProviderName, string>` tag
- `ModelName` — `Context.Service<ModelName, string>` tag
- `make` — `(provider, modelName, layer) => Model<...>` constructor

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Model.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
- [[effect-ai-embedding-model]]
