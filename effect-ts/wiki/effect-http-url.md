---
title: Url (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Url (unstable)

Safe wrappers around the DOM `URL` API that return `Result` instead of throwing, plus helpers to set/modify query string parameters via `UrlParams`. Useful for constructing request URLs without `try/catch`.

## Key Exports
- `fromString` — parse a string (with optional base) into `Result<URL, IllegalArgumentError>`
- `setUrlParams` — replace the search component from a `UrlParams`
- `mutateUrlParams` — apply a transformation to search params
- `modifyUrl` — dual to update individual fields

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Url.ts`

## Related
- [[effect-http]]
- [[effect-http-url-params]]
- [[effect-result]]
