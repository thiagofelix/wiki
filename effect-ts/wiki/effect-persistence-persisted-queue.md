---
title: PersistedQueue (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# PersistedQueue (unstable)

Durable queue backed by SQL or Redis. Producers `offer` schema-typed elements (optionally with a custom id for dedupe); consumers `take` a handler that processes an element, with automatic retry up to `maxAttempts` and leasing via scopes. Factory constructs per-name queues sharing a backing store.

## Key Exports
- `PersistedQueue` — interface with `offer` and `take`
- `PersistedQueueFactory` — Context service creating queues from `{ name, schema }`
- `make` — accessor that obtains a queue from the factory
- `makeFactory` — build the factory from a `PersistedQueueStore`
- `PersistedQueueStore` — low-level store contract (`offer`, `take`)
- `PersistedQueueError` — tagged error for queue failures
- `layerSql` / `layerRedis` — backing store layers

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/PersistedQueue.ts`

## Related
- [[effect-persistence-persistence]]
- [[effect-persistence-redis]]
- [[effect-sql-sql-client]]
