---
title: Permissions (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Permissions (@effect/platform-browser)

Effect service wrapping `navigator.permissions`. Provides a typed `query` operation where the resulting `PermissionStatus.name` is narrowed to the name that was queried, with DOMException failures mapped to a tagged `PermissionsError`.

## Key Exports
- `Permissions` — Context.Service tag
- `PermissionsError` — tagged error with reason union
- `PermissionsInvalidStateError` — DOMException-backed reason
- `PermissionsTypeError` — non-DOMException reason
- `layer` — default layer over `navigator.permissions`

## Source
- `raw/effect-smol/packages/platform-browser/src/Permissions.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
