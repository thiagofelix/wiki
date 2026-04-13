---
title: ChildProcess (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ChildProcess (unstable)

AST-based child process API. Commands are built first with `make` (or a tagged template) and then spawned through the `ChildProcessSpawner` service. Supports piped command pipelines, stdio streams, custom file descriptors, kill signals, and yieldable integration so commands can be `yield*`ed inside effects.

## Key Exports
- `make` — builds a `StandardCommand` from string/args/options or a template literal
- `Command` — union of `StandardCommand` and `PipedCommand`
- `pipeTo` — composes commands into a `PipedCommand` with `from`/`to` options
- `PipeFromOption` — `"stdout" | "stderr" | "all" | fd${n}`
- `PipeToOption` — `"stdin" | fd${n}`
- `CommandOptions` — env, cwd, stdio, gid/uid, signal, etc.
- `KillOptions` — signal selection
- Commands are `Pipeable` and `Effect.Yieldable`
- Yielding a command calls `spawn` and returns a `ChildProcessHandle`

## Source
- `raw/effect-smol/packages/effect/src/unstable/process/ChildProcess.ts`

## Related
- [[effect-process]]
- [[effect-process-child-process-spawner]]
- [[effect-stream]]
