---
title: SpecFetcher (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SpecFetcher (@effect/ai-codegen)

Service for fetching OpenAPI specifications from URLs, the filesystem, or through the Stainless `stats.yml` indirection (which contains a nested `openapi_spec_url`). Parses JSON or YAML depending on file extension and returns the decoded spec value.

## Key Exports
- `SpecFetcher` — service tag with `fetch(source, provider)` returning unknown JSON
- `SpecFetchError` — tagged error with provider/source context
- `layer` — Layer depending on `FileSystem` and `HttpClient`

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/SpecFetcher.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-codegen-config]]
- [[effect-pkg-tools-ai-codegen-generator]]
