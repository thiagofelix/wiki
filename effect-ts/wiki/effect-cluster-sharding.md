---
title: Sharding (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Sharding (unstable)

Central sharding runtime that assigns shards to runners, routes messages to the right runner, and manages entity lifecycle on the local node. Uses a `HashRing` plus `RunnerStorage` locks to coordinate ownership, integrates with `MessageStorage` for durable mailboxes, handles singletons, interruption propagation, shard group allocation, and publishes registration events.

## Key Exports
- `Sharding` — the main service with `registerEntity`, `registerSingleton`, `send`, `notify`, `shardId`, `activeEntityCount`, etc.
- `layer` — default layer wiring sharding with runners, storage, and health
- `ShardingTag` / `Sharding` context tag
- `make` — effect building the service implementation
- Events/types re-exported: `EntityRegistered`, `SingletonRegistered`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Sharding.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runners]]
- [[effect-cluster-sharding-config]]
- [[effect-cluster-message-storage]]
