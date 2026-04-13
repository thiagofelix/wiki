---
title: Effect Pkg Sql Sqlite React Native Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### SqliteClient (@effect/sql-sqlite-react-native)

SqlClient for React Native using `@op-engineering/op-sqlite`. Supports sync and async query modes: callers can opt into async execution per-effect via `withAsyncQuery`, controlled by the `AsyncQuery` context reference. Encryption keys and custom file locations are configurable.

## Key Exports
- `SqliteClient` (tag, interface) — SqlClient specialization
- `SqliteClientConfig` — `{ filename, location, encryptionKey, transformResultNames, transformQueryNames, spanAttributes }`
- `AsyncQuery` — `Context.Reference<boolean>` fiber ref toggling async execution
- `withAsyncQuery(effect)` — run an effect under async query mode
- `make(config)` — `Effect<SqliteClient, never, Scope | Reactivity>`
- `layer(config)` / `layerConfig(config)` — Layers
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/sqlite-react-native/src/SqliteClient.ts`

## Related
- [[effect-pkg-sql-sqlite-react-native-migrator]]
- [[effect-pkg-sql]]
- [[effect-sql]]
