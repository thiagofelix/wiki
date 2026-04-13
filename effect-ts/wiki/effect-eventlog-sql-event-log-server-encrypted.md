---
title: SqlEventLogServerEncrypted (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SqlEventLogServerEncrypted (unstable)

SQL-backed `Storage` for `EventLogServerEncrypted`. Persists per-public-key encrypted entries across dialects, with configurable table prefix and batch size. Also stores session-auth bindings and the server's `RemoteId` singleton.

## Key Exports
- `makeStorage` — builds `Storage` service; requires `SqlClient`, `EventLogEncryption`, `Scope`
- Options: `entryTablePrefix` (default `effect_events`), `remoteIdTable`, `insertBatchSize` (default 200)
- Creates tables via dialect-aware DDL
- Uses `RcMap` for per-store connection caching
- Handles session auth binding storage
- Delegates encryption/decryption to `EventLogEncryption`

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/SqlEventLogServerEncrypted.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-server-encrypted]]
- [[effect-sql-sql-client]]
