---
title: HttpClientRequest (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpClientRequest (unstable)

Immutable value object describing an outgoing HTTP request: method, URL, URL params, hash, headers, and body. Provides builders for each HTTP method, body helpers (json, text, formData, urlParams, schemaBody, fileBody), and combinators for setting headers, params, and auth.

## Key Exports
- `HttpClientRequest` — immutable request interface
- `Options` / `Options.NoUrl` — option bags for constructors
- `make` / `get` / `post` / `put` / `patch` / `del` / `head` / `options` — method constructors
- `setMethod` / `setUrl` / `setHeader` / `setHeaders` / `setBody` — setters
- `bodyJson` / `bodyText` / `bodyFormData` / `bodyUrlParams` / `bodyUint8Array` — body setters
- `bearerToken` / `basicAuth` — auth helpers
- `prependUrl` / `appendUrl` / `updateUrl` — URL ops
- `schemaBodyJson` / `schemaBodyUrlParams` — Schema-encoded bodies

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpClientRequest.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client]]
- [[effect-http-http-body]]
