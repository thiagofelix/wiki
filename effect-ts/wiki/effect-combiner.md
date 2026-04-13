---
title: Combiner
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Combiner

Abstraction over "how to merge two values of the same type". A `Combiner<A>` is a single `combine(self, that): A` function, representing a semigroup-style operation with no identity element. Use `Combiner` when describing reusable merging strategies; use `Reducer` (which extends `Combiner`) when you also need a neutral initial value. Combiners are pure and composable, and can be lifted into `Option`, `Struct`, and `Tuple` via helpers in those modules.

## Key Exports
- `Combiner<A>` — interface with `combine(self, that): A`
- `make` — build a combiner from a binary function
- `flip` — swap argument order
- `min`, `max` — select via an `Order<A>`
- `first`, `last` — keep the left or right operand
- `constant` — always return a fixed result
- `intercalate` — insert a separator between combined values (curried)

## Source
- `raw/effect-smol/packages/effect/src/Combiner.ts`

## Related
- [[effect-ts-v4]]
