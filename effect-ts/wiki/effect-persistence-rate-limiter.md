---
title: RateLimiter (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# RateLimiter (unstable)

Distributed rate limiter supporting fixed-window and token-bucket algorithms with either fail-fast or delay-based back-pressure. Backed by a pluggable `RateLimiterStore` (in-memory, SQL, Redis) so multiple processes can share state.

## Key Exports
- `RateLimiter` — Context service with `consume({ algorithm, onExceeded, window, limit, key, tokens })`
- `ConsumeResult` — `{ delay, limit, remaining, resetAfter }`
- `RateLimiterError` — error wrapping a reason (e.g. `RateLimitExceeded`)
- `RateLimitExceeded` — schema tagged with `key`, `retryAfter`, `limit`, `remaining`
- `RateLimiterStore` — low-level service with `fixedWindow` and `tokenBucket` ops
- `make` — build a `RateLimiter` from a store
- `layerMemory` / `layerSql` / `layerRedis` — store layers

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/RateLimiter.ts`

## Related
- [[effect-persistence-redis]]
- [[effect-sql-sql-client]]
