---
title: Struct
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Struct

Immutable utilities for plain TypeScript objects with fixed keys. Every function returns a new object. Supports picking, omitting, merging, renaming, evolving selected values/keys, and building Equivalence/Order/Combiner/Reducer instances. Uses a type-level `Lambda` for `map`-style operations that track value-type changes.

## Key Exports
- `Simplify<T>` / `Mutable<T>` / `Assign<T, U>` — type-level helpers
- `get` — access a property in a pipeline
- `keys` — typed `Array<keyof S & string>`
- `pick` / `omit` — subset selection
- `assign` — merge with right-wins semantics
- `renameKeys` — key renaming
- `evolve` / `evolveKeys` / `evolveEntries` — selective transforms
- `map` / `mapPick` / `mapOmit` — Lambda-based value mapping
- `makeEquivalence` / `makeOrder` / `makeCombiner` / `makeReducer` — instance constructors

## Source
- `raw/effect-smol/packages/effect/src/Struct.ts`

## Related
- [[effect-ts-v4]]
- Companion to Record; paired with [[effect-tuple]] for positional variants
