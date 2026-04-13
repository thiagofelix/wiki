---
title: Effect Pkg Sql Clickhouse Migrator
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### ClickhouseMigrator (@effect/sql-clickhouse)

Thin wrapper over the core `effect/unstable/sql/Migrator` configured for ClickHouse. Re-exports the migrator module and provides `run` plus a `layer` that runs migrations against any `SqlClient`. No ClickHouse-specific dump support is enabled.

## Key Exports
- `run(options)` — execute migrations, returns the applied ids/names
- `layer(options)` — Layer that runs migrations at startup
- Re-exports everything from `effect/unstable/sql/Migrator` (e.g. `Migration`, `MigratorOptions`, `MigrationError`)

## Source
- `raw/effect-smol/packages/sql/clickhouse/src/ClickhouseMigrator.ts`

## Related
- [[effect-pkg-sql-clickhouse-client]]
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
