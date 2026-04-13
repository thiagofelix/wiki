---
title: JsonSchemaGenerator (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# JsonSchemaGenerator (@effect/openapi-generator)

Low-level engine that converts a JSON Schema `components` map (OpenAPI 3.0 or 3.1) into Effect `Schema.*` TypeScript source. Handles recursive references with forward-referenced declarations, optional type-only output, and schema-node rewriting via an `onEnter` hook.

## Key Exports
- `make()` — creates a generator instance with an internal schema store
- `generate(source, components, typeOnly, options?)` — renders non-recursive and recursive definitions
- `generateHttpApi(...)` — variant emitting types for use inside HttpApi groups
- `addSchema(name, schema)` — register additional schemas

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/JsonSchemaGenerator.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
