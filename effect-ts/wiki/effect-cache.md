---
title: Cache
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Cache

Effectful key-value cache with capacity limits, TTL management, and an automatic lookup function that populates the cache on miss. Entries are stored in a `MutableHashMap` keyed by `Equal`-based equality, and each `get` either returns a cached success/failure or invokes the `lookup` effect. Reach for it for memoization, request deduplication, or any "compute once per key" pattern inside Effect.

## Key Exports
- `Cache<Key, A, E, R>` — model with `map`, `capacity`, `lookup`, and `timeToLive`
- `Entry<A, E>` — internal cache entry holding an `Exit` and expiration
- `make` — build a cache from `{ capacity, lookup, timeToLive? }`
- `makeWith` — variant where TTL is computed per-entry from the `Exit`
- `get` — lookup or populate
- `getOption`, `getOptionUnsafe` — read without triggering lookup
- `set`, `invalidate`, `invalidateAll`, `refresh` — mutation
- `size`, `contains`, `keys`, `values`, `entries` — inspection

## Source
- `raw/effect-smol/packages/effect/src/Cache.ts`

## Related
- [[effect-ts-v4]]
- [[effect-deferred]]
- [[effect-duration]]
