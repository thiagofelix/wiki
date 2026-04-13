---
title: SqlModel (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlModel (unstable)

Builds simple CRUD repositories from a `unstable/schema/Model`. Given a table name, span prefix, and id column, emits typed `insert`, `update`, `findById`, `delete` (and `*Void` variants) that use the Model's `insert`, `update`, `select`, and field schemas for validation and encoding.

## Key Exports
- `makeRepository` — construct a CRUD repository effect from a `Model` class with `tableName`, `spanPrefix`, `idColumn`
- Repository `insert` / `insertVoid` — insert a row via the Model's insert variant, optionally returning the selected row
- Repository `update` / `updateVoid` — update by id using the Model's update variant
- Repository `findById` — fetch a single row by id, failing with `NoSuchElementError`
- Repository `delete` — delete a row by id

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlModel.ts`

## Related
- [[effect-unstable-schema-model]]
- [[effect-sql-sql-schema]]
