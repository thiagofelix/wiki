---
title: Migrator (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# Migrator (unstable)

Runs SQL migrations against a `SqlClient`, tracking applied versions in a dedicated migrations table (default `effect_sql_migrations`). Dialect-aware DDL, exclusive locking (Postgres), and pluggable loaders that produce `ResolvedMigration` tuples from files or modules.

## Key Exports
- `make` — construct a migrator factory given a `dumpSchema` function, returning a runner that takes `MigratorOptions`
- `MigratorOptions` — config with `loader`, optional `schemaDirectory` and `table`
- `Loader` — Effect producing an array of `ResolvedMigration`
- `ResolvedMigration` — `[id, name, loadEffect]` tuple
- `Migration` — record for applied migrations with id, name, createdAt
- `MigrationError` — tagged error with kinds `BadState`, `ImportError`, `Failed`, `Duplicates`, `Locked`

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/Migrator.ts`

## Related
- [[effect-sql-sql-client]]
- [[effect-sql-sql-error]]
