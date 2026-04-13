---
title: SqlConnection (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlConnection (unstable)

Low-level database connection contract that SQL drivers implement. A `Connection` exposes prepared, raw, unprepared, streaming, and values-only execute operations plus a scoped `Acquirer` type. Used internally by `SqlClient` to dispatch statements.

## Key Exports
- `Connection` — interface with `execute`, `executeRaw`, `executeStream`, `executeValues`, `executeUnprepared`
- `Connection` (tag) — Context service key for the current connection
- `Acquirer` — `Effect<Connection, SqlError, Scope>` type alias used by driver layers
- `Row` — `{ [column: string]: unknown }` type alias

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlConnection.ts`

## Related
- [[effect-sql-sql-client]]
- [[effect-sql-sql-error]]
