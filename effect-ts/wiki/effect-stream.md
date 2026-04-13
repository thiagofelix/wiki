---
title: Stream
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Stream

Pull-based stream of chunked values with effectful evaluation. `Stream<A, E, R>` emits many `A` values, may fail with `E`, and requires services `R`. Built on top of `Channel`, streams support backpressure, chunked emission for performance, monadic composition, merging, partitioning, schedules, PubSub/Queue integration, and fold into sinks.

## Key Exports
- `Stream<A, E, R>` — interface wrapping a Channel
- `StreamTypeLambda` / `Variance` — HKT machinery
- `DefaultChunkSize` — default chunk size from Channel (4096)
- `make` / `fromIterable` / `fromPubSub` / `fromQueue` — constructors
- `map` / `flatMap` / `filter` / `scan` — transformations
- `merge` / `zip` / `concat` — combinators
- `run` / `runForEach` / `runCollect` / `runDrain` — sinks
- `schedule` / `throttle` — time-based operators
- `Success` / `Error` / `Services` — type extractors

## Source
- `raw/effect-smol/packages/effect/src/Stream.ts`

## Related
- [[effect-ts-v4]]
- Paired with [[effect-sink]], [[effect-take]]; built on Channel and Pull
