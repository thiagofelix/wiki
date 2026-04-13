---
title: Effect Pkg Sql Sqlite Wasm Opfs Worker
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### OpfsWorker (@effect/sql-sqlite-wasm)

Worker-side runtime for the OPFS-backed sqlite-wasm client. Boots `@effect/wa-sqlite` with the `AccessHandlePoolVFS`, opens the configured database, and serves a message protocol used by `SqliteClient.make`: query execution, import/export (serialize/deserialize), update hooks, and close. Designed to be invoked from a `Worker`, `SharedWorker`, or `MessagePort`.

## Key Exports
- `OpfsWorkerConfig` — `{ port: EventTarget & Pick<MessagePort, "postMessage" | "close">, dbName: string }`
- `run(options)` — `Effect<void, SqlError>` that wires up the message handler and keeps the worker alive until `close`

## Protocol (internal)
- `[id, sql, params]` — execute query, replies `[id, error, [columns, rows]]`
- `["import", id, data]` / `["export", id]` — serialize roundtrip
- `["update_hook"]` — enable row-change notifications
- `["close"]` — shut down

## Source
- `raw/effect-smol/packages/sql/sqlite-wasm/src/OpfsWorker.ts`

## Related
- [[effect-pkg-sql-sqlite-wasm-client]]
- [[effect-pkg-sql-sqlite-wasm-internal]]
- [[effect-pkg-sql]]
