---
title: Ordering
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Ordering

The result type of a comparison: `-1 | 0 | 1`. Provides composable operations for combining multiple comparison results and pattern-matching on outcomes. Foundation for the `Order` type class.

## Key Exports
- `Ordering` — `-1 | 0 | 1`
- `reverse` — flip `-1` and `1`, leave `0`
- `match` — pattern match with `onLessThan`/`onEqual`/`onGreaterThan`
- `combine` — take the first non-zero ordering
- `combineMany` / `combineAll` — fold multiple orderings
- `Reducer` — `Reducer<Ordering>` that short-circuits on the first non-zero

## Source
- `raw/effect-smol/packages/effect/src/Ordering.ts`

## Related
- [[effect-ts-v4]]
- [[effect-order]]
