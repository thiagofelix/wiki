---
title: Channel
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Channel

Bi-directional streaming abstraction that is the foundation for Effect's `Stream` and `Sink`. A `Channel<OutElem, OutErr, OutDone, InElem, InErr, InDone, Env>` both reads input and emits output, while tracking error and done types on each side. Channels can be piped, sequenced, and concatenated, giving resource-safe composition of producers, transformers, and consumers. Reach for it when you need lower-level control than `Stream`/`Sink` or when building custom streaming operators.

## Key Exports
- `Channel<OutElem, OutErr, OutDone, InElem, InErr, InDone, Env>` — core type
- `succeed`, `fail`, `failCause`, `sync`, `suspend`, `fromEffect` — constructors
- `fromArray`, `fromIterable`, `fromQueue`, `fromPubSub`, `fromPull` — input sources
- `map`, `mapEffect`, `flatMap`, `mapError`, `mapOut` — transformation
- `pipeTo`, `concatAll`, `zip`, `merge`, `mergeAll` — composition
- `run`, `runDrain`, `runCollect`, `runFold` — terminal operators
- `interruptWhen`, `ensuring`, `scoped` — resource and lifecycle
- `fromTransform` — build a channel from a `(upstream, scope) => Effect` transform

## Source
- `raw/effect-smol/packages/effect/src/Channel.ts`

## Related
- [[effect-ts-v4]]
- [[effect-chunk]]
- [[effect-channel-schema]]
