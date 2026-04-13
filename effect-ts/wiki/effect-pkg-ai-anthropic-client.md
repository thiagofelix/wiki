---
title: AnthropicClient (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicClient (@effect/ai-anthropic)

Type-safe Effect-based HTTP client wrapping Anthropic's Messages API. Provides both synchronous message creation and streaming via Server-Sent Events, delegating to the codegen'd `Generated.AnthropicClient` for low-level request plumbing and mapping all errors to the unified `AiError`.

## Key Exports
- `Service` — interface exposing `client`, `streamRequest`, `createMessage`, `createMessageStream`
- `AnthropicClient` — `Context.Service` tag keyed at `@effect/ai-anthropic/AnthropicClient`
- `MessageStreamEvent` — union of SSE event types (message_start/delta/stop, content_block_start/delta/stop, error)
- `Options` — `apiKey` (Redacted), `apiUrl`, `apiVersion` (defaults `2023-06-01`), `transformClient`
- `make` — effectful constructor requiring `HttpClient.HttpClient`; handles `x-api-key` + `anthropic-version` headers and registers redacted header names
- `layer` — `Layer` from `Options` to `AnthropicClient` service
- `layerConfig` — `Layer` variant using Effect `Config` values for each option

## Source
- `raw/effect-smol/packages/ai/anthropic/src/AnthropicClient.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-ai]]
- [[effect-ai]]
