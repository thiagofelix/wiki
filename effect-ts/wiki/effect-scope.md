---
title: Scope
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Scope

Resource lifecycle container. A `Scope` holds a set of finalizers that run when the scope is closed, either sequentially (reverse order) or in parallel. Scopes are the backbone of Effect's resource safety — every `acquireRelease`, `Layer`, and `ScopedRef` registers finalizers with some Scope.

## Key Exports
- `Scope` — interface with `strategy` and `state` (Open/Closed/Empty)
- `Closeable` — extends `Scope` with ability to run finalizers
- `State.Open` / `State.Closed` / `State.Empty` — state tags
- `Scope` (service tag) — request the ambient scope from context
- `make` / `makeUnsafe` — create a fresh Closeable scope
- `addFinalizer` — register cleanup to run on close
- `close` — execute finalizers with an Exit
- `provide` — run an effect with a specific scope

## Source
- `raw/effect-smol/packages/effect/src/Scope.ts`

## Related
- [[effect-ts-v4]]
- Central to Layer, ScopedRef, ScopedCache, Stream lifetime, and Effect.acquireRelease
