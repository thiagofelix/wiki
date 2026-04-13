---
title: NodeSocket (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeSocket (@effect/platform-node-shared)

Implements the core `Socket` service over Node `net` and `ws`. Supports TCP client connections via `makeNet`, generic `Duplex` adapters via `fromDuplex`, and a re-export of the `ws` package for WebSocket clients. Exposes `NetSocket` as a service so handlers can reach the underlying Node socket.

## Key Exports
- `NetSocket` — Context.Service tag carrying the raw `net.Socket`
- `NodeWS` — re-export of the `ws` library
- `makeNet` — TCP client socket with open timeout and finalizer
- `fromDuplex` — Socket from any Node Duplex stream

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-socket-socket]]
