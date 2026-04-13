---
title: Pull
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Pull

A pull-based stream primitive representing an Effect that either yields a value, fails, or signals completion by failing with `Cause.Done<Leftover>`. Pulls are the internal building block behind streams and channels: a done error carries an optional leftover value that downstream stages can consume. Provides combinators to distinguish and handle the done signal separately from ordinary failures.

## Key Exports
- `Pull<A, E, Done, R>` — Effect alias with `Cause.Done<Done>` in error channel
- `Success`, `Error`, `Leftover`, `Services`, `ExcludeDone` — type extractors
- `catchDone(f)` — recover from done with another effect
- `isDoneCause`, `isDoneFailure` — cause inspection
- `filterDone`, `filterDoneVoid`, `filterNoDone`, `filterDoneLeftover` — cause filters
- `doneExitFromCause` — convert cause to `Exit` extracting leftover
- `matchEffect({ onSuccess, onFailure, onDone })` — pattern match

## Source
- `raw/effect-smol/packages/effect/src/Pull.ts`

## Related
- [[effect-ts-v4]]
- [[effect-stream]]
- [[effect-channel]]
