---
title: Effect Pkg Sql Sqlite Wasm Internal
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### Internal (@effect/sql-sqlite-wasm)

Aggregated notes on `packages/sql/sqlite-wasm/src/internal/`, currently containing only the shared worker message protocol type.

## Contents
- `opfsWorker.ts` — defines `OpfsWorkerMessage`, the tagged-tuple union exchanged between `SqliteClient` and the `OpfsWorker` script: `[id, sql, params] | ["import", id, data] | ["export", id] | ["update_hook"] | ["close"]`. Imported as a type from both the client and worker entrypoints.

## Source
- `raw/effect-smol/packages/sql/sqlite-wasm/src/internal/opfsWorker.ts`

## Related
- [[effect-pkg-sql-sqlite-wasm-client]]
- [[effect-pkg-sql-sqlite-wasm-opfs-worker]]
- [[effect-pkg-sql]]
