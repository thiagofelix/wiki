---
title: EntityProxy (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EntityProxy (unstable)

Derives a flat `RpcGroup` (and companion `HttpApiGroup`) from an `Entity` so external clients can address it via regular RPC/HTTP. Each entity rpc produces a `type.tag` rpc taking an `entityId` plus original payload, together with a `Discard` variant for fire-and-forget.

## Key Exports
- `toRpcGroup` — derive an `RpcGroup` that forwards to entity rpcs
- `toHttpApiGroup` — derive an `HttpApiGroup` exposing the entity over HTTP
- `ConvertRpcs` — type helper mapping entity rpcs to proxy rpcs

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/EntityProxy.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-entity]]
- [[effect-cluster-entity-proxy-server]]
- [[effect-rpc-rpc-group]]
