---
title: Effect Testing
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Effect Testing

`packages/effect/src/testing/` is the built-in testing subpackage of Effect, imported as `effect/testing`. It provides deterministic replacements for time and console, a Schema assertion harness, and a re-export of the `fast-check` property-based testing library. These modules are not re-exported from the top-level `effect` barrel — users must import them from `effect/testing` (or `effect/testing/TestClock`, etc.), which keeps test-only code out of production bundles.

The barrel file `index.ts` re-exports all four modules as namespaces (`FastCheck`, `TestClock`, `TestConsole`, `TestSchema`).

## Contents
- `FastCheck.ts` — full re-export of the `fast-check` library (arbitraries, `property`, `assert`, shrinking). Lets users depend on a single version of fast-check through `effect/testing/FastCheck`.
- `TestClock.ts` — a Layer-provided `Clock` implementation whose time only advances when tests call `TestClock.adjust(duration)` or `setTime(...)`. Schedules and sleeps resolve synchronously in clock order, making time-dependent Effects (`sleep`, `timeout`, `Schedule`, `repeat`, `retry`) deterministic and instant.
- `TestConsole.ts` — a Layer-provided `Console` that captures all `log`, `error`, `warn`, `info`, `debug` output into arrays queryable via `TestConsole.logLines`, `errorLines`, etc. Lets tests assert on console output without touching the real stdout.
- `TestSchema.ts` — the `Asserts` class and supporting `Decoding` / `Encoding` / `Make` / `Arbitrary` helpers for verifying Schema behavior: `decoding().succeed(input, expected)`, `decoding().fail(input, message)`, `verifyLosslessTransformation()`, `arbitrary().verifyGeneration()`, etc. Uses `assert.deepStrictEqual` under the hood and runs property tests through FastCheck.
- `index.ts` — barrel that re-exports the four modules under namespaces.

## Notes
- `TestClock` and `TestConsole` are provided as Layers (`TestClock.layer`, `TestConsole.layer`) and work with the standard `Effect.provide` mechanism.
- `TestSchema.Asserts` methods return `Promise<void>`, so tests should `await` them; parsers may be effectful.
- `effect/testing` is the canonical place to consume fast-check — avoid adding a direct dep on the upstream package.

## Source
- `raw/effect-smol/packages/effect/src/testing/`

## Related
- [[effect-ts-v4]]
- [[source-effect-smol-repo]]
- [[effect-internal]]
- [[effect-index]]
