---
title: PartitionedSemaphore
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PartitionedSemaphore

A semaphore that controls access to a shared permit pool while tracking waiters by partition key. Waiting permits are distributed across partitions in round-robin order, preventing any single key from monopolizing the pool under contention. Useful for fair concurrency limits across tenants, users, or resources.

## Key Exports
- `PartitionedSemaphore<K>` — interface carrying `capacity`, `available`, `take`, `release`
- `PartitionedTypeId` — brand type id
- `makeUnsafe({ permits })` — constructs a partitioned semaphore synchronously
- `take(key, permits)` — acquire permits under a partition key
- `release(permits)` — return permits, waking round-robin waiters
- `withPermits(key, permits)` — scoped acquire/release wrapping an Effect
- `withPermit(key)` — convenience for a single permit
- `withPermitsIfAvailable(permits)` — non-blocking attempt returning `Option`

## Source
- `raw/effect-smol/packages/effect/src/PartitionedSemaphore.ts`

## Related
- [[effect-ts-v4]]
- [[effect-semaphore]]
- [[effect-pool]]
