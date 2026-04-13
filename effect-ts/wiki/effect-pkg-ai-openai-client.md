---
title: OpenAiClient (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiClient (@effect/ai-openai)

Type-safe Effect-based wrapper over OpenAI's Responses, Embeddings, and Realtime APIs. Supports HTTP and WebSocket streaming, organization/project headers, and delegates request plumbing to `Generated.OpenAiClient`. All failures are converted to `AiError`.

## Key Exports
- `Service` — interface with `client`, `createResponse`, `createResponseStream`, `createEmbedding`
- `OpenAiClient` — `Context.Service` at `@effect/ai-openai/OpenAiClient`
- `Options` — `apiKey`, `apiUrl`, `organizationId`, `projectId`, `transformClient`, etc.
- `make` — constructs the HTTP-backed service, setting bearer token and OpenAI headers
- `layer`, `layerConfig` — layers from static `Options` or Effect `Config`
- `ResponseStreamEvent` — type of streamed response events
- `OpenAiSocket` — `Context.Service` for WebSocket-based streaming responses
- `withWebSocketMode` — opts an Effect into WebSocket-mode responses
- `layerWebSocketMode` — layer providing the `OpenAiSocket` service

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiClient.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
