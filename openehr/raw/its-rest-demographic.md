# Demographic API openEHR Specifications

## Document Information

- **Title**: Demographic API openEHR REST Specifications
- **Status**: Development
- **License**: Creative Commons Attribution-NoDerivs 3.0 Unported
- **Contact**: info@openehr.org
- **URL**: https://specifications.openehr.org/

---

## Table of Contents

1. [Overview](#overview)
2. [Purpose](#purpose)
3. [Related Documents](#related-documents)
4. [API Endpoints](#api-endpoints)
5. [Resource Endpoints](#resource-endpoints)

---

## Overview

This specification document describes REST service endpoints, resources, and operations for interacting with the Demographic openEHR API. It details request and response structures for demographic data management within the openEHR framework.

### Purpose

The specification provides comprehensive documentation for developers implementing or consuming demographic services within openEHR systems. It covers HTTP operations, resource management, and data validation requirements.

### Related Documents

**Prerequisite Reading:**
- Demographic Information Model documentation
- openEHR Architecture Overview
- openEHR Global Class Index
- XML-Schemas (XSD) specifications
- JSON-Schemas and Simplified Formats

---

## API Endpoints Overview

The Demographic API provides RESTful endpoints for managing party demographic data across multiple resource types.

### Base URL Structure

```
https://{baseUrl}/v1/demographic/{resource}
```

### Supported Resources

- AGENT
- GROUP
- ORGANISATION
- PERSON
- ROLE
- VERSIONED_PARTY
- CONTRIBUTION
- ITEM_TAG

---

## Resource Endpoints

### AGENT Management

#### Create AGENT

**Endpoint:** `POST /demographic/agent`

**Purpose**: Creates the initial version of a new AGENT record.

**Request Headers:**
| Header | Type | Description |
|--------|------|-------------|
| Prefer | string | Controls response detail level (return=minimal, return=representation, return=identifier) |
| Accept | string | Desired response format (application/json, application/xml, application/openehr.wt.flat+json, application/openehr.wt.structured+json) |
| Content-Type | string | Request payload format |
| openehr-item-tag | array | Associated metadata tags for AGENT |
| openehr-version-item-tag | array | Version-specific metadata tags |

**Request Body Schema:**

```json
{
  "_type": "AGENT",
  "name": {
    "_type": "DV_TEXT",
    "value": "string"
  },
  "archetype_node_id": "string",
  "uid": {
    "_type": "HIER_OBJECT_ID",
    "value": "uuid"
  },
  "links": [
    {
      "meaning": { "_type": "DV_TEXT", "value": "string" },
      "type": { "_type": "DV_TEXT", "value": "string" },
      "target": { "_type": "DV_EHR_URI", "value": "string" }
    }
  ],
  "identities": [
    { }
  ],
  "contacts": [
    { }
  ],
  "details": { },
  "relationships": [
    { }
  ],
  "languages": [
    { "_type": "DV_TEXT", "value": "string" }
  ],
  "roles": [
    {
      "id": { "_type": "HIER_OBJECT_ID", "value": "uuid" },
      "namespace": "string",
      "type": "string"
    }
  ]
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 201 | Created - Resource successfully created |
| 400 | Bad Request - Invalid syntax or missing required parameters |
| 404 | Not Found - Target resource does not exist |
| 422 | Unprocessable Entity - Semantic validation errors detected |

**Response Headers (on Success):**
- Location: URI of newly created resource
- ETag: Version identifier
- openehr-item-tag: Returned metadata tags
- openehr-version-item-tag: Version-specific metadata tags

---

#### Get AGENT

**Endpoint:** `GET /demographic/agent/{uid_based_id}`

**Purpose**: Retrieves a specific version of an AGENT record.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| uid_based_id | string (UUID) | Either OBJECT_VERSION_ID (for specific version) or HIER_OBJECT_ID (for latest version) |

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| version_at_time | string (datetime, ISO 8601) | Retrieves version existing at specified timestamp |

**Request Headers:**
- Accept: Desired response format

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | OK - Resource successfully retrieved |
| 204 | No Content - Resource exists but was deleted at specified time |
| 404 | Not Found - Resource or version not found |

**Response Body**: Complete AGENT object with all properties

---

#### Update AGENT

**Endpoint:** `PUT /demographic/agent/{uid_based_id}`

**Purpose**: Updates an existing AGENT record, creating a new version.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| uid_based_id | string (UUID) | HIER_OBJECT_ID of the AGENT to update |

**Request Headers:**

| Header | Required | Description |
|--------|----------|-------------|
| If-Match | Yes | Current version_uid in quotes (prevents concurrent updates) |
| Prefer | No | Response preference (return=representation/minimal/identifier) |
| Accept | No | Response format |
| Content-Type | No | Request payload format |
| openehr-version-item-tag | No | Tags to associate with new version |

**Request Body Schema**: Updated AGENT object (must match create schema)

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | OK - Update successful with resource representation |
| 204 | No Content - Update successful without body (Prefer=return=minimal) |
| 400 | Bad Request - Invalid syntax |
| 404 | Not Found - Target resource not found |
| 412 | Precondition Failed - If-Match header mismatch |
| 422 | Unprocessable Entity - Semantic validation errors |

---

#### Delete AGENT

**Endpoint:** `DELETE /demographic/agent/{uid_based_id}`

**Purpose**: Logically deletes an AGENT record by creating a deletion version.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| uid_based_id | string (UUID) | HIER_OBJECT_ID of AGENT to delete |

**Request Headers:**
- If-Match: Current version_uid

**Response Codes:**

| Code | Description |
|------|-------------|
| 204 | No Content - Deletion successful |
| 400 | Bad Request - Invalid request |
| 404 | Not Found - Resource not found |
| 412 | Precondition Failed - Version mismatch |

---

### Similar Endpoints for Other Resources

The following resource types follow the same CRUD operation patterns as AGENT:

- **GROUP**: `/demographic/group`
- **ORGANISATION**: `/demographic/organisation`
- **PERSON**: `/demographic/person`
- **ROLE**: `/demographic/role`

Each supports identical POST, GET, PUT, and DELETE operations with matching request/response structures.

---

## VERSIONED_PARTY Endpoints

### Get VERSIONED_PARTY

**Endpoint:** `GET /demographic/{resource_type}/{uid_based_id}`

Retrieves version history and specific versions of party objects.

### Get VERSIONED_PARTY Revision History

**Endpoint:** `GET /demographic/{resource_type}/{uid_based_id}/history`

Returns complete version history including timestamps and version identifiers.

### Get VERSIONED_PARTY Version at Time

**Endpoint:** `GET /demographic/{resource_type}/{uid_based_id}?version_at_time={ISO8601}`

Retrieves the version active at a specified point in time.

### Get VERSIONED_PARTY Version by ID

**Endpoint:** `GET /demographic/{resource_type}/{uid_based_id}/version/{version_id}`

Retrieves a specific version by its version identifier.

---

## CONTRIBUTION Endpoints

### Create CONTRIBUTION

**Endpoint:** `POST /demographic/contribution`

Records a batch of demographic changes as a single contribution.

**Request Body**: Array of VERSIONED_OBJECT changes with change types (creation, modification, deletion)

**Response**: 201 Created with contribution identifier

### Get CONTRIBUTION by ID

**Endpoint:** `GET /demographic/contribution/{contribution_id}`

**Response**: Complete contribution record with all associated changes

---

## ITEM_TAG Management

Item tags provide metadata labeling for demographic records. The following operations are supported for each resource type:

### Get Tags

**Endpoint:** `GET /demographic/{resource_type}/{uid_based_id}/tags`

Retrieves all tags associated with a demographic record.

### Update Tags

**Endpoint:** `PUT /demographic/{resource_type}/{uid_based_id}/tags`

Modifies tag associations for a demographic record.

**Request Body**:
```json
{
  "tags": [
    {
      "key": "string",
      "value": "string",
      "target_path": "string"
    }
  ]
}
```

### Delete Tags

**Endpoint:** `DELETE /demographic/{resource_type}/{uid_based_id}/tags`

Removes tag associations from a demographic record.

---

## Related Schemas

### CAPABILITY

Describes capabilities and permissions associated with party roles.

### CONTACT

Defines contact information including addresses, phone numbers, and communication channels.

### ITEM

Base structure for party items.

### ITEM_STRUCTURE

Hierarchical container for structured demographic data.

### PARTY_IDENTITY

Represents identity information for a party (names, identifiers, credentials).

### PARTY_RELATIONSHIP

Defines relationships between parties (familial, organizational, professional).

---

## HTTP Headers Reference

### Standard Request Headers

| Header | Values | Purpose |
|--------|--------|---------|
| Accept | application/json, application/xml, application/openehr.wt.flat+json, application/openehr.wt.structured+json | Specifies desired response format |
| Content-Type | Same as Accept | Specifies request body format |
| If-Match | version_uid | Conditional request (optimistic locking) |
| Prefer | return=minimal, return=representation, return=identifier | Controls response body content |

### Custom openEHR Headers

| Header | Type | Purpose |
|--------|------|---------|
| openehr-item-tag | Array of UPDATE_ITEM_TAG | Sets metadata tags on resource |
| openehr-version-item-tag | Array of UPDATE_ITEM_TAG | Sets version-specific metadata tags |

### Standard Response Headers

| Header | Contains |
|--------|----------|
| ETag | Current version_uid |
| Location | URI of created/updated resource |
| openehr-item-tag | Current resource-level tags |
| openehr-version-item-tag | Current version-level tags |

---

## Error Response Format

All error responses follow a consistent structure:

```json
{
  "error": {
    "code": "string",
    "message": "Human-readable error description",
    "details": [
      {
        "field": "property_name",
        "message": "Field-specific error message"
      }
    ]
  }
}
```

---

## Status and Development

This specification is currently in **DEVELOPMENT** status. The computable OpenAPI specifications are available in YAML format:

- **Validation Version**: `computable/OAS/demographic-validation.openapi.yaml`
- **Code Generation Version**: `computable/OAS/demographic-codegen.openapi.yaml`

Development documentation: https://specifications.openehr.org/releases/ITS-REST/development/demographic.html

---

## Implementation Notes

- All datetime values use extended ISO 8601 format with timezone information
- UUID identifiers follow standard format with namespace qualifiers
- Pagination and filtering may be supported depending on server implementation
- Concurrent modification protection via If-Match/ETag mechanism
- Soft deletion supported (resources marked deleted but retained for audit)
