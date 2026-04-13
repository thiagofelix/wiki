---
title: OpenApiGenerator (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenApiGenerator (@effect/openapi-generator)

Primary service entry point that takes an `OpenAPISpec` (Swagger 2 or OpenAPI 3.x) and emits TypeScript source in one of three formats: `httpclient`, `httpclient-type-only`, or `httpapi`. Orchestrates Swagger conversion, operation parsing, and delegates rendering to `HttpApiTransformer` or `OpenApiTransformer`.

## Key Exports
- `OpenApiGenerator` — Context service `{ generate(spec, options) }`
- `OpenApiGeneratorFormat` — `"httpclient" | "httpclient-type-only" | "httpapi"`
- `OpenApiGenerateOptions` — name, format, onEnter hook, onWarning callback
- `OpenApiGeneratorWarning` / `OpenApiGeneratorWarningCode` — non-fatal warning channel
- `make` — Effect that builds the service
- `layerTransformerSchema` / `layerTransformerTs` — Layers selecting transformer flavor

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/OpenApiGenerator.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapitransformer]]
- [[effect-pkg-tools-openapi-generator-httpapitransformer]]
