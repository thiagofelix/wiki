---
title: Equal
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Equal

Structural and custom equality for Effect values. `Equal.equals` performs deep comparison on primitives, plain objects, arrays, Maps, Sets, Dates, and RegExps, while allowing types to override via the `[Equal.symbol]` method paired with `[Hash.symbol]`. Uses a hash-first shortcut and WeakMap caching, so objects must be treated as immutable after their first comparison. Foundational for HashMap/HashSet key semantics.

## Key Exports
- `Equal` — interface for types with custom equality (extends `Hash.Hash`)
- `symbol` — property key for equality method implementation
- `equals` — curried/dual structural comparison
- `isEqual` — type guard for Equal implementors
- `asEquivalence` — adapt to `Equivalence<A>`
- `byReference`, `byReferenceUnsafe` — opt individual objects out of structural compare

## Source
- `raw/effect-smol/packages/effect/src/Equal.ts`

## Related
- [[effect-ts-v4]]
- [[effect-hash]]
- [[effect-equivalence]]
