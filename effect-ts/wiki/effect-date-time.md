---
title: DateTime
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DateTime

Immutable instant-in-time type with optional timezone awareness. `DateTime` is a tagged union of `Utc` (bare instant) and `Zoned` (instant attached to a `TimeZone`), both represented by a numeric `epochMilliseconds` plus cached date parts. The module provides constructors from many input shapes, arithmetic (add/subtract units), formatting, parsing, and comparisons, and integrates with `Effect` through `Layer`-provided timezone services. Reach for it instead of native `Date` whenever you need immutability, typed timezone handling, or Effect-native time operations.

## Key Exports
- `DateTime = Utc | Zoned` — tagged union type
- `Utc`, `Zoned` — the two variants, with cached `parts` and epoch millis
- `TimeZone` — named or offset-based timezone
- `DateTime.Input` — polymorphic input (DateTime, Parts, Date, number, string, Instant)
- `DateTime.Unit` / `UnitSingular` / `UnitPlural` — millisecond..year unit tags
- `make`, `makeZoned`, `unsafeMake`, `now`, `nowInCurrentZone` — constructors
- `add`, `subtract`, `startOf`, `endOf`, `setParts` — arithmetic
- `toDate`, `toEpochMillis`, `format`, `formatIso`, `formatLocal` — conversion/rendering
- `zoneFromString`, `zoneMakeNamed`, `zoneMakeOffset`, `setZone`, `withCurrentZone` — timezone operations
- `Order`, `Equivalence` — typeclass instances

## Source
- `raw/effect-smol/packages/effect/src/DateTime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-duration]]
- [[effect-clock]]
- [[effect-cron]]
