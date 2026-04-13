---
title: IndexedDbTable (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# IndexedDbTable (@effect/platform-browser)

Type-level description of an IndexedDB object store: name, row Schema, indexes, key path, autoIncrement flag, and transaction durability hint. Combined with `IndexedDbVersion` it defines the migration source of truth for the query builder.

## Key Exports
- `IndexedDbTable` — core interface with tableName, schemas, indexes, keyPath
- `AnySchemaStruct` — helper type (Schema.Top with fields)
- `Any` / `AnyWithProps` — existential helpers
- `TableName` / `TableSchema` / `KeyPath` / `AutoIncrement` — type accessors
- `make` — table constructor

## Source
- `raw/effect-smol/packages/platform-browser/src/IndexedDbTable.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-pkg-platform-browser-indexed-db-version]]
- [[effect-pkg-platform-browser-indexed-db-query-builder]]
