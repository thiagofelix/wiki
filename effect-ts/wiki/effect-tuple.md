---
title: Tuple
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Tuple

Utilities for fixed-length readonly arrays where each position may have a distinct type. All operations are immutable and dual. Includes index-based pick/omit, evolve, append, rename, and typed comparisons. Uses `Struct`'s `Lambda` for type-tracking `map` variants.

## Key Exports
- `make` — build a tuple preserving literal types
- `get` — index-constrained accessor
- `pick` / `omit` — select or drop by indices
- `appendElement` / `appendElements` — extend a tuple
- `evolve` — transform specific positions
- `renameIndices` — reorder elements
- `map` / `mapPick` / `mapOmit` — Lambda-based element mapping
- `isTupleOf` / `isTupleOfAtLeast` — runtime length guards
- `makeEquivalence` / `makeOrder` / `makeCombiner` / `makeReducer` — instances

## Source
- `raw/effect-smol/packages/effect/src/Tuple.ts`

## Related
- [[effect-ts-v4]]
- Positional sibling of [[effect-struct]]; uses [[effect-types]] helpers
