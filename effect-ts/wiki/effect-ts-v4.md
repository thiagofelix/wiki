---
title: Effect v4 (Smol)
type: overview
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Effect v4 (Smol)

Effect v4, codenamed "Smol," is the next major version of Effect — a TypeScript library that provides a comprehensive standard library for building production-grade software with typed effects, structured concurrency, and composable error handling. The v4 rewrite lives in a separate repository (Effect-TS/effect-smol) and is published as `effect@beta` on npm. It consolidates many previously separate packages into the core `effect` package, introduces an unstable module system for evolving APIs, and rewrites the fiber runtime for reduced memory overhead (~6.3 KB minified+gzipped for a minimal program).

## Metadata

- **Repository:** https://github.com/Effect-TS/effect-smol
- **npm:** `effect@beta` (4.0.0-beta.46 as of April 2026)
- **Language:** TypeScript
- **Package manager:** pnpm
- **Type checker:** `@effect/tsgo` (TypeScript-Go)
- **Raw source:** `raw/effect-smol/`

## Packages

The monorepo contains the following packages:

- **effect** — Core library: effects, fibers, streams, layers, schemas, HTTP, RPC, cluster, CLI, and more (consolidates v3's `@effect/platform`, `@effect/rpc`, `@effect/cluster`)
- **ai** — AI/LLM integration: provider-agnostic `LanguageModel`, tools, chat sessions
- **atom** — Reactive state primitives (with framework-specific bindings as separate packages)
- **opentelemetry** — OpenTelemetry integration (NodeSdk for existing OTel setups)
- **platform-browser** — Browser runtime platform
- **platform-bun** — Bun runtime platform
- **platform-node** — Node.js runtime platform
- **platform-node-shared** — Shared Node.js platform utilities
- **sql** — SQL database layer (driver-specific packages like `@effect/sql-pg` remain separate)
- **tools** — Developer tooling (including `@effect/tsgo` for TypeScript-Go language service)
- **vitest** — Testing helpers (`it.effect`, `assert` instead of `expect`)

## Key Changes from v3

### Package Consolidation
All Effect ecosystem packages now share a **single version number** and are released together. Functionality from `@effect/platform`, `@effect/rpc`, `@effect/cluster`, and others now lives directly in the core `effect` package. Packages that remain separate are platform-specific, provider-specific, or technology-specific.

### Unstable Module System
v4 introduces **unstable modules** under `effect/unstable/*` import paths. These may receive breaking changes in minor releases, while top-level modules follow strict semver. Unstable modules include: `ai`, `cli`, `cluster`, `devtools`, `http`, `httpapi`, `observability`, `process`, `rpc`, `schema`, `sql`, `workflow`, `workers`, and more.

### Services: `Context.Tag` → `Context.Service`
All service definition APIs (`Context.Tag`, `Context.GenericTag`, `Effect.Tag`, `Effect.Service`) are replaced by `Context.Service`. The class syntax changes from `Context.Tag(id)<Self, Shape>()` to `Context.Service<Self, Shape>()(id)`. Static accessor proxies are removed in favor of `yield*` or `.use()`.

### Function Constructors
- **`Effect.fn("name")`** — Traced reusable functions (public APIs), creates spans + stack traces
- **`Effect.fnUntraced`** — Untraced functions for library internals / hot paths
- **`Effect.gen`** — Inline one-off composition (unchanged)

### Error Handling
- `Effect.catch` replaces `Effect.catchAll`
- `Effect.catchTag` accepts arrays: `Effect.catchTag(["ErrorA", "ErrorB"], handler)`
- New `Effect.catchReason` / `Effect.catchReasons` for reason-based error handling
- Custom errors use `Schema.TaggedErrorClass` (preferred) or `Data.TaggedError`

### Other Breaking Changes
- `Runtime<R>` removed
- `FiberRef` → `Context.Reference`
- Cause structure flattened
- Effect subtyping → Yieldable pattern
- Layer memoization now works across `Effect.provide` calls
- Fiber keep-alive: automatic process lifetime management
- Layer naming convention: `.layer` instead of `.Default` or `.Live`

## Core Patterns

### Writing Effect Code
Use `Effect.gen` for imperative-style composition with `yield*`. Use `Effect.fn("name")` for reusable functions. Always use `return yield*` when raising errors to make termination explicit.

### Services
Define services with `Context.Service` class syntax. Attach layers explicitly with `Layer.effect`. Use `Context.Reference` for services with default values (e.g. config).

### Testing
Use `@effect/vitest` with `it.effect` for all Effect-based tests. Use `assert` methods (not `expect`). Use `TestClock` for time-dependent tests.

### Key Modules
- **Effect** — Core effect type and combinators
- **Stream** — Pull-based effectful sequences (from iterables, async iterables, events, paginated APIs)
- **Schema** — Runtime validation and encoding/decoding
- **Layer** — Dependency injection and resource management
- **HttpApi** — Schema-first HTTP APIs with typed clients and OpenAPI
- **HttpClient** — HTTP client with schema integration
- **PubSub** — In-process fan-out messaging
- **Schedule** — Retry, repeat, and polling patterns
- **ManagedRuntime** — Bridge Effect programs with non-Effect code (e.g. Hono, Express)
- **LanguageModel** (unstable/ai) — Provider-agnostic LLM integration with text, object, and stream generation
- **ChildProcessSpawner** (unstable/process) — Typed child process management
- **Cluster** (unstable/cluster) — Distributed entity RPCs

## Related

- [[airbyte]] — Another open-source tool in the raw sources
