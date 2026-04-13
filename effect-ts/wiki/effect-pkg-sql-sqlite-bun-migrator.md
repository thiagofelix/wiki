---
title: Effect Pkg Sql Sqlite Bun Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteMigrator (@effect/sql-sqlite-bun)

Migrator wrapper for the Bun sqlite client. Re-exports the core migrator with no custom schema dump (a sqlite3-based dumper is stubbed in comments pending the platform `Command` module).

## Key Exports
- `run(options)` — execute migrations
- `layer(options)` — Layer applying migrations at startup
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/sqlite-bun/src/SqliteMigrator.ts`

## Related
- [[effect-pkg-sql-sqlite-bun-client]]
- [[effect-pkg-sql]]
