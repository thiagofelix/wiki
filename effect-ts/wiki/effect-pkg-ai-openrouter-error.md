---
title: OpenRouterError (@effect/ai-openrouter)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenRouterError (@effect/ai-openrouter)

Declaration-only module augmenting `effect/unstable/ai/AiError` metadata interfaces with OpenRouter-specific fields. Adds typed access to OpenRouter error codes, request IDs, and rate-limit headers across every AI error variant.

## Key Exports
- `OpenRouterErrorMetadata` — `{ errorCode, errorType, requestId }`
- `OpenRouterRateLimitMetadata` — extends base with `limit`, `remaining`, `resetRequests`, `resetTokens`
- Module augmentations adding an optional `openrouter` field to every `*ErrorMetadata` in `effect/unstable/ai/AiError`

## Source
- `raw/effect-smol/packages/ai/openrouter/src/OpenRouterError.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
