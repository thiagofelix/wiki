# EHR API - openEHR REST Specifications

## Introduction

This document provides comprehensive REST API specifications for managing Electronic Health Records (EHRs) using the openEHR standard. The specifications are built on OpenAPI 3.0.3 and cover resource endpoints, operations, request/response formats, and HTTP status codes.

## Document Metadata

**Status:** STABLE
**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
**Editor:** Sebastian Iancu, Architect, Code24, Netherlands
**Contact:** info@openehr.org
**URL:** https://specifications.openehr.org/

## Amendment History

| Issue | Details | Completed |
|-------|---------|-----------|
| Release-1.0.3 | SPECITS-66: Migrate REST API specs to OpenAPI Specification | 19 Dec 2022 |
| Release-1.0.2 | SPECITS-41: Add double quotes to ETag and If-Match headers | 21 Mar 2021 |
| Release-1.0.2 | SPECITS-49: Clarify Resource Identification for COMPOSITION retrieval | 08 Mar 2021 |
| Release-1.0.2 | SPECITS-52: Fix revision history examples | 06 Mar 2021 |
| Release-1.0.1 | SPECITS-38: Fix response status for validation errors | 01 Oct 2019 |

## Related Documentation

- **EHR Information Model:** https://specifications.openehr.org/releases/RM/latest/ehr.html
- **OpenEHR Architecture Overview:** https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html
- **Global Class Index:** https://specifications.openehr.org/classes
- **XML Schemas:** https://specifications.openehr.org/releases/ITS-XML/latest
- **JSON Schemas:** https://specifications.openehr.org/releases/ITS-JSON/latest
- **Platform Service Model:** https://specifications.openehr.org/releases/SM/latest/openehr_platform.html

---

# Resource Endpoints

## EHR Management

### Create EHR

**Endpoint:** `POST /v1/ehr`

Creates a new EHR with an auto-generated identifier.

An EHR_STATUS resource is mandatory and will be created during EHR initialization. The client may supply an EHR_STATUS in the request body; if omitted, a default EHR_STATUS is created with:

- `is_queryable`: true
- `is_modifiable`: true
- `subject`: PARTY_SELF object

All additional required EHR attributes and resources follow EHR creation semantics automatically.

#### Request Headers

| Header | Type | Values | Default |
|--------|------|--------|---------|
| Prefer | string | `return=representation`, `return=minimal` | `return=minimal` |

#### Request Body (application/json)

```json
{
  "archetype_node_id": "openEHR-EHR-EHR_STATUS.generic.v1",
  "name": {
    "value": "EHR status"
  },
  "uid": {
    "_type": "OBJECT_VERSION_ID",
    "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
  },
  "subject": {
    "_type": "PARTY_SELF"
  },
  "is_queryable": true,
  "is_modifiable": true
}
```

#### Response Codes

| Code | Description |
|------|-------------|
| 201 | Created successfully. Full resource returned if `Prefer: return=representation` |
| 400 | Invalid request URL or body content |
| 409 | Conflict - EHR with same subject id/namespace already exists |

#### Response Body (201 Created)

```json
{
  "system_id": {
    "value": "9624982A-9F42-41A5-9318-AE13D5F5031F"
  },
  "ehr_id": {
    "value": "7d44b88c-4199-4bad-97dc-d78268e01398"
  },
  "ehr_status": {
    "id": {
      "_type": "OBJECT_VERSION_ID",
      "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
    },
    "namespace": "local",
    "type": "EHR_STATUS"
  },
  "ehr_access": {
    "id": {
      "_type": "OBJECT_VERSION_ID",
      "value": "59a8d0ac-140e-4feb-b2d6-af99f8e68af8::openEHRSys.example.com::1"
    },
    "namespace": "local",
    "type": "EHR_ACCESS"
  },
  "time_created": {
    "value": "2015-01-20T19:30:22.765+01:00"
  }
}
```

---

### Get EHR by Subject ID

**Endpoint:** `GET /v1/ehr`

Retrieves an EHR using subject identification parameters. Parameters are matched against `EHR_STATUS.subject.external_ref.id.value` and `EHR_STATUS.subject.external_ref.namespace`.

