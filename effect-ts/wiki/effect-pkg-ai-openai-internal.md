---
title: Internal (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Internal (@effect/ai-openai)

Non-exported helpers backing the OpenAI adapter. `errors.ts` maps HTTP status codes, schema decode failures, and OpenAI error payloads to the unified `AiError` variants (rate limit, authentication, content policy, quota exhausted, invalid request/output, etc.) while extracting OpenAI metadata and rate-limit headers. `utilities.ts` provides small helpers consumed by `OpenAiLanguageModel` and `OpenAiEmbeddingModel`.

## Key Exports
- `errors.mapHttpClientError` — maps transport errors to `AiError`
- `errors.mapClientError` — converts typed client 4XX/5XX errors to `AiError`
- `errors.mapSchemaError` — wraps schema decoding failures as invalid-output
- Utility helpers for normalizing finish reasons and response shaping

## Source
- `raw/effect-smol/packages/ai/openai/src/internal/errors.ts`
- `raw/effect-smol/packages/ai/openai/src/internal/utilities.ts`

## Related
- [[effect-pkg-ai-openai-client]]
- [[effect-pkg-ai-openai-language-model]]
- [[effect-ai]]
