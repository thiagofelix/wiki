---
title: Effect Pkg Sql Mysql2 Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### MysqlClient (@effect/sql-mysql2)

SqlClient for MySQL/MariaDB using the `mysql2` driver with its connection pool. Maps mysql errno values into SqlError subclasses (connection, auth, authorization, syntax, constraint, deadlock, lock timeout, statement timeout). Streaming is powered by the shared `asyncPauseResume` helper from `effect/unstable/sql/SqlStream`.

## Key Exports
- `MysqlClient` (tag, interface) — SqlClient specialization
- `MysqlClientConfig` — `{ url, host, port, database, username, password, maxConnections, connectionTTL, poolConfig, transformResultNames, transformQueryNames, spanAttributes }`
- `make(config)` — `Effect<MysqlClient, SqlError, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `makeCompiler(transformQueryNames)` — MySQL compiler
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/mysql2/src/MysqlClient.ts`

## Related
- [[effect-pkg-sql-mysql2-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
