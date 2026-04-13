---
title: HttpRunner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpRunner (unstable)

Layers that wire up a cluster runner's inter-runner transport over HTTP (or WebSocket) using the RPC infrastructure. Provides both the client-side `RpcClientProtocol` implementations and the server-side route/handler layers, letting runners talk to each other without a dedicated socket protocol.

## Key Exports
- `layerClientProtocolHttp` — client protocol over HTTP with configurable path/https
- `layerClientProtocolHttpDefault` — default root path HTTP client protocol
- `layerClientProtocolWebsocket` — client protocol over WebSocket
- `layerHttpRouter` — mount the runner rpc server on an `HttpRouter`
- `layerHttp` — full layer bundling HTTP client protocol and server
- `layerWebsocket` — full layer bundling WebSocket client protocol and server

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/HttpRunner.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runners]]
- [[effect-cluster-runner-server]]
- [[effect-http-http-router]]
