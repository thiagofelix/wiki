---
title: HashSet
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HashSet

Immutable persistent set of unique values backed by a `HashMap`. Membership is determined by `Equal`/`Hash`, so types implementing the `Equal` interface are compared structurally. All mutation-style operations return a new set through structural sharing. A `HashSet.HashSet.Value` type-level extractor is provided for reusing the element type.

## Key Exports
- `HashSet<V>` — immutable set interface (iterable, equal, pipeable)
- `empty`, `make`, `fromIterable` — constructors
- `has`, `size`, `isEmpty` — inspection
- `add`, `remove`, `toggle` — updates
- `union`, `intersection`, `difference` — set algebra
- `map`, `filter`, `flatMap`, `reduce`, `some`, `every` — traversal
- `beginMutation`, `endMutation`, `mutate` — batch update helpers
- `HashSet.Value` — type extractor

## Source
- `raw/effect-smol/packages/effect/src/HashSet.ts`

## Related
- [[effect-ts-v4]]
- [[effect-hash-map]]
- [[effect-hash]]
- [[effect-equal]]
