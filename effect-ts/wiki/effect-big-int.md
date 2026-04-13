---
title: BigInt
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BigInt

Utility functions and typeclass instances for the native `bigint` type. Provides arithmetic, comparison, and predicate helpers that follow the same dual / data-last conventions as the rest of the Effect standard library. Reach for it when you want curry-friendly, pipeable versions of bigint operations or need `Order`, `Equivalence`, `Combiner`, and `Reducer` instances for `bigint`.

## Key Exports
- `BigInt` — re-export of the global `BigInt` constructor
- `isBigInt` — runtime guard
- `sum`, `multiply`, `subtract`, `divide`, `unsafeDivide`, `increment`, `decrement`, `negate`, `remainder` — arithmetic
- `sign`, `abs`, `gcd`, `lcm`, `sqrt`, `unsafeSqrt` — number theory helpers
- `lessThan`, `greaterThan`, `lessThanOrEqualTo`, `between`, `clamp`, `min`, `max` — comparisons
- `Order`, `Equivalence` — typeclass instances
- `ReducerSum`, `ReducerMultiply` — monoidal reducers for folds

## Source
- `raw/effect-smol/packages/effect/src/BigInt.ts`

## Related
- [[effect-ts-v4]]
- [[effect-big-decimal]]
