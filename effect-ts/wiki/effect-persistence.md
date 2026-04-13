---
title: Effect Persistence (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]]

# Effect Persistence (unstable)

Hub for the `effect/unstable/persistence` subsystem: durable storage primitives for requests, caches, queues, and rate limits. `Persistable` marries a `Request` with a primary key and success/error schemas; `Persistence` provides a schema-aware store for `Exit` values on top of a pluggable `BackingPersistence` (memory, KeyValueStore, SQL, Redis). Higher-level services layer this into `PersistedCache`, `PersistedQueue`, and distributed `RateLimiter`, with `Redis` and `KeyValueStore` acting as reusable backends.

## Modules
- [[effect-persistence-persistable]] — request classes with primary key + success/error schemas
- [[effect-persistence-persistence]] — schema-aware Exit store and backing-store abstraction
- [[effect-persistence-persisted-cache]] — two-tier cache (in-memory + durable)
- [[effect-persistence-persisted-queue]] — durable at-least-once queue with retries
- [[effect-persistence-rate-limiter]] — fixed-window / token-bucket distributed rate limiter
- [[effect-persistence-key-value-store]] — generic KV service with memory/fs/sql backends
- [[effect-persistence-redis]] — minimal Redis client service with EVALSHA script caching

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/`

## Related
- [[effect-sql]]
- [[effect-schema]]
- [[effect-cache]]
