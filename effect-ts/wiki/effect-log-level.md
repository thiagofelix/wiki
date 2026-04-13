---
title: LogLevel
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# LogLevel

String-literal type describing log severity (`All`, `Fatal`, `Error`, `Warn`, `Info`, `Debug`, `Trace`, `None`) with ordering, equivalence, and comparison utilities. Used by `Logger` and `Effect.log*` functions to decide whether messages should be emitted.

## Key Exports
- `LogLevel` — union type of all level names
- `Severity` — subset excluding `All` and `None`
- `values` — readonly array of all levels in order
- `Order` — `Order<LogLevel>` instance
- `Equivalence` — strict equivalence instance
- `getOrdinal` — numeric ordinal for a level
- `isGreaterThan` / `isGreaterThanOrEqualTo` / `isLessThan` / `isLessThanOrEqualTo` — level comparators

## Source
- `raw/effect-smol/packages/effect/src/LogLevel.ts`

## Related
- [[effect-ts-v4]]
- [[effect-logger]]
- [[effect-order]]
