---
title: effect/unstable/rpc (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/rpc (unstable)

Schema-first RPC framework underpinning both client/server code generation and the cluster subsystem. Endpoints are described by `Rpc` values with payload/success/error schemas and optional middleware, grouped into `RpcGroup`s, and exposed over pluggable protocols (HTTP, WebSocket, socket, worker, stdio). Ships with JSON, NDJSON, and MessagePack serializers and integrates with `Stream` for streaming rpcs plus durable mailboxes through the cluster layer.

## Modules
- [[effect-rpc-rpc]] — single rpc endpoint definition
- [[effect-rpc-rpc-client]] — generated client and transport protocols
- [[effect-rpc-rpc-client-error]] — transport-level client errors
- [[effect-rpc-rpc-group]] — composition of rpcs into service groups
- [[effect-rpc-rpc-message]] — wire-level message types
- [[effect-rpc-rpc-middleware]] — server and client middlewares
- [[effect-rpc-rpc-schema]] — `Stream` schema and cause annotations
- [[effect-rpc-rpc-serialization]] — JSON/NDJSON/MsgPack serializers
- [[effect-rpc-rpc-server]] — server runtime and transport layers
- [[effect-rpc-rpc-test]] — in-memory client/server helper
- [[effect-rpc-rpc-worker]] — initial-message helper for worker protocol
- [[effect-rpc-utils]] — shared `withRun`/`withRunClient` helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/`

## Related
- [[effect-ts-v4]]
- [[effect-cluster]]
- [[effect-workflow]]
- [[effect-http]]
