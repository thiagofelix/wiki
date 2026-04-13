---
title: Effect Pkg Sql Mssql Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### MssqlMigrator (@effect/sql-mssql)

Migrator wrapper for MSSQL; re-exports the core migrator module and provides the standard `run`/`layer` helpers.

## Key Exports
- `run(options)` — execute migrations, returns list of applied `[id, name]`
- `layer(options)` — Layer applying migrations at startup
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/mssql/src/MssqlMigrator.ts`

## Related
- [[effect-pkg-sql-mssql-client]]
- [[effect-pkg-sql]]
- [[effect-sql]]
