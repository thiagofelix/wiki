---
title: Record
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Record

Utility functions for working with immutable `ReadonlyRecord<K, V>` objects: creation, traversal, mapping, filtering, merging, and conversion to/from arrays. Provides type-level helpers for key manipulation (literal vs non-literal strings, intersection of key sets) and HKT support via `ReadonlyRecordTypeLambda`.

## Key Exports
- `ReadonlyRecord<K, V>` — readonly object map type
- `ReadonlyRecordTypeLambda` — HKT representation
- `empty()`, `fromIterable`, `fromEntries` — constructors
- `isEmptyRecord`, `isEmptyReadonlyRecord` — guards
- `get`, `set`, `remove`, `has`, `modify` — entry ops
- `map`, `filter`, `filterMap`, `partition`, `reduce` — traversals
- `keys`, `values`, `toEntries` — extraction
- `union`, `intersection`, `difference` — merge operations
- `singleton`, `size`, `isSubrecord`

## Source
- `raw/effect-smol/packages/effect/src/Record.ts`

## Related
- [[effect-ts-v4]]
- [[effect-hash-map]]
- [[effect-struct]]
