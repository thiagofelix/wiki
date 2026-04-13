---
title: Clipboard (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Clipboard (@effect/platform-browser)

An Effect service wrapping the browser `navigator.clipboard` API. Exposes read/write operations for text, blobs, and `ClipboardItem` arrays, returning errors as a tagged `ClipboardError`.

## Key Exports
- `Clipboard` — Context.Service tag
- `ClipboardError` — tagged error for clipboard failures
- `make` — builds a Clipboard from a reduced implementation
- `layer` — default layer bound to `navigator.clipboard`

## Source
- `raw/effect-smol/packages/platform-browser/src/Clipboard.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
