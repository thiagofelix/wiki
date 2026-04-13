---
title: SqlEventLogServerUnencrypted (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SqlEventLogServerUnencrypted (unstable)

SQL-backed `Storage` for `EventLogServerUnencrypted`. Persists plaintext entries per store with a dedicated entries table and a stores table, enabling server-side handlers and queries over typed payloads.

## Key Exports
- `makeStorage` — builds `Storage` service; requires `SqlClient`, `Scope`
- Options: `entryTablePrefix` (default `effect_events`), `remoteIdTable`, `insertBatchSize` (default 200)
- Creates entries, stores, and session-auth bindings tables per dialect
- Singleton row for `remoteId`
- Batched inserts with configurable batch size
- Streams change events via `PubSub`

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/SqlEventLogServerUnencrypted.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-server-unencrypted]]
- [[effect-sql-sql-client]]
