---
title: Effect Internal
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Effect Internal

`packages/effect/src/internal/` holds the private implementation of the Effect core package. Modules here contain the actual runtime logic, data-structure representations, proto objects, type IDs, and cross-module helpers that public modules (e.g. `Effect.ts`, `Stream.ts`, `Schema.ts`) delegate to. They are marked with `/** @internal */` JSDoc tags, are not re-exported from `index.ts`, and are not part of the stable public API — their shape can change between releases without notice. Code that imports from `effect/internal/...` is unsupported.

The pattern is consistent: each public module `Foo.ts` has a thin facade that re-exports and types internal symbols defined in `internal/foo.ts` (or `internal/core.ts` for the Effect/Exit/Fiber cluster). Schema is large enough to warrant its own subdirectory.

## Contents
- `array.ts` — internal helpers for `Array` module (non-empty array primitives, sort/group impls).
- `concurrency.ts` — concurrency-mode resolution shared by forEach/all/race operators.
- `core.ts` — foundational Effect/Exit/Fiber proto objects, `EffectTypeId`, `ExitTypeId`, primitive constructors that `effect.ts` builds on top of.
- `dateTime.ts` — `DateTime` value representation and arithmetic internals.
- `doNotation.ts` — generic `Do` / `bind` / `let` machinery reused by Effect, Option, Result, Stream, etc. via HKT.
- `effect.ts` — the big one: runtime, fiber implementation, scheduling, scope, most `Effect.*` operators, Context/Ref/Latch/Metric glue.
- `equal.ts` — structural equality helpers and hash-consing used by `Equal`/`Hash`.
- `errors.ts` — tiny helper (`errorWithPath`) for attaching JSON-path context to thrown errors (mostly Schema).
- `executionPlan.ts` — `ExecutionPlan` internals for RequestResolver batching/fallback strategies.
- `hashMap.ts` — CHAMP/HAMT implementation backing `HashMap`.
- `hashSet.ts` — `HashSet` implementation on top of `hashMap`.
- `layer.ts` — `provide`/`provideMerge` logic that wires Layers into Effects.
- `matcher.ts` — pattern-matching engine behind the `Match` module.
- `metric.ts` — fiber runtime metrics key used by observability.
- `option.ts` — `Option` proto and constructors.
- `random.ts` — PRNG implementation used by `Random` and test seeds.
- `rcRef.ts` — reference-counted resource wrapper internals (`RcRef`, `RcMap`).
- `record.ts` — record-as-dictionary helpers (safe key iteration, merges).
- `redacted.ts` — `Redacted` value wrapper that hides secrets from logs/inspect.
- `references.ts` — `Context.Reference` definitions for runtime knobs (`CurrentConcurrency`, error reporters, stack frames, span links, log level, etc.).
- `request.ts` — `Request`/`RequestResolver` machinery including dedup and batching.
- `result.ts` — `Result` (success/failure) proto and constructors.
- `schedule.ts` — `repeatOrElse`, `retryOrElse`, and Schedule driver loops.
- `schema/` — Schema internals split into multiple files (see below).
- `stream.ts` — `Stream` proto and Channel-backed core operators.
- `tracer.ts` — tracer service, span creation, context propagation internals.
- `trie.ts` — prefix-trie implementation backing `Trie`.
- `version.ts` — generated package version string (`"dev"` in source).

### `schema/` subdirectory
- `annotations.ts` — internal annotation keys used by Schema AST.
- `arbitrary.ts` — FastCheck `Arbitrary` derivation from a Schema AST.
- `equivalence.ts` — derives `Equivalence` instances from a Schema AST.
- `representation.ts` — pretty/structural representation of schemas.
- `schema.ts` — `Schema` proto, `TypeId`, base class used by `Schema.*`.
- `to-codec.ts` — compiles a Schema AST into decoder/encoder functions.

## Source
- `raw/effect-smol/packages/effect/src/internal/`

## Related
- [[effect-ts-v4]]
- [[source-effect-smol-repo]]
- [[effect-testing]]
- [[effect-index]]