#### Query Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| subject_id | string | Yes | `ins01` |
| subject_namespace | string | Yes | `examples` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | EHR retrieved successfully |
| 404 | EHR with supplied subject parameters not found |

#### Response Body (200 OK)

```json
{
  "system_id": {
    "value": "9624982A-9F42-41A5-9318-AE13D5F5031F"
  },
  "ehr_id": {
    "value": "7d44b88c-4199-4bad-97dc-d78268e01398"
  },
  "ehr_status": {
    "id": {
      "_type": "OBJECT_VERSION_ID",
      "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
    },
    "namespace": "local",
    "type": "EHR_STATUS"
  },
  "ehr_access": {
    "id": {
      "_type": "OBJECT_VERSION_ID",
      "value": "59a8d0ac-140e-4feb-b2d6-af99f8e68af8::openEHRSys.example.com::1"
    },
    "namespace": "local",
    "type": "EHR_ACCESS"
  },
  "time_created": {
    "value": "2015-01-20T19:30:22.765+01:00"
  }
}
```

---

### Create EHR with ID

**Endpoint:** `PUT /v1/ehr/{ehr_id}`

Creates a new EHR with a specified identifier. The `ehr_id` must be a valid HIER_OBJECT_ID (UUID strongly recommended).

An EHR_STATUS resource will be created. Client may supply it in the request body; if omitted, defaults are applied as per standard EHR creation.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Values | Default |
|--------|------|--------|---------|
| Prefer | string | `return=representation`, `return=minimal` | `return=minimal` |

#### Request Body (application/json)

```json
{
  "archetype_node_id": "openEHR-EHR-EHR_STATUS.generic.v1",
  "name": {
    "value": "EHR status"
  },
  "subject": {
    "_type": "PARTY_SELF"
  },
  "is_queryable": true,
  "is_modifiable": true
}
```

#### Response Codes

| Code | Description |
|------|-------------|
| 201 | Created successfully |
| 400 | Invalid request URL or body content |
| 409 | Conflict - EHR with same ehr_id already exists |

---

### Get EHR by ID

**Endpoint:** `GET /v1/ehr/{ehr_id}`

Retrieves an EHR using its unique identifier.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | EHR retrieved successfully |
| 404 | EHR with ehr_id not found |

---

## EHR_STATUS Management

### Get EHR_STATUS by Version ID

**Endpoint:** `GET /v1/ehr/{ehr_id}/ehr_status/{version_uid}`

Retrieves a specific version of EHR_STATUS identified by version_uid.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| version_uid | string | `6cb19121-4307-4648-9da0-d62e4d51f19b::openEHRSys.example.com::2` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | EHR_STATUS retrieved successfully |
| 404 | EHR not found or version_uid does not exist |

#### Response Body (200 OK)

```json
{
  "archetype_node_id": "openEHR-EHR-EHR_STATUS.generic.v1",
  "name": {
    "value": "EHR status"
  },
  "uid": {
    "_type": "OBJECT_VERSION_ID",
    "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
  },
  "subject": {
    "_type": "PARTY_SELF"
  },
  "is_queryable": true,
  "is_modifiable": true
}
```

---

### Get EHR_STATUS at Time

**Endpoint:** `GET /v1/ehr/{ehr_id}/ehr_status`

Retrieves EHR_STATUS at a specified time, or the latest version if no time is supplied.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Query Parameters

| Parameter | Type | Required | Format | Example |
|-----------|------|----------|--------|---------|
| version_at_time | string | No | ISO 8601 | `2015-01-20T19:30:22.765+01:00` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | EHR_STATUS retrieved successfully |
| 400 | Invalid version_at_time format |
| 404 | EHR not found or version does not exist at specified time |

---

### Update EHR_STATUS

**Endpoint:** `PUT /v1/ehr/{ehr_id}/ehr_status`

Updates the EHR_STATUS. The current version_uid must be supplied in the `If-Match` header to prevent concurrent update conflicts.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Required | Format | Example |
|--------|------|----------|--------|---------|
| If-Match | string | Yes | Quoted version_uid | `"6cb19121-4307-4648-9da0-d62e4d51f19b::openEHRSys.example.com::1"` |
| Prefer | string | No | `return=representation`, `return=minimal` | `return=minimal` |

