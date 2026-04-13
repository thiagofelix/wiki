---
title: EntityProxyServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EntityProxyServer (unstable)

Provides layers that implement the `RpcGroup` / `HttpApiGroup` derived by `EntityProxy` by forwarding each proxy rpc to the underlying entity client. Logs, annotates, and handles both normal and `Discard` variants.

## Key Exports
- `layerHttpApi` — layer implementing an `HttpApiBuilder` group from an entity
- `layerRpcHandlers` — layer implementing the rpc handlers derived by `EntityProxy.toRpcGroup`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/EntityProxyServer.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-entity-proxy]]
- [[effect-cluster-entity]]
- [[effect-httpapi-http-api-builder]]
