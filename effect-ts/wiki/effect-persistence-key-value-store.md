---
title: KeyValueStore (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# KeyValueStore (unstable)

Simple string/binary key-value service abstraction with multiple backends. Supports `get`, `set`, `remove`, `clear`, `size`, `has`, `isEmpty`, `modify`, and typed sub-stores via schemas. Backends include in-memory, filesystem, SQL, and layer-composable custom stores.

## Key Exports
- `KeyValueStore` — Context service interface with string/Uint8Array operations
- `make` — build a store from a `MakeOptions` partial implementation, filling in defaults
- `makeStringOnly` — build a string-only store from a minimal `MakeStringOptions`
- `prefix` — derive a sub-store with prefixed keys
- `layerMemory` — in-memory layer
- `layerFileSystem` — filesystem-backed layer using `FileSystem` service
- `layerSql` — SQL-backed layer (uses `SqlClient`)
- `KeyValueStoreError` — tagged error for store failures
- `SchemaStore` — typed store view decoding/encoding values via a `Schema`

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/KeyValueStore.ts`

## Related
- [[effect-persistence-persistence]]
- [[effect-sql-sql-client]]
