---
title: Internal (@effect/ai-openrouter)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Internal (@effect/ai-openrouter)

Non-exported helpers used by the OpenRouter adapter. `errors.ts` maps HTTP status codes and decoding failures to `AiError` variants, attaching OpenRouter metadata. `utilities.ts` contains helpers such as `ReasoningDetailsDuplicateTracker` (deduplicating reasoning blocks across streamed chunks) and `resolveFinishReason` (normalizing finish reasons to the unified AI vocabulary).

## Key Exports
- `errors.mapHttpClientError`, `errors.mapClientError`, `errors.mapSchemaError` — transport/schema error mappers
- `ReasoningDetailsDuplicateTracker` — tracks streamed reasoning blocks to avoid duplicate emission
- `resolveFinishReason` — maps OpenRouter finish reasons to Effect AI `Response.FinishReason`

## Source
- `raw/effect-smol/packages/ai/openrouter/src/internal/errors.ts`
- `raw/effect-smol/packages/ai/openrouter/src/internal/utilities.ts`

## Related
- [[effect-pkg-ai-openrouter-client]]
- [[effect-pkg-ai-openrouter-language-model]]
- [[effect-ai]]
