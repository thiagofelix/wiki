---
title: Undici (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Undici (@effect/platform-node)

Thin re-export of the `undici` package. Used by NodeHttpClient (Undici-backed HttpClient) and cluster transports that need an HTTP client without DNS fallbacks.

## Key Exports
- default `Undici`
- Re-exports all named exports of `undici` (Agent, Dispatcher, fetch, ...)

## Source
- `raw/effect-smol/packages/platform-node/src/Undici.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-node-node-http-client]]
