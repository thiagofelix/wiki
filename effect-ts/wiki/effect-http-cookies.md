---
title: Cookies (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Cookies (unstable)

HTTP cookie jar representation for request/response handling. Provides an immutable `Cookies` record with per-cookie metadata (domain, path, expires, secure, httpOnly, sameSite, maxAge) and Schema integration for parsing Set-Cookie headers and serializing back to headers. Lives under `effect/unstable/http`.

## Key Exports
- `Cookies` — interface wrapping a read-only record of named cookies
- `CookiesSchema` — declared Schema for Cookies with codec links
- `Cookie` / `CookieSchema` — individual cookie with options
- `isCookies` / `isCookie` — type guards
- `fromSetCookie` — parse Set-Cookie header array into Cookies
- `toSetCookieHeaders` — serialize Cookies back to Set-Cookie header array
- `fromReadonlyRecord` — build Cookies from record
- `empty` — empty cookie jar
- `set` / `remove` / `get` — manipulate entries

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Cookies.ts`

## Related
- [[effect-http]]
- [[effect-http-headers]]
- [[effect-ts-v4]]