#### Request Body (application/json)

```json
{
  "archetype_node_id": "openEHR-EHR-EHR_STATUS.generic.v1",
  "name": {
    "value": "EHR status"
  },
  "subject": {
    "_type": "PARTY_SELF"
  },
  "is_queryable": true,
  "is_modifiable": true
}
```

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | Updated successfully. Full resource returned if `Prefer: return=representation` |
| 204 | Updated successfully. No content (default if Prefer header missing) |
| 400 | Invalid request URL or body content |
| 404 | EHR not found |
| 412 | Precondition failed - If-Match version does not match current version |

---

### Get Versioned EHR_STATUS

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_ehr_status`

Retrieves the complete VERSIONED_EHR_STATUS object containing all version metadata.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | VERSIONED_EHR_STATUS retrieved successfully |
| 404 | EHR not found |

#### Response Body (200 OK)

```json
{
  "uid": {
    "value": "6cb19121-4307-4648-9da0-d62e4d51f19b"
  },
  "owner_id": {
    "id": {
      "_type": "HIER_OBJECT_ID",
      "value": "7d44b88c-4199-4bad-97dc-d78268e01398"
    },
    "namespace": "local",
    "type": "EHR"
  },
  "time_created": {
    "value": "2015-01-20T19:30:22.765+01:00"
  }
}
```

---

### Get Versioned EHR_STATUS Revision History

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_ehr_status/revision_history`

Retrieves the revision history of VERSIONED_EHR_STATUS including all version audits and change metadata.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | Revision history retrieved successfully |
| 404 | EHR not found |

#### Response Body (200 OK)

```json
{
  "items": [
    {
      "version_id": {
        "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
      },
      "audits": [
        {
          "system_id": "d60e2348-b083-48ce-93b9-916cef1d3a5a",
          "time_committed": {
            "value": "2015-01-20T19:30:22.765+01:00"
          },
          "change_type": {
            "value": "creation",
            "defining_code": {
              "terminology_id": {
                "value": "openehr"
              },
              "code_string": "249"
            }
          },
          "description": {
            "value": "An optional description string"
          },
          "committer": {
            "_type": "PARTY_IDENTIFIED",
            "name": "A user name"
          }
        }
      ]
    }
  ]
}
```

---

### Get Versioned EHR_STATUS Version at Time

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_ehr_status/version`

Retrieves a VERSION from VERSIONED_EHR_STATUS at a specified time, or the latest if no time supplied.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Query Parameters

| Parameter | Type | Required | Format | Example |
|-----------|------|----------|--------|---------|
| version_at_time | string | No | ISO 8601 | `2015-01-20T19:30:22.765+01:00` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | VERSION retrieved successfully |
| 400 | Invalid version_at_time format |
| 404 | EHR not found or version does not exist at specified time |

---

### Get Versioned EHR_STATUS Version by ID

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_ehr_status/version/{version_uid}`

Retrieves a specific VERSION identified by version_uid from VERSIONED_EHR_STATUS.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| version_uid | string | `6cb19121-4307-4648-9da0-d62e4d51f19b::openEHRSys.example.com::2` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | VERSION retrieved successfully |
| 404 | EHR not found or version_uid does not exist |

---

## COMPOSITION Management

### Create COMPOSITION

**Endpoint:** `POST /v1/ehr/{ehr_id}/composition`

Creates the first version of a new COMPOSITION in the specified EHR.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Values | Default |
|--------|------|--------|---------|
| Prefer | string | `return=representation`, `return=minimal` | `return=minimal` |

#### Request Body (application/json)

