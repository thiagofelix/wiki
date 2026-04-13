---
title: RegistryContext (@effect/atom-solid)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RegistryContext (@effect/atom-solid)

SolidJS context providing the `AtomRegistry` used by `@effect/atom-solid` composables. A module-level default registry is created immediately; `RegistryProvider` creates a fresh registry per component and disposes it via `onCleanup`.

## Key Exports
- `RegistryContext` — `createContext<AtomRegistry>` consumed by hooks
- `RegistryProvider` — component that instantiates and disposes a per-scope registry

## Provider Options
- `initialValues` — iterable of seeded `[atom, value]` pairs
- `scheduleTask` — custom task scheduler
- `timeoutResolution` — registry timer granularity
- `defaultIdleTTL` — idle atom disposal TTL (default 400ms)

## Source
- `raw/effect-smol/packages/atom/solid/src/RegistryContext.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-pkg-atom-solid-hooks]]
- [[effect-unstable-reactivity-atomregistry]]
- [[effect-ts-v4]]
