---
title: OpenApiTransformer (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenApiTransformer (@effect/openapi-generator)

Transformer that emits an HttpClient interface and its concrete implementation from a `ParsedOpenApi`. Generates operation methods including optional params/payload, SSE stream methods, binary response methods, and a tagged client error type.

## Key Exports
- `OpenApiTransformer` — Context service `{ imports, toTypes, toImplementation }`
- `makeTransformerSchema()` — schema-based transformer implementation
- `layerTransformerSchema` / `layerTransformerTs` — Layer variants (exported via OpenApiGenerator)

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/OpenApiTransformer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
- [[effect-pkg-tools-openapi-generator-parsedoperation]]
