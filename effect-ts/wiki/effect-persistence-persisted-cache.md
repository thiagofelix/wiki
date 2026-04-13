---
title: PersistedCache (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# PersistedCache (unstable)

Two-tier cache that pairs an in-memory `Cache` with a durable `Persistence` store. On miss, looks up from persistent storage; if still missing, runs the supplied effect and persists the `Exit`. Supports separate TTLs for the in-memory and persistent layers.

## Key Exports
- `PersistedCache` — interface exposing `inMemory`, `get`, `invalidate`
- `make` — build a `PersistedCache` from a lookup effect and options (`storeId`, `timeToLive`, `inMemoryCapacity`, `inMemoryTTL`, `requireServicesAt`)
- `TypeId` — brand

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/PersistedCache.ts`

## Related
- [[effect-persistence-persistence]]
- [[effect-persistence-persistable]]
