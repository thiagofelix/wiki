---
title: BunSocket (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunSocket (@effect/platform-bun)

Re-exports `@effect/platform-node-shared/NodeSocket` for TCP/net.Socket support and adds a browser-style WebSocket layer that uses Bun's `globalThis.WebSocket`. This unifies client TCP and WebSocket connectivity on Bun.

## Key Exports
- All exports of `NodeSocket` (layerNet, makeNet, ...)
- `layerWebSocketConstructor` — provides `Socket.WebSocketConstructor`
- `layerWebSocket` — Socket layer for a given WebSocket URL

## Source
- `raw/effect-smol/packages/platform-bun/src/BunSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-socket]]
- [[effect-unstable-socket-socket]]
