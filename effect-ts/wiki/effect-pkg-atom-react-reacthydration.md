---
title: ReactHydration (@effect/atom-react)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ReactHydration (@effect/atom-react)

SSR hydration boundary component that applies dehydrated atom state into the client registry. New atoms are hydrated during render for immediate availability; atoms that already exist in the registry are deferred to a `useEffect` to avoid disrupting in-flight transitions.

## Key Exports
- `HydrationBoundary` — `React.FC` that reads `state: Iterable<DehydratedAtom>` and hydrates the contextual registry
- `HydrationBoundaryProps` — props interface with `state` and `children`

## Behavior Notes
- Delegates actual hydration to `effect/unstable/reactivity/Hydration.hydrate`
- Splits dehydrated atoms into "new" (hydrated in render) vs "existing" (hydrated in effect) buckets
- `Hydration.hydrate` is idempotent so repeated calls are safe

## Source
- `raw/effect-smol/packages/atom/react/src/ReactHydration.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-pkg-atom-react-registrycontext]]
- [[effect-unstable-reactivity-hydration]]
- [[effect-ts-v4]]
