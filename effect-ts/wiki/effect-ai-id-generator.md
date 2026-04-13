---
title: IdGenerator (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# IdGenerator (unstable)

Pluggable ID generation service used throughout the AI SDK for tool-call IDs and similar identifiers. Supports custom alphabet, prefix, separator, and size, and exposes a default service plus a `Layer` factory for overrides.

## Key Exports
- `IdGenerator` — `Context.Service` tag
- `Service` — interface with `generateId(): Effect<string>`
- `MakeOptions` — `{ alphabet, prefix?, separator, size }`
- `make` — constructs a `Service` from `MakeOptions`
- `makeDefault` — the built-in generator (URL-safe alphabet, `id_` prefix)
- `defaultIdGenerator` — default `Service` instance
- `layer` — creates a `Layer<IdGenerator>` from `MakeOptions`
- `layerDefault` — layer providing the default generator

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/IdGenerator.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
