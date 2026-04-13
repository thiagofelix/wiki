---
title: Persistence (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# Persistence (unstable)

Service abstraction for storing `Exit<A, E>` values keyed by `Persistable` requests. Splits into `Persistence` (high-level, schema-aware) and `BackingPersistence` (low-level, object-valued) so backends can be swapped independently. Used by `PersistedCache` and request-level memoization.

## Key Exports
- `Persistence` — Context service with `make({ storeId, timeToLive })` returning a `PersistenceStore`
- `PersistenceStore` — `get`, `getMany`, `set`, `setMany`, `remove`, `clear` over `Persistable` keys
- `BackingPersistence` — low-level service producing `BackingPersistenceStore`
- `BackingPersistenceStore` — raw get/set/remove for encoded objects with TTL
- `layer` — adapts a `BackingPersistence` into a `Persistence`
- `layerMemory` — in-memory backing store
- `layerKeyValueStore` — backing store built on `KeyValueStore`
- `layerSql` / `layerRedis` — SQL and Redis backing layers
- `PersistenceError` — schema-backed tagged error

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/Persistence.ts`

## Related
- [[effect-persistence-persistable]]
- [[effect-persistence-persisted-cache]]
