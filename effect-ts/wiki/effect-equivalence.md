---
title: Equivalence
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Equivalence

Utilities for defining equivalence relations — binary `(a: A, b: A) => boolean` functions that are reflexive, symmetric, and transitive. Used for deduplication, comparison, and collection operations. Composable via `combine`/`combineAll` (AND semantics) and `mapInput` for contravariant transformation. Includes structured-type helpers for tuples, records, arrays, and structs.

## Key Exports
- `Equivalence<A>` — the relation type
- `make` — custom equivalence with `===` fast path
- `strictEqual` — `===`-based instance
- `combine`, `combineAll` — compose multiple equivalences
- `mapInput` — contravariant transform
- `Struct`, `Tuple`, `Array`, `Record` — derived equivalences for structured types
- `EquivalenceTypeLambda` — HKT encoding

## Source
- `raw/effect-smol/packages/effect/src/Equivalence.ts`

## Related
- [[effect-ts-v4]]
- [[effect-equal]]
- [[effect-order]]
