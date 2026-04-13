---
title: SingletonAddress (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SingletonAddress (unstable)

`Schema.Class` identifying a singleton by its name and owning shard. Used in registration events and runner-side tracking.

## Key Exports
- `SingletonAddress` — schema class with `shardId` and `name`, implementing `Equal` / `Hash`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/SingletonAddress.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-singleton]]
- [[effect-cluster-shard-id]]
