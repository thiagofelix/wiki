# Admin API Specification

**Version:** development
**Status:** DEVELOPMENT
**Last Updated:** Current

**Contact:** Specifications Editorial Committee openEHR
**Email:** info@openehr.org
**URL:** https://specifications.openehr.org/
**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Description

### Purpose

This specification outlines service endpoints, resources, and operations for interacting with the Admin openEHR API using RESTful principles. It details the structure of requests and responses when managing administrative functions within an openEHR system.

### Related Documents

#### Prerequisite Reading

- The [EHR Information Model](https://specifications.openehr.org/releases/RM/latest/ehr.html#_the_ehr_information_model)
- The [Demographic Information Model](https://specifications.openehr.org/releases/RM/latest/demographic.html#_demographic_package)
- The [Operational Template 2](https://specifications.openehr.org/releases/AM/latest/OPT2.html)
- The [Archetype Query Language (AQL)](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)

#### Supporting References

- [openEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [Global Class Index](https://specifications.openehr.org/classes)
- [XML-Schemas (XSD)](https://specifications.openehr.org/releases/ITS-XML/latest)
- [JSON-Schemas and Simplified Formats](https://specifications.openehr.org/releases/ITS-JSON/latest)

### Status Information

This specification remains under active development. The OpenAPI specification (YAML format) is available for:
- [Validation](computable/OAS/admin-validation.openapi.yaml)
- [Code generation](computable/OAS/admin-codegen.openapi.yaml)

Community feedback is welcomed. The development version resides at: https://specifications.openehr.org/releases/ITS-REST/development/admin.html

---

## Server Information

**Base URL:** `https://{baseUrl}/v1`

**Example:** `https://openEHRSys.example.com/v1`

---

## Resource Endpoints

### EHR Management

Administrative operations for [Electronic Health Records](https://specifications.openehr.org/releases/RM/latest/ehr.html#_ehr_class).

---

## Endpoints

### Delete EHR by ID

**Operation ID:** `admin_ehr_delete`

Removes the EHR identified by the specified `ehr_id`.

#### Description

The operation permanently and physically deletes an EHR instance. All associated resources—including COMPOSITION, EHR_STATUS, ITEM_TAG, CONTRIBUTION, and historical versions—are also removed in accordance with applicable data protection regulations (e.g., GDPR).

The server may process this asynchronously, returning `202 Accepted`. Synchronous completion returns `204 No Content`.

#### Request

**Method:** DELETE

**Path:** `/admin/ehr/{ehr_id}`

**Full URL Example:** `https://openEHRSys.example.com/v1/admin/ehr/7d44b88c-4199-4bad-97dc-d78268e01398`

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ehr_id` | UUID | Yes | EHR identifier from EHR.ehr_id.value |

**Example Value:** `7d44b88c-4199-4bad-97dc-d78268e01398`

#### Response Codes

| Status | Description |
|--------|-------------|
| 202 | Operation accepted for processing; completion pending or not started (asynchronous processing). |
| 204 | Operation successful; resource physically deleted (hard-delete). |
| 404 | EHR with specified `ehr_id` does not exist. |

---

### Delete Multiple EHRs

**Operation ID:** `admin_ehr_delete_all`

Removes all EHRs or a specified subset identified via query parameters.

#### Description

This operation deletes multiple or all EHR instances. Targeted for development and testing scenarios; production deployments may disable this endpoint, returning `405 Method Not Allowed`.

All associated resources—COMPOSITION, EHR_STATUS, ITEM_TAG, CONTRIBUTION, and historical versions—are permanently removed per applicable data protection standards (e.g., GDPR).

The server may process asynchronously, returning `202 Accepted`. Synchronous completion returns `204 No Content`.

#### Request

**Method:** DELETE

**Path:** `/admin/ehr/all{?ehr_id*}`

**Full URL Example:** `https://openEHRSys.example.com/v1/admin/ehr/all?ehr_id=7d44b88c-4199-4bad-97dc-d78268e01398&ehr_id=297c3e91-7c17-4497-85dd-01e05aaae44e`

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ehr_id` | UUID | No | Optional parameter to target a subset of EHRs. Supports single or multiple values. |

**Single EHR Example:**
`ehr_id=7d44b88c-4199-4bad-97dc-d78268e01398`

**Multiple EHRs Example:**
`ehr_id=7d44b88c-4199-4bad-97dc-d78268e01398&ehr_id=297c3e91-7c17-4497-85dd-01e05aaae44e`

#### Response Codes

| Status | Description |
|--------|-------------|
| 202 | Operation accepted for processing; completion pending or not started (asynchronous processing). |
| 204 | Operation successful; resource(s) physically deleted (hard-delete). |
| 404 | No target resource found matching request parameters. |
| 405 | Request method not supported for this resource (e.g., disabled in production). |

---

## Implementation Notes

- Deletion operations comply with data protection regulations, including the General Data Protection Regulation (GDPR).
- Asynchronous processing may batch deletions for performance optimization.
- Production environments may restrict the bulk deletion endpoint for security purposes.
- All deletions are permanent and non-recoverable.
