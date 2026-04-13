---
title: Entity (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Entity (unstable)

Core abstraction for sharded stateful actors. An `Entity` wraps an `RpcGroup` protocol with a type name, shard group routing, client construction, and annotation APIs. Handlers are implemented against the entity's RPCs and get materialized per-entity-id by `Sharding`, providing durable mailbox semantics when `Persisted` is set.

## Key Exports
- `Entity` — interface exposing protocol, client, annotate helpers, `getShardId`
- `make` — create an entity from a type name and list of RPCs
- `client` — effect yielding an RPC client factory keyed by entity id
- `annotate` / `annotateRpcs` — attach cluster schema annotations
- `CurrentAddress` — context reference for the active entity address
- `CurrentRunnerAddress` — reference to the local runner address
- `keepAlive` — opt-in to keeping entity instance alive across activity
- `HandlersFrom` — type helper for implementing entity handlers

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Entity.ts`

## Related
- [[effect-cluster]]
- [[effect-rpc-rpc-group]]
- [[effect-cluster-sharding]]
- [[effect-cluster-cluster-schema]]
