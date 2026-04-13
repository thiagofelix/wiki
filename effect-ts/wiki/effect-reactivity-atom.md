---
title: Atom (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Atom (unstable)

Core reactive primitive inspired by Jotai-style atoms. Atoms encapsulate derived or stored values that are read inside an `AtomRegistry`. They support keep-alive, lazy evaluation, idle TTL, label metadata for devtools, and serialization for hydration. Effectful atoms yield `AsyncResult` values and can be set/updated when writable.

## Key Exports
- `Atom<A>` — base interface (`read(get)`, `keepAlive`, `lazy`, `idleTTL`, `label`)
- `Writable<R, W>` — atom supporting `set`/`update`
- `make`, `makeResult`, `effect`, `fnSync`, `fn` — constructors
- `family` — factory for keyed atom families
- `keepAlive`, `setIdleTTL`, `withLabel` — configuration combinators
- `AtomRuntime` — scoped runtime carrying service context
- `Serializable` — atoms with encode/decode for SSR hydration
- `kvs` — `KeyValueStore`-backed persistence helpers
- Integrates with `Reactivity` for invalidation dependencies

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/Atom.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom-registry]]
- [[effect-reactivity-async-result]]
- [[effect-reactivity-reactivity]]
