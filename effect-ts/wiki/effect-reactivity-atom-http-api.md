---
title: AtomHttpApi (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AtomHttpApi (unstable)

Integration between the reactive `Atom` system and `HttpApi`-defined endpoints. Generates a typed `AtomHttpApiClient` service class that exposes per-endpoint query and mutation atom factories, backed by an `HttpApiClient` under the hood and automatically invalidating dependent atoms through `Reactivity`.

## Key Exports
- `AtomHttpApiClient<Self, Id, Groups>` — service class interface
- `make<Self>(id, options)` — factory building the service class
- `.query(group, endpoint, options?)` — returns a query atom factory
- `.mutation(group, endpoint, options?)` — returns a writable mutation atom
- `ResponseMode` — client response mode passthrough
- Errors include `HttpClientError` and decoded `SchemaError`
- Reactivity keys drive cross-atom invalidation

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/AtomHttpApi.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
- [[effect-reactivity-atom-rpc]]
- [[effect-unstable-http-api]]
