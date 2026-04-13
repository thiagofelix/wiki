---
title: Effect Pkg Sql Mssql Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### MssqlClient (@effect/sql-mssql)

SqlClient for Microsoft SQL Server using the `tedious` driver. Uses an Effect `Pool` of Tedious connections and maps mssql error numbers into SqlError variants (connection, authentication, authorization, constraint, deadlock, serialization, lock timeout, syntax). Exposes a `call` method for invoking typed stored procedures via the companion `Procedure` module, along with a custom `param` helper that produces Tedious `DataType`-typed fragments.

## Key Exports
- `MssqlClient` (tag, interface) — SqlClient + `param`, `call`
- `MssqlClientConfig` — `{ server, port, database, username, password, authType, domain, encrypt, trustServer, min/maxConnections, connectionTTL, parameterTypes, ... }`
- `make(config)` — `Effect<MssqlClient, SqlError, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `makeCompiler(transformQueryNames)` — MSSQL statement compiler
- `defaultParameterTypes` — default map from `PrimitiveKind` to Tedious `DataType`
- `TypeId` — symbol brand

## Source
- `raw/effect-smol/packages/sql/mssql/src/MssqlClient.ts`

## Related
- [[effect-pkg-sql-mssql-parameter]]
- [[effect-pkg-sql-mssql-procedure]]
- [[effect-pkg-sql-mssql-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
