---
title: TxHashMap
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxHashMap

Transactional hash map — wraps an immutable `HashMap<K, V>` inside a `TxRef` so all reads and mutations participate in STM transactions. Provides atomic get/set/remove/modify over key-value pairs, with retry on conflict. Multi-step updates composed under `Effect.tx` commit as a single atomic unit.

## Key Exports
- `make` — variadic constructor from key-value tuples
- `empty` / `fromIterable` — alternate constructors
- `get` — read a value by key
- `set` — insert or replace a key
- `remove` — delete a key
- `modify` / `modifyAt` — atomic update of a specific entry
- `size` / `isEmpty` / `has` — observers
- `keys` / `values` / `entries` — enumeration
- Type-level helpers: `TxHashMap.Key`, `TxHashMap.Value`, `TxHashMap.Entry`

## Source
- `raw/effect-smol/packages/effect/src/TxHashMap.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-hash-map]]
