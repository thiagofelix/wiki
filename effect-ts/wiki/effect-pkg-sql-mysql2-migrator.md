---
title: Effect Pkg Sql Mysql2 Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### MysqlMigrator (@effect/sql-mysql2)

Migrator wrapper for MySQL. Currently re-exports the core migrator with no dump-schema hook enabled (the mysqldump integration is commented out pending the platform `Command` module). Provides the standard `run`/`layer` helpers.

## Key Exports
- `run(options)` — execute migrations returning applied `[id, name]` pairs
- `layer(options)` — Layer applying migrations at startup
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/mysql2/src/MysqlMigrator.ts`

## Related
- [[effect-pkg-sql-mysql2-client]]
- [[effect-pkg-sql]]
- [[effect-sql]]
