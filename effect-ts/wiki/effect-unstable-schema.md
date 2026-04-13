---
title: Effect Unstable Schema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-schema]]

# Effect Unstable Schema (unstable)

Hub for the `effect/unstable/schema` subsystem. Builds on top of core [[effect-schema]] to add per-variant schemas — one declaration that produces distinct schemas for database selects, inserts, updates, and JSON wire variants. The `Model` module is the ergonomic face used by `SqlModel` repositories; `VariantSchema` is the low-level primitive.

## Modules
- [[effect-unstable-schema-model]] — domain model classes with `select`, `insert`, `update`, `json`, `jsonCreate`, `jsonUpdate` variants
- [[effect-unstable-schema-variant-schema]] — low-level multi-variant schema primitive powering `Model`

## Source
- `raw/effect-smol/packages/effect/src/unstable/schema/`

## Related
- [[effect-schema]]
- [[effect-sql]]
- [[effect-sql-sql-model]]
