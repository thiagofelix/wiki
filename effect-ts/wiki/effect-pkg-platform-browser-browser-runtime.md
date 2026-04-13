---
title: BrowserRuntime (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserRuntime (@effect/platform-browser)

Provides `runMain` for running a top-level Effect in a browser page. Hooks the window `beforeunload` event so that the root fiber is interrupted when the user navigates away, ensuring finalizers execute.

## Key Exports
- `runMain` — runs an Effect as the root fiber, wiring beforeunload to interrupt

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserRuntime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-runtime]]
