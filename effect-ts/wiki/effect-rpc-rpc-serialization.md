---
title: RpcSerialization (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcSerialization (unstable)

Pluggable serializer used by RPC transports. Implementations expose a `Parser` with `encode`/`decode` methods, a content type, and whether the format includes framing. Built-ins cover JSON, NDJSON, and MessagePack via `msgpackr`.

## Key Exports
- `RpcSerialization` — context service holding a serializer factory
- `Parser` — encode/decode pair produced per connection
- `json` / `layerJson` — plain JSON (no framing)
- `ndjson` / `layerNdjson` — newline-delimited JSON with framing
- `msgpack` / `layerMsgPack` — `msgpackr`-based binary format

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcSerialization.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-client]]
- [[effect-rpc-rpc-server]]
