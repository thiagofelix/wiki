---
title: TxHashSet
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxHashSet

Transactional hash set of unique values, backed by `TxRef<HashSet<V>>`. Mutation operations (`add`, `remove`, `clear`) modify the set in place and return `Effect<void|boolean>`; transform operations (`union`, `intersection`, `difference`, `map`, `filter`) produce new TxHashSet instances leaving the original untouched. All operations are atomic within STM transactions.

## Key Exports
- `make` — variadic constructor
- `empty` / `fromIterable` — alternate constructors
- `add` / `remove` / `clear` — in-place mutations
- `has` / `size` / `isEmpty` — observers
- `union` / `intersection` / `difference` — set operations producing new sets
- `map` / `filter` — transformations producing new sets
- Type-level helper: `TxHashSet.Value`

## Source
- `raw/effect-smol/packages/effect/src/TxHashSet.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-hash-set]]
- [[effect-tx-hash-map]]
