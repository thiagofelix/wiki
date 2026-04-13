---
title: RegistryContext (@effect/atom-react)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RegistryContext (@effect/atom-react)

React context that supplies an `AtomRegistry` to the hooks in `@effect/atom-react`. A default registry is created at module load using React's scheduler for low-priority task scheduling; apps can override via `RegistryProvider` to scope registry lifetime and supply initial values.

## Key Exports
- `RegistryContext` — `React.Context<AtomRegistry>` consumed by all hooks
- `RegistryProvider` — component that creates a per-tree registry with lifecycle cleanup (disposes after unmount)
- `scheduleTask` — wraps `scheduler.unstable_scheduleCallback` at low priority; returned cancel fn

## Provider Options
- `initialValues` — iterable of `[atom, value]` seeded on creation
- `scheduleTask` — override task scheduling strategy
- `timeoutResolution` — registry timer granularity
- `defaultIdleTTL` — time (ms) before idle atoms are disposed (default 400)

## Source
- `raw/effect-smol/packages/atom/react/src/RegistryContext.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-pkg-atom-react-hooks]]
- [[effect-unstable-reactivity-atomregistry]]
- [[effect-ts-v4]]
