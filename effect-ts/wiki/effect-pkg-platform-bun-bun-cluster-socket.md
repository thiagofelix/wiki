---
title: BunClusterSocket (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunClusterSocket (@effect/platform-bun)

Wires up an Effect cluster runner over raw TCP sockets using the Node shared socket server (Bun is compatible). Re-exports `layerClientProtocol` and `layerSocketServer` from `@effect/platform-node-shared/NodeClusterSocket` and exposes a configurable `layer` with sharding, storage, and runner-health options.

## Key Exports
- `layerClientProtocol` — re-exported client protocol layer
- `layerSocketServer` — re-exported socket server layer
- `layer` — full cluster layer (clientOnly, storage, runnerHealth, shardingConfig)

## Source
- `raw/effect-smol/packages/platform-bun/src/BunClusterSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-cluster-socket]]
- [[effect-cluster-socket-runner]]
