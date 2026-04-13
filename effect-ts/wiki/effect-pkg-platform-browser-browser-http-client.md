---
title: BrowserHttpClient (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserHttpClient (@effect/platform-browser)

Browser-side HTTP client implementations. Re-exports the Fetch-based HttpClient and adds an XMLHttpRequest-backed alternative so callers can opt into XHR semantics (progress, sync response types) while still using the effect HttpClient service.

## Key Exports
- `Fetch` — re-exported Fetch service tag
- `layerFetch` — layer providing HttpClient via `fetch`
- `RequestInit` — re-exported Context reference for fetch init options
- `XHRResponseType` — `"arraybuffer" | "text"`
- `CurrentXHRResponseType` — context reference controlling XHR responseType
- `withXHRArrayBuffer` — sets response type to arraybuffer for an effect
- `XMLHttpRequest` — service tag for the XHR constructor
- `layerXMLHttpRequest` — layer providing HttpClient via XHR

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserHttpClient.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-unstable-http-http-client]]
