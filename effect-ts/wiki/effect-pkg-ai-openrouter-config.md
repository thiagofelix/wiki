---
title: OpenRouterConfig (@effect/ai-openrouter)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenRouterConfig (@effect/ai-openrouter)

Per-Effect configuration service for the OpenRouter client. Holds an optional `transformClient` hook used to wrap middleware around the shared `HttpClient` without rebuilding the client layer.

## Key Exports
- `OpenRouterConfig` — `Context.Service` at `@effect/ai-openrouter/OpenRouterConfig`
- `OpenRouterConfig.Service` — `{ transformClient? }`
- `OpenRouterConfig.getOrUndefined` — reads the current config from context without failing
- `withClientTransform` — dual helper that provides a transformed config to the wrapped Effect

## Source
- `raw/effect-smol/packages/ai/openrouter/src/OpenRouterConfig.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openrouter-client]]
