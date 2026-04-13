---
title: OpenAiError (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiError (@effect/ai-openai-compat)

Declaration-only module augmenting `effect/unstable/ai/AiError` metadata with OpenAI-compat specific fields. Mirrors the shape used by `@effect/ai-openai` but under a separate surface for compat providers.

## Key Exports
- `OpenAiErrorMetadata` — `{ errorCode, errorType, requestId }`
- `OpenAiRateLimitMetadata` — extends base with `limit`, `remaining`, `resetRequests`, `resetTokens`
- Module augmentations adding an optional `openai` field to each `*ErrorMetadata` in `effect/unstable/ai/AiError`

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/OpenAiError.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-ai]]