```json
{
  "archetype_node_id": "openEHR-EHR-COMPOSITION.encounter.v1",
  "name": {
    "value": "Vital Signs"
  },
  "uid": {
    "_type": "OBJECT_VERSION_ID",
    "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
  },
  "archetype_details": {
    "archetype_id": {
      "value": "openEHR-EHR-COMPOSITION.encounter.v1"
    },
    "template_id": {
      "value": "Example.v1::c7ec861c-c413-39ff-9965-a198ebf44747"
    },
    "rm_version": "1.0.2"
  },
  "language": {
    "terminology_id": {
      "value": "ISO_639-1"
    },
    "code_string": "en"
  },
  "territory": {
    "terminology_id": {
      "value": "ISO_3166-1"
    },
    "code_string": "NL"
  },
  "category": {
    "value": "event",
    "defining_code": {
      "terminology_id": {
        "value": "openehr"
      },
      "code_string": "433"
    }
  },
  "composer": {
    "_type": "PARTY_IDENTIFIED",
    "external_ref": {
      "id": {
        "_type": "GENERIC_ID",
        "value": "16b74749-e6aa-4945-b760-b42bdc07098a",
        "scheme": "pid"
      },
      "namespace": "openEHRSys.example.com",
      "type": "PERSON"
    },
    "name": "A name"
  },
  "context": {
    "start_time": {
      "value": "2014-11-18T09:50:35.000+01:00"
    },
    "setting": {
      "value": "other care",
      "defining_code": {
        "terminology_id": {
          "value": "openehr"
        },
        "code_string": "238"
      }
    }
  },
  "content": []
}
```

#### Response Codes

| Code | Description |
|------|-------------|
| 201 | COMPOSITION created successfully. Full resource returned if `Prefer: return=representation` |
| 400 | Invalid request URL, body content, or ehr_id |
| 404 | EHR not found |
| 422 | Semantic validation error (e.g., unknown template or validation failure) |

---

### Get COMPOSITION

**Endpoint:** `GET /v1/ehr/{ehr_id}/composition/{composition_uid}`

Retrieves a COMPOSITION by version_uid or latest version if only object_uid provided.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1` |

#### Query Parameters

| Parameter | Type | Required | Format | Example |
|-----------|------|----------|--------|---------|
| version_at_time | string | No | ISO 8601 | `2015-01-20T19:30:22.765+01:00` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | COMPOSITION retrieved successfully |
| 400 | Invalid request format |
| 404 | EHR or COMPOSITION not found |

---

### Update COMPOSITION

**Endpoint:** `PUT /v1/ehr/{ehr_id}/composition/{composition_uid}`

Updates a COMPOSITION. The current version_uid must be supplied in the `If-Match` header.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1` |

#### Request Headers

| Header | Type | Required | Format |
|--------|------|----------|--------|
| If-Match | string | Yes | Quoted version_uid |
| Prefer | string | No | `return=representation` or `return=minimal` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | Updated successfully with full resource (if Prefer: return=representation) |
| 204 | Updated successfully with no content |
| 400 | Invalid request |
| 404 | EHR or COMPOSITION not found |
| 412 | Precondition failed - version mismatch |
| 422 | Semantic validation error |

---

### Delete COMPOSITION

**Endpoint:** `DELETE /v1/ehr/{ehr_id}/composition/{composition_uid}`

Logically deletes a COMPOSITION by creating a new version with deletion marker.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1` |

#### Request Headers

| Header | Type | Required | Format |
|--------|------|----------|--------|
| If-Match | string | Yes | Quoted version_uid |

#### Response Codes

| Code | Description |
|------|-------------|
| 204 | Deleted successfully |
| 400 | Invalid request |
| 404 | EHR or COMPOSITION not found |
| 412 | Precondition failed - version mismatch |

---

### Get Versioned COMPOSITION

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_composition/{composition_uid}`

Retrieves the complete VERSIONED_COMPOSITION object with all version metadata.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | VERSIONED_COMPOSITION retrieved successfully |
| 404 | EHR or COMPOSITION not found |

---

### Get Versioned COMPOSITION Revision History

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_composition/{composition_uid}/revision_history`

Retrieves the revision history of VERSIONED_COMPOSITION.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | Revision history retrieved successfully |
| 404 | EHR or COMPOSITION not found |

---

### Get Versioned COMPOSITION Version at Time

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_composition/{composition_uid}/version`

Retrieves a VERSION from VERSIONED_COMPOSITION at a specified time, or latest if no time supplied.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515` |

#### Query Parameters

| Parameter | Type | Required | Format |
|-----------|------|----------|--------|
| version_at_time | string | No | ISO 8601 |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | VERSION retrieved successfully |
| 400 | Invalid version_at_time format |
| 404 | EHR or COMPOSITION not found |

---

### Get Versioned COMPOSITION Version by ID

**Endpoint:** `GET /v1/ehr/{ehr_id}/versioned_composition/{composition_uid}/version/{version_uid}`

Retrieves a specific VERSION identified by version_uid from VERSIONED_COMPOSITION.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| composition_uid | string | `8849182c-82ad-4088-a07f-48ead4180515` |
| version_uid | string | `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | VERSION retrieved successfully |
| 404 | EHR or COMPOSITION not found |

