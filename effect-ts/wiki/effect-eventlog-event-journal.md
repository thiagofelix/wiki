---
title: EventJournal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventJournal (unstable)

Low-level persistent log of events with local/remote sequencing, compaction support, and a pub/sub change feed. Provides services for appending local events, ingesting remote entries with conflict detection, and tracking remote sequence numbers.

## Key Exports
- `EventJournal` — service with `entries`, `write`, `writeFromRemote`, `withRemoteUncommited`, `nextRemoteSequence`, `changes`, `destroy`
- `Entry`, `RemoteEntry` — schema types with ids, payloads, sequences
- `EntryId`, `RemoteId` — branded ids with unsafe constructors
- `EventJournalError` — tagged error
- `entriesForRemote` — read uncommitted entries for a remote
- `makeEntryIdUnsafe`, `makeRemoteIdUnsafe` — UUID generation
- Uses `Msgpack` for payload encoding

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventJournal.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log]]
- [[effect-eventlog-sql-event-journal]]
