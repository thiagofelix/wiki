---
title: Effect Pkg Sql Mssql
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### @effect/sql-mssql (hub)

MSSQL driver for Effect's SQL subsystem, built on `tedious`. Compared to other drivers this subpackage ships extra primitives for typed stored procedures: `Parameter` for declaring typed input/output slots and `Procedure` for composing them into a call-site contract consumed by `MssqlClient.call`. The client itself uses a pooled Tedious connection with comprehensive mssql error-number classification.

## Modules
- [[effect-pkg-sql-mssql-client]] — `MssqlClient`, pool, compiler, layers
- [[effect-pkg-sql-mssql-parameter]] — typed `Parameter<A>` model and constructor
- [[effect-pkg-sql-mssql-procedure]] — typed stored procedure builder
- [[effect-pkg-sql-mssql-migrator]] — `run`/`layer` wrapper over the core migrator

## Source
- `raw/effect-smol/packages/sql/mssql/`

## Related
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
