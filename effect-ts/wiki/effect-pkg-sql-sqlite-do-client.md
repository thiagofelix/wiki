---
title: Effect Pkg Sql Sqlite Do Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteClient (@effect/sql-sqlite-do)

SqlClient for Cloudflare Durable Object SQL storage (`SqlStorage` from `@cloudflare/workers-types`). Because DO SQL is synchronous and single-instance, iteration is done eagerly with a generator that wraps `ArrayBuffer` values into `Uint8Array`. Transactions are supported via the DO storage API.

## Key Exports
- `SqliteClient` (tag, interface) — SqlClient specialization
- `SqliteClientConfig` — `{ db: SqlStorage, transformResultNames, transformQueryNames, spanAttributes }`
- `make(config)` — `Effect<SqliteClient, never, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `TypeId` — branded identifier

## Notes
- `updateValues` is not supported
- Streaming reads produce rows lazily from a DO `exec` cursor

## Source
- `raw/effect-smol/packages/sql/sqlite-do/src/SqliteClient.ts`

## Related
- [[effect-pkg-sql-sqlite-do-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
