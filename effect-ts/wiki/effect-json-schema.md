---
title: JsonSchema
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# JsonSchema

`JsonSchema` converts JSON Schema documents between dialects — Draft-07, Draft 2020-12, OpenAPI 3.1, and OpenAPI 3.0. Every input dialect is first normalized to an internal `Document<"draft-2020-12">` representation, after which it can be optionally converted to any supported output dialect. The module is the JSON Schema side of Effect's schema tooling: `Schema.toJsonSchemaDocument` and `SchemaRepresentation.toJsonSchemaDocument` both emit values handled by this module.

## Mental Model
- `JsonSchema` is an open record (`[x: string]: unknown`) representing a single node.
- `Document<D>` pairs a root `schema`, a `definitions` map, and the target `dialect`; `MultiDocument<D>` carries multiple roots sharing one definitions pool.
- Definitions live under different ref prefixes per dialect (`$defs`, `definitions`, `components/schemas`).

## Key Exports
- `JsonSchema`, `Dialect`, `Type`, `Definitions` — core types
- `Document`, `MultiDocument` — container types
- `fromSchemaDraft07`, `fromSchemaDraft2020_12`, `fromSchemaOpenApi3_1`, `fromSchemaOpenApi3_0` — normalize to canonical form
- `toDocumentDraft07`, `toDocumentDraft2020_12`, `toDocumentOpenApi3_1`, `toDocumentOpenApi3_0` — convert to output dialects
- `toMultiDocumentDraft07`, `toMultiDocumentOpenApi3_1`, `toMultiDocumentOpenApi3_0` — multi-root equivalents
- `resolve$ref`, `resolveTopLevel$ref` — reference resolution
- `META_SCHEMA_URI_DRAFT_07` — dialect meta-schema URI constant

## Gotchas
- Unsupported keywords are silently dropped during conversion.
- Draft-07 tuple syntax (`items` array + `additionalItems`) is converted to/from 2020-12 (`prefixItems` + `items`).
- OpenAPI 3.0 `nullable: true` is expanded to `type` arrays or `anyOf`.
- `resolve$ref` only matches the last path segment against definitions.

## Source
- `raw/effect-smol/packages/effect/src/JsonSchema.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-representation]]
- [[effect-json-pointer]]
