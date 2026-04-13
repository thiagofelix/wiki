---
title: effect/unstable/reactivity (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/reactivity (hub)

Reactive primitives powering Effect-based UI state management. Built around `Atom`, `AtomRegistry`, and a generic `Reactivity` key-invalidation bus. Includes SSR hydration, RPC/HTTP API integrations that derive query/mutation atoms from typed APIs, and a three-state `AsyncResult` for pending/settled values.

## Entries
- [[effect-reactivity-async-result]] — `Initial | Success | Failure` result type
- [[effect-reactivity-atom]] — reactive atom primitive
- [[effect-reactivity-atom-registry]] — runtime holding atom state
- [[effect-reactivity-atom-ref]] — mutable ref primitive for form state
- [[effect-reactivity-atom-http-api]] — HttpApi to atom integration
- [[effect-reactivity-atom-rpc]] — RPC client to atom integration
- [[effect-reactivity-hydration]] — SSR dehydrate/hydrate
- [[effect-reactivity-reactivity]] — generic key invalidation bus

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/`

## Related
- [[effect-ts-v4]]
- [[effect-httpapi-http-api]]
- [[effect-rpc-rpc-client]]
- [[effect-eventlog]]
