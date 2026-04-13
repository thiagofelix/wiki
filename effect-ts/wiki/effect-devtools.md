---
title: effect/unstable/devtools (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/devtools (hub)

Bidirectional protocol for streaming Effect tracing spans and metric snapshots to a DevTools UI over a WebSocket/Socket. The client installs a wrapping `Tracer` that pushes spans in real time, and the server runs a handler for each connected client. Schema is shared between client and server and encoded as NDJSON.

## Entries
- [[effect-devtools-dev-tools]] — top-level layers (`layer`, `layerWebSocket`, `layerSocket`)
- [[effect-devtools-dev-tools-client]] — client service and `Tracer` wrapper
- [[effect-devtools-dev-tools-server]] — server runner over `SocketServer`
- [[effect-devtools-dev-tools-schema]] — protocol schemas for requests and responses

## Source
- `raw/effect-smol/packages/effect/src/unstable/devtools/`

## Related
- [[effect-ts-v4]]
- [[effect-socket]]
- [[effect-unstable-encoding-ndjson]]
- [[effect-tracer]]
