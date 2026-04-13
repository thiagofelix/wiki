---
title: Generator (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Generator (@effect/ai-codegen)

Code generator service that wraps `@effect/openapi-generator` to turn a discovered provider plus its fetched OpenAPI spec into Effect HttpClient TypeScript source. Applies JSON Patch documents, transforms schemas via `onEnter` hooks, and honors exclude/additionalProperties options from the config.

## Key Exports
- `CodeGenerator` — service tag producing generated source strings
- `GenerationError` — tagged error wrapping `OpenApiGenerator` failures
- `PatchError` — tagged error wrapping patch parsing/application failures
- `layer` — Layer that depends on an `OpenApiGenerator`
- `layerSchema` — Layer providing the schema transformer variant
- `layerTypeScript` — Layer providing the TypeScript-only transformer variant

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/Generator.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
- [[effect-pkg-tools-ai-codegen-discovery]]
