---
title: Redis (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# Redis (unstable)

Minimal Redis client service used by persistence backends. Exposes a generic `send(command, ...args)` for arbitrary commands and an `eval` helper that caches `SCRIPT LOAD` results so Lua scripts can be invoked via `EVALSHA` with typed params and return values.

## Key Exports
- `Redis` — Context service with `send` and `eval`
- `make` — build a service from a driver `send` function, wiring the script-SHA cache
- `RedisError` — schema tagged error carrying a defect cause
- `Script` — typed Lua script with `lua`, `params`, `numberOfKeys`, and `withReturnType<T>()`
- `script` — constructor that builds a `Script` from a params function and Lua source

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/Redis.ts`

## Related
- [[effect-persistence-rate-limiter]]
- [[effect-persistence-persisted-queue]]
