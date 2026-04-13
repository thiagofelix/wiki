---
title: effect/unstable/cluster (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/cluster (unstable)

Sharded actor-style cluster runtime built on top of the effect RPC subsystem. Provides durable entities (stateful actors keyed by id), singletons (at-most-one-across-cluster effects), cron jobs, durable workflows, message/runner storage (memory or SQL), runner-to-runner transports (HTTP, WebSocket, Socket), and Kubernetes-aware health. The core entry point is `Sharding`, which assigns shards to runners and routes messages to the right owner with idempotent, persisted mailbox semantics when requested.

## Modules
- [[effect-cluster-cluster-cron]] — cron jobs via entities + singletons
- [[effect-cluster-cluster-error]] — cluster-wide tagged errors
- [[effect-cluster-cluster-metrics]] — prebuilt metrics gauges
- [[effect-cluster-cluster-schema]] — rpc annotations that tune cluster behavior
- [[effect-cluster-cluster-workflow-engine]] — workflow engine on top of sharding
- [[effect-cluster-deliver-at]] — delayed delivery trait for payloads
- [[effect-cluster-entity]] — sharded entity definition
- [[effect-cluster-entity-address]] — entity placement address
- [[effect-cluster-entity-id]] — branded entity id
- [[effect-cluster-entity-proxy]] — derive flat rpc/http apis from entities
- [[effect-cluster-entity-proxy-server]] — server layers for entity proxies
- [[effect-cluster-entity-resource]] — long-lived entity-scoped resources
- [[effect-cluster-entity-type]] — branded entity type name
- [[effect-cluster-envelope]] — wire-level envelope types
- [[effect-cluster-http-runner]] — HTTP/WebSocket runner transport layers
- [[effect-cluster-k8s-http-client]] — Kubernetes API http client
- [[effect-cluster-machine-id]] — branded machine id used by snowflake
- [[effect-cluster-message]] — incoming/outgoing message wrappers
- [[effect-cluster-message-storage]] — durable mailbox service + memory driver
- [[effect-cluster-reply]] — reply types and codecs
- [[effect-cluster-runner]] — runner schema class
- [[effect-cluster-runner-address]] — host/port schema class
- [[effect-cluster-runner-health]] — runner liveness checks
- [[effect-cluster-runner-server]] — rpc handlers + server layers for runners
- [[effect-cluster-runner-storage]] — persistent membership and shard locks
- [[effect-cluster-runners]] — peer runner client service
- [[effect-cluster-shard-id]] — shard id with grouping
- [[effect-cluster-sharding]] — sharding runtime (assignment + routing)
- [[effect-cluster-sharding-config]] — per-runner sharding configuration
- [[effect-cluster-sharding-registration-event]] — registration pubsub events
- [[effect-cluster-single-runner]] — single-node SQL-backed cluster layer
- [[effect-cluster-singleton]] — cluster-wide singletons
- [[effect-cluster-singleton-address]] — singleton address schema class
- [[effect-cluster-snowflake]] — snowflake id generator
- [[effect-cluster-socket-runner]] — raw socket runner transport layers
- [[effect-cluster-sql-message-storage]] — SQL-backed message storage
- [[effect-cluster-sql-runner-storage]] — SQL-backed runner storage with advisory locks
- [[effect-cluster-test-runner]] — in-memory cluster layer for tests
- [[effect-cluster-internal]] — internal helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/`

## Related
- [[effect-ts-v4]]
- [[effect-rpc]]
- [[effect-workflow]]
