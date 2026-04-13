---
title: BunRuntime (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunRuntime (@effect/platform-bun)

Re-exports the Node shared `runMain` which wires exit codes, signal handling, pretty error logging, and optional custom teardown. Bun's process model is Node-compatible so no special handling is needed.

## Key Exports
- `runMain` — top-level Effect runner with interrupt and teardown handling

## Source
- `raw/effect-smol/packages/platform-bun/src/BunRuntime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-runtime]]
- [[effect-runtime]]
