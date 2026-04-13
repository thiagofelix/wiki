---
title: Headers (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Headers (unstable)

Case-insensitive HTTP header store with `Redactable` integration for safely hiding sensitive headers (Authorization, Cookie, etc.) in logs and inspectors. Normalizes keys to lowercase and supports merging, setting, and redaction contexts via `CurrentRedactedNames`.

## Key Exports
- `Headers` — interface extending Redactable with lowercase keys
- `TypeId` / `isHeaders` — type id and guard
- `empty` — empty headers
- `fromInput` / `fromRecordUnsafe` — constructors from records or iterables
- `merge` — combine two header sets (right wins)
- `set` / `setAll` / `remove` / `has` / `get` — manipulation
- `redact` — redact headers based on a set of names
- `CurrentRedactedNames` — Context Reference for redact list

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Headers.ts`

## Related
- [[effect-http]]
- [[effect-http-http-incoming-message]]
- [[effect-ts-v4]]
