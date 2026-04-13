---
title: NodeClusterSocket (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeClusterSocket (@effect/platform-node-shared)

Cluster transport helpers that plug the socket-based runner protocol into the Effect cluster module using `NodeSocket` and `NodeSocketServer`. Provides a client protocol layer (for RPC over TCP) and a listening socket server layer whose address comes from ShardingConfig.

## Key Exports
- `layerClientProtocol` — `Runners.RpcClientProtocol` via Node net sockets
- `layerSocketServer` — SocketServer layer bound to runnerListenAddress

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeClusterSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-unstable-cluster-runners]]
- [[effect-unstable-cluster-sharding-config]]
