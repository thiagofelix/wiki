---
title: ShardId (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ShardId (unstable)

Identifier for a shard: a `(group, id)` pair with interned instances, equality, hashing, and primary-key support. Shard groups let you partition the cluster into isolated pools; shard ids inside a group are numeric indexes.

## Key Exports
- `ShardId` — interface with `group` and `id`, plus `Equal`/`Hash`/`PrimaryKey`
- `make` — intern or return a cached `ShardId`
- `isShardId` — type guard
- `toString` / `fromString` / `fromStringEncoded` — string encoding helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ShardId.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sharding]]
- [[effect-cluster-entity-address]]
