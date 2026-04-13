---
title: Effect Pkg Sql Libsql Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### LibsqlClient (@effect/sql-libsql)

SqlClient backed by the `@libsql/client` driver (supports local file, remote libsql, HTTP, WebSocket, and embedded-replica URLs). Handles sqlite error classification via the shared `classifySqliteError` helper, and uses a semaphore-guarded connection plus a custom transaction tracker tagged under a dedicated context key.

## Key Exports
- `LibsqlClient` (tag, interface) — SqlClient specialization
- `LibsqlClientConfig` — union of `Full` and `Live` configs
- `LibsqlClientConfig.Full` — `{ url, authToken, encryptionKey, syncUrl, syncInterval, tls, intMode, concurrency, ... }`
- `LibsqlClientConfig.Live` — wraps an already-constructed `@libsql/client` instance
- `make(config)` — constructor `Effect<LibsqlClient, never, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/libsql/src/LibsqlClient.ts`

## Related
- [[effect-pkg-sql-libsql-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
