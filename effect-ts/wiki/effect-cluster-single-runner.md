---
title: SingleRunner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SingleRunner (unstable)

Convenience layer that spins up a single-node cluster backed by SQL storage for message and runner state. Useful for durable entities and workflows without running multiple runners.

## Key Exports
- `layer` — build `Sharding`, `Runners`, and `MessageStorage` from a `SqlClient`, with optional `shardingConfig` overrides and a choice between memory or SQL runner storage

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/SingleRunner.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sharding]]
- [[effect-cluster-sql-message-storage]]
- [[effect-cluster-test-runner]]
