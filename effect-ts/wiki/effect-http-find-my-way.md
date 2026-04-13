---
title: FindMyWay (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# FindMyWay (unstable)

Thin re-export of the `find-my-way-ts` package, a high-performance radix-tree HTTP router used internally by `HttpRouter` for path matching. Exists so consumers can access the underlying router primitives without an extra dependency.

## Key Exports
- Re-exports everything from `find-my-way-ts` (router constructor, types, path helpers)

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/FindMyWay.ts`

## Related
- [[effect-http]]
- [[effect-http-http-router]]
- [[effect-ts-v4]]
