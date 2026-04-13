---
title: RunnerHealth (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RunnerHealth (unstable)

Service that answers whether a given runner is currently considered alive. Used by sharding to decide when shards can be reassigned. Ships with a no-op, a ping-based (via `Runners.ping`), and a Kubernetes-based implementation.

## Key Exports
- `RunnerHealth` — service with `isAlive`
- `layerNoop` — treat every runner as healthy (for tests)
- `makePing` / `layerPing` — effect / layer using `Runners.ping` with timeout and retries
- `makeK8s` / `layerK8s` — effect / layer backed by the Kubernetes pods API

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/RunnerHealth.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runners]]
- [[effect-cluster-k8s-http-client]]
