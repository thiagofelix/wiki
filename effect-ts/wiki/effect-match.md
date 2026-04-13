---
title: Match
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Match

Type-safe pattern matching for TypeScript. Build a matcher with `Match.type<T>()` or `Match.value(v)`, add cases via `when`/`not`/`tag`, and finalize with `exhaustive`/`orElse`/`option`. Compile-time exhaustiveness checking eliminates missed cases on discriminated unions.

## Key Exports
- `Matcher` / `TypeMatcher` / `ValueMatcher` — matcher shapes
- `type` — begin a type-level matcher
- `value` — begin a matcher for a concrete value
- `when` / `whenOr` / `whenAnd` — positive pattern cases
- `not` — negative pattern case
- `tag` / `tagStartsWith` / `tagsExhaustive` — discriminated union helpers
- `discriminator` / `discriminators` — custom discriminator key
- `exhaustive` — finalize; compile error if any case is missing
- `orElse` / `orElseAbsurd` — catch-all fallback
- `option` / `either` — finalize to an `Option`/`Either`
- Primitive guards: `string`, `number`, `boolean`, `bigint`, `date`, `null`, `undefined`, `any`, `defined`, `record`, `instanceOf`

## Source
- `raw/effect-smol/packages/effect/src/Match.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-option]]
