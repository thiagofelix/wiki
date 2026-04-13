# System API Specification

**Status:** STABLE
**Version:** latest
**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Description

### Purpose

This specification outlines service endpoints, resources, and operations for interacting with the System openEHR API using RESTful principles.

### Related Documents

**Prerequisites:**
- The openEHR REST API Specifications Overview
- The openEHR Architecture Overview

**Related References:**
- openEHR Global Class Index
- XML-Schemas (XSD)
- JSON-Schemas and Simplified Formats

### Specification Status

This document is in the `STABLE` state. It is available as an OpenAPI 3.0.3 specification in YAML format for both validation and code generation purposes.

The development version can be found at: `https://specifications.openehr.org/releases/ITS-REST/development/system.html`

---

## Resource Endpoints

### Options

#### OPTIONS and Conformance

The `OPTIONS` HTTP method enables clients to determine options and requirements associated with a resource, service, or system without performing resource actions.

Services should respond with appropriate HTTP codes, headers, and potentially a payload revealing service details. This method also exposes service capabilities for conformance manifests.

**Endpoint:** `OPTIONS /`

**Base URL:** `https://{baseUrl}/v1`

**Server Variables:**
- `baseUrl` (default: `openEHRSys.example.com`): Server base URL prefix providing openEHR services

##### Request Headers

| Parameter | Type | Description |
|-----------|------|-------------|
| Accept | string | Required: `application/json` |

##### Responses

**200 OK** -- Options and conformance statement retrieved successfully.

**Response Headers:**
- `Allow`: Lists supported methods (e.g., GET, POST, PUT, DELETE, OPTIONS)
- `Content-Type`: `application/json`

**Response Body Schema:**

```json
{
  "solution": "string",
  "solution_version": "string",
  "vendor": "string",
  "restapi_specs_version": "string",
  "conformance_profile": "string",
  "endpoints": ["string"]
}
```

**Example Response:**

```json
{
  "solution": "openEHRSys",
  "solution_version": "v1.0",
  "vendor": "My-openEHR",
  "restapi_specs_version": "1.1.0",
  "conformance_profile": "STANDARD",
  "endpoints": [
    "/ehr",
    "/demographic",
    "/definition",
    "/query",
    "/admin"
  ]
}
```

---

## Contact

**Specifications Editorial Committee**
Email: info@openehr.org
URL: https://specifications.openehr.org/
