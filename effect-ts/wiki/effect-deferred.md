---
title: Deferred
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Deferred

Single-assignment asynchronous variable used to coordinate between fibers. A `Deferred<A, E>` can be completed at most once — with success, failure, or interruption — and any number of fibers can `await` it and be woken when it resolves. Reach for it to build producer/consumer patterns, one-shot signals, cached async computations, and primitives that need multiple fibers to synchronize on a single result.

## Key Exports
- `Deferred<A, E>` — single-set async variable
- `make` — create an empty deferred
- `await` — suspend until the deferred is completed
- `succeed`, `fail`, `failCause`, `die`, `interrupt` — completion operations
- `complete`, `completeWith`, `done` — complete from an `Exit`/`Effect`
- `poll` — non-blocking read returning `Option<Exit<A, E>>`
- `isDone` — check whether the deferred has been set
- `unsafeDone`, `unsafeMake` — sync escape hatches

## Source
- `raw/effect-smol/packages/effect/src/Deferred.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cause]]
