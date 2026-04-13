---
title: NodeSocketServer (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeSocketServer (@effect/platform-node-shared)

Implements `SocketServer` using Node's `net.createServer`. Collects pending connections before `run`, dispatches each accepted socket to the user handler as an Effect, and supplies the raw `net.Socket` via the `NetSocket` service. Also defines an `IncomingMessage` tag for bridging with HTTP upgrades.

## Key Exports
- `IncomingMessage` — Context.Service tag for HTTP upgrade requests
- `make` — constructs a SocketServer from ServerOpts + ListenOptions
- `layer` — SocketServer layer

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeSocketServer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-unstable-socket-socket-server]]
