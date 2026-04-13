---
title: AtomRef (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AtomRef (unstable)

Lightweight mutable reference primitive used by `Atom` for form-like state. `AtomRef` exposes `.set`, `.update`, `.prop` (for nested fields), and `.map` for read-only derivations. Supports a `Collection` variant with `push`/`insertAt`/`remove` operations.

## Key Exports
- `ReadonlyRef<A>` — base interface with `value`, `subscribe`, `map`
- `AtomRef<A>` — adds `set`, `update`, `prop`
- `Collection<A>` — `ReadonlyRef<ReadonlyArray<AtomRef<A>>>` with mutation helpers
- `make<A>(value)` — constructor returning `AtomRef<A>`
- `makeCollection` — build a collection ref
- `TypeId` — branding identifier
- Implements `Equal` and `Hash`

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/AtomRef.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
