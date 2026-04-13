---
title: ManagedRuntime
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ManagedRuntime

Converts a `Layer` into a reusable runtime with methods to execute `Effect`s using the provided services. Bridges the Effect world and imperative code (e.g. HTTP handlers, React, CLIs): build once, run many effects, dispose explicitly to release resources.

## Key Exports
- `ManagedRuntime<R, ER>` — interface exposing run methods, `memoMap`, `scope`, `dispose`
- `make` — construct a ManagedRuntime from a `Layer<R, ER, never>`
- `isManagedRuntime` — type guard
- `runFork` — launch an effect as a fiber
- `runSync` / `runSyncExit` — synchronous execution (edges only)
- `runPromise` / `runPromiseExit` — Promise-based execution
- `runCallback` — execute with an exit callback
- `dispose` / `disposeEffect` — release the runtime's scope

## Source
- `raw/effect-smol/packages/effect/src/ManagedRuntime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-layer]]
- [[effect-scope]]
