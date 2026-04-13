---
title: ErrorReporter
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ErrorReporter

Pluggable error reporting for Effect programs. Reporters receive structured callbacks with the failing `Cause`, a pretty-printed `Error`, severity, and extra attributes, making it easy to forward failures to Sentry, Datadog, or custom logging backends. Activated by `Effect.withErrorReporting` or built-in boundaries in HTTP/RPC servers. Error classes opt into or out of reporting via the `ignore`, `severity`, and `attributes` annotation symbols.

## Key Exports
- `ErrorReporter` — interface receiving `{ cause, fiber, timestamp }`
- `make` — construct a reporter from a callback (handles dedup, severity, attributes)
- `layer` — provide one or more reporters via a Layer
- `report` — manually report a cause
- `ignore`, `severity`, `attributes` — annotation symbols for error classes
- `TypeId` — `"~effect/ErrorReporter"`

## Source
- `raw/effect-smol/packages/effect/src/ErrorReporter.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cause]]
- [[effect-effect]]
