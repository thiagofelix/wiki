---
title: ConfigProvider
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ConfigProvider

Data source layer underneath the `Config` module. A `ConfigProvider` knows how to load raw configuration nodes — represented as a discriminated union of `Value`, `Record`, and `Array` — from some backing store (environment variables, JSON objects, `.env` files, file trees). Providers compose via prefixing, key transformation, and fallback. Registered as a `Context.Reference` that defaults to `fromEnv()`, so configuration works without explicit provision.

## Key Exports
- `ConfigProvider` — interface with `load(path): Effect<Node | undefined, SourceError>`
- `Node` — union of `Value | Record | Array`
- `Path` — array of string or numeric path segments
- `SourceError` — typed I/O failure
- `make` — build a provider from a lookup function
- `fromEnv` — backed by `process.env`, with underscore splitting to expose nested records
- `fromUnknown` — backed by a plain JS object or JSON
- `fromDotEnvContents`, `fromDotEnv` — parse `.env` text or file
- `fromDir` — read a directory tree (files as leaves)
- `orElse` — fall back to another provider on missing paths
- `nested` — prefix all paths with extra segments
- `mapInput`, `constantCase` — transform path segments (e.g. camelCase → CONSTANT_CASE)
- `layer`, `layerAdd` — install a provider as a `Layer`

## Source
- `raw/effect-smol/packages/effect/src/ConfigProvider.ts`

## Related
- [[effect-ts-v4]]
- [[effect-config]]
