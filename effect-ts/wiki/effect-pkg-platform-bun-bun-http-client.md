---
title: BunHttpClient (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunHttpClient (@effect/platform-bun)

Re-exports the core `FetchHttpClient` module. Bun provides a native `fetch` implementation, so the HTTP client defaults to fetch-based semantics without additional adapters.

## Key Exports
- All exports of `effect/unstable/http/FetchHttpClient` (Fetch, layer, RequestInit, ...)

## Source
- `raw/effect-smol/packages/platform-bun/src/BunHttpClient.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-http-fetch-http-client]]
