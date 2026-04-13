---
title: Trie
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Trie

Immutable prefix tree keyed by strings. Behaves like a HashMap with string keys but unlocks prefix-based queries: listing all keys under a prefix, computing longest-prefix matches, and efficient completion lookups. Lookups are O(n) in key length.

## Key Exports
- `Trie<Value>` — iterable equal-aware structure
- `empty` — construct an empty trie
- `fromIterable` — build from key/value pairs
- `make` — variadic entry constructor
- `insert` — add a key/value
- `get` / `has` / `size` — queries
- `keys` / `values` / entries iterators (alphabetical order)
- `keysWithPrefix` / `longestPrefixOf` — prefix queries

## Source
- `raw/effect-smol/packages/effect/src/Trie.ts`

## Related
- [[effect-ts-v4]]
- String-keyed counterpart to HashMap
