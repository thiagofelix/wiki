---
title: OpenApi (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenApi (unstable)

Produces an OpenAPI 3.1 specification from an `HttpApi` definition. Walks groups and endpoints, converts Schemas to JSON Schema via `JsonSchema`/`SchemaRepresentation`, reads `HttpApiSchema` annotations for status and encoding, and emits metadata tags (title, version, description, license, servers, external docs) supplied via Context Services.

## Key Exports
- `fromApi` — build an OpenAPI spec object from an `HttpApi`
- `Identifier` / `Title` / `Version` / `Description` / `License` / `ExternalDocs` / `Servers` — Context Services for top-level metadata
- `Format` / `Summary` — Context Services for endpoint metadata
- `OpenAPISpecLicense` / `OpenAPISpecServer` / `OpenAPISpecExternalDocs` — OpenAPI types

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/OpenApi.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api-scalar]]
- [[effect-httpapi-http-api-swagger]]
- [[effect-json-schema]]
