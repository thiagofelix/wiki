---
title: Stdio
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Stdio

Service abstraction over process standard I/O streams. Exposes `args`, a readable `stdin` stream, and `stdout`/`stderr` sinks. A test layer is provided that routes output to `Sink.drain` and stdin to an empty stream.

## Key Exports
- `Stdio` — interface with `args`, `stdin`, `stdout`, `stderr`
- `Stdio` (Context.Service) — service tag for dependency injection
- `make` — construct a Stdio implementation
- `layerTest` — layer providing a silent Stdio for tests
- `TypeId` — brand for the service

## Source
- `raw/effect-smol/packages/effect/src/Stdio.ts`

## Related
- [[effect-ts-v4]]
- Built on [[effect-sink]] and [[effect-stream]]; complements [[effect-terminal]]
