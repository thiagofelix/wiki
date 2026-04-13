---
title: IndexedDbVersion (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# IndexedDbVersion (@effect/platform-browser)

A versioned bundle of `IndexedDbTable`s that forms a single database schema version. Instances are used as the endpoints of migration chains defined on `IndexedDbSchema`.

## Key Exports
- `IndexedDbVersion` — interface holding a ReadonlyMap of tables
- `Any` / `AnyWithProps` — existential helpers
- `Tables` / `TableWithName` / `SchemaWithName` — type-level accessors
- `make` — build a version from a non-empty list of tables

## Source
- `raw/effect-smol/packages/platform-browser/src/IndexedDbVersion.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-pkg-platform-browser-indexed-db-table]]
- [[effect-pkg-platform-browser-indexed-db-database]]
