---
title: Effect Pkg Sql Pg Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### PgMigrator (@effect/sql-pg)

Postgres migrator built on `effect/unstable/sql/Migrator` with a custom `dumpSchema` implementation that shells out to `pg_dump` via `effect/unstable/process/ChildProcess`, using the active `PgClient` config for host/port/user/password/database/ssl env vars and stripping `SET`/comment lines.

## Key Exports
- `run(options)` — execute migrations, returns applied `[id, name]`
- `layer(options)` — Layer applying migrations at startup; requires `PgClient`, `ChildProcessSpawner`, `FileSystem`, `Path`
- Re-exports all of `effect/unstable/sql/Migrator`

## Source
- `raw/effect-smol/packages/sql/pg/src/PgMigrator.ts`

## Related
- [[effect-pkg-sql-pg-client]]
- [[effect-pkg-sql]]
- [[effect-sql]]
