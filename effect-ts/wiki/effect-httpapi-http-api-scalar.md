---
title: HttpApiScalar (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiScalar (unstable)

Serves interactive API documentation using the Scalar UI, generated from the `HttpApi`'s OpenAPI spec. Provided as a `Layer` that mounts on the current `HttpRouter` (default path `/docs`). Supports numerous Scalar configuration options (theme, layout, auth, sidebar, searching).

## Key Exports
- `layer` — Layer mounting the Scalar documentation UI
- `ScalarConfig` — configuration type
- `ScalarThemeId` — union of built-in theme ids

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiScalar.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-open-api]]
- [[effect-httpapi-http-api-swagger]]
