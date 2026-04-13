---
title: ScopedCache
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ScopedCache

A capacity-bounded cache whose entries own `Scope`d resources. Each cache miss calls a `lookup` effect inside a child scope; evicted entries have their scopes closed, cleaning up associated resources. Supports optional TTL driven by the `Exit` of the lookup.

## Key Exports
- `ScopedCache<Key, A, E, R>` — interface holding capacity, lookup, ttl
- `State` — `Open` (map of entries) or `Closed`
- `Entry` — deferred value with owning scope and expiry
- `make` — construct cache with uniform TTL
- `makeWith` — TTL computed per entry from its `Exit`
- `get` — fetch or compute an entry, refreshing LRU order

## Source
- `raw/effect-smol/packages/effect/src/ScopedCache.ts`

## Related
- [[effect-ts-v4]]
- Built on [[effect-scope]], MutableHashMap, Deferred
