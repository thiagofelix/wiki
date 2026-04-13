---
title: OpenAiClient (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiClient (@effect/ai-openai-compat)

Lean OpenAI-compatible HTTP client targeting the Chat Completions shape used by OSS/proxy providers (e.g. Ollama, vLLM, LM Studio, Groq, Together AI). Unlike `@effect/ai-openai`, this package hand-rolls request/response Schemas rather than using the full OpenAI OpenAPI, keeping it focused on the endpoints compatible providers implement.

## Key Exports
- `Service` — interface with `client`, `createResponse`, `createResponseStream`, `createEmbedding`
- `OpenAiClient` — `Context.Service` at `@effect/ai-openai-compat/OpenAiClient`
- `Options` — `apiKey`, `apiUrl`, `organizationId`, `projectId`, `transformClient`
- `make`, `layer`, `layerConfig` — constructors/layers wiring bearer + organization/project headers
- `ChatCompletionRequest`, `ChatCompletionResponse`, `ChatCompletionChunk` — request/response schemas
- `ChatCompletionStreamEvent` — union of chunk events and `"[DONE]"` sentinel
- `CreateEmbeddingRequest`, `CreateEmbeddingResponse` — embeddings schemas
- `CreateResponse`, `Response`, `ResponseStreamEvent`, `InputItem`, `ReasoningItem`, `Annotation`, `Tool`, `TextResponseFormatConfiguration` — Responses-shape adapter types for the LanguageModel

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/OpenAiClient.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-client]]
- [[effect-ai]]
