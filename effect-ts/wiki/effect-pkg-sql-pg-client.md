---
title: Effect Pkg Sql Pg Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### PgClient (@effect/sql-pg)

SqlClient for PostgreSQL built on the `pg` driver, `pg-cursor` for streaming, and `pg-connection-string` for URL parsing. Uses a `Pool` and Effect `RcRef` + `Semaphore` for connection management, mapping postgres error codes into SqlError variants (auth, authorization, connection, constraint, deadlock, lock timeout, serialization, statement timeout, syntax). Adds LISTEN/NOTIFY helpers and a JSON fragment builder.

## Key Exports
- `PgClient` (tag, interface) — SqlClient + `json`, `listen`, `notify`
- `PgClientConfig` — `{ url, host, port, path, ssl, database, username, password, connectTimeout, applicationName, stream, types, transformJson, ... }`
- `PgPoolConfig` — extends with `idleTimeout`, `min/maxConnections`, `connectionTTL`
- `make(config)` — `Effect<PgClient, SqlError, Scope | Reactivity>`
- `fromPool(options)` — lower-level constructor from an existing `pg.Pool`
- `layer(config)` / `layerConfig(config)` — Layers
- `makeCompiler(transformQueryNames, transformJson?)` — PostgreSQL statement compiler
- `listen(channel)` — `Stream<string, SqlError>` over `LISTEN`
- `notify(channel, payload)` — `Effect<void, SqlError>` sending `NOTIFY`
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/pg/src/PgClient.ts`

## Related
- [[effect-pkg-sql-pg-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
