---
title: index (@effect/vitest)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# index (@effect/vitest)

Main entry point that re-exports Vitest's API and layers on Effect-aware test helpers. Exposes `it.effect` / `it.live` testers that expect functions returning `Effect`, a `layer` helper for sharing layers across describe blocks, property-based testing via fast-check, flaky test retries, and Effect equality testers.

## Key Exports
- `effect` — `Vitest.Tester<Scope.Scope>` running tests inside TestContext
- `live` — `Vitest.Tester<Scope.Scope>` running against the live runtime
- `layer(layer, options?)` — share a Layer across tests with optional describe name
- `flakyTest(self, timeout?)` — retry an Effect test until it passes
- `prop(name, arbitraries, self, options?)` — fast-check property tests bound to schemas/arbitraries
- `addEqualityTesters` — install Effect `Equal.equals` testers on Vitest
- `Vitest` namespace — `TestFunction`, `Test`, `Tester`, `Arbitraries`, `Methods`, `MethodsNonLive`
- Re-exports everything from `vitest`

## Source
- `raw/effect-smol/packages/vitest/src/index.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-vitest]]
- [[effect-pkg-vitest-utils]]
