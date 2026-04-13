---
title: Sink
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Sink

Consumer of stream elements. `Sink<A, In, L, E, R>` reads a variable number of `In` chunks, may fail with `E`, and yields a summary `A` plus optional leftovers `L`. Sinks are the dual of `Stream` — they fold, count, collect, or forward to effects.

## Key Exports
- `Sink<A, In, L, E, R>` — interface with a `transform` function running over a Pull
- `End<A, L>` — result tuple `[value, leftovers?]`
- `succeed` / `fail` — constant sinks
- `drain` — consume and discard all elements
- `collectAll` — accumulate elements to an array
- `forEach` / `forEachChunk` — effectful per-element consumers
- `SinkUnify` — type-level unification hook

## Source
- `raw/effect-smol/packages/effect/src/Sink.ts`

## Related
- [[effect-ts-v4]]
- Pairs with [[effect-stream]]; built on Channel, Pull, Scope
