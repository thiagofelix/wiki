---
title: EntityId (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EntityId (unstable)

Branded string schema representing the logical id of an entity instance within its type. Used as a key into sharding/routing decisions and mailbox storage.

## Key Exports
- `EntityId` — branded string schema (`~effect/cluster/EntityId`)
- `make` — brand an arbitrary string as an `EntityId`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/EntityId.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-entity]]
- [[effect-cluster-entity-address]]
