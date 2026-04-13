---
title: AI internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AI internal (unstable)

Internal implementation helpers used by `effect/unstable/ai` modules. Not part of the public API. Currently contains a single module providing a default codec-to-JSON-schema transformer used by `LanguageModel` when no provider-specific transformer (Anthropic, OpenAI) is supplied.

## Contents
- `codec-transformer.ts` — exports `defaultCodecTransformer: CodecTransformer`, which resolves top-level `$ref`s from `Schema.toJsonSchemaDocument` and returns `{ codec, jsonSchema }` with any `$defs` attached. This is the fallback used by `LanguageModel.generateObject` when the selected provider does not supply its own structured-output transformer.

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/internal/codec-transformer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
- [[effect-ai-anthropic-structured-output]]
- [[effect-ai-open-ai-structured-output]]
