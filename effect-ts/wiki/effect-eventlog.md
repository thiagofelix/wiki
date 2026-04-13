---
title: effect/unstable/eventlog (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/eventlog (hub)

Event-sourced local-first log with optional end-to-end encryption and remote synchronization. Applications define `EventGroup`s of typed `Event`s, persist them in an `EventJournal` (SQL or in-memory), and optionally sync with an `EventLogRemote` backed by an encrypted or unencrypted server. Integrates with `Reactivity` for derived state invalidation.

## Entries
- [[effect-eventlog-event]] — individual event schema and metadata
- [[effect-eventlog-event-group]] — typed collection of events
- [[effect-eventlog-event-journal]] — low-level persistence service
- [[effect-eventlog-event-log]] — top-level write API with `Registry`
- [[effect-eventlog-event-log-encryption]] — per-identity encryption service
- [[effect-eventlog-event-log-message]] — RPC protocol definitions
- [[effect-eventlog-event-log-remote]] — client for remote sync
- [[effect-eventlog-event-log-server]] — shared server RPC scaffolding
- [[effect-eventlog-event-log-server-encrypted]] — opaque-storage server
- [[effect-eventlog-event-log-server-unencrypted]] — plaintext-handling server
- [[effect-eventlog-event-log-session-auth]] — Ed25519 session auth
- [[effect-eventlog-sql-event-journal]] — SQL `EventJournal`
- [[effect-eventlog-sql-event-log-server-encrypted]] — SQL encrypted server storage
- [[effect-eventlog-sql-event-log-server-unencrypted]] — SQL unencrypted server storage
- [[effect-eventlog-internal]] — internal identity key derivation

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/`

## Related
- [[effect-ts-v4]]
- [[effect-reactivity]]
- [[effect-rpc]]
- [[effect-sql]]
