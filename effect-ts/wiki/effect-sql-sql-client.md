---
title: SqlClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlClient (unstable)

Core service abstraction for SQL databases. A `SqlClient` is a callable tagged-template `Statement.Constructor` augmented with transaction management, reactive queries, connection reservation, and transform toggling. Implementations (pg, mysql, sqlite, mssql, clickhouse) are built by passing acquirers and compilers to `make`.

## Key Exports
- `SqlClient` — Context service with `reserve`, `withTransaction`, `reactive`, `reactiveMailbox`, `safe`, `withoutTransforms`
- `SqlClient.MakeOptions` — acquirer, compiler, span attributes, begin/commit/rollback/savepoint overrides, row transformer, reactive queue
- `make` — build a `SqlClient` from `MakeOptions` (uses `Reactivity` service)
- `makeWithTransaction` — generic transaction wrapper with savepoint support
- `TransactionConnection` — service holding the active transaction connection + counter
- `onDialectOrElse` — dialect dispatch helper used throughout SQL family

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlClient.ts`

## Related
- [[effect-sql-statement]]
- [[effect-sql-sql-connection]]
