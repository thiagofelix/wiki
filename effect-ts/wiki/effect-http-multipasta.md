---
title: Multipasta (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Multipasta (unstable)

Thin re-exports of the `multipasta` package, a streaming multipart/form-data parser used by `Multipart`. The main module re-exports the root package and the `HeadersParser` submodule re-exports its part header parser; both exist so consumers and platform packages can reach the raw parser without adding a direct dependency.

## Files
- `Multipasta.ts` — `export * from "multipasta"`
- `Multipasta/HeadersParser.ts` — `export * from "multipasta/HeadersParser"`

## Key Exports
- Re-exports the `multipasta` parser constructors, event types, and the MIME-style headers parser

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Multipasta.ts`
- `raw/effect-smol/packages/effect/src/unstable/http/Multipasta/HeadersParser.ts`

## Related
- [[effect-http]]
- [[effect-http-multipart]]
- [[effect-ts-v4]]
