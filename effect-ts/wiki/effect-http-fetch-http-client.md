---
title: FetchHttpClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# FetchHttpClient (unstable)

Implementation of `HttpClient` backed by the global `fetch` API. Converts HttpClientRequest bodies (Raw, Uint8Array, FormData, Stream) into `fetch`-compatible calls and wraps responses via `HttpClientResponse.fromWeb`. Works in browsers, Node, Deno, and Bun.

## Key Exports
- `Fetch` — Context Reference for the `fetch` function (defaults to `globalThis.fetch`)
- `RequestInit` — Context Service supplying extra `RequestInit` options
- `layer` — Layer providing a full `HttpClient` using fetch

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/FetchHttpClient.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client]]
- [[effect-ts-v4]]
