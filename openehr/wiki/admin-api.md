---
title: Admin API
type: entity
sources:
  - raw/its-rest-admin.md
created: 2026-04-13
updated: 2026-04-13
---

# Admin API

The Admin API provides administrative endpoints for **hard-deleting** EHR records from an openEHR platform. Unlike the standard [[rest-api|EHR API]] `DELETE` operation (which performs a logical delete), the Admin API permanently and physically removes data, including all associated resources: COMPOSITIONs, EHR_STATUS, ITEM_TAGs, CONTRIBUTIONs, and historical versions.

**Status**: DEVELOPMENT

## Purpose

The primary use cases for the Admin API are:

- **GDPR compliance** -- permanently erasing patient data in accordance with data protection regulations (right to erasure / right to be forgotten).
- **Development and testing** -- cleaning up test data from non-production environments.

All deletions are **permanent and non-recoverable**.

## Endpoints

### Delete Single EHR

| | |
|---|---|
| **Method** | `DELETE` |
| **Path** | `/admin/ehr/{ehr_id}` |
| **Description** | Permanently deletes the EHR identified by `ehr_id` and all associated resources |

**Path Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ehr_id` | UUID | Yes | EHR identifier (`EHR.ehr_id.value`) |

**Response Codes:**

| Status | Description |
|--------|-------------|
| 202 | Accepted -- async processing; deletion pending |
| 204 | No Content -- synchronous deletion completed |
| 404 | EHR not found |

### Delete Multiple EHRs (Bulk)

| | |
|---|---|
| **Method** | `DELETE` |
| **Path** | `/admin/ehr/all{?ehr_id*}` |
| **Description** | Deletes multiple or all EHR instances |

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ehr_id` | UUID | No | Optional subset of EHRs to delete (supports multiple values) |

If no `ehr_id` parameters are provided, **all** EHRs in the system are targeted.

**Response Codes:**

| Status | Description |
|--------|-------------|
| 202 | Accepted -- async processing; deletion pending |
| 204 | No Content -- synchronous deletion completed |
| 404 | No matching EHRs found |
| 405 | Method Not Allowed -- endpoint disabled in production |

## Async Processing

Both endpoints may process deletions asynchronously, returning `202 Accepted` rather than waiting for completion. This allows the server to batch deletions for performance optimization, particularly when deleting EHRs with extensive version histories.

## Production Safety

The bulk deletion endpoint (`/admin/ehr/all`) is primarily intended for development and testing environments. Production deployments **may disable** this endpoint entirely, returning `405 Method Not Allowed`. This protects against accidental mass data loss in clinical systems.

The single-EHR endpoint remains available in all environments to support individual GDPR erasure requests.

## Development Status

The Admin API specification is currently in **DEVELOPMENT** status and has not yet reached a stable release. The OpenAPI specification is available in YAML format for validation and code generation purposes. Implementers should expect potential changes before the specification is finalized.

## See Also

- [[rest-api]] -- main REST API specification
- [[rest-api-overview]] -- overview of all openEHR REST APIs
- [[ehr-information-model]] -- the EHR data structures that the Admin API deletes
