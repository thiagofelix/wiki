---
title: Runner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Runner (unstable)

`Schema.Class` describing a physical runner (application server) in the cluster. Holds an address, the list of shard groups it can serve, and a weight used during shard rebalancing. Equality/hash are driven by address and weight; also supports JSON encode/decode.

## Key Exports
- `Runner` — schema class with `address`, `groups`, `weight`
- `make` — construct a runner from plain options
- `decodeSync` / `encodeSync` — JSON codec helpers
- `format` — pretty formatter

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Runner.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runner-address]]
- [[effect-cluster-runner-storage]]
