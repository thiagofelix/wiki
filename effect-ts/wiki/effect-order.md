---
title: Order
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Order

Type class for total orderings. An `Order<A>` is a `(self, that) => -1 | 0 | 1` comparison function satisfying totality, antisymmetry, and transitivity. Compose orders for multi-criteria sorts and transform with `mapInput`.

## Key Exports
- `Order<A>` — the comparison function interface
- `make` — build an order from a compare function (with `===` shortcut)
- `String` / `Number` / `Boolean` / `BigInt` / `Date` — built-in instances
- `reverse` — flip ascending to descending
- `combine` / `combineAll` / `combineMany` — compose multiple orders
- `mapInput` — derive an order on `B` from an order on `A` via a selector
- `Array` / `Tuple` / `Struct` — structural orderings
- `isLessThan` / `isGreaterThan` / `isLessThanOrEqualTo` / `isGreaterThanOrEqualTo` — comparators
- `min` / `max` / `clamp` / `between` — value helpers
- `Reducer` — reducer over orders

## Source
- `raw/effect-smol/packages/effect/src/Order.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ordering]]
- [[effect-equivalence]]
