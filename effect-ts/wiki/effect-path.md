---
title: Path
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Path

Platform-abstracted filesystem path service modelled after Node's `path` module. Exposed as a `Context` service so programs depend on an interface rather than a concrete implementation, allowing POSIX/Windows and test variants to be swapped via Layer. Errors from URL conversions surface as `BadArgument` from PlatformError.

## Key Exports
- `Path` — `Context.Service` tag for the path service
- `Path` interface — `sep`, `basename`, `dirname`, `extname`, `format`, `parse`
- `join`, `normalize`, `relative`, `resolve`, `isAbsolute` — path string operations
- `fromFileUrl`, `toFileUrl` — URL <-> path conversion returning Effect with `BadArgument`
- `toNamespacedPath` — Windows namespaced path conversion
- `Path.Parsed` — `{ root, dir, base, ext, name }` structure
- `TypeId` — `"~effect/platform/Path"`

## Source
- `raw/effect-smol/packages/effect/src/Path.ts`

## Related
- [[effect-ts-v4]]
- [[effect-platform-error]]
- [[effect-file-system]]
