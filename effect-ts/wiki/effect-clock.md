---
title: Clock
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Clock

Core runtime service that abstracts access to the current time and the ability to sleep. Every Effect fiber resolves time through a `Clock`, which makes time observable, injectable, and mockable — the `TestClock` variant lets tests advance time deterministically without real delays. Reach for it directly when you need precise timing, measurement, or to pass the clock explicitly; most code just uses `Effect.sleep` which consults the ambient clock.

## Key Exports
- `Clock` — interface with `currentTimeMillis`, `currentTimeNanos`, `sleep`, plus unsafe variants
- `Clock` (service tag) — `Context.Reference` for injecting and overriding the clock
- `currentTimeMillis` — `Effect<number>` reading the current clock
- `currentTimeNanos` — `Effect<bigint>` nanosecond variant
- `sleep` — suspend a fiber for a `Duration`
- `clockWith` — build an effect that depends on the current `Clock`
- `make` — construct a custom `Clock` implementation

## Source
- `raw/effect-smol/packages/effect/src/Clock.ts`

## Related
- [[effect-ts-v4]]
- [[effect-duration]]
- [[effect-date-time]]
