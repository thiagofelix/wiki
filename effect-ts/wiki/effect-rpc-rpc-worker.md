---
title: RpcWorker (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcWorker (unstable)

Support for sending an initial schema-encoded message over the worker transport, used to bootstrap a Web Worker with its configuration before normal RPC traffic begins.

## Key Exports
- `InitialMessage` — context service providing the initial payload effect
- `InitialMessage.Encoded` — wire-format initial message
- `makeInitialMessage` — schema-encode a value plus collected transferables
- `layerInitialMessage` — layer providing `InitialMessage` from a schema and effect
- `initialMessage` — decode the initial message on the worker side

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcWorker.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-client]]
- [[effect-workers]]
