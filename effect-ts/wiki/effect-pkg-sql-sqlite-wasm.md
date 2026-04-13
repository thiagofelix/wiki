---
title: Effect Pkg Sql Sqlite Wasm
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### @effect/sql-sqlite-wasm (hub)

Browser SQLite driver built on `@effect/wa-sqlite`. Unlike the other sqlite subpackages this one ships two client modes (in-thread MemoryVFS and worker-backed OPFS AccessHandlePoolVFS) plus a standalone worker entrypoint to host the OPFS database and a small internal protocol module shared between client and worker.

## Modules
- [[effect-pkg-sql-sqlite-wasm-client]] — `SqliteClient` with `makeMemory` and `make` (worker) constructors
- [[effect-pkg-sql-sqlite-wasm-opfs-worker]] — `OpfsWorker` script hosting the OPFS database
- [[effect-pkg-sql-sqlite-wasm-migrator]] — `run`/`layer` migrator wrapper
- [[effect-pkg-sql-sqlite-wasm-internal]] — shared `OpfsWorkerMessage` protocol type

## Source
- `raw/effect-smol/packages/sql/sqlite-wasm/`

## Related
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
