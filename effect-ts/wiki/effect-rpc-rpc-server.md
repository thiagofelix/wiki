---
title: RpcServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcServer (unstable)

Server runtime for an `RpcGroup`. Decodes incoming messages, dispatches to handlers, manages tracing spans, enforces concurrency limits, streams responses with ack-based flow control, and supports multiple transports (HTTP router, socket server, worker runner, stdio).

## Key Exports
- `RpcServer<A>` — interface with `write` and `disconnect`
- `makeNoSerialization` — build a server bypassing serialization (for in-process use)
- `Protocol` — context tag for the pluggable server transport
- `layer` — build a server layer from a group
- `layerHttpRouter` — expose a server over an HTTP router endpoint
- `layerProtocolHttp` / `layerProtocolSocketServer` / `layerProtocolWorkerRunner` / `layerProtocolStdio` — transport layers
- `layerClientProtocolHttp` — client-facing HTTP protocol layer used by peers

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcServer.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-client]]
- [[effect-rpc-rpc-group]]
- [[effect-rpc-rpc-serialization]]
