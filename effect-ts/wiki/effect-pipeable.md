---
title: Pipeable
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Pipeable

Defines the `Pipeable` interface whose `.pipe` method enables fluent, left-to-right composition of unary functions on any Effect value. Virtually every type in the library extends this interface, making `value.pipe(fn1, fn2, ...)` the idiomatic way to chain operations without deep nesting. The overloads support up to many sequential transformations while preserving type inference.

## Key Exports
- `Pipeable` — interface with overloaded `pipe` method (0..N args)
- `pipeArguments(self, args)` — runtime helper used by implementors to apply the pipe chain

## Source
- `raw/effect-smol/packages/effect/src/Pipeable.ts`

## Related
- [[effect-ts-v4]]
- [[effect-function]]
