---
title: K8sHttpClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# K8sHttpClient (unstable)

Context-tagged `HttpClient` preconfigured to talk to the Kubernetes API from inside a pod. Reads the service account token, sets the API server base URL, filters status errors, and retries transient failures. Also exposes helpers to list pods for runner health checks.

## Key Exports
- `K8sHttpClient` — context service wrapping an `HttpClient` for Kubernetes
- `layer` — layer building the client from in-cluster credentials
- `makeGetPods` — build an effect that lists running pods with optional namespace/label filter
- `Pod` — decoded pod representation with readiness helper

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/K8sHttpClient.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runner-health]]
- [[effect-http-http-client]]
