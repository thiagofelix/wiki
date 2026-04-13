---
title: MutableList
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# MutableList

Bucket-based mutable linked list optimized for high-throughput append/prepend/take workloads such as logging buffers, producer-consumer queues, and streaming pipelines. Amortized O(1) for appends, prepends, and single takes.

## Key Exports
- `MutableList<A>` — interface with `head`, `tail`, `length`
- `MutableList.Bucket<A>` — internal bucket model
- `Empty` — unique symbol returned by `take` on an empty list
- `make` — construct an empty list
- `append` / `prepend` — add a single element
- `appendAll` / `prependAll` — bulk append/prepend
- `take` — remove and return the head element or `Empty`
- `takeN` / `takeAll` — bulk takes into an array
- `length` — current size
- `clear` — reset the list
- `filter` / `filterInPlace` — remove elements by predicate

## Source
- `raw/effect-smol/packages/effect/src/MutableList.ts`

## Related
- [[effect-ts-v4]]
