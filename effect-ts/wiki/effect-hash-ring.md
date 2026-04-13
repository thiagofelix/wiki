---
title: HashRing
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HashRing

Consistent hash ring used by the cluster subsystem to map keys to nodes with minimal churn on membership changes. Each node (identified by a `PrimaryKey`) is placed on the ring multiple times, scaled by `baseWeight` and a per-node `weight`, so heavier nodes receive proportionally more keys. Supports adding/removing nodes and resolving the owning node for a given key.

## Key Exports
- `HashRing<A>` — iterable ring of weighted nodes
- `make` — construct (options: `baseWeight`)
- `addMany`, `add` — insert/update nodes
- `remove` — remove a node
- `get` — resolve the owning node for a key
- `isHashRing` — guard
- `TypeId` — `"~effect/cluster/HashRing"`

## Source
- `raw/effect-smol/packages/effect/src/HashRing.ts`

## Related
- [[effect-ts-v4]]
- [[effect-hash]]
- [[effect-primary-key]]
