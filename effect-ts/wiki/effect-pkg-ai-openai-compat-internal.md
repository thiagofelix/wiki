---
title: Internal (@effect/ai-openai-compat)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Internal (@effect/ai-openai-compat)

Non-exported helpers for the OpenAI-compat adapter. `errors.ts` maps HTTP and decoding failures to the unified `AiError` variants using the compat-shaped metadata, while `utilities.ts` provides small helpers consumed by the LanguageModel implementation (e.g. finish reason mapping, id allocation).

## Key Exports
- `errors.mapHttpClientError` — converts transport errors to `AiError`
- `errors.mapSchemaError` — wraps schema decode failures as invalid-output errors
- Helpers for mapping compat-provider response fields back onto the Effect AI models

## Source
- `raw/effect-smol/packages/ai/openai-compat/src/internal/errors.ts`
- `raw/effect-smol/packages/ai/openai-compat/src/internal/utilities.ts`

## Related
- [[effect-pkg-ai-openai-compat-client]]
- [[effect-pkg-ai-openai-compat-language-model]]
- [[effect-ai]]
