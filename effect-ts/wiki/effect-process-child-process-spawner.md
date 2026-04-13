---
title: ChildProcessSpawner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ChildProcessSpawner (unstable)

Service tag for spawning child processes. Implemented by platform-specific packages (e.g. `@effect/platform-node`). Also defines the `ChildProcessHandle` interface exposing pid, exit code, kill, and typed stdio `Stream`/`Sink` values.

## Key Exports
- `ChildProcessSpawner` — `Context.Service` with a `spawn(command)` method
- `ChildProcessHandle` — `{ pid, exitCode, isRunning, kill, stdin, stdout, stderr, unref }`
- `ExitCode` — branded number type with constructor
- `ProcessId` — branded number type with constructor
- `Reref` — `Effect<void>` returned by `unref` to restore parent-process reference count
- `stdin: Sink<void, Uint8Array>`
- `stdout`, `stderr: Stream<Uint8Array, PlatformError>`

## Source
- `raw/effect-smol/packages/effect/src/unstable/process/ChildProcessSpawner.ts`

## Related
- [[effect-process]]
- [[effect-process-child-process]]
- [[effect-platform-error]]
