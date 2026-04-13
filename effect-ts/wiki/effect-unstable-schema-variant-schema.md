---
title: VariantSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-unstable-schema]] [[effect-schema]]

# VariantSchema (unstable)

Primitive for building schemas that carry multiple variants (e.g. `select`, `insert`, `update`, `json`). A `VariantSchema.Struct` stores per-field variant configs; `extract` produces a regular `Schema.Struct` for a chosen variant with memoisation. Powers the higher-level `Model` module.

## Key Exports
- `TypeId` — brand for variant structs
- `make` — build a variant schema namespace given a list of variants and a default variant
- `Struct` — type of a variant-aware struct
- `Field` — type of a per-variant field with `schemas` config
- `isStruct` / `isField` — guards
- `ExtractFields` / `Extract` — type-level variant extraction helpers
- `extract` — pull out a single variant as a `Schema.Struct`
- `fields` — accessor for raw field map
- `Override` — brand marking a user-supplied override value

## Source
- `raw/effect-smol/packages/effect/src/unstable/schema/VariantSchema.ts`

## Related
- [[effect-schema]]
- [[effect-unstable-schema-model]]
