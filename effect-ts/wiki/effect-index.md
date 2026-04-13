---
title: Effect Package Index
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Effect Package Index

`packages/effect/src/index.ts` is the public entry point of the `effect` package. It is a ~4350-line, auto-generated barrel file (`@barrel: Auto-generated exports. Do not edit manually.`) that re-exports every public module as a namespace via `export * as Name from "./Name.ts"`, together with a few direct re-exports from `Function.ts` (`absurd`, `cast`, `flow`, `hole`, `identity`, `pipe`). Each namespace export is accompanied by an extensive JSDoc block — mental model, common tasks tables, gotchas, quickstart examples — making `index.ts` also serve as the primary prose documentation surface for the package.

Consumers typically write `import { Effect, Stream, Schema } from "effect"` and then call `Effect.map`, `Stream.run`, etc. Internal (`internal/`) and testing (`testing/`) directories are deliberately not re-exported here.

## Categories of exports
Roughly 130 namespace exports, grouped by theme:

- **Core runtime**: `Effect`, `Exit`, `Cause`, `Fiber`, `FiberHandle`, `FiberMap`, `FiberSet`, `Runtime`, `ManagedRuntime`, `Scheduler`, `Scope`, `Layer`, `LayerMap`, `Context`, `References`.
- **Concurrency & coordination**: `Deferred`, `Latch`, `Semaphore`, `PartitionedSemaphore`, `PubSub`, `Queue`, `Pool`, `RcRef`, `RcMap`, `Resource`, `Ref`, `SynchronizedRef`, `SubscriptionRef`, `ScopedRef`, `ScopedCache`, `Cache`.
- **Error handling**: `Cause`, `Exit`, `Result`, `ErrorReporter`, `ExecutionPlan`.
- **Streaming & channels**: `Stream`, `Sink`, `Channel`, `ChannelSchema`, `Pull`, `Take`.
- **Schema & parsing**: `Schema`, `SchemaAST`, `SchemaGetter`, `SchemaIssue`, `SchemaParser`, `SchemaRepresentation`, `SchemaTransformation`, `SchemaUtils`, `JsonSchema`, `JsonPatch`, `JsonPointer`.
- **Data structures**: `Array`, `Chunk`, `HashMap`, `HashSet`, `HashRing`, `MutableHashMap`, `MutableHashSet`, `MutableList`, `MutableRef`, `Record`, `Struct`, `Tuple`, `Graph`, `Trie`, `NonEmptyIterable`, `Iterable`.
- **Transactional (Tx)**: `TxRef`, `TxChunk`, `TxDeferred`, `TxHashMap`, `TxHashSet`, `TxPriorityQueue`, `TxPubSub`, `TxQueue`, `TxReentrantLock`, `TxSemaphore`, `TxSubscriptionRef`.
- **Primitives & math**: `BigDecimal`, `BigInt`, `Boolean`, `Number`, `String`, `Symbol`, `RegExp`, `DateTime`, `Duration`, `Cron`.
- **Functional programming**: `Function`, `Pipeable`, `Predicate`, `Filter`, `Option`, `UndefinedOr`, `Order`, `Ordering`, `Equal`, `Equivalence`, `Combiner`, `Reducer`, `Differ`, `HKT`, `Newtype`, `Brand`, `Data`, `Match`, `Optic`, `Types`, `Unify`, `Utils`.
- **Effects/services**: `Clock`, `Console`, `Logger`, `LogLevel`, `Random`, `Tracer`, `Metric`, `Config`, `ConfigProvider`, `Redactable`, `Redacted`, `PrimaryKey`, `Request`, `RequestResolver`, `Schedule`.
- **Platform abstractions**: `FileSystem`, `Path`, `Terminal`, `Stdio`, `PlatformError`, `Encoding`, `Formatter`, `Inspectable`, `Hash`.

## Source
- `raw/effect-smol/packages/effect/src/index.ts`

## Related
- [[effect-ts-v4]]
- [[source-effect-smol-repo]]
- [[effect-internal]]
- [[effect-testing]]
