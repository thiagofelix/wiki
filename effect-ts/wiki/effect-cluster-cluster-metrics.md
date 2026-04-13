---
title: ClusterMetrics (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ClusterMetrics (unstable)

Predefined `Metric.gauge` instances the sharding runtime updates to report cluster state. Values are bigints representing counts of entities, singletons, runners, healthy runners, and shards.

## Key Exports
- `entities` — gauge of active entities on this runner
- `singletons` — gauge of active singletons on this runner
- `runners` — gauge of known runners in the cluster
- `runnersHealthy` — gauge of runners considered healthy
- `shards` — gauge of shards currently owned by this runner

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ClusterMetrics.ts`

## Related
- [[effect-cluster]]
- [[effect-ts-v4]]
- [[effect-metric]]
