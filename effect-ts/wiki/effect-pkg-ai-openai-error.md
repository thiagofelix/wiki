---
title: OpenAiError (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiError (@effect/ai-openai)

Declaration-only module augmenting `effect/unstable/ai/AiError` metadata interfaces with OpenAI-specific fields. Adds typed access to OpenAI error codes, request IDs, and rate-limit headers on each AI error variant.

## Key Exports
- `OpenAiErrorMetadata` — `{ errorCode, errorType, requestId }`
- `OpenAiRateLimitMetadata` — extends base with `limit`, `remaining`, `resetRequests`, `resetTokens`
- Module augmentations adding an optional `openai` field to every `*ErrorMetadata` in `effect/unstable/ai/AiError`

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiError.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
