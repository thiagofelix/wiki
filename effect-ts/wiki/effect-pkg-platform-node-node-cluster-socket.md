---
title: NodeClusterSocket (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeClusterSocket (@effect/platform-node)

Wires an Effect cluster runner over raw TCP sockets. Re-exports `layerClientProtocol` and `layerSocketServer` from node-shared and exposes a configurable `layer` plus a k8s-aware `layerK8sHttpClient` that uses Undici for in-cluster discovery.

## Key Exports
- `layerClientProtocol` — re-exported client RPC protocol layer
- `layerSocketServer` — re-exported socket server layer
- `layerK8sHttpClient` — k8s HttpClient layer via Undici
- `layer` — cluster layer with storage and runner-health options

## Source
- `raw/effect-smol/packages/platform-node/src/NodeClusterSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-node-shared-node-cluster-socket]]
- [[effect-cluster-socket-runner]]
