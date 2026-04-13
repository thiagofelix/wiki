---
title: HttpApiSwagger (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiSwagger (unstable)

Serves an interactive Swagger UI for an `HttpApi`, generated from the OpenAPI spec produced by `OpenApi.fromApi`. Provided as a `Layer` that mounts on the current `HttpRouter`, defaulting to `/docs` but configurable via an options path.

## Key Exports
- `layer` — Layer mounting Swagger documentation UI at a configurable path

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiSwagger.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-open-api]]
- [[effect-httpapi-http-api-scalar]]
