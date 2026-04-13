---
title: JsonPointer
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# JsonPointer

`JsonPointer` provides the two escaping utilities required by RFC 6901 for JSON Pointer reference tokens. A reference token is a single path segment (e.g. `"foo"`, `"bar/baz"`); when a token contains `~` or `/` those characters must be escaped to `~0` and `~1` so it can be safely joined into a full JSON Pointer string. The module is consumed by `JsonPatch` for operation paths and by `JsonSchema` for `$ref` resolution.

## Mental Model
- `escapeToken` replaces `~` first then `/` to avoid double-escaping.
- `unescapeToken` replaces `~1` first then `~0` for the inverse.
- Empty strings are valid tokens and returned unchanged.
- These functions operate on individual tokens, not full `/foo/bar` pointers — split on `/` first.

## Key Exports
- `escapeToken(token)` — encode a reference token per RFC 6901
- `unescapeToken(token)` — decode an escaped reference token

## Source
- `raw/effect-smol/packages/effect/src/JsonPointer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-json-patch]]
- [[effect-json-schema]]
