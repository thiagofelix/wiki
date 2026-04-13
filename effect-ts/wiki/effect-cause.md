---
title: Cause
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Cause

Structured representation of how an `Effect` can fail. A `Cause<E>` holds a flat array of `Reason` values where each reason is either a typed `Fail`, an untyped `Die` defect, or an `Interrupt` carrying an optional fiber id. Concurrent and sequential failures are stored together in `cause.reasons`, each with tracing annotations. Reach for it whenever you need to inspect, combine, or pretty-print the full failure of an effect instead of collapsing to a single thrown error.

## Key Exports
- `Cause<E>` — core interface with `reasons: ReadonlyArray<Reason<E>>`
- `Reason<E>` — union of `Fail | Die | Interrupt`, each with `annotations`
- `empty`, `fail`, `die`, `interrupt`, `fromReasons` — constructors
- `isCause`, `isFailReason`, `isDieReason`, `isInterruptReason` — guards
- `hasFails`, `hasDies`, `hasInterrupts` — kind predicates
- `findError`, `findDefect`, `findFail`, `findDie`, `findErrorOption` — extraction
- `combine`, `map`, `squash` — transformation
- `pretty`, `prettyErrors` — human-readable rendering
- `annotate`, `annotations`, `reasonAnnotations` — tracing metadata
- Built-in error classes: `NoSuchElementError`, `TimeoutError`, `IllegalArgumentError`, `ExceededCapacityError`, `UnknownError`, plus the `Done` completion signal

## Source
- `raw/effect-smol/packages/effect/src/Cause.ts`

## Related
- [[effect-ts-v4]]
