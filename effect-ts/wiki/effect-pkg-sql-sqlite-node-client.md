---
title: Effect Pkg Sql Sqlite Node Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteClient (@effect/sql-sqlite-node)

SqlClient for Node.js backed by `better-sqlite3`. Uses an Effect `Cache` to memoize prepared statements with a configurable capacity/TTL, enables WAL by default, and exposes backup/export/load-extension helpers. Errors are classified via `classifySqliteError`.

## Key Exports
- `SqliteClient` (tag, interface) — SqlClient + `export`, `backup`, `loadExtension`
- `SqliteClientConfig` — `{ filename, readonly, prepareCacheSize, prepareCacheTTL, disableWAL, transformResultNames, transformQueryNames, spanAttributes }`
- `BackupMetadata` — `{ totalPages, remainingPages }`
- `make(config)` — `Effect<SqliteClient, never, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `TypeId` — branded identifier

## Notes
- `updateValues` is not supported
- A semaphore serializes access to the synchronous driver

## Source
- `raw/effect-smol/packages/sql/sqlite-node/src/SqliteClient.ts`

## Related
- [[effect-pkg-sql-sqlite-node-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
