---
title: BrowserWorker (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserWorker (@effect/platform-browser)

Implements the core `WorkerPlatform` interface for browser `Worker`, `SharedWorker`, and `MessagePort`. Handles spawn, setup, event listeners, error reporting, and scope-driven cleanup so the generic workers module can communicate with any standard browser worker type.

## Key Exports
- `layer` — merges `layerPlatform` with a user-provided spawner factory
- `layerPlatform` — WorkerPlatform layer implementation for browser workers

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserWorker.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-unstable-workers-worker]]
