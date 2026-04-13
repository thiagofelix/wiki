---
title: Effect Pkg Sql Mssql Procedure
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### Procedure (@effect/sql-mssql)

Builder for typed MSSQL stored procedure calls. Starts from `make(name)` and accretes input/output parameters via `param` and `outputParam`. `withRows` narrows the expected row type, `compile` binds actual input values to produce a `ProcedureWithValues` that `MssqlClient.call` executes, returning `{ output, rows }`.

## Key Exports
- `Procedure<I, O, A>` — pipeable procedure model with `name`, `params`, `outputParams`
- `ProcedureWithValues<I, O, A>` — `Procedure` bound with input `values`
- `Procedure.ParametersRecord<A>` — mapped type extracting value types from param records
- `Procedure.Result<O, A>` — `{ output, rows }` shape
- `make(name)` — empty procedure builder
- `param<A>()(name, type, options?)` — add an input parameter
- `outputParam<A>()(name, type, options?)` — add an output parameter
- `withRows<A>()` — type-only annotation for row shape
- `compile(self)(values)` — bind input values producing `ProcedureWithValues`
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/mssql/src/Procedure.ts`

## Related
- [[effect-pkg-sql-mssql-parameter]]
- [[effect-pkg-sql-mssql-client]]
- [[effect-pkg-sql]]
