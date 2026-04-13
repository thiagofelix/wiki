---
title: OpenAiConfig (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiConfig (@effect/ai-openai-compat)

Per-Effect configuration service for the OpenAI-compat client, holding an optional `transformClient` hook that wraps middleware around the shared `HttpClient`.

## Key Exports
- `OpenAiConfig` — `Context.Service` at `@effect/ai-openai-compat/OpenAiConfig`
- `OpenAiConfig.Service` — `{ transformClient? }`
- `OpenAiConfig.getOrUndefined` — reads the current config from context without failing
- `withClientTransform` — dual helper providing a transformed config to the wrapped Effect

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/OpenAiConfig.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-compat-client]]
