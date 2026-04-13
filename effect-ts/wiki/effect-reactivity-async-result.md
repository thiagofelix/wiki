---
title: AsyncResult (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AsyncResult (unstable)

Three-state result type for async computations used throughout the `Atom` reactive system. Unlike `Result`, it distinguishes an `Initial` pre-fetch state from `Success` and `Failure`, each of which may still be `waiting` for a refresh. Integrates with `Cause`/`Exit`/`Schema` for error handling.

## Key Exports
- `AsyncResult<A, E>` — union of `Initial | Success | Failure`
- `Initial`, `Success`, `Failure` — state interfaces (with `waiting` flag)
- `initial`, `success`, `failure`, `failureWithPrevious` — constructors
- `isAsyncResult`, `isInitial`, `isSuccess`, `isFailure`
- `map`, `mapError`, `match`, `getOrElse`
- `waitingFrom` — mark an existing result as waiting
- `fromExit`, `fromResult` — conversion helpers
- Schema codec for serialization/hydration

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/AsyncResult.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
- [[effect-result]]
