---
title: Differ
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Differ

Minimal abstraction for computing and applying diffs between two values of the same type. A `Differ<T, Patch>` pairs a `diff(old, new): Patch` function with `patch(old, patch): T` and a `combine(first, second): Patch` operation for composing patches, plus an `empty` identity patch. It is used internally by Effect's concurrent data structures (e.g. fiber refs, context overrides) to propagate incremental updates efficiently. Reach for it when you need a reusable patch-based update protocol.

## Key Exports
- `Differ<T, Patch>` — interface with `empty`, `diff`, `combine`, `patch`

## Source
- `raw/effect-smol/packages/effect/src/Differ.ts`

## Related
- [[effect-ts-v4]]
- [[effect-context]]
