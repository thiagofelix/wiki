---
title: BunHttpServerRequest (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunHttpServerRequest (@effect/platform-bun)

Tiny helper to recover the underlying `Bun.BunRequest` from an Effect `HttpServerRequest`. Useful when application code needs to reach into Bun-specific fields (like typed route params) that the portable abstraction does not expose.

## Key Exports
- `toBunServerRequest` — accessor returning the raw `Bun.BunRequest`

## Source
- `raw/effect-smol/packages/platform-bun/src/BunHttpServerRequest.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-unstable-http-http-server-request]]
