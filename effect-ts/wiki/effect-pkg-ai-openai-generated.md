---
title: Generated (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Generated (@effect/ai-openai)

Auto-generated Schema and HTTP client for OpenAI's full OpenAPI surface (Responses, Chat Completions, Embeddings, Assistants, Files, Images, Audio, Vector Stores, Batches, Fine-tuning, etc.). Provides typed request and response schemas along with a `make` function that builds a typed `OpenAiClient` bound to a shared `HttpClient`.

## Key Exports
- `CreateResponse`, `Response` — Responses API request/response schemas
- `ResponseStreamEvent` — union of Responses streaming events
- `CreateEmbeddingRequest`, `CreateEmbeddingResponse` — embeddings API schemas
- `ModelIdsResponses`, `ModelIdsShared` — enumerations of model identifiers
- `CodeInterpreterTool`, `FileSearchTool`, `ImageGenTool`, `WebSearchTool`, `WebSearchPreviewTool`, `MCPTool`, `LocalShellToolCall`, `ApplyPatchToolCall`, `FunctionShellCall` — provider tool schemas
- `OpenAiClient` — typed client interface exposing REST endpoints
- `make` — constructs an `OpenAiClient` from an `HttpClient` with optional transformer

## Source
- `raw/effect-smol/packages/ai/openai/src/Generated.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-client]]
