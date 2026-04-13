---
title: Internal utilities (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Internal utilities (@effect/platform-node-shared)

Internal helpers shared across node-shared modules. Contains `handleErrnoException`, which maps Node `ErrnoException` codes (ENOENT, EACCES, EEXIST, ...) to the appropriate `PlatformError.SystemError` tag so FileSystem, ChildProcess, and similar wrappers surface consistent errors.

## Key Exports
- `handleErrnoException` — curried error mapper from errno code to PlatformError

## Source
- `raw/effect-smol/packages/platform-node-shared/src/internal/utils.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-platform-error]]
