---
title: HttpClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpClient (unstable)

Core HTTP client abstraction. An `HttpClient` executes `HttpClientRequest` values and produces `HttpClientResponse` effects, with built-in support for retries, rate limiting, tracing, transformation, accept/acceptJson, and merged preprocess/postprocess hooks. Composable via pipeline operators like `transformResponse`, `mapRequest`, and `withTracerDisabledWhen`.

## Key Exports
- `HttpClient` — service interface with `execute` and per-method helpers (get, post, put, etc.)
- `HttpClient.With<E, R>` — variant with configurable error/environment
- `make` — construct a client from a send function
- `layerMergedContext` — build a layer that merges Fiber context on execute
- `transform` / `transformResponse` / `mapRequest` / `mapRequestEffect` — combinators
- `retry` / `retryTransient` — retry with Schedule
- `withTracerDisabledWhen` / `withSpanNameGenerator` — tracing controls
- `followRedirects` — automatic redirect following
- `tapRequest` / `tap` — debugging hooks
- `filterStatus` / `filterStatusOk` — response filtering

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpClient.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client-request]]
- [[effect-http-http-client-response]]
- [[effect-http-fetch-http-client]]
