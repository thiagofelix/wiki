---
title: RunnerServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RunnerServer (unstable)

Server-side RPC handlers that implement the `Runners.Rpcs` protocol on a runner: `Ping`, `Notify`, `Effect`. Incoming effect calls are converted into `IncomingRequest`s and forwarded to `Sharding` with an adapter that streams replies back to the caller.

## Key Exports
- `layerHandlers` — layer implementing the `Runners.Rpcs` handlers
- `layerWithClients` — full layer wiring handlers, protocol server, and client protocol
- `layerClientOnly` — layer for client-only deployments (no inbound traffic)

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/RunnerServer.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runners]]
- [[effect-cluster-http-runner]]
- [[effect-cluster-socket-runner]]
