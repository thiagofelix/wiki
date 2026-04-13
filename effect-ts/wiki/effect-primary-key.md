---
title: PrimaryKey
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PrimaryKey

A minimal interface for objects that can expose a unique string identifier. Objects implement `[PrimaryKey.symbol](): string` and the `value` accessor extracts it. Used throughout Effect for cache keys, request deduplication, persistence, and any scenario needing a structural unique identifier.

## Key Exports
- `PrimaryKey` — interface with `[symbol](): string`
- `symbol` — the identifier `"~effect/interfaces/PrimaryKey"`
- `isPrimaryKey(u)` — type guard
- `value(self)` — extracts the string key

## Source
- `raw/effect-smol/packages/effect/src/PrimaryKey.ts`

## Related
- [[effect-ts-v4]]
- [[effect-request-resolver]]
- [[effect-equal]]
