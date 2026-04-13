---
title: OpenAiStructuredOutput (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiStructuredOutput (unstable)

Codec/schema transformer that rewrites an Effect `Schema.Codec` into a form compatible with OpenAI's structured-output constraints. Similar to the Anthropic transformer, but also flattens `allOf` in the post-processed JSON schema and merges regex filters into a single `pattern` via lookaheads.

## Key Exports
- `toCodecOpenAI` — transforms a codec into `{ codec, jsonSchema }` for OpenAI
- Tuples → objects with numeric string keys (rest under `"__rest__"`)
- Optional properties → `T | null` unions
- Records → arrays of `[key, value]` pairs
- `oneOf` unions → `anyOf` unions
- Multiple regex filters merged into single `pattern` via lookaheads
- `allOf` nodes are flattened into the parent object
- Unsupported AST nodes raise `UnsupportedSchemaError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/OpenAiStructuredOutput.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-anthropic-structured-output]]
- [[effect-ai-tool]]
