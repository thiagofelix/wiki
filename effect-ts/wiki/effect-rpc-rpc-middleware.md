---
title: RpcMiddleware (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcMiddleware (unstable)

Server and client middleware definitions for RPC. Server middlewares wrap a handler effect to supply services, tracing, auth, etc. Client middlewares wrap outgoing requests. Both are defined via `Context.Service` so they can be provided as layers and referenced by rpcs through `middleware(...)`.

## Key Exports
- `TypeId` — middleware discriminator symbol
- `RpcMiddleware` — server middleware function signature (effect + options)
- `RpcMiddlewareClient` — client middleware function signature
- `SuccessValue` — nominal type used to hide success shape from middleware
- `layer` — build a middleware service layer
- `AnyService` / `AnyClient` — structural types for erased middlewares
- `fromContext` — derive middleware from a context tag
- `provide` / `provideClient` — helpers for providing middleware to effects

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcMiddleware.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc]]
- [[effect-rpc-rpc-group]]
