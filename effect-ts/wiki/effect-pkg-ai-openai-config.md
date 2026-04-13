---
title: OpenAiConfig (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiConfig (@effect/ai-openai)

Per-Effect configuration service for the OpenAI client, carrying an optional `transformClient` hook used to add middleware around the shared `HttpClient` without rebuilding the underlying layer.

## Key Exports
- `OpenAiConfig` — `Context.Service` at `@effect/ai-openai/OpenAiConfig`
- `OpenAiConfig.Service` — `{ transformClient? }` shape
- `OpenAiConfig.getOrUndefined` — reads the current config without failing when absent
- `withClientTransform` — dual helper that provides a transformed config to the wrapped Effect

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiConfig.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-client]]
