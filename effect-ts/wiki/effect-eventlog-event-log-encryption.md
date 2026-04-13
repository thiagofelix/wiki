---
title: EventLogEncryption (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogEncryption (unstable)

Service for encrypting and decrypting event journal entries using per-identity derived keys. Entries are encrypted into `EncryptedEntry`/`EncryptedRemoteEntry` structures that can be transmitted to untrusted remotes without exposing payload content.

## Key Exports
- `EventLogEncryption` — service with `encrypt`, `decrypt`
- `EncryptedEntry` — `{ entryId, encryptedEntry }` schema
- `EncryptedRemoteEntry` — adds `sequence`, `iv`
- `layerSubtle` — Web Crypto `SubtleCrypto` implementation
- Derives encryption keys from the identity's root secret
- Uses AES-GCM with random IV per batch
- Integrates with `Transferable.Uint8Array` for zero-copy transport

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogEncryption.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log]]
- [[effect-eventlog-internal]]
- [[effect-workers-transferable]]
