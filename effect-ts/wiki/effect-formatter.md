---
title: Formatter
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Formatter

Utilities for rendering arbitrary JavaScript values into human-readable strings, handling types that `JSON.stringify` cannot (`BigInt`, `Symbol`, `Set`, `Map`, `Date`, `RegExp`, class instances) and replacing circular references with `"[Circular]"`. Values implementing the `Redactable` protocol are automatically redacted. Two entrypoints: `format` for pretty-printing (not valid JSON) and `formatJson` for safe JSON serialization.

## Key Exports
- `Formatter<Value, Format>` — callable formatter type
- `format` — pretty-print any value (options: `space`, `ignoreToString`)
- `formatJson` — safe JSON.stringify wrapper (drops circular refs)
- `formatPropertyKey` — render a single object key
- `formatPath` — render a property path like `["a"]["b"]`
- `formatDate` — safe ISO string conversion

## Source
- `raw/effect-smol/packages/effect/src/Formatter.ts`

## Related
- [[effect-ts-v4]]
- [[effect-inspectable]]
- [[effect-redactable]]
