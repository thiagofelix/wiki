---
title: Context
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Context

Type-safe dependency injection map used by Effect for services and references. A `Context<Services>` is an immutable table mapping service `Key`s to their implementations. Services are declared with `Context.Service` / `Context.ServiceClass` (which assign a unique identifier) and accessed via `yield*` inside `Effect.gen`, with the required services tracked in the effect's `R` channel. Reach for it whenever you need to define, provide, or consume application services.

## Key Exports
- `Context<Services>` — immutable service map
- `Key<Identifier, Shape>` — base type for all context keys
- `Service<Identifier, Shape>` — yieldable service key with `.of`, `.use`, `.useSync`, `.context`
- `ServiceClass` — class-based service declaration
- `Reference` — service key with a default value (used for built-ins like `Clock`, `ConfigProvider`)
- `make`, `empty`, `add`, `merge` — construct and compose contexts
- `get`, `getOption`, `unsafeGet` — read services
- `pick`, `omit` — narrow the service set
- `isContext`, `isKey`, `isReference` — runtime guards

## Source
- `raw/effect-smol/packages/effect/src/Context.ts`

## Related
- [[effect-ts-v4]]
