---
title: Filter
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Filter

A filter is a function `(input) => Result<Pass, Fail>` that either transforms an input through to a pass value or rejects it with a fail value. Unlike plain predicates, filters can refine types (pass differs from input) and carry reason information on rejection. Used throughout the core library for pattern-matching style error handling (`Effect.catchFilter`, `Exit.filterSuccess`, etc.) and for building composable validation pipelines; an effectful variant allows async/effectful filtering.

## Key Exports
- `Filter<Input, Pass, Fail>` — synchronous filter interface
- `FilterEffect<Input, Pass, Fail, E, R>` — effectful variant
- `make`, `makeEffect` — constructors
- `fromPredicate`, `fromRefinement` — derive from predicates
- `isTagged`, `tagged` — tag-based filters
- `compose`, `or`, `and` — combinators
- `fail` — sentinel for rejection

## Source
- `raw/effect-smol/packages/effect/src/Filter.ts`

## Related
- [[effect-ts-v4]]
- [[effect-predicate]]
- [[effect-result]]
