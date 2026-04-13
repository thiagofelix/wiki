---
title: Effect Pkg Sql Mssql Parameter
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### Parameter (@effect/sql-mssql)

Typed parameter descriptor for MSSQL stored procedure inputs and outputs. A `Parameter<A>` bundles a name, a Tedious `DataType`, and optional `ParameterOptions`, phantom-typed by its TypeScript representation so callers get end-to-end typing when defining procedures.

## Key Exports
- `Parameter<A>` — model interface with `_tag`, `name`, `type`, `options`
- `make(name, type, options?)` — constructor producing a `Parameter<A>`
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/mssql/src/Parameter.ts`

## Related
- [[effect-pkg-sql-mssql-procedure]]
- [[effect-pkg-sql-mssql-client]]
- [[effect-pkg-sql]]
