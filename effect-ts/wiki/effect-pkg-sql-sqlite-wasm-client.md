---
title: Effect Pkg Sql Sqlite Wasm Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteClient (@effect/sql-sqlite-wasm)

Browser SqlClient built on `@effect/wa-sqlite` offering two modes: `makeMemory` runs SQLite in the main thread using the MemoryVFS, while `make` delegates to a Worker/SharedWorker/MessagePort running the OPFS-backed `AccessHandlePoolVFS` via the companion `OpfsWorker` script. Both expose `export`/`import` for database serialization and optionally install Reactivity update hooks that invalidate table keys on writes.

## Key Exports
- `SqliteClient` (tag, interface) — SqlClient + `export`, `import`
- `SqliteClientMemoryConfig` — in-thread config `{ installReactivityHooks, transformResultNames, transformQueryNames, spanAttributes }`
- `SqliteClientConfig` — worker-mode config adding `worker: Effect<Worker | SharedWorker | MessagePort, never, Scope>`
- `makeMemory(config)` — in-thread constructor using MemoryVFS
- `make(config)` — worker-backed constructor using OPFS
- `layerMemory(config)` / `layerMemoryConfig(config)` — Layers for in-thread mode
- `layer(config)` / `layerConfig(config)` — Layers for worker mode
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/sqlite-wasm/src/SqliteClient.ts`

## Related
- [[effect-pkg-sql-sqlite-wasm-opfs-worker]]
- [[effect-pkg-sql-sqlite-wasm-internal]]
- [[effect-pkg-sql-sqlite-wasm-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
