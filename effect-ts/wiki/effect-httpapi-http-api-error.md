---
title: HttpApiError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiError (unstable)

Canonical set of HTTP error schemas for `HttpApi`, each annotated with an `httpApiStatus` and implementing `HttpServerRespondable` so they produce the correct status response. Covers 400, 401, 403, 404, 405, 406, 408, 409, 410, 500, 501, and 503.

## Key Exports
- `BadRequest` (400) / `BadRequestNoContent` / `BadRequestFromSchemaError`
- `Unauthorized` (401)
- `Forbidden` (403)
- `NotFound` (404)
- `MethodNotAllowed` (405)
- `NotAcceptable` (406)
- `RequestTimeout` (408)
- `Conflict` (409)
- `Gone` (410)
- `InternalServerError` (500)
- `NotImplemented` (501)
- `ServiceUnavailable` (503)

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiError.ts`

## Related
- [[effect-httpapi]]
- [[effect-http-http-server-respondable]]
- [[effect-httpapi-http-api-schema]]
