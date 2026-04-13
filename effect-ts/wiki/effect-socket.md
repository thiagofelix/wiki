---
title: effect/unstable/socket (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/socket (hub)

Abstract bidirectional socket primitives. `Socket` represents a client connection with send/receive handlers and channel adapters. `SocketServer` represents a server accepting multiple `Socket` clients. A built-in WebSocket implementation is included; TCP/Unix implementations come from platform packages.

## Entries
- [[effect-socket-socket]] — client socket service and WebSocket layer
- [[effect-socket-socket-server]] — server socket service tag and address model

## Source
- `raw/effect-smol/packages/effect/src/unstable/socket/`

## Related
- [[effect-ts-v4]]
- [[effect-channel]]
- [[effect-devtools]]
- [[effect-unstable-http-client]]
