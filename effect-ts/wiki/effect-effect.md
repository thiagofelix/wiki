---
title: Effect
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Effect

The core module of the Effect library. `Effect<A, E, R>` models a lazy, immutable description of a computation that may succeed with `A`, fail with typed error `E`, and require a context `R`. Provides structured concurrency, typed errors, resource management, interruption, tracing, metrics, and a vast combinator surface. Everything else in the library composes around this type.

## Key Exports
- `Effect<A, E, R>` — core computation type
- `succeed`, `fail`, `failCause`, `die`, `interrupt` — base constructors
- `sync`, `async`, `promise`, `tryPromise` — effectful constructors
- `gen` — generator-based do-notation
- `map`, `flatMap`, `tap`, `zip`, `all` — core combinators
- `match`, `catchAll`, `catchTag`, `mapError` — error handling
- `forkChild`, `race`, `timeout` — concurrency primitives
- `provide`, `provideService` — context injection
- `withSpan`, `withExecutionPlan`, `withErrorReporting` — observability
- `runPromise`, `runFork`, `runSync` — runtime execution
- `acquireRelease`, `scoped` — resource management

## Source
- `raw/effect-smol/packages/effect/src/Effect.ts`

## Related
- [[effect-ts-v4]]
- [[effect-fiber]]
- [[effect-exit]]
- [[effect-cause]]
