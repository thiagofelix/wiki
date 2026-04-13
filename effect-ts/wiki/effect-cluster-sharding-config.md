---
title: ShardingConfig (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ShardingConfig (unstable)

Context service holding per-runner sharding configuration: listen/announce addresses, shard groups served, shards per group, weight, lock refresh intervals, advisory lock toggles, and entity reaping. Layers build it from env/config providers and defaults.

## Key Exports
- `ShardingConfig` — service interface
- `layer` — build a config from static options
- `layerFromEnv` — build a config from the environment/config provider with overrides
- `defaults` — default field values used by layers

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ShardingConfig.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sharding]]
- [[effect-cluster-runner-address]]
