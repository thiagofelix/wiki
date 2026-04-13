---
title: Discovery (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Discovery (@effect/ai-codegen)

Service that locates AI provider codegen configs on disk by globbing `packages/ai/*/codegen.{json,yaml,yml}`, parsing each file and decoding it with the `CodegenConfig` schema. Produces a list of `DiscoveredProvider` records with resolved paths and spec sources.

## Key Exports
- `ProviderDiscovery` — service tag with `discover` and `discoverOne` methods
- `DiscoveredProvider` — `{ name, packagePath, config, specSource, outputPath }`
- `DiscoveryError` — tagged error for read/parse failures
- `ProviderNotFoundError` — tagged error listing available providers
- `layer` — Layer implementing `ProviderDiscovery` on top of Glob, FileSystem, Path

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/Discovery.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-codegen-config]]
- [[effect-pkg-tools-ai-codegen-generator]]
