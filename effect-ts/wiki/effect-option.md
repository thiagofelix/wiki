---
title: Option
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Option

Type-safe representation of optional values. `Option<A>` is either `Some<A>` (with `.value`) or `None`. Yieldable in `Effect.gen` (short-circuits with `NoSuchElementError`), and usable as a standalone data type for transformations, fallbacks, and partial functions.

## Key Exports
- `Option<A>` — `None<A> | Some<A>`
- `some` / `none` — constructors
- `isSome` / `isNone` — type guards
- `fromNullishOr` / `fromNullOr` / `fromUndefinedOr` — lift nullable values
- `fromIterable` — first element as `Some`, else `None`
- `map` / `flatMap` / `andThen` — transformations
- `getOrElse` / `getOrNull` / `getOrUndefined` / `getOrThrow` / `getOrThrowWith` — unwrapping
- `match` — pattern match on `Some`/`None`
- `orElse` / `orElseSome` / `firstSomeOf` — fallbacks
- `filter` / `filterMap` — refinement
- `all` / `zipWith` / `product` — combine multiple options
- `gen` / `Do` / `bind` — generator and do-notation
- `contains` / `exists` — predicates on inner value
- `getSuccess` / `getFailure` — convert from `Result`

## Source
- `raw/effect-smol/packages/effect/src/Option.ts`

## Related
- [[effect-ts-v4]]
- [[effect-result]]
