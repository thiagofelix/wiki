---
title: utils (@effect/vitest)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# utils (@effect/vitest)

Assertion helpers that bridge `node:assert`, Vitest's `assert`, and Effect's `Equal`, `Option`, `Result`, `Exit`, and `Cause` modules. Provides a rich set of `assert*` functions designed to give precise diffs when comparing Effect data types.

## Key Exports
- `deepStrictEqual` / `notDeepStrictEqual` / `strictEqual` — structural equality
- `assertEquals` — uses `Equal.equals` with diff fallback
- `assertTrue` / `assertFalse` / `assertInclude` / `assertMatch`
- `throws` / `throwsAsync` / `doesNotThrow`
- `assertInstanceOf` / `assertDefined`
- `assertNone` — Option helpers (plus more assertSome, assertSuccess, assertFailure for Result/Exit)
- `fail(message)` — thin wrapper around `node:assert.fail`

## Source
- `raw/effect-smol/packages/vitest/src/utils.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-vitest]]
- [[effect-pkg-vitest-index]]
