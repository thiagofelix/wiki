---
title: Function
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Function

Utilities for working with plain functions: composition, currying, piping, and the `dual` helper used across the library to expose APIs in both data-first and data-last styles. This is the low-level plumbing that makes Effect's pipeable API ergonomic.

## Key Exports
- `dual` — create functions that accept data-first or data-last call styles
- `pipe` — left-to-right function application
- `flow` — left-to-right function composition
- `identity`, `constant`, `constVoid`, `constTrue`, `constFalse` — common constants
- `compose` — right-to-left composition
- `tupled`, `untupled` — argument shape transforms
- `LazyArg` — `() => A` type alias
- `apply`, `absurd` — miscellaneous helpers
- `FunctionTypeLambda` — HKT encoding

## Source
- `raw/effect-smol/packages/effect/src/Function.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pipeable]]
- [[effect-hkt]]
