---
title: Runtime
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Runtime

Utilities for running Effect programs as main entry points, managing process signals, teardown, and exit codes. `makeRunMain` builds a platform-specific runner (e.g. for Node.js) that wires SIGINT/SIGTERM to fiber interruption and converts the final `Exit` into an OS exit code. The default teardown follows Unix conventions: 0 on success, 130 on interruption-only, 1 otherwise.

## Key Exports
- `Teardown` — `(exit, onExit) => void` signature
- `defaultTeardown` — standard Unix exit-code mapping
- `makeRunMain(f)` — builds a `runMain` runner given platform setup callback
- `RunMain` — runner type returned by `makeRunMain`

## Source
- `raw/effect-smol/packages/effect/src/Runtime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-managed-runtime]]
- [[effect-fiber]]
