---
title: Effect Pkg Sql Libsql Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### LibsqlMigrator (@effect/sql-libsql)

Migrator wrapper for libsql. Re-exports the core `effect/unstable/sql/Migrator` and provides preconfigured `run`/`layer` helpers. No custom schema dump logic.

## Key Exports
- `run(options)` — execute migrations
- `layer(options)` — Layer that applies migrations at startup
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/libsql/src/LibsqlMigrator.ts`

## Related
- [[effect-pkg-sql-libsql-client]]
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
