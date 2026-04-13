---
title: Boolean
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Boolean

Utility functions and typeclass instances for the native `boolean` type. Provides logical combinators, pattern matching, and predicates in the dual data-first / data-last style. Small but convenient when composing predicates or folding boolean results.

## Key Exports
- `Boolean` — re-export of the global `Boolean` constructor
- `isBoolean` — runtime guard
- `match` — pattern match on `{ onTrue, onFalse }` thunks
- `and`, `or`, `xor`, `nand`, `nor`, `implies`, `eqv`, `not` — logical combinators
- `Order` — `Order<boolean>` where `false < true`
- `Equivalence` — equality instance
- `ReducerEvery`, `ReducerSome` — monoidal reducers (AND / OR folds)

## Source
- `raw/effect-smol/packages/effect/src/Boolean.ts`

## Related
- [[effect-ts-v4]]
- [[effect-predicate]]
