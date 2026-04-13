---
title: SqlEventJournal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SqlEventJournal (unstable)

SQL-backed implementation of `EventJournal` supporting Postgres, MySQL, MSSQL, and SQLite dialects. Creates the required tables on first use and exposes a `make` function returning an `EventJournal.Service`. Uses dialect-aware DDL via `SqlClient.onDialectOrElse`.

## Key Exports
- `make` — builds an `EventJournal` backed by a `SqlClient`
- Options: `entryTable` (default `effect_event_journal`), `remotesTable` (default `effect_event_remotes`)
- Creates tables with dialect-specific column types (UUID/BYTEA/BINARY/BLOB)
- Writes entries with primary key + msgpack payload + timestamp
- Uses `PubSub` to broadcast local entry changes
- Tracks remote sequences in the remotes table

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/SqlEventJournal.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-journal]]
- [[effect-unstable-sql-client]]
