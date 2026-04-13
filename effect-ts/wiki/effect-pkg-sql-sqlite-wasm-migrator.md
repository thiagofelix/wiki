---
title: Effect Pkg Sql Sqlite Wasm Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteMigrator (@effect/sql-sqlite-wasm)

Migrator wrapper for the WASM sqlite client; re-exports the core migrator.

## Key Exports
- `run(options)` — execute migrations
- `layer(options)` — Layer applying migrations at startup
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/sqlite-wasm/src/SqliteMigrator.ts`

## Related
- [[effect-pkg-sql-sqlite-wasm-client]]
- [[effect-pkg-sql]]
