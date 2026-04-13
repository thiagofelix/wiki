---
title: EntityAddress (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EntityAddress (unstable)

`Schema.Class` identifying the physical placement of an entity instance: the owning shard, the entity type, and the entity id. Used throughout cluster routing, error reporting, and mailbox storage keys with equality based on all three fields.

## Key Exports
- `EntityAddress` — schema class with `shardId`, `entityType`, `entityId`
- `make` — unchecked constructor from a plain options object

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/EntityAddress.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-entity]]
- [[effect-cluster-shard-id]]
