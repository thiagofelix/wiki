---
title: ClusterCron (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ClusterCron (unstable)

Schedules cron-driven jobs across a sharded cluster so each cron fires exactly once cluster-wide. `make` builds a Layer that creates an `Entity` plus a `Singleton` responsible for computing the next cron tick, persisting it, and dispatching execution. Supports per-cron shard groups, mode to calculate the next run from previous or wall clock, and a `skipIfOlderThan` staleness guard.

## Key Exports
- `make` — build a Layer that registers a cron job entity and driver singleton
- `CronPayload` — schema for cron message payloads carrying the scheduled `DateTime`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ClusterCron.ts`

## Related
- [[effect-cluster]]
- [[effect-ts-v4]]
- [[effect-cluster-entity]]
- [[effect-cluster-singleton]]
