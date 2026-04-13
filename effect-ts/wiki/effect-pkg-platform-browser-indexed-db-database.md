---
title: IndexedDbDatabase (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# IndexedDbDatabase (@effect/platform-browser)

Represents an opened IndexedDB database plus its schema, migration chain and rebuild capability. Exposes the `IndexedDbSchema` type with typed migrations, layer construction bound to a database name, and a `Transaction` view over the query builder.

## Key Exports
- `IndexedDbDatabase` — Context.Service carrying the live `IDBDatabase`
- `IndexedDbDatabaseError` — tagged error with TransactionError/OpenError/etc reasons
- `IndexedDbSchema` — versioned schema type with `add`, `migrate`, `layer`
- `Transaction` — transactional query builder view
- `make` / `makeSchema` — schema constructors over `IndexedDbVersion`

## Source
- `raw/effect-smol/packages/platform-browser/src/IndexedDbDatabase.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-pkg-platform-browser-indexed-db]]
- [[effect-pkg-platform-browser-indexed-db-query-builder]]
