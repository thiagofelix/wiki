---
title: @effect/vitest (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/vitest (hub)

Small package that adds Effect-aware test helpers on top of Vitest. Re-exports the Vitest API and introduces `it.effect` / `it.live` testers, a shared-Layer `layer` helper, fast-check property testing bound to Effect Schemas/Arbitraries, flaky test retries, and a library of assertion helpers tuned for Effect data types (Option, Result, Exit, Cause).

## Modules
- [[effect-pkg-vitest-index]] — `effect`, `live`, `layer`, `flakyTest`, `prop`, `addEqualityTesters`, `Vitest` namespace
- [[effect-pkg-vitest-utils]] — `deepStrictEqual`, `assertEquals`, `assertTrue`, `assertInstanceOf`, `throws`, `assertNone`, and more

## Source
- `raw/effect-smol/packages/vitest/src/`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-opentelemetry]]
