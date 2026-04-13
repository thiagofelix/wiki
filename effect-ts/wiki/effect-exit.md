---
title: Exit
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Exit

The outcome of an Effect computation as a plain, synchronously inspectable value. `Exit<A, E>` is a union of `Success<A>` (wraps a value) and `Failure<A, E>` (wraps a `Cause<E>` that may contain typed errors, defects, or interruptions). Exits are themselves Effects, so they can be yielded in `Effect.gen`. Use Exit when you need to observe a result without running additional effects.

## Key Exports
- `Exit<A, E>` — union of `Success` / `Failure`
- `succeed`, `fail`, `failCause`, `die`, `interrupt` — constructors
- `isSuccess`, `isFailure`, `match` — inspection
- `getSuccess`, `getCause`, `findError`, `findDefect` — extraction
- `map`, `mapError`, `mapBoth` — transforms
- `hasFails`, `hasDies`, `hasInterrupts` — failure category checks
- `asVoidAll` — combine multiple exits

## Source
- `raw/effect-smol/packages/effect/src/Exit.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cause]]
- [[effect-effect]]
