---
title: Schedule
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Schedule

Strategies for repeating and retrying effects. A `Schedule<Output, Input, Error, Env>` consumes inputs (successes or failures) and decides whether to continue, with what delay, producing an output. Schedules compose via union/intersection and support jitter, exponential backoff, cron, and windowed timings.

## Key Exports
- `Schedule` — interface modeling a repetition/retry policy
- `InputMetadata` / `Metadata` — timing info passed to schedule functions
- `CurrentMetadata` — context reference for active schedule metadata
- `exponential` / `spaced` / `fixed` / `recurs` — primitive schedules
- `both` / `either` — combine schedules by intersection/union
- `jittered` — add randomness to delays
- `addDelay` / `tapOutput` / `collectWhile` — combinators
- `unfold` — build a schedule from a stateful function

## Source
- `raw/effect-smol/packages/effect/src/Schedule.ts`

## Related
- [[effect-ts-v4]]
- Uses Effect, Duration, Cron; consumed by `Effect.retry` and `Effect.repeat`
