---
title: Number
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Number

Utility functions and type-class instances for the `number` primitive: arithmetic, comparison, rounding, and `Order`/`Equivalence`/`Reducer` instances. Use for dual-signature, pipeable numeric operations.

## Key Exports
- `Number` — re-export of the global `Number` constructor
- `isNumber` — type guard
- `sum` / `subtract` / `multiply` — dual-signature arithmetic
- `divide` — safe division returning `Option`
- `divideUnsafe` — throws on division by zero
- `increment` / `decrement` — add/subtract 1
- `Order` — numeric `Order` instance
- `Equivalence` — strict equivalence instance
- `sumAll` / `multiplyAll` — reduce over collections
- `min` / `max` / `clamp` / `between` — comparison helpers
- `remainder` / `round` / `sign` — numeric utilities

## Source
- `raw/effect-smol/packages/effect/src/Number.ts`

## Related
- [[effect-ts-v4]]
- [[effect-order]]
- [[effect-big-int]]
