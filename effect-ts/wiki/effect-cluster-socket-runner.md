---
title: SocketRunner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SocketRunner (unstable)

Layers that wire up runner-to-runner communication over a raw TCP/Unix socket using `SocketServer` and the RPC socket protocol. Logs the bound address on startup and provides both full-runner and client-only variants.

## Key Exports
- `layer` — full socket runner layer (runner server + clients)
- `layerClientOnly` — client-only socket layer

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/SocketRunner.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runner-server]]
- [[effect-cluster-http-runner]]
- [[effect-socket-socket-server]]
