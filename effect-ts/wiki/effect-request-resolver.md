---
title: RequestResolver
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RequestResolver

Batched request execution engine for Effect's data-loader pattern. A `RequestResolver<A>` collects `Request.Entry<A>` values into batches (grouped by `batchKey`) and runs them together, enabling automatic deduplication, caching, and N+1 query elimination when combined with `Effect.request`. Supports custom batching delay, `collectWhile` gates, and pre-check filters.

## Key Exports
- `RequestResolver<A>` — pipeable resolver interface with `runAll`, `batchKey`, `collectWhile`, `preCheck`, `delay`
- `make(runAll)` — simple resolver from a run function
- `makeWith({ batchKey, preCheck?, delay, collectWhile, runAll })` — full control constructor
- `isRequestResolver` — guard
- `contextFromEffect`, `provideContext` — R environment handling
- `around`, `batchN`, `eitherWith`, `locally` — combinators
- Persistence-backed variants via `unstable/persistence`

## Source
- `raw/effect-smol/packages/effect/src/RequestResolver.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cache]]
- [[effect-primary-key]]
