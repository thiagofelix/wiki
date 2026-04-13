---
title: Generated (@effect/ai-openrouter)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Generated (@effect/ai-openrouter)

Auto-generated Schema and HTTP client for OpenRouter's OpenAPI surface. Covers the Chat Completions endpoint, streaming SSE chunks, tool declarations, reasoning details, assistant/system/user message shapes, and file annotations, plus a `make` helper that wires a typed `OpenRouterClient` to an `HttpClient`.

## Key Exports
- `ChatGenerationParams` — request schema for chat completions
- `SendChatCompletionRequest200` — success response schema
- `ChatStreamingResponseChunk` — SSE chunk envelope
- `AssistantMessage`, `SystemMessage`, `UserMessage`, `ToolMessage` — message content schemas including `reasoning_details`
- `Tool`, `ToolChoice` — tool-call schemas
- `OpenRouterClient` — typed client interface
- `make` — constructs an `OpenRouterClient` from an `HttpClient`

## Source
- `raw/effect-smol/packages/ai/openrouter/src/Generated.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openrouter-client]]
