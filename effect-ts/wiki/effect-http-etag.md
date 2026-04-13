---
title: Etag (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Etag (unstable)

Entity tag generation for HTTP responses, used by `HttpPlatform` to add ETag headers to file responses. Provides a `Generator` service that builds Weak or Strong ETags from FileSystem file info or Web FileLike objects using size and mtime.

## Key Exports
- `Etag` — union of `Weak | Strong` tag variants
- `Weak` / `Strong` — tagged models with value strings
- `Generator` — Context.Service producing ETags from file info
- `toString` — format ETag for HTTP header (`"value"` or `W/"value"`)
- `layer` — default Layer providing a Strong ETag `Generator`

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Etag.ts`

## Related
- [[effect-http]]
- [[effect-http-http-platform]]
- [[effect-ts-v4]]
