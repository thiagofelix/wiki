---
title: Types
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Types

Compile-time-only type utility library used throughout Effect. Provides generic tools for manipulating object shapes, tagged unions, tuples, variance markers, and nested "reason" error patterns. Nothing here has a runtime representation.

## Key Exports
- `Simplify<T>` — flatten intersection types
- `Mutable<T>` / `DeepMutable<T>` — strip readonly
- `Equals` / `EqualsWith` — compile-time equality
- `MergeLeft` / `MergeRight` / `MergeRecord` — object merging
- `Tags<E>` / `ExtractTag` / `ExcludeTag` / `NarrowReason` — tagged union ops
- `ReasonOf` / `ReasonTags` / `ExtractReason` / `ExcludeReason` / `OmitReason` — reason error pattern
- `TupleOf<N, T>` / `TupleOfAtLeast<N, T>` — fixed-length tuples
- `Covariant` / `Contravariant` / `Invariant` — variance markers
- `Concurrency` — `number | "unbounded" | "inherit"`
- `NoInfer` / `IsUnion` / `unassigned` / `unhandled` — misc helpers

## Source
- `raw/effect-smol/packages/effect/src/Types.ts`

## Related
- [[effect-ts-v4]]
- Used by nearly every module; complements [[effect-utils]]
