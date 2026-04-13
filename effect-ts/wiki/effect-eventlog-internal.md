---
title: eventlog/internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# eventlog/internal (unstable)

Aggregate note covering internal identity root-secret derivation used by `EventLogEncryption`. Derives encryption and signing key material from an `Identity`'s root secret using labeled HKDF-style derivation.

## Key Modules
- `internal/identityRootSecretDerivation.ts`
- `makeGetIdentityRootSecretMaterial` — cached derivation per identity
- `IdentityRootSecretMaterial` — `{ encryptionKeyMaterial, encryptionKey, signingPublicKey, signingPrivateKey }`
- Constants: `EncryptionDerivationLabelV1`, `SigningDerivationLabelV1`
- `Ed25519PublicKeyLength = 32`, `Ed25519Pkcs8SeedPrefix` bytes for key import
- Uses Web Crypto `SubtleCrypto`

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/internal/identityRootSecretDerivation.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-encryption]]
- [[effect-eventlog-event-log-session-auth]]
