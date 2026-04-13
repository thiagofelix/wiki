---
title: NodeClusterHttp (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeClusterHttp (@effect/platform-node)

Wires an Effect cluster runner over HTTP/WebSocket using Node's HTTP server and Undici HTTP client. Exposes `layerHttpServer` (binding to ShardingConfig.runnerAddress) and a configurable `layer` accepting transport, serialization, storage, and runner-health options (ping or k8s).

## Key Exports
- `layerK8sHttpClient` — re-exported from NodeClusterSocket
- `layerHttpServer` — bound HTTP server layer
- `layer` — full cluster layer builder

## Source
- `raw/effect-smol/packages/platform-node/src/NodeClusterHttp.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-cluster-http-runner]]
- [[effect-pkg-platform-node-node-http-server]]
