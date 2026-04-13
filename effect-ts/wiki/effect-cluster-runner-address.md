---
title: RunnerAddress (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RunnerAddress (unstable)

`Schema.Class` pairing a host and port that other runners use to reach a given node. Implements `Equal`, `Hash`, and `PrimaryKey` so it can be used as a map/record key.

## Key Exports
- `RunnerAddress` — schema class with `host`, `port`
- `make` — unchecked constructor from host and port

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/RunnerAddress.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runner]]
- [[effect-cluster-sharding-config]]
