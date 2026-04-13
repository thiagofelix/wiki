---
title: Effect Pkg Sql Clickhouse Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### ClickhouseClient (@effect/sql-clickhouse)

An Effect SqlClient implementation for ClickHouse built on `@clickhouse/client`. Extends the base SqlClient with ClickHouse-specific features: typed query parameters, `insertQuery` for streaming inserts, query-id tagging, per-effect setting overrides, and stream-based result iteration. Errors from the underlying driver are classified into SqlError variants (auth, syntax, timeout, connection).

## Key Exports
- `ClickhouseClient` (tag, interface) — SqlClient + Clickhouse extensions
- `ClickhouseClientConfig` — connection/auth/HTTP options
- `make` — constructor returning `Effect<ClickhouseClient, SqlError, Scope | Reactivity>`
- `layer` — live Layer from a static config
- `layerConfig` — live Layer from `Config.Wrap`
- `param(dataType, value)` — typed parameter fragment
- `asCommand` — execute effect as a command (no result rows)
- `insertQuery({ table, values, format })` — bulk insert helper
- `withQueryId(queryId)` — tag effect with ClickHouse query id
- `withClickhouseSettings(settings)` — override session settings
- `TypeId` — branded identifier

## Source
- `raw/effect-smol/packages/sql/clickhouse/src/ClickhouseClient.ts`

## Related
- [[effect-pkg-sql]]
- [[effect-pkg-sql-clickhouse-migrator]]
- [[effect-sql]]
- [[effect-ts-v4]]
