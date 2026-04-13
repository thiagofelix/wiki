---
title: Pool
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Pool

A `Pool<A, E>` manages a set of acquirable items (database connections, workers, etc.) with min/max sizing, per-item concurrency, target utilization, and optional time-to-live invalidation strategies. The pool is scoped: items are released when the enclosing scope closes. Different strategies (noop, creation-TTL, usage-TTL) control when idle items are invalidated.

## Key Exports
- `Pool<A, E>` — pipeable pool interface with `config` and `state`
- `make({ acquire, size, concurrency, targetUtilization })` — fixed-size pool
- `makeWithTTL({ acquire, min, max, timeToLive, timeToLiveStrategy })` — sizeable pool with expiry
- `makeWithStrategy` — custom strategy constructor
- `Strategy<A, E>` — interface for run/onAcquire/reclaim logic
- `Config<A, E>`, `State<A, E>`, `PoolItem<A, E>` — internal models
- `isPool` — refinement guard

## Source
- `raw/effect-smol/packages/effect/src/Pool.ts`

## Related
- [[effect-ts-v4]]
- [[effect-rc-map]]
- [[effect-resource]]
