---
title: EventLogServerEncrypted (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogServerEncrypted (unstable)

Storage-abstract encrypted event log server. Entries are stored as opaque `PersistedEntry` blobs and the server only sees public-key-scoped store ids, never plaintext payloads. Uses `EventLogServer.layerRpcHandlers` with a `Storage` service for persistence.

## Key Exports
- `Storage` — service with `getId`, `write`, `read`, `getOrCreateSessionAuthBinding`
- `PersistedEntry` — `{ entryId, iv, encryptedEntry }` record
- `layerRpcHandlers` — plug-and-play layer wiring encrypted server to storage
- Delegates to `EventLogServer.layerRpcHandlers`
- Decodes `WriteEntries` and persists encrypted payloads per publicKey/storeId

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogServerEncrypted.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-server]]
- [[effect-eventlog-sql-event-log-server-encrypted]]
