---
title: "Source: Effect-Smol Repository"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Effect-Smol Repository

Raw clone of the Effect v4 (Smol) repository stored at `raw/effect-smol/`. Contains the full monorepo source for Effect's next major version, including the core library, AI modules, platform packages, and comprehensive migration guides.

## Key Files

- `LLMS.md` — Comprehensive AI-oriented documentation covering all major Effect APIs, services, error handling, streams, HTTP, testing, observability, AI modules, and cluster
- `AGENTS.md` — Development guidelines: use `pnpm`, `Effect.fnUntraced` over `Effect.gen` for functions, `Context.Service` class syntax, never use async/await or try/catch, never use `Date.now`/`new Date` (use `Clock` module)
- `MIGRATION.md` — v3→v4 migration overview: unified versioning, package consolidation, unstable module system, performance improvements
- `migration/` — Detailed per-topic migration guides (services, cause, error-handling, forking, yieldable, fiber-keep-alive, layer-memoization, fiberref, runtime, scope, equality, schema, generators)
- `.patterns/` — Development patterns (effect-library-development, error-handling, jsdoc-documentation, module-organization, platform-integration, testing-patterns)
- `ai-docs/` — AI-oriented code examples organized by topic
- `packages/` — All 11 packages (effect, ai, atom, opentelemetry, platform-*, sql, tools, vitest)

## Insights Extracted

- v4 consolidates `@effect/platform`, `@effect/rpc`, `@effect/cluster` into the core `effect` package
- All ecosystem packages share a single version number (unified releases)
- Unstable modules live under `effect/unstable/*` and may break in minor releases
- Fiber runtime rewritten for performance: ~6.3 KB min+gzip for minimal program, ~15 KB with Schema
- `Context.Tag` → `Context.Service`, `Effect.Tag` accessors removed in favor of `yield*` / `.use()`
- `Effect.fn("name")` provides automatic tracing spans; `Effect.fnUntraced` for hot paths
- Error handling renamed: `catchAll` → `catch`, `catchTag` now accepts arrays
- Testing uses `@effect/vitest` with `it.effect` and `assert` (not `expect`)
- Type checking via `@effect/tsgo` (TypeScript-Go language service)

## Related

- [[effect-ts-v4]] — Main wiki article
