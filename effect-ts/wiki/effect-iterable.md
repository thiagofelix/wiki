---
title: Iterable
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Iterable

Lazy, potentially infinite sequence operations over any `Iterable<A>`. Mirrors much of the `Array` API but preserves laziness so iterables can be composed without materializing arrays. Reach for this when sources are streamable or unbounded.

## Key Exports
- `makeBy` — build an iterable from an index function, optional length
- `range` — inclusive integer range, open-ended if `end` omitted
- `replicate` — repeat a value N times
- `repeat` / `forever` — repeat an iterable N or infinitely many times
- `fromRecord` — iterate record entries as `[key, value]`
- `prepend` / `append` — add elements at either end
- `map` / `filter` / `flatMap` / `flatten` — classic transformations
- `take` / `drop` / `zip` / `unfold` — slicing and building
- `reduce` / `forEach` — folding and effects

## Source
- `raw/effect-smol/packages/effect/src/Iterable.ts`

## Related
- [[effect-ts-v4]]
- [[effect-non-empty-iterable]]
