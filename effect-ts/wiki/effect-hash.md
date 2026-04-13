---
title: Hash
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Hash

Hashing utilities that power hash-based collections and structural equality. `Hash.hash` produces a numeric hash for any value, dispatching on type and invoking custom `[Hash.symbol]()` methods on objects that implement the `Hash` interface. Results are cached in a WeakMap, so hashed objects must be treated as immutable afterwards. Primitives have dedicated combinators for composing hashes when implementing custom types.

## Key Exports
- `Hash` — interface requiring `[Hash.symbol](): number`
- `symbol` — property key for the hash method
- `hash` — polymorphic entrypoint
- `string`, `number`, `bigint` — primitive hashers
- `array`, `structure` — composite hashers
- `combine` — merge two hashes
- `random` — identity-based hash via WeakMap
- `isHash` — type guard
- `cached` — memoize a computed hash on an object

## Source
- `raw/effect-smol/packages/effect/src/Hash.ts`

## Related
- [[effect-ts-v4]]
- [[effect-equal]]
- [[effect-hash-map]]
