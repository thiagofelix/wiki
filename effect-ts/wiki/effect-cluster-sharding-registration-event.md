---
title: ShardingRegistrationEvent (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ShardingRegistrationEvent (unstable)

Tagged enum of events emitted whenever a runner registers an entity or singleton. Consumers subscribe via `Sharding` pubsub to react to topology changes in-process.

## Key Exports
- `ShardingRegistrationEvent` — union of `EntityRegistered` / `SingletonRegistered`
- `EntityRegistered` — event carrying the registered `Entity`
- `SingletonRegistered` — event carrying the registered `SingletonAddress`
- `match` — pattern match helper via `Data.taggedEnum`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ShardingRegistrationEvent.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sharding]]
- [[effect-cluster-singleton]]
