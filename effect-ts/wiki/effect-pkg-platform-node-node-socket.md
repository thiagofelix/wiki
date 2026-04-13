---
title: NodeSocket (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeSocket (@effect/platform-node)

Re-exports the shared `NodeSocket` module (TCP clients and generic Duplex adapters) and adds a WebSocket constructor layer using the `ws` library for Node runtimes.

## Key Exports
- All exports of node-shared NodeSocket (NetSocket, NodeWS, makeNet, fromDuplex)
- `layerWebSocketConstructor` — WebSocket constructor layer via `ws`
- `layerWebSocket` — Socket layer for a given WebSocket URL

## Source
- `raw/effect-smol/packages/platform-node/src/NodeSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-node-shared-node-socket]]
- [[effect-socket-socket]]
