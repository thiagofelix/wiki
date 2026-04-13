---
title: HashMap
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HashMap

Immutable persistent key-value map backed by a Hash Array Mapped Trie (HAMT) for efficient lookup, insertion, and deletion with structural sharing. Keys are compared using `Equal`/`Hash`, so types with custom equality behave correctly as keys. The `HashMap.HashMap` namespace provides type-level utilities to extract key/value/entry types from a concrete map.

## Key Exports
- `HashMap<K, V>` — immutable map interface (iterable, equal, pipeable)
- `empty`, `make`, `fromIterable` — constructors
- `get`, `has`, `unsafeGet` — access
- `set`, `remove`, `modify`, `modifyAt` — updates (return new map)
- `keys`, `values`, `entries`, `size`, `isEmpty` — inspection
- `map`, `filter`, `flatMap`, `reduce` — traversal
- `union`, `intersection`, `difference` — set algebra
- `beginMutation`, `endMutation`, `mutate` — batch update helpers
- `HashMap.Key`, `HashMap.Value`, `HashMap.Entry` — type extractors

## Source
- `raw/effect-smol/packages/effect/src/HashMap.ts`

## Related
- [[effect-ts-v4]]
- [[effect-hash-set]]
- [[effect-hash]]
- [[effect-equal]]
