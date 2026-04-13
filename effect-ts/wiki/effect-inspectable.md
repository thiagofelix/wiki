---
title: Inspectable
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Inspectable

Standard interface and helpers for giving values custom string, JSON, and Node.js `util.inspect` representations. Supports safe circular serialization and integrates with the redaction system for sensitive data.

## Key Exports
- `Inspectable` — interface requiring `toString`, `toJSON`, and `[NodeInspectSymbol]`
- `Class` — base class implementing `Inspectable`
- `NodeInspectSymbol` — re-export of `Symbol.for("nodejs.util.inspect.custom")`
- `toJson` — safe recursive JSON extraction honoring `toJSON` methods
- `toStringUnknown` — best-effort stringification of any value
- `stringifyCircular` — `JSON.stringify` with circular-ref and redaction support
- `format` — pretty print (re-exported from Formatter)

## Source
- `raw/effect-smol/packages/effect/src/Inspectable.ts`

## Related
- [[effect-ts-v4]]
