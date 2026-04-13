---
title: Internal (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Internal (@effect/ai-anthropic)

Non-exported helpers used across the Anthropic adapter. `errors.ts` maps HTTP status codes, schema decoding failures, and Anthropic error payloads to the unified `AiError` hierarchy (rate limit, authentication, content policy, quota exhausted, invalid request/output, etc.), extracting Anthropic metadata and rate-limit headers. `utilities.ts` hosts misc helpers (model capability lookup, beta header accumulation) consumed by `AnthropicLanguageModel`.

## Key Exports
- `errors.mapClientError` — converts `BetaMessagesPost4XX` variants into typed `AiError`s
- `errors.mapHttpClientError` — maps transport errors (decoding, response status) to `AiError`
- `errors.mapSchemaError` — wraps schema decode failures as invalid-output errors
- Utility helpers for model capability detection and response post-processing

## Source
- `raw/effect-smol/packages/ai/anthropic/src/internal/errors.ts`
- `raw/effect-smol/packages/ai/anthropic/src/internal/utilities.ts`

## Related
- [[effect-pkg-ai-anthropic-client]]
- [[effect-pkg-ai-anthropic-language-model]]
- [[effect-ai]]
