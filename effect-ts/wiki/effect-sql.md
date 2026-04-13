---
title: Effect SQL (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]]

# Effect SQL (unstable)

Hub for the `effect/unstable/sql` subsystem: a driver-agnostic SQL toolkit built around a tagged-template DSL. `Statement` compiles fragments to `[sql, params]`; `SqlClient` runs them against a `SqlConnection`, adding transactions, reactive queries, and span instrumentation. `SqlSchema` and `SqlResolver` wrap queries in schema-validated single-shot or batched executions, while `SqlModel` derives CRUD repositories from [[effect-unstable-schema-model]]. `Migrator` applies versioned migrations per dialect.

## Modules
- [[effect-sql-statement]] — tagged-template DSL, compilers, fragments, transformers
- [[effect-sql-sql-client]] — Context service, transactions, reactive queries
- [[effect-sql-sql-connection]] — low-level driver connection contract
- [[effect-sql-sql-error]] — schema-tagged error hierarchy with retryability flags
- [[effect-sql-sql-schema]] — one-shot schema-validated query constructors
- [[effect-sql-sql-resolver]] — batched `RequestResolver`s for SQL queries
- [[effect-sql-sql-stream]] — pause/resume stream helpers for cursor drivers
- [[effect-sql-sql-model]] — CRUD repository factory over `Model`
- [[effect-sql-migrator]] — dialect-aware migration runner

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/`

## Related
- [[effect-unstable-schema]]
- [[effect-persistence]]
- [[effect-schema]]