---

## DIRECTORY Management

### Create Directory

**Endpoint:** `POST /v1/ehr/{ehr_id}/directory`

Creates a new DIRECTORY (folder structure) in the specified EHR.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Values | Default |
|--------|------|--------|---------|
| Prefer | string | `return=representation`, `return=minimal` | `return=minimal` |

#### Response Codes

| Code | Description |
|------|-------------|
| 201 | DIRECTORY created successfully |
| 400 | Invalid request |
| 404 | EHR not found |

---

### Update Directory

**Endpoint:** `PUT /v1/ehr/{ehr_id}/directory`

Updates the DIRECTORY structure. Requires current version_uid in `If-Match` header.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Required | Format |
|--------|------|----------|--------|
| If-Match | string | Yes | Quoted version_uid |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | Updated successfully |
| 204 | Updated (no content response) |
| 400 | Invalid request |
| 404 | EHR not found |
| 412 | Version mismatch |

---

### Delete Directory

**Endpoint:** `DELETE /v1/ehr/{ehr_id}/directory`

Logically deletes the DIRECTORY by creating a new version with deletion marker.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Required |
|--------|------|----------|
| If-Match | string | Yes |

#### Response Codes

| Code | Description |
|------|-------------|
| 204 | Deleted successfully |
| 400 | Invalid request |
| 404 | EHR not found |
| 412 | Version mismatch |

---

### Get Folder in Directory Version at Time

**Endpoint:** `GET /v1/ehr/{ehr_id}/directory/{folder_uid}`

Retrieves a folder/directory structure at a specified time, or latest version.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| folder_uid | string | folder identifier |

#### Query Parameters

| Parameter | Type | Required | Format |
|-----------|------|----------|--------|
| version_at_time | string | No | ISO 8601 |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | Folder retrieved successfully |
| 400 | Invalid request format |
| 404 | EHR or folder not found |

---

### Get Folder in Directory Version

**Endpoint:** `GET /v1/ehr/{ehr_id}/directory`

Retrieves the current DIRECTORY structure.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | DIRECTORY retrieved successfully |
| 404 | EHR not found |

---

## CONTRIBUTION Management

### Create CONTRIBUTION

**Endpoint:** `POST /v1/ehr/{ehr_id}/contribution`

Creates a new CONTRIBUTION grouping multiple changes (modifications to EHR_STATUS, COMPOSITIONs, DIRECTORY).

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |

#### Request Headers

| Header | Type | Values | Default |
|--------|------|--------|---------|
| Prefer | string | `return=representation`, `return=minimal` | `return=minimal` |

#### Response Codes

| Code | Description |
|------|-------------|
| 201 | CONTRIBUTION created successfully |
| 400 | Invalid request |
| 404 | EHR not found |

---

### Get CONTRIBUTION by ID

**Endpoint:** `GET /v1/ehr/{ehr_id}/contribution/{contribution_uid}`

Retrieves a CONTRIBUTION identified by contribution_uid.

#### Path Parameters

| Parameter | Type | Example |
|-----------|------|---------|
| ehr_id | string | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| contribution_uid | string | contribution identifier |

#### Response Codes

| Code | Description |
|------|-------------|
| 200 | CONTRIBUTION retrieved successfully |
| 404 | EHR or CONTRIBUTION not found |

---

# Resource Schemas

## EHR Schema

The EHR resource represents an Electronic Health Record containing:

- **system_id**: Identifier of the system managing the EHR
- **ehr_id**: Unique EHR identifier (HIER_OBJECT_ID)
- **ehr_status**: Reference to EHR_STATUS resource
- **ehr_access**: Reference to access control information
- **time_created**: Timestamp of EHR creation

## EHR_STATUS Schema

EHR_STATUS represents the status and metadata of an EHR:

