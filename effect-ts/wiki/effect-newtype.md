---
title: Newtype
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Newtype

Compile-time branded wrappers around a carrier type (e.g. `UserId` vs `OrderId`, both `string`). Zero runtime overhead — the tag exists only in the type system. Use to prevent accidental mixing of structurally identical values and to lift instances (`Equivalence`, `Order`, `Combiner`, `Reducer`) from carrier to newtype.

## Key Exports
- `Newtype<Key, Carrier>` — tagged interface to extend
- `Newtype.Any` / `Newtype.Key` / `Newtype.Carrier` — type-level helpers
- `value` — unwrap a newtype (identity cast)
- `makeIso` — build an `Optic.Iso` for wrap/unwrap
- `makeEquivalence` — lift an `Equivalence` from carrier to newtype
- `makeOrder` — lift an `Order`
- `makeCombiner` — lift a `Combiner`
- `makeReducer` — lift a `Reducer`

## Source
- `raw/effect-smol/packages/effect/src/Newtype.ts`

## Related
- [[effect-ts-v4]]
- [[effect-optic]]
- [[effect-order]]
