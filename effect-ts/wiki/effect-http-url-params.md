---
title: UrlParams (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# UrlParams (unstable)

Immutable, order-preserving URL query parameter representation. Unlike `URLSearchParams`, it is iterable as `[key, value]` tuples, structurally equal and hashable, and Schema-integrated so records of typed params can be decoded directly.

## Key Exports
- `UrlParams` — interface wrapping `ReadonlyArray<[string, string]>`
- `Input` / `Coercible` — accepted constructor inputs
- `empty` / `fromInput` / `fromUrl` — constructors
- `append` / `appendAll` / `set` / `setAll` / `remove` — manipulation
- `toString` — serialize to query string
- `getAll` / `getFirst` / `getLast` — lookups
- `schemaRecord` — Schema decoder to `ReadonlyRecord<string, string | string[]>`
- `schemaParse` — decode a typed schema from params
- `isUrlParams` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/UrlParams.ts`

## Related
- [[effect-http]]
- [[effect-http-url]]
- [[effect-http-http-client-request]]
