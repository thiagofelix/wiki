---
title: IndexedDbQueryBuilder (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# IndexedDbQueryBuilder (@effect/platform-browser)

Fluent query builder for IndexedDB tables. Supports select/insert/update/delete over declared tables, schema-driven decode/encode of rows, index-based lookups, `withTransaction` composition and reactivity integration so mutations invalidate readers.

## Key Exports
- `IndexedDbQueryBuilder` — builder interface with `from`, `use`, `clearAll`, `withTransaction`
- `IndexedDbQueryError` — tagged error (NotFoundError, DecodeError, etc.)
- `IndexedDbQuery` — namespace of From/Select/Insert/Update/Delete types
- `makeProto` — internal constructor shared with IndexedDbDatabase

## Source
- `raw/effect-smol/packages/platform-browser/src/IndexedDbQueryBuilder.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-pkg-platform-browser-indexed-db-database]]
- [[effect-pkg-platform-browser-indexed-db-table]]
