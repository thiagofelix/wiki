---
title: SchemaRepresentation
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaRepresentation

`SchemaRepresentation` is a serializable intermediate representation (IR) that sits between Effect's internal `SchemaAST` and external formats like JSON Schema, generated TypeScript code, and serialized JSON. A `Representation` is a tagged union describing primitives, literals, objects, arrays, unions, declarations, references, and suspensions in a form that can be round-tripped through JSON. A `Document` pairs a representation with a named `references` map (analogous to JSON Schema `$defs`).

## Mental Model
- `fromAST` / `fromASTs` lower a `SchemaAST` node into a `Document` / `MultiDocument`.
- `toSchema` reconstructs a runtime `Schema` from a document, using a `Reviver` for custom types.
- `toJsonSchemaDocument` / `fromJsonSchemaDocument` bridge to the `JsonSchema` module.
- `toCodeDocument` emits TypeScript source strings for schemas and their types.

## Key Exports
- `Representation` — the core tagged union
- `Document`, `MultiDocument`, `References` — containers and reference maps
- `Declaration`, `Reference`, `Suspend`, `Null`, `Undefined`, `Void` — variants
- `StringMeta`, `NumberMeta`, `ArraysMeta`, `DeclarationMeta` — typed check metadata
- `Check`, `Filter`, `FilterGroup` — validation constraints on representations
- `fromAST`, `fromASTs` — build documents from AST
- `toSchema`, `toSchemaDefaultReviver` — reconstruct runtime schemas
- `toJsonSchemaDocument`, `toJsonSchemaMultiDocument` — emit JSON Schema
- `fromJsonSchemaDocument`, `fromJsonSchemaMultiDocument` — parse JSON Schema
- `toCodeDocument` — generate TypeScript source
- `toMultiDocument`, `DocumentFromJson`, `MultiDocumentFromJson` — serialization codecs
- `$Representation`, `$Document`, `$MultiDocument` — Schema codecs for the IR itself

## Source
- `raw/effect-smol/packages/effect/src/SchemaRepresentation.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-ast]]
- [[effect-json-schema]]
