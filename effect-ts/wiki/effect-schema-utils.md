---
title: SchemaUtils
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaUtils

`SchemaUtils` is a small experimental helper module for bridging native JavaScript classes to Effect schemas. It exposes `getNativeClassSchema`, which takes a class constructor and a backing `Struct` encoding and produces a `Schema.decodeTo` that decodes struct values into class instances and encodes them back. The decode direction calls `new Constructor(props)` and encode is the identity, letting existing JS classes participate in schema pipelines without rewriting them as `Schema.Class`.

## Key Exports
- `getNativeClassSchema` — wrap a class constructor as a `Schema.decodeTo<instanceOf<C>, S>` with the supplied struct encoding and optional declaration annotations

## Gotchas
- Marked `@experimental`; API may change.
- Encode direction is a pure identity — the class must expose its props in the same shape as the encoding struct.

## Source
- `raw/effect-smol/packages/effect/src/SchemaUtils.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-transformation]]
