---
title: NonEmptyIterable
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NonEmptyIterable

Branded iterable type with a compile-time guarantee of at least one element. Enables safe operations (first element, reduce without seed, max/min) that would otherwise require runtime checks. The brand is a phantom symbol — values are regular iterables at runtime.

## Key Exports
- `NonEmptyIterable<A>` — branded iterable type with ≥1 element
- `nonEmpty` — the phantom unique symbol used for branding
- `unprepend` — destructure into `[head, restIterator]`

## Source
- `raw/effect-smol/packages/effect/src/NonEmptyIterable.ts`

## Related
- [[effect-ts-v4]]
- [[effect-iterable]]
- [[effect-array]]
