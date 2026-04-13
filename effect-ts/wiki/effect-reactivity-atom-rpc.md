---
title: AtomRpc (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AtomRpc (unstable)

Integration between the reactive `Atom` system and RPC clients. Generates an `AtomRpcClient` service class exposing per-RPC query and mutation atom factories backed by an `RpcClient`, with first-class support for streaming RPCs via `Stream`-backed atoms.

## Key Exports
- `AtomRpcClient<Self, Id, Rpcs>` — service class interface
- `make<Self>(id, options)` — factory building the service class
- `.query(tag)` — query atom for request/response RPCs
- `.mutation(tag)` — writable mutation atom
- `.stream(tag)` — stream atom for `RpcSchema.Stream`-typed results
- Errors default to `RpcClientError`
- Reactivity keys thread through mutations to invalidate queries
- Uses `HttpApiClient`-style headers pass-through

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/AtomRpc.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
- [[effect-reactivity-atom-http-api]]
- [[effect-rpc-rpc-client]]
