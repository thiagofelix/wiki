---
title: Duration
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Duration

Immutable span of time with nanosecond precision. A `Duration` is stored as either a `Millis` number, a `Nanos` bigint, or one of the infinities, and can be constructed from numbers, bigints, tuples, duration strings (`"5 seconds"`), or object descriptors. Supports arithmetic, comparisons, conversion between units, and pretty printing. Used throughout Effect for timeouts, sleeps, schedules, TTLs, and anything time-span related.

## Key Exports
- `Duration` — immutable interface with `Equal`, `Pipeable`, `Inspectable`
- `DurationValue` — internal union `Millis | Nanos | Infinity | NegativeInfinity`
- `Unit` — string unit tags from `"nano"` to `"weeks"`
- `Input` — polymorphic constructor input
- `nanos`, `micros`, `millis`, `seconds`, `minutes`, `hours`, `days`, `weeks`, `infinity`, `zero` — constructors
- `decode`, `decodeUnknown` — parse an `Input` into a `Duration`
- `sum`, `subtract`, `times`, `divide` — arithmetic
- `lessThan`, `greaterThan`, `between`, `min`, `max`, `clamp`, `Order`, `Equivalence` — comparisons
- `toMillis`, `toNanos`, `toSeconds`, `toMinutes`, `unsafeToNanos`, `parts` — conversion
- `format`, `formatIso` — human-readable output
- `Combiner` / `Reducer` instances for summing durations

## Source
- `raw/effect-smol/packages/effect/src/Duration.ts`

## Related
- [[effect-ts-v4]]
- [[effect-clock]]
- [[effect-date-time]]
