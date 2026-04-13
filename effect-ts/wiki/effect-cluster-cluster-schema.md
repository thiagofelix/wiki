---
title: ClusterSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ClusterSchema (unstable)

Context `Reference` annotations that tune how RPC-defined entity requests are handled by the cluster. Applied via `Rpc.annotate` to opt-in to persistence, transactions, interrupt semantics, shard group routing, tracing, and dynamic per-request overrides.

## Key Exports
- `Persisted` — mark requests as durable (stored in mailbox)
- `WithTransaction` — wrap request handler with a storage transaction
- `Uninterruptible` — mark request uninterruptible on client, server, or both
- `isUninterruptibleForServer` / `isUninterruptibleForClient` — read helpers
- `ShardGroup` — function to map entity id to a shard group
- `ClientTracingEnabled` — toggle tracing spans on client-side calls
- `Dynamic` — dynamically transform annotations per incoming request

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ClusterSchema.ts`

## Related
- [[effect-cluster]]
- [[effect-ts-v4]]
- [[effect-cluster-entity]]
- [[effect-rpc-rpc]]
