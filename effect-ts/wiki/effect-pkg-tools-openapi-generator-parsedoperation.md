---
title: ParsedOperation (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ParsedOperation (@effect/openapi-generator)

Type definitions for the intermediate representation produced after parsing an OpenAPI spec. Collects metadata, tags, security schemes, and per-operation parameter/body/response descriptors that transformers consume to emit code.

## Key Exports
- `ParsedOpenApi` — metadata, tags, security schemes, operations
- `ParsedOpenApiMetadata` — title, version, servers, license, descriptions
- `ParsedOpenApiTag` / `ParsedOpenApiSecurityScheme`
- `ParsedOperation` — id, method, path, params, payload, responses, sseSchema, binaryResponse
- `ParsedOperationParameter` / `ParsedOperationRequestBody`
- `ParsedOperationMediaTypeSchema` / `ParsedOperationMediaTypeEncoding`
- `ParsedOperationResponse`

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/ParsedOperation.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
