---
title: OpenApiPatch (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenApiPatch (@effect/openapi-generator)

Utilities for parsing and applying JSON Patch (RFC 6902) documents against OpenAPI specs prior to code generation. Accepts patches from JSON/YAML files or inline JSON array strings, validates them against a schema, then applies them via `effect/JsonPatch`.

## Key Exports
- `parsePatchInput(input)` — detects file vs inline and decodes the patch
- `applyPatches(parsed, spec)` — applies a list of named patches
- `JsonPatchParseError` — error for read/parse failures
- `JsonPatchValidationError` — error for schema-invalid patches

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/OpenApiPatch.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
