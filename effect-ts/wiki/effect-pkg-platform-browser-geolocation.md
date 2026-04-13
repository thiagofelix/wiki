---
title: Geolocation (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Geolocation (@effect/platform-browser)

Wraps the browser `navigator.geolocation` API as an Effect service. `getCurrentPosition` produces a one-shot Effect while `watchPosition` produces a Stream backed by an internal sliding queue; both surface errors as a tagged `GeolocationError`.

## Key Exports
- `Geolocation` — Context.Service tag
- `GeolocationError` — tagged error with a reason union
- `PositionUnavailable`, `PermissionDenied`, `Timeout` — error reason classes
- `layer` — default layer over `navigator.geolocation`
- `watchPosition` — convenience accessor yielding a Stream

## Source
- `raw/effect-smol/packages/platform-browser/src/Geolocation.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
