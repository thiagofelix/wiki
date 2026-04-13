---
title: Effect Pkg Sql
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### packages/sql (hub)

The `packages/sql` subtree of effect-smol contains driver-specific SqlClient implementations that layer on top of the in-core `effect/unstable/sql` subsystem ([[effect-sql]]). Each subpackage adapts a third-party driver to produce an `Effect<SqlClient>` with a matching `Layer`, reuses the shared `Statement` compiler/error types, and typically ships a companion `Migrator` module that thin-wraps `effect/unstable/sql/Migrator`. There is no top-level `@effect/sql` package in this subtree — that lives in core.

## Subpackages
- [[effect-pkg-sql-clickhouse-client]] / [[effect-pkg-sql-clickhouse-migrator]] — `@effect/sql-clickhouse` over `@clickhouse/client`
- [[effect-pkg-sql-d1-client]] — `@effect/sql-d1` for Cloudflare D1 (Workers)
- [[effect-pkg-sql-libsql-client]] / [[effect-pkg-sql-libsql-migrator]] — `@effect/sql-libsql` over `@libsql/client`
- [[effect-pkg-sql-mssql]] hub — `@effect/sql-mssql` over `tedious` (client, parameter, procedure, migrator)
- [[effect-pkg-sql-mysql2-client]] / [[effect-pkg-sql-mysql2-migrator]] — `@effect/sql-mysql2` over `mysql2`
- [[effect-pkg-sql-pg-client]] / [[effect-pkg-sql-pg-migrator]] — `@effect/sql-pg` over `pg` + `pg-cursor`
- [[effect-pkg-sql-sqlite-bun-client]] / [[effect-pkg-sql-sqlite-bun-migrator]] — `bun:sqlite`
- [[effect-pkg-sql-sqlite-do-client]] / [[effect-pkg-sql-sqlite-do-migrator]] — Cloudflare Durable Object SQL storage
- [[effect-pkg-sql-sqlite-node-client]] / [[effect-pkg-sql-sqlite-node-migrator]] — `better-sqlite3`
- [[effect-pkg-sql-sqlite-react-native-client]] / [[effect-pkg-sql-sqlite-react-native-migrator]] — `@op-engineering/op-sqlite`
- [[effect-pkg-sql-sqlite-wasm]] hub — `@effect/wa-sqlite` (memory + OPFS worker + migrator + internal)

## Common patterns
- Each client exports `TypeId`, a Context tag, a config interface, `make`, and `layer`/`layerConfig`
- Drivers share `classifySqliteError` (sqlite family) or a per-driver error-code table
- Each migrator re-exports `effect/unstable/sql/Migrator` plus preconfigured `run`/`layer`; only `pg` ships a real `dumpSchema`

## Source
- `raw/effect-smol/packages/sql/`

## Related
- [[effect-sql]] — the in-core `effect/unstable/sql` subsystem these drivers build on
- [[effect-ts-v4]]
- [[effect-related]]
