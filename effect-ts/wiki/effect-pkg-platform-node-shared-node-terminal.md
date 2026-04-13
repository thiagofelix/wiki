---
title: NodeTerminal (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeTerminal (@effect/platform-node-shared)

Implements the core `Terminal` service using Node's `readline`. Handles TTY raw-mode toggling via an RcRef-backed readline interface, forwards keypress events into an Effect `Queue`, and supports line reading and prompt display. Default shouldQuit triggers on Ctrl-C and Ctrl-D.

## Key Exports
- `make` — Effect constructor accepting a shouldQuit predicate
- `layer` — default Terminal layer

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeTerminal.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-terminal]]
