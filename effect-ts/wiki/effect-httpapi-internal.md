---
title: httpapi/internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# httpapi/internal (unstable)

Private helpers shared between modules under `unstable/httpapi`. Not part of the public API.

## Files
- `html.ts` — `escape` for HTML entities and `escapeJson` that safely embeds JSON inside `<script>` tags (escapes `</script>`, U+2028, U+2029).
- `httpApiScalar.ts` — the inlined HTML/CSS/JS assets used by `HttpApiScalar.layer` to render the Scalar documentation UI.
- `httpApiSwagger.ts` — the inlined HTML/CSS/JS assets used by `HttpApiSwagger.layer` to render the Swagger UI.

## Key Exports
- `escape` / `escapeJson` — HTML-safe string helpers
- `css` / `javascript` — inlined asset strings for the Scalar and Swagger loaders

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/internal/html.ts`
- `raw/effect-smol/packages/effect/src/unstable/httpapi/internal/httpApiScalar.ts`
- `raw/effect-smol/packages/effect/src/unstable/httpapi/internal/httpApiSwagger.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api-scalar]]
- [[effect-httpapi-http-api-swagger]]
