---
title: Array
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Array

Utilities for working with immutable arrays (and non-empty arrays) in a functional style. All functions return new arrays rather than mutating input, and most are dual — callable data-first (`Array.map(arr, fn)`) or data-last for piping (`pipe(arr, Array.map(fn))`). Reach for it whenever you need safe, typed collection operations beyond the built-in `Array` prototype, including non-empty guarantees, set operations, and `Option`-returning element accessors.

## Key Exports
- `NonEmptyReadonlyArray` / `NonEmptyArray` — type-level non-empty array guarantees
- `make`, `of`, `empty`, `fromIterable`, `range`, `makeBy`, `replicate`, `unfold` — constructors
- `head`, `last`, `get`, `tail`, `init` — safe element access returning `Option`
- `map`, `flatMap`, `flatten`, `filter`, `partition`, `dedupe` — transformation and filtering
- `append`, `prepend`, `appendAll`, `zip`, `cartesian` — combination
- `splitAt`, `chunksOf`, `span`, `window`, `groupBy`, `group` — splitting and grouping
- `sort`, `sortBy`, `sortWith` — ordering via `Order`
- `reduce`, `scan`, `join` — folds
- `union`, `intersection`, `difference` — set operations using `Equal.equivalence`
- `match`, `matchLeft`, `matchRight` — pattern matching on empty vs non-empty
- `isArray`, `isArrayNonEmpty`, `every`, `some` — predicates

## Source
- `raw/effect-smol/packages/effect/src/Array.ts`

## Related
- [[effect-ts-v4]]
- [[effect-chunk]]
