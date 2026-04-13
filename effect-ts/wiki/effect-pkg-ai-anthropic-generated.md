---
title: Generated (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Generated (@effect/ai-anthropic)

Auto-generated Schema and HTTP client for Anthropic's OpenAPI spec. Defines request/response models for the Messages API (sync and streaming), beta features, content blocks, tool-use variants, and error shapes, along with a `make` function returning a typed `AnthropicClient` bound to a provided `HttpClient`.

## Key Exports
- `Model` — literal union of Claude model IDs
- `BetaCreateMessageParams`, `BetaMessagesPostParams` — request schemas for the Messages endpoint
- `BetaMessage` — message response schema
- `BetaMessageStartEvent`, `BetaMessageDeltaEvent`, `BetaMessageStopEvent` — streaming lifecycle events
- `BetaContentBlockStartEvent`, `BetaContentBlockDeltaEvent`, `BetaContentBlockStopEvent` — content block streaming events
- `BetaErrorResponse`, `APIError`, `AuthenticationError`, `Base64ImageSource`, `Base64PDFSource`, `CacheControlEphemeral` — shared schemas
- `BetaTool`, `ResponseThinkingBlock`, `ResponseRedactedThinkingBlock` — tool and reasoning block schemas
- `AnthropicClient` — typed client interface with endpoint methods
- `make` — builds an `AnthropicClient` from an `HttpClient` and optional `transformClient`

## Source
- `raw/effect-smol/packages/ai/anthropic/src/Generated.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-anthropic-client]]
