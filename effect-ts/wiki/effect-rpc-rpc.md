---
title: Rpc (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Rpc (unstable)

Core definition of an RPC endpoint. Each `Rpc` carries a tag, payload/success/error schemas, middlewares, and context annotations. Endpoints can be composed into `RpcGroup`s and served/consumed uniformly. Also exposes helpers for primary keys, headers, and typing of handlers.

## Key Exports
- `Rpc` — interface describing an endpoint with schemas and annotations
- `make` — constructor for an rpc with payload/success/error schemas
- `setSuccess` / `setError` / `setPayload` — reshape schemas
- `annotate` / `annotateMerge` — attach context annotations
- `middleware` — attach middleware services to the endpoint
- `isRpc` — type guard
- `ServerClient` — server-side invocation interface
- `Payload` / `Success` / `Error` / `Tag` — type helpers
- `AnyWithProps` — structural type for erased rpcs

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/Rpc.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-group]]
- [[effect-rpc-rpc-middleware]]
- [[effect-ts-v4]]
