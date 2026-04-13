---
title: SMART on openEHR
type: entity
sources:
  - raw/its-rest-smart-app-launch.md
created: 2026-04-13
updated: 2026-04-13
---

# SMART on openEHR

SMART on openEHR is an adaptation of the SMART App Launch Framework (originally developed for HL7 FHIR) for openEHR-enabled platforms. It standardizes how third-party applications authenticate, discover services, obtain authorization, and receive clinical context when interacting with openEHR REST APIs. The specification is currently in **DEVELOPMENT** status (ITS-REST development release).

SMART stands for Substitutable Medical Applications and Reusable Technologies, originating from Boston Children's Hospital's Computational Health Informatics Program.

## Purpose

Modern healthcare systems require a "best-of-breed" architecture where applications from multiple vendors operate together. Without standardization, each integration requires lengthy manual effort. SMART on openEHR addresses this by defining a clear contract between Application Vendors and Platform Vendors covering:

- Application registration and credential management
- Service discovery across multiple API types
- OAuth 2.0 / OpenID Connect authentication
- Fine-grained authorization via scopes
- Clinical context selection (EHR, patient, episode)
- Embedded iFrame launch within platform UIs

## Service Discovery

Platforms expose a well-known configuration endpoint relative to the platform base URL:

```
GET https://platform.example.com/.well-known/smart-configuration
```

The response (JSON) advertises OAuth endpoints, supported capabilities, and a `services` map.

### Services Map

The `services` section uses reverse domain name keys to identify available APIs:

| Service Key | Description | Status |
|------------|-------------|--------|
| `org.openehr.rest` | openEHR REST API base URL | **Required** |
| `org.fhir.rest` | FHIR API base URL | Recommended |
| `org.dicomstandard.dicomweb.rest` | DICOMWeb REST API | Optional |
| Custom vendor keys | Any vendor-specific API | Optional |

Each service entry includes `baseUrl` (required), plus optional `description`, `version`, `documentation`, and `openapi` fields.

**Key difference from SMART on FHIR:** The configuration endpoint is defined relative to the Platform base URL (gateway), not the FHIR server base URL. This allows advertising services beyond FHIR, including openEHR REST APIs and other non-FHIR APIs.

### openEHR-Specific Capabilities

In addition to standard SMART capabilities, the following are defined:

| Capability | Description |
|-----------|-------------|
| `context-openehr-ehr` | Supports EHR-level launch context via `ehrId` token claim |
| `context-openehr-episode` | Supports episode-level context via `episodeId` (experimental) |
| `openehr-permission-v1` | Fine-grained scopes over openEHR resources |
| `launch-base64-json` | Launch context encoded as base64 JSON in `launch` parameter |

## Application Types

### By Credential Handling

- **Confidential Applications** -- can securely hold secrets (backend services, server-side web apps). Use `client_secret` or private key authentication.
- **Public Applications** -- cannot store secrets (mobile apps, SPAs). Must use PKCE-based flows.

### By User Interaction

- **Patient-facing** -- used by patients or launched by practitioners in patient context
- **Practitioner-facing** -- used by healthcare professionals, may operate with or without patient context
- **Backend Services** -- autonomous system-to-system communication without direct user interaction

## Authentication Flows

| Flow | Suitable For | Description |
|------|-------------|-------------|
| Authorization Code + PKCE | Public clients | Recommended for browser/mobile apps; no client secret needed |
| Authorization Code + client_secret | Confidential clients | For backend web apps that can store secrets |
| Client Credentials Grant | Backend services | No end-user involved; system-to-system |
| JWT Bearer Token Grant | Confidential clients | Asymmetric key authentication via signed JWTs (preferred for confidential clients) |

**Deprecated flows:** Implicit Grant and Resource Owner Password Credentials Grant are explicitly prohibited due to security concerns.

## Authorization and Launch Contexts

### Standalone Launch

The application is initiated directly by the end-user outside the platform UI. The user visits the application URL, selects the target platform, and the app begins the SMART authorization sequence using the platform's `.well-known/smart-configuration`.

During standalone launch, the application can request context selection assistance from the platform. Using the `launch/patient` scope, the platform prompts the user to select a patient/EHR if needed.

### Embedded iFrame Launch

The application is launched from within the platform's UI (typically in an iFrame). The platform passes two URL parameters:

- `iss` -- the platform's issuer URL
- `launch` -- an opaque token or base64-encoded JSON containing session context

Example: `https://myapp.example.com?launch=123&iss=https://platform.example.com`

The application retrieves the SMART configuration from `{iss}/.well-known/smart-configuration` and initiates the OAuth 2.0 Authorization Code Flow with the `launch` parameter.

### Context Parameters in Token Response

| Parameter | Description |
|-----------|-------------|
| `ehrId` | openEHR EHR identifier for the selected patient |
| `episodeId` | Clinical episode identifier (experimental) |
| `patient` | FHIR Patient ID (standard SMART parameter) |

## Scope Syntax

Scopes follow the pattern:

```
<compartment>/<resource>.<permission>
```

### Compartments

| Compartment | Description |
|------------|-------------|
| `patient` | Access limited to current patient's EHR |
| `user` | Access based on authenticated user's permissions |
| `system` | Unrestricted backend/server-to-server access |

### Resource Types

- `composition-<templateId>` -- compositions matching a template ID pattern
- `template-<templateId>` -- operational templates
- `aql-<queryName>` -- AQL queries (pre-defined or ad-hoc with `*` wildcard)

Template and query identifiers support wildcard matching: `*` matches within a segment, `MyHospital::*` matches all templates in a namespace.

### Permissions

- `c` -- Create
- `r` -- Read
- `u` -- Update
- `d` -- Delete
- `s` -- Search/Execute

### Examples

| Scope | Meaning |
|-------|---------|
| `patient/composition-MyHospital::BP.v1.crud` | Full CRUD on BP compositions in current patient's EHR |
| `user/aql-*.rs` | Read and execute all AQL queries the user has access to |
| `system/template-*.r` | Read all templates system-wide |

## Key Differences from SMART on FHIR

1. **Service discovery scope** -- the `.well-known/smart-configuration` endpoint is relative to the platform gateway, not just the FHIR server, enabling multi-API discovery
2. **Services map** -- the `services` section with reverse-domain keys is an openEHR extension not present in SMART on FHIR
3. **EHR context** -- openEHR-specific `ehrId` parameter in token responses (alongside FHIR's `patient`)
4. **Resource scopes** -- scope resources reference openEHR concepts (compositions by template ID, AQL queries) rather than FHIR resource types
5. **Episode context** -- experimental `episodeId` concept not present in SMART on FHIR
6. **Terminology** -- "EHR" is reserved for the openEHR `EHR` container; the FHIR concept of "EHR system" is called "Platform"

## Development Status

The specification is in DEVELOPMENT status (v1.1.0 as of May 2025). Episode context support is explicitly marked as experimental. Primary authors are Sidharth Ramesh (Medblocks) and Sebastian Iancu (Code24).

## Related Pages

- [[rest-api]] -- the openEHR REST API that SMART on openEHR secures
- [[rest-api-overview]] -- REST API conventions, headers, and content negotiation
