---
title: cluster/internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# cluster/internal (unstable)

Private helpers used by the cluster runtime. Not part of the public surface, included here for navigation only.

## Modules
- `entityManager.ts` — per-entity-type manager coordinating mailbox, handlers, and shutdown
- `entityReaper.ts` — background reaper for idle entities using the configured TTL
- `hash.ts` — `hashString` utility used for shard selection and message ids
- `interruptors.ts` — internal set of interruption hooks shared across the runtime
- `resourceMap.ts` — refcounted map of scoped resources keyed by id
- `resourceRef.ts` — scoped ref holding a single resource rebuild-able on demand

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/internal/`

## Related
- [[effect-cluster]]
- [[effect-cluster-sharding]]
- [[effect-cluster-entity]]
