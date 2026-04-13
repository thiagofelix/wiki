---
title: MessageStorage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# MessageStorage (unstable)

Context service abstraction for the durable mailbox backing persisted entity requests. Stores requests, envelopes, and replies keyed by snowflake, supports querying unprocessed messages, reply retrieval/clearing, and driver extensions. Includes a memory driver layer (`layerMemory`) plus a `MemoryDriver` service for test inspection.

## Key Exports
- `MessageStorage` — service with `saveRequest`, `saveEnvelope`, `saveReply`, `clearReplies`, etc.
- `SaveResult` — tagged result of a save attempt (persisted/duplicated/ignored)
- `layerMemory` — in-memory implementation layer
- `MemoryDriver` — inspection/control service exposed by the memory driver
- `makeMemoryDriver` — effect building the memory driver directly

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/MessageStorage.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-sql-message-storage]]
- [[effect-cluster-message]]
- [[effect-cluster-reply]]