```
archetype_node_id: string (required)
name: DV_TEXT (required)
uid: UID_BASED_ID
subject: PARTY_PROXY (required)
is_queryable: boolean (default: true)
is_modifiable: boolean (default: true)
other_details: ITEM_STRUCTURE
```

## COMPOSITION Schema

COMPOSITION represents clinical documents or encounters:

```
archetype_node_id: string (required)
name: DV_TEXT (required)
uid: UID_BASED_ID
archetype_details: ARCHETYPED
language: CODE_PHRASE (required)
territory: CODE_PHRASE (required)
category: DV_CODED_TEXT (required)
context: EVENT_CONTEXT (required)
composer: PARTY_PROXY (required)
content: CONTENT_ITEM[] (required)
```

## DIRECTORY Schema

DIRECTORY represents folder/organizational structures within EHRs:

- Hierarchical organization of clinical documents
- Links to COMPOSITION resources
- Time-based versioning support

## CONTRIBUTION Schema

CONTRIBUTION groups related changes:

```
uid: UID_BASED_ID
audit: AUDIT_DETAILS
versions: OBJECT_REF[] (references to modified versions)
```

---

# Common Data Types

## CODE_PHRASE

```json
{
  "terminology_id": {
    "value": "ISO_639-1"
  },
  "code_string": "en"
}
```

## DV_CODED_TEXT

```json
{
  "value": "event",
  "defining_code": {
    "terminology_id": {
      "value": "openehr"
    },
    "code_string": "433"
  }
}
```

## DV_TEXT

```json
{
  "value": "Display text"
}
```

## OBJECT_VERSION_ID

```json
{
  "_type": "OBJECT_VERSION_ID",
  "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
}
```

## PARTY_IDENTIFIED

```json
{
  "_type": "PARTY_IDENTIFIED",
  "name": "Person name",
  "external_ref": {
    "id": {
      "_type": "GENERIC_ID",
      "value": "identifier-value",
      "scheme": "scheme-name"
    },
    "namespace": "openEHRSys.example.com",
    "type": "PERSON"
  }
}
```

---

# HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET, successful PUT with representation |
| 201 | Created | Successful POST or PUT creating new resource |
| 204 | No Content | Successful DELETE or PUT without representation |
| 400 | Bad Request | Malformed request, invalid parameters |
| 404 | Not Found | Resource does not exist |
| 409 | Conflict | Resource already exists (duplicate creation) |
| 412 | Precondition Failed | If-Match header version mismatch |
| 422 | Unprocessable Entity | Semantic validation errors |

---

# Request/Response Headers

## Standard Request Headers

| Header | Purpose | Values |
|--------|---------|--------|
| Prefer | Response preference | `return=representation` or `return=minimal` |
| If-Match | Optimistic locking | Quoted version_uid |
| Content-Type | Request body format | `application/json` |

## Standard Response Headers

| Header | Purpose | Example |
|--------|---------|---------|
| ETag | Resource version tag | `"version_uid"` |
| Location | Resource URI | `/v1/ehr/{ehr_id}/composition/{uid}` |
| Content-Type | Response format | `application/json` |

---

# Error Handling

Errors follow standard HTTP status codes with optional JSON response body containing:

```json
{
  "status": 400,
  "error": "Error description",
  "details": "Additional context if available"
}
```

---

# Conformance

Implementations claiming conformance to this EHR API specification MUST:

1. Support all mandatory endpoints and HTTP methods
2. Return correct HTTP status codes
3. Validate EHR_STATUS on creation
4. Enforce version control for updates
5. Support ISO 8601 timestamps
6. Maintain referential integrity across resources

---

# Related Specifications

- **openEHR Reference Model (RM):** https://specifications.openehr.org/releases/RM/latest/
- **Service Model (SM):** https://specifications.openehr.org/releases/SM/latest/
- **Base Types:** https://specifications.openehr.org/releases/BASE/latest/
- **OpenAPI 3.0.3:** https://spec.openapis.org/oas/v3.0.3

---

**Document Version:** Latest STABLE
**Last Updated:** December 2022
**License:** CC-BY-ND 3.0 Unported
**Source:** https://specifications.openehr.org/releases/ITS-REST/latest/ehr.html
