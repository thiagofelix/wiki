---
title: MutableHashMap
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# MutableHashMap

High-performance mutable hash map supporting both referential and structural (via `Equal`/`Hash`) keys. Referential keys go to a native `Map`; structural keys use bucketed collision handling. Reach for this in perf-sensitive code where immutable `HashMap` would be too costly.

## Key Exports
- `MutableHashMap<K, V>` — interface, `Iterable<[K, V]>`, `Inspectable`
- `isMutableHashMap` — type guard
- `empty` — create an empty map
- `make` — variadic constructor from `[K, V]` tuples
- `fromIterable` — build from any iterable of entries
- `get` / `has` — lookup operations (returns `Option` for `get`)
- `set` — insert or update a key
- `remove` — delete a key
- `clear` — drop all entries
- `size` — number of entries
- `modify` / `modifyAt` — in-place updates

## Source
- `raw/effect-smol/packages/effect/src/MutableHashMap.ts`

## Related
- [[effect-ts-v4]]
- [[effect-mutable-hash-set]]
