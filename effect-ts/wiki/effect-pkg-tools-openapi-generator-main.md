---
title: main (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# main (@effect/openapi-generator)

CLI entrypoint for the `openapigen` command. Accepts an input spec file, an output name, a format, and optional JSON Patch inputs, then runs `OpenApiGenerator.generate` and prints the resulting TypeScript source to stdout, logging any non-fatal warnings to stderr.

## Key Exports
- `root` — `Command.make("openapigen", ...)` top-level command
- Flags: `--spec/-s`, `--name/-n`, `--format/-f`, `--patch/-p`
- Chooses `layerTransformerTs` vs `layerTransformerSchema` based on format

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/main.ts`
- `raw/effect-smol/packages/tools/openapi-generator/src/bin.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-openapigenerator]]
- [[effect-pkg-tools-openapi-generator-openapipatch]]
