---
title: EntityResource (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EntityResource (unstable)

A scoped resource abstraction bound to an entity's lifetime so that the resource survives restarts caused by shard movement or node shutdown. The resource is released only when explicitly closed or after `idleTimeToLive` elapses. Uses a private `CloseScope` that is not tied to the handler's scope.

## Key Exports
- `EntityResource` — interface with `get` (scoped acquire) and `close`
- `make` — build an `EntityResource` from an acquire effect, with optional `idleTimeToLive`
- `CloseScope` — service representing the resource's long-lived scope
- `TypeId` — unique resource type identifier

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/EntityResource.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-entity]]
- [[effect-scope]]
