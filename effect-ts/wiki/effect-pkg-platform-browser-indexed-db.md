---
title: IndexedDb (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# IndexedDb (@effect/platform-browser)

Core service tag that represents access to `globalThis.indexedDB` and `IDBKeyRange`. Consumers depend on this service to open databases; the provided layer reads the factories from `window` and fails with a ConfigError when unavailable.

## Key Exports
- `IndexedDb` — Context.Service tag holding `indexedDB` and `IDBKeyRange`
- `IDBValidKey` — Schema for IndexedDB valid keys
- `AutoIncrement` — Schema for autoIncrement key paths
- `make` — constructor accepting a bare implementation
- `layerWindow` — layer reading `window.indexedDB`

## Source
- `raw/effect-smol/packages/platform-browser/src/IndexedDb.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-pkg-platform-browser-indexed-db-database]]
