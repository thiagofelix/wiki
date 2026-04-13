---
title: Effect Pkg Sql Sqlite Bun Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteClient (@effect/sql-sqlite-bun)

SqlClient for Bun's built-in `bun:sqlite` driver. Respects the `Client.SafeIntegers` context reference to toggle bigint integer mode per fiber, enables WAL by default, and supports `export` (serialize database) and `loadExtension`.

## Key Exports
- `SqliteClient` (tag, interface) — SqlClient + `export`, `loadExtension`
- `SqliteClientConfig` — `{ filename, readonly, create, readwrite, disableWAL, transformResultNames, transformQueryNames, spanAttributes }`
- `make(config)` — `Effect<SqliteClient, never, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `TypeId` — branded identifier

## Notes
- `updateValues` is not supported
- Uses a semaphore to serialize access to the synchronous driver

## Source
- `raw/effect-smol/packages/sql/sqlite-bun/src/SqliteClient.ts`

## Related
- [[effect-pkg-sql-sqlite-bun-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
