---
title: HttpApiSecurity (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiSecurity (unstable)

Describes authentication schemes that can be attached to `HttpApi` middlewares and surfaced in OpenAPI. Supports Bearer tokens, API keys (header, query, or cookie), and HTTP Basic. Credentials are typed as `Redacted` values so they don't leak into logs.

## Key Exports
- `HttpApiSecurity` — union of `Bearer | ApiKey | Basic`
- `Bearer` — bearer token scheme
- `ApiKey` — API key with `in: "header" | "query" | "cookie"` and `key`
- `Basic` — HTTP Basic auth
- `bearer` / `apiKey` / `basic` — constructors
- `annotate` — add OpenAPI annotations to a scheme

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiSecurity.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api-middleware]]
- [[effect-httpapi-open-api]]
