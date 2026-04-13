---
title: Encoding
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Encoding

Encoding and decoding utilities for Base64 (RFC4648), Base64Url, and Hex. Works on both `string` and `Uint8Array` inputs. Decoders return a `Result` carrying an `EncodingError` on failure, so encoding operations compose cleanly with effectful pipelines without throwing.

## Key Exports
- `EncodingError` — tagged error carrying kind, module, input, message
- `isEncodingError` — type guard
- `encodeBase64`, `decodeBase64`, `decodeBase64String` — RFC4648
- `encodeBase64Url`, `decodeBase64Url`, `decodeBase64UrlString` — URL-safe variant
- `encodeHex`, `decodeHex`, `decodeHexString` — hex encoding

## Source
- `raw/effect-smol/packages/effect/src/Encoding.ts`

## Related
- [[effect-ts-v4]]
- [[effect-result]]
