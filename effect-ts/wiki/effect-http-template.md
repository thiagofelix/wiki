---
title: Template (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Template (unstable)

Tagged-template literal helper for building HTTP response bodies (HTML, text, JSON string fragments) from primitives, `Option`s, `Effect`s, and `Stream`s. Values that resolve asynchronously are flattened into the final rendered output, making it easy to stream partially-computed HTML.

## Key Exports
- `PrimitiveValue` / `Primitive` — string/number/bigint/boolean/null/undefined (+ arrays)
- `Interpolated` — Primitive | Option | Effect of Primitive
- `InterpolatedWithStream` — adds `Stream` of Primitive
- `Interpolated.Context<A>` — extract required env from interpolations
- `make` — template tag returning an Effect of string
- `stream` — template tag returning a Stream of string chunks

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Template.ts`

## Related
- [[effect-http]]
- [[effect-http-http-server-response]]
- [[effect-ts-v4]]
