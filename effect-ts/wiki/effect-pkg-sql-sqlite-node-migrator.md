---
title: Effect Pkg Sql Sqlite Node Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteMigrator (@effect/sql-sqlite-node)

Migrator wrapper for the Node (better-sqlite3) client. Re-exports the core migrator (a sqlite3 CLI-based dumper is stubbed in comments pending the platform `Command` module).

## Key Exports
- `run(options)` — execute migrations
- `layer(options)` — Layer applying migrations at startup
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/sqlite-node/src/SqliteMigrator.ts`

## Related
- [[effect-pkg-sql-sqlite-node-client]]
- [[effect-pkg-sql]]
