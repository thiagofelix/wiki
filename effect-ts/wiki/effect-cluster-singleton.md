---
title: Singleton (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Singleton (unstable)

Registers a named effect to run at most once across the cluster at any given time. The scheduled effect is pinned to a shard within a shard group, and `Sharding` ensures failover when the owning runner dies.

## Key Exports
- `make` — layer registering a named singleton effect with optional `shardGroup`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Singleton.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sharding]]
- [[effect-cluster-singleton-address]]
