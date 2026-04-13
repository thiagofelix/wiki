---
title: SocketServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SocketServer (unstable)

Abstract TCP/Unix socket server service tag. Platform packages provide concrete implementations that accept incoming connections and dispatch them to a handler receiving a `Socket` per client. Defines tagged errors and a union `Address` type for TCP and Unix domain sockets.

## Key Exports
- `SocketServer` — service with `address` and `run(handler)`
- `SocketServerError` — tagged error wrapping `reason`
- `SocketServerOpenError`, `SocketServerUnknownError` — error reasons
- `Address` — `TcpAddress | UnixAddress` union
- `TcpAddress` — `{ hostname, port }`
- `UnixAddress` — `{ path }`
- `ErrorTypeId` — branding

## Source
- `raw/effect-smol/packages/effect/src/unstable/socket/SocketServer.ts`

## Related
- [[effect-socket]]
- [[effect-socket-socket]]
- [[effect-devtools-dev-tools-server]]
