---
title: AnthropicError (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicError (@effect/ai-anthropic)

Declaration-only module that augments `effect/unstable/ai/AiError` metadata interfaces with Anthropic-specific fields. Enables typed access to Anthropic error codes, request IDs, and rate-limit headers through the unified AI error types without runtime cost.

## Key Exports
- `AnthropicErrorMetadata` — `{ errorType, requestId }` common metadata
- `AnthropicRateLimitMetadata` — extends base with `requestsLimit/Remaining/Reset` and `tokensLimit/Remaining/Reset`
- Module augmentations adding optional `anthropic` field to `RateLimitErrorMetadata`, `QuotaExhaustedErrorMetadata`, `AuthenticationErrorMetadata`, `ContentPolicyErrorMetadata`, `InvalidRequestErrorMetadata`, `InternalProviderErrorMetadata`, `InvalidOutputErrorMetadata`, `StructuredOutputErrorMetadata`, `UnsupportedSchemaErrorMetadata`, `UnknownErrorMetadata`

## Source
- `raw/effect-smol/packages/ai/anthropic/src/AnthropicError.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
