---
title: NodeRuntime (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeRuntime (@effect/platform-node-shared)

Provides `runMain` for Node processes. Wires SIGINT/SIGTERM to fiber interruption, honors a user-supplied teardown, and exits with the correct process code only when a signal was received or the exit was non-zero, so daemons can keep the event loop alive.

## Key Exports
- `runMain` — top-level Effect runner with signal + teardown handling

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeRuntime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-runtime]]
