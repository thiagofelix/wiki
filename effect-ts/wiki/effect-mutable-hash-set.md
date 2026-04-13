---
title: MutableHashSet
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# MutableHashSet

Mutable set built on top of `MutableHashMap`, supporting structural or referential equality for elements. Use for fast dedup and membership testing in perf-critical paths.

## Key Exports
- `MutableHashSet<V>` — interface, `Iterable<V>`, `Inspectable`
- `isMutableHashSet` — type guard
- `empty` — create an empty set
- `make` — variadic constructor
- `fromIterable` — dedup from any iterable
- `add` — insert a value (no-op if present)
- `has` — membership check
- `remove` — delete a value
- `clear` — drop all entries
- `size` — number of elements

## Source
- `raw/effect-smol/packages/effect/src/MutableHashSet.ts`

## Related
- [[effect-ts-v4]]
- [[effect-mutable-hash-map]]
