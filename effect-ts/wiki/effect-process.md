---
title: effect/unstable/process (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/process (hub)

Effect-native API for spawning and managing child processes. Commands are built as an AST so they can be composed (e.g. piped) before execution, and the actual spawn is delegated to a platform-provided `ChildProcessSpawner` service. Produces streaming `stdout`/`stderr` and a sink `stdin`.

## Entries
- [[effect-process-child-process]] — command AST, builders, pipelines
- [[effect-process-child-process-spawner]] — spawner service tag and process handle

## Source
- `raw/effect-smol/packages/effect/src/unstable/process/`

## Related
- [[effect-ts-v4]]
- [[effect-stream]]
- [[effect-sink]]
- [[effect-platform-error]]
