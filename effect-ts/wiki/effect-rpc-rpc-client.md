---
title: RpcClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcClient (unstable)

Client runtime for invoking an `RpcGroup`. Handles request lifecycle (tracing, acks, streaming), serialization via `RpcSerialization`, transport protocols (HTTP, WebSocket, worker, custom), reconnection, and exposes each rpc as a strongly-typed function on a generated client object.

## Key Exports
- `RpcClient<Rpcs>` — type representing the generated client
- `make` — build a client from a group and a `Protocol`
- `makeNoSerialization` — build a bare client when serialization is elsewhere
- `Protocol` — context tag for the pluggable client transport
- `layerProtocolHttp` — HTTP-based `Protocol` layer
- `layerProtocolSocket` — WebSocket-based `Protocol` layer
- `layerProtocolWorker` — Web Worker-based `Protocol` layer
- `makeProtocolHttp` — build an HTTP protocol from an `HttpClient`
- `makeProtocolSocket` — build a socket protocol
- `withRunClient` — helper wiring run semantics into a custom protocol

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcClient.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-server]]
- [[effect-rpc-rpc-serialization]]
- [[effect-rpc-rpc-client-error]]
