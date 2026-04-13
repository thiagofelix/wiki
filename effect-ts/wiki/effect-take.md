---
title: Take
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Take

Representation of a single "chunk or end" value produced by a stream pull. A `Take<A, E, Done>` is either a non-empty chunk of `A`s or an `Exit` terminating the stream with either success (`Done`) or failure (`E`).

## Key Exports
- `Take<A, E, Done>` — `NonEmptyReadonlyArray<A> | Exit<Done, E>`
- `toPull` — convert a `Take` back into a `Pull` effect for downstream consumption

## Source
- `raw/effect-smol/packages/effect/src/Take.ts`

## Related
- [[effect-ts-v4]]
- Used by [[effect-stream]] and Pull for buffered element transport
