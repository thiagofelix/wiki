---
title: Tokenizer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Tokenizer (unstable)

Service abstraction for tokenizing and truncating prompts, used to manage context-window budgets. Providers plug in a tokenization function; the service then exposes both token counting and prompt truncation derived from it.

## Key Exports
- `Tokenizer` — `Context.Service` tag
- `Service` — interface with `tokenize` and `truncate`
- `tokenize` — `(input: Prompt.RawInput) => Effect<number[], AiError>`
- `truncate` — `(input: Prompt.RawInput, maxTokens: number) => Effect<Prompt, AiError>`
- `make` — constructs a `Service` from a `tokenize` function
- `layer` — creates a `Layer<Tokenizer>` from options

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Tokenizer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-prompt]]
- [[effect-ai-language-model]]
