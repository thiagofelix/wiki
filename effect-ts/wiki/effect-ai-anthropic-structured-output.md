---
title: AnthropicStructuredOutput (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicStructuredOutput (unstable)

Codec/schema transformer that rewrites an Effect `Schema.Codec` into a form compatible with Anthropic's structured-output JSON schema constraints. It walks the schema AST, converting unsupported constructs (tuples, optional properties, records, `oneOf` unions) into forms Anthropic accepts while preserving descriptions and compatible formats.

## Key Exports
- `toCodecAnthropic` — transforms a `Schema.Codec` into `{ codec, jsonSchema }` compatible with Anthropic
- Tuples → objects with numeric string keys (rest under `"__rest__"`)
- Optional properties → `T | null` unions
- Records → arrays of `[key, value]` pairs
- `oneOf` unions → `anyOf` unions
- Preserves supported annotations/formats (`date-time`, `email`, `uuid`, ...)
- Unsupported AST nodes raise `UnsupportedSchemaError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/AnthropicStructuredOutput.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-open-ai-structured-output]]
- [[effect-ai-tool]]
