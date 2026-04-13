---
title: BunTerminal (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunTerminal (@effect/platform-bun)

Provides the core `Terminal` service on Bun by delegating to `NodeTerminal`. Supports interactive keystroke reading with an optional shouldQuit predicate.

## Key Exports
- `make` — constructor taking an optional shouldQuit predicate
- `layer` — default Terminal layer

## Source
- `raw/effect-smol/packages/platform-bun/src/BunTerminal.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-terminal]]
- [[effect-terminal]]
