---
title: SqlRunnerStorage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SqlRunnerStorage (unstable)

SQL-backed `RunnerStorage`. Manages the `cluster_runners`, `cluster_shards`, and `cluster_locks` tables plus dialect-specific advisory locks (Postgres `pg_advisory_lock`, MySQL `GET_LOCK`) to coordinate shard ownership across runners. Supports a pure-lease fallback when advisory locks are disabled.

## Key Exports
- `make` — effect building a `RunnerStorage` service from a `SqlClient`
- `layer` — layer providing `RunnerStorage` backed by SQL

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/SqlRunnerStorage.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runner-storage]]
- [[effect-sql-sql-client]]
- [[effect-cluster-sharding-config]]
