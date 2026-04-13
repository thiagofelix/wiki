---
title: PlatformError
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PlatformError

Tagged error hierarchy used across platform services (FileSystem, Path, etc.) to represent filesystem and system call failures. Wraps either a `BadArgument` (caller-side validation error) or a `SystemError` (OS-level failure categorized by a fixed tag set). Designed to unify error handling in cross-platform I/O code.

## Key Exports
- `PlatformError` — outer tagged error class with `reason`
- `BadArgument` — validation error with `module`, `method`, `description`
- `SystemError` — OS error carrying a `SystemErrorTag`, `syscall`, `pathOrDescriptor`
- `SystemErrorTag` — `"AlreadyExists" | "BadResource" | "Busy" | "InvalidData" | "NotFound" | "PermissionDenied" | "TimedOut" | "UnexpectedEof" | "Unknown" | "WouldBlock" | "WriteZero"`
- `systemError(options)` — constructor for system errors
- `badArgument(options)` — constructor for bad-argument errors

## Source
- `raw/effect-smol/packages/effect/src/PlatformError.ts`

## Related
- [[effect-ts-v4]]
- [[effect-path]]
- [[effect-data]]
