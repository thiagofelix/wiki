---
title: JsonPatch
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# JsonPatch

`JsonPatch` implements a deterministic subset of RFC 6902 (JSON Patch) for transforming JSON documents. A `JsonPatch` is an ordered list of `JsonPatchOperation`s — `add`, `remove`, or `replace` — each targeting a JSON Pointer path. The module exposes `get` to compute structural diffs between two JSON values and `apply` to execute a patch against an input document, with inputs never mutated and empty patches returning the original reference.

## Mental Model
- Paths use JSON Pointer syntax; empty string `""` targets the root.
- Array appends use `-` as the final token (e.g. `/items/-`).
- Operations apply sequentially; later operations see earlier changes.
- Array removals are emitted from highest to lowest index to avoid shifting.

## Key Exports
- `JsonPatchOperation` — `add | remove | replace` discriminated union
- `JsonPatch` — `ReadonlyArray<JsonPatchOperation>`
- `get(oldValue, newValue)` — compute a structural diff patch
- `apply(patch, value)` — apply operations in order to transform a document

## Gotchas
- Generated patches are deterministic but not guaranteed minimal.
- Array diff is index-based; no move or copy detection.
- Invalid paths or operations throw rather than returning a result type.
- Object keys are processed in sorted order for stable output.

## Source
- `raw/effect-smol/packages/effect/src/JsonPatch.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-json-pointer]]
