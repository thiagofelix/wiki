---
title: Random
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Random

Context-backed service for generating random values inside Effect programs. Because it is a service, it can be swapped for a deterministic/test implementation in tests. Offers integers, floats, ranges, booleans, UUIDs, and shuffling; the underlying generator exposes `nextDoubleUnsafe`/`nextIntUnsafe` on the `Random` reference.

## Key Exports
- `Random` — `Context.Reference` for the random number generator service
- `next` — float in `[0, 1]`
- `nextBoolean`
- `nextInt` — safe integer range
- `nextBetween(min, max)`, `nextIntBetween(min, max, { halfOpen })`
- `shuffle(iterable)` — Fisher-Yates shuffle
- `nextUUIDv4` — RFC 4122 UUID string
- `choice(iterable)` — pick a random element

## Source
- `raw/effect-smol/packages/effect/src/Random.ts`

## Related
- [[effect-ts-v4]]
- [[effect-clock]]
- [[effect-context]]
