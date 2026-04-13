---
title: FileSystem
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# FileSystem

Cross-platform file system abstraction exposed as an Effect service. The `FileSystem` interface provides read/write, streaming, directory, permissions, timestamp, file-watching, and metadata operations, each returning an `Effect` that can fail with `PlatformError`. Concrete implementations are supplied by the Node/Bun/Browser platform packages via a Layer.

## Key Exports
- `FileSystem` — service interface (access, copy, chmod, chown, exists, link, stat, readFile, writeFile, readDirectory, remove, rename, makeDirectory, watch, open, etc.)
- `FileSystem` — Context.Tag for DI
- `File` — open file handle interface
- `OpenFlag`, `AccessFileOptions`, `MakeDirectoryOptions` — options types
- `Size`, `SizeInput` — branded byte-count type
- `makeNoop` — stub implementation
- `TypeId` — `"~effect/platform/FileSystem"`

## Source
- `raw/effect-smol/packages/effect/src/FileSystem.ts`

## Related
- [[effect-ts-v4]]
- [[effect-path]]
- [[effect-platform-error]]
- [[effect-stream]]
