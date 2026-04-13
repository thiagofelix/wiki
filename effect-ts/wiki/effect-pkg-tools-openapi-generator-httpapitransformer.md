---
title: HttpApiTransformer (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiTransformer (@effect/openapi-generator)

Transformer that renders a parsed OpenAPI document into `HttpApi`/`HttpApiGroup`/`HttpApiEndpoint` class declarations from `effect/unstable/httpapi`. Groups operations by tag, emits security middleware declarations, and wires API-level annotations.

## Key Exports
- `imports` — produces import statements for the generated module
- `toImplementation` — renders the `HttpApi` class and group classes for a `ParsedOpenApi`
- Internal `GroupRenderModel` / `SecurityRenderModel` types

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/HttpApiTransformer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
- [[effect-pkg-tools-openapi-generator-parsedoperation]]
