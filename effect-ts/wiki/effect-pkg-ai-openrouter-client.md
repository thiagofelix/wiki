---
title: OpenRouterClient (@effect/ai-openrouter)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenRouterClient (@effect/ai-openrouter)

Type-safe Effect-based client for OpenRouter's Chat Completions API. Supports both single-shot and streaming SSE chat generation and propagates optional `HTTP-Referer` and `X-Title` headers for OpenRouter site attribution/rankings.

## Key Exports
- `Service` — interface with `client`, `createChatCompletion`, `createChatCompletionStream`
- `OpenRouterClient` — `Context.Service` at `@effect/ai-openrouter/OpenRouterClient`
- `Options` — `apiKey`, `apiUrl`, `siteReferrer`, `siteTitle`, `transformClient`
- `ChatStreamingResponseChunkData` — type of streamed chunk payloads
- `make` — effectful constructor producing the service from an `HttpClient`
- `layer`, `layerConfig` — layer variants from static `Options` or Effect `Config`

## Source
- `raw/effect-smol/packages/ai/openrouter/src/OpenRouterClient.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
