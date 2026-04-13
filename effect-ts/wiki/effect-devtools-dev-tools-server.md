---
title: DevToolsServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DevToolsServer (unstable)

Server-side runner that accepts `Socket` connections from DevTools clients and dispatches their span/metric requests to a handler function. Built on `SocketServer` and the same NDJSON-over-socket transport used by the client.

## Key Exports
- `Client` — `{ queue: Dequeue<Request.WithoutPing>, send: (Response.WithoutPong) => Effect<void> }`
- `run` — accepts a handler `(client: Client) => Effect<_, E, R>` and returns an `Effect` requiring `SocketServer`
- Auto-responds to `Ping` with `Pong`
- Uses `Ndjson.duplexSchemaString` with reversed I/O schemas vs the client
- Per-connection scope with cleanup via `Queue.shutdown`

## Source
- `raw/effect-smol/packages/effect/src/unstable/devtools/DevToolsServer.ts`

## Related
- [[effect-devtools]]
- [[effect-devtools-dev-tools-schema]]
- [[effect-socket-socket-server]]
