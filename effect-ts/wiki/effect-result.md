---
title: Result
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Result

A synchronous, pure discriminated union representing a computation that either succeeded (`Success<A>`) or failed (`Failure<E>`). Replaces `Either` from Effect 3.x. Unlike `Effect`, `Result` is evaluated eagerly and side-effect free. It is monadic, pipeable, and yieldable inside `Effect.gen`, where yielding a `Failure` short-circuits the surrounding effect.

## Key Exports
- `Result<A, E>` — `Success<A, E> | Failure<A, E>` union
- `succeed(value)`, `fail(error)` — constructors
- `fromNullishOr`, `fromOption`, `try` / `try_`, `liftPredicate` — alt constructors
- `map`, `mapError`, `mapBoth`, `flatMap`, `andThen`, `all` — transforms
- `getOrElse`, `getOrNull`, `getOrUndefined`, `getOrThrow`, `getOrThrowWith` — unwrap
- `match({ onSuccess, onFailure })` — pattern match
- `orElse`, `filterOrFail` — recovery/filtering
- `getSuccess`, `getFailure` — convert to `Option`
- `gen`, `Do`, `bind`, `let` — generator and do-notation
- `isResult`, `isSuccess`, `isFailure` — guards

## Source
- `raw/effect-smol/packages/effect/src/Result.ts`

## Related
- [[effect-ts-v4]]
- [[effect-option]]
- [[effect-exit]]
