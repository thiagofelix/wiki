---
title: RunnerStorage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RunnerStorage (unstable)

Persistent cluster membership and shard ownership store. Runners register themselves (getting a machine id), mark their health, and cooperatively acquire/refresh shard locks. This is how the cluster achieves at-most-one-owner semantics for each shard.

## Key Exports
- `RunnerStorage` — service with `register`, `unregister`, `getRunners`, `setRunnerHealth`, `acquire`, `refresh`, and shard queries
- `layerMemory` — in-memory implementation for tests

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/RunnerStorage.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sql-runner-storage]]
- [[effect-cluster-runner]]
- [[effect-cluster-sharding-config]]
