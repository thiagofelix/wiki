---
title: Config (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Config (@effect/ai-codegen)

Schema definitions and data types describing how an AI provider SDK should be generated from an OpenAPI specification. Defines the `CodegenConfig` class consumed by the discovery pipeline along with the tagged `SpecSource` union (URL, File, Stainless stats indirection).

## Key Exports
- `CodegenConfig` — `Schema.Class` capturing spec, output, name, patches, replacements, excludeAnnotations, disableAdditionalProperties
- `Replacement` — `{ from, to }` text-substitution applied after generation
- `SpecSourceConfig` — structured spec source for Stainless `stats.yml` indirection
- `SpecSource` — tagged union `Url | File | StainlessStats`
- `SpecSource.Url` / `SpecSource.File` — constructors for spec sources
- `SpecSource.fromConfig` — resolve raw spec value to a `SpecSource`
- `CodegenConfig#clientName` / `isTypeOnly` / `patchList` / `replacementList` / `headerContent` — derived accessors

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/Config.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-codegen-discovery]]
