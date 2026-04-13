# SMART on openEHR (SMART) Specification

**Document Title:** SMART on openEHR (SMART)
**Issuer:** openEHR Specification Program
**Release:** ITS-REST development
**Status:** DEVELOPMENT
**Revision:** [latest_issue]
**Date:** [latest_issue_date]
**Keywords:** JSON, REST, SMART, OAuth2, OIDC, Authentication, Authorization, Application, App

---

## Table of Contents

- [Amendment Record](#amendment-record)
- [Acknowledgements](#acknowledgements)
- [1. Preface](#1-preface)
- [2. Overview](#2-overview)
- [3. Application Registration](#3-application-registration)
- [4. Service Discovery](#4-service-discovery)
- [5. Application Types](#5-application-types)
- [6. Authentication](#6-authentication)
- [7. Authorization](#7-authorization)
- [8. Scopes](#8-scopes)
- [9. Experimental Features](#9-experimental-features)
- [References](#references)

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| 1.1.0 | Reworded and structurally improved multiple sections for clarity, consistency, and technical accuracy; introduced consolidated experimental features section. | S Iancu | 20 May 2025 |
| 1.0.0 | SPECITS-69. Adding "SMART on openEHR" specifications. | S Ramesh, S Iancu | 09 Sep 2023 |

---

## Acknowledgements

### Primary Author

- Sidharth Ramesh; Medblocks
- Sebastian Iancu; Architect, Code24, Netherlands

### Contributors

This specification benefited from formal and informal input from the openEHR and health informatics community. The openEHR Foundation recognizes the following contributions:

- Ian McNicoll MD, FreshEHR, UK
- Bostjan Lah, Senior Architect, Better, Slovenia

Design ideas derived from:
- SMART App Launch - Release 2.1.0, published by HL7 FHIR standard

### Trademarks

- 'openEHR' is a registered trademark of the openEHR Foundation
- HL7 and FHIR are registered trademarks of Health Level Seven International
- SMART and SMART logos are trademarks of The Children's Medical Center Corporation

---

## 1. Preface

### 1.1. Purpose

This document describes the SMART framework for openEHR-enabled platforms.

**Intended Audience:**
- EHR systems, Platform or Application vendors
- Standards bodies producing health informatics standards
- Solution vendors

### 1.2. Related Documents

Prerequisite documents:

- [openEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [openEHR REST APIs](https://specifications.openehr.org/releases/ITS-REST/development)
- [HL7 FHIR SMART App Launch Implementation Guide](https://hl7.org/fhir/smart-app-launch/STU2.1/)
- [About SMART - SMART Health IT](https://smarthealthit.org/about-smart-2/)
- [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
- [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html#Authentication)

### 1.3. Status

This specification is in **DEVELOPMENT** state. Development version available at:
[https://specifications.openehr.org/releases/ITS-REST/development/smart_app_launch.html](https://specifications.openehr.org/releases/ITS-REST/development/smart_app_launch.html)

Known omissions indicated with "to be determined" (TBD) paragraphs.

### 1.4. Feedback

**Forum:** [openEHR ITS Forum](https://discourse.openehr.org/c/specifications/its)

**Issue Tracker:** [Specifications Problem Report Tracker](https://specifications.openehr.org/components/ITS-REST/open_issues)

**Change History:** [ITS-REST Component Change Request Tracker](https://specifications.openehr.org/components/ITS-REST/history)

---

## 2. Overview

### 2.1. Background

**SMART** (Substitutable Medical Applications and Reusable Technologies) is a healthcare standard enabling applications to access clinical information from data stores. Originally proposed by the SMART Health IT project (Computational Health Informatics Program, Boston Children's Hospital), it was later formalized as the SMART App Launch Framework, layered on FHIR APIs.

The specification builds on [OAuth 2.0](https://tools.ietf.org/html/rfc6749) and [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html#Authentication)--widely adopted industry standards for authentication and authorization. It allows third-party applications to authenticate and interoperate securely with compliant systems.

It defines:
- Launch sequences
- Token scopes
- Context passing mechanisms
- API-based data access norms

### 2.2. Glossary

| Term | Definition |
|------|-----------|
| **SMART on openEHR** | This specification detailing the SMART framework for openEHR-enabled platforms |
| **SMART App Launch** | Original SMART framework specified by HL7 FHIR; often referred to as "SMART on FHIR" |
| **Vendor** | Entity that develops and supplies software to end-users |
| **User** | Individual operating the Application; also referred to as "end-user" |
| **Application** | Software application developed by a Vendor to operate with a Platform. In OAuth terminology, the "client"; in FHIR, often called "SMART App" |
| **Platform** | Software ecosystem comprising at minimum an Authorization Server, openEHR Clinical Data Repository (CDR), and FHIR Server. Exposes openEHR REST APIs, FHIR APIs, and possibly other APIs. In FHIR, often referred to as "EHR system" |
| **Launcher** | User-facing application, typically developed by Platform vendor, which initiates Application launch within context of specific Patient or Practitioner. May be integrated into Platform's main application or exist independently |
| **EHR** | Session context representing the openEHR `EHR` container for corresponding Patient, indicating subject of interactions through Application |

**Note on Terminology:**

The SMART App Launch Framework uses terms "_EHR_" and "_EHR system_" to describe a system comprising FHIR Server, Authorization Server, and potentially other components. OpenEHR defines an EHR Information Model centered on the root `EHR` container. This specification reserves the term "_EHR_" exclusively for openEHR constructs (e.g., EHR type, EHR ID). Alternate terminology describes equivalent FHIR-based system components.

### 2.3. Why SMART on openEHR?

Modern healthcare systems require diverse specialized solutions rather than monolithic vendor suites. This "best-of-breed" architecture depends on collaborative ecosystems where applications from multiple vendors operate together.

Current implementations involve lengthy, complex manual integration phases--an expensive barrier to entry for new vendors.

**SMART addresses this by standardizing security and interactions** between systems and applications, establishing a clear contract between Application Vendor and Platform Vendor:

- Application runs on Application Vendor's domain
- Platform operates on Platform Vendor's domain
- Application discovers Platform's API services
- Application authenticates with Platform
- Platform authorizes Application for specific actions and data access
- Application determines active operational context (e.g., current EHR)
- Application embeds within Platform's UI while maintaining context

**SMART on openEHR** maintains compatibility with SMART App Launch Framework while extending it to work with openEHR REST APIs and other API types. It supports:

- Application Registration
- Service Discovery
- Authentication
- Authorization
- Scopes
- Context Selection
- Embedded iFrame Launch

### 2.4. Foundational Concepts

The [openEHR Reference Model](https://specifications.openehr.org/releases/RM/latest/index) and [openEHR REST API specification](https://specifications.openehr.org/releases/ITS-REST/development/ehr.html) provide foundational structure for interoperable Applications. For true portability across systems and vendors, standardized authentication and authorization approaches are essential.

**Authentication:** Verifying the identity of an end-user or client application.

**Authorization:** Determining what access or privileges that entity has.

**SMART on openEHR** builds on [OAuth 2.0 Framework](https://tools.ietf.org/html/rfc6749) and optionally [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html#Authentication), allowing third-party applications to securely obtain authorized access to protected healthcare data exposed as APIs by the Platform.

Many applications operate within context of specific Patient or Episode. Therefore, appropriate context selection becomes a critical prerequisite for launching the Application.

---

## 3. Application Registration

Before an Application can integrate with a Platform, it must be registered. This process establishes a trusted relationship between Application Vendor and Platform Vendor.

### Registration Steps

**Application Registration:** Application Vendor submits metadata including:
- Application name, logo, and identifier
- Authorized domains and redirection URIs (`redirect_uri`)
- Supported launch contexts (e.g., patient, practitioner)
- Application type (e.g., confidential or public client)
- Client JSON Web Keys (JWKs) or JWK Set URL
- Requested OAuth 2.0 scopes

**Credential Issuance:** Upon successful registration, Platform issues credentials:
- Unique `client_id` (always required)
- `client_secret` (for confidential clients)
- Optionally, JSON Web Keys (JWKs) or JWK Set URL (`jwks_uri`) for JWT-based client authentication

These credentials enable subsequent OAuth 2.0 flows for authentication and secure, scoped resource access.

### Registration Approach

The [SMART App Launch Framework](https://hl7.org/fhir/smart-app-launch/STU2.1/client-confidential-asymmetric.html#registering-a-client-communicating-public-keys) describes corresponding registration flow, including public key registration via `jwks` or `jwks_uri` for secure client authentication. **SMART on openEHR** adopts a compatible approach, extending these mechanisms for openEHR-based APIs and platforms.

While the [OAuth 2.0 Dynamic Client Registration Protocol](https://tools.ietf.org/html/rfc7591) could formalize this process, current recommendation is handling registration out-of-band in practical ways for both vendors.

**Example:** Platform provides dedicated registration portal where Application Vendors submit applications for review, supporting approval workflows, audit trails, and administrative oversight before issuing credentials, ensuring only vetted applications interact with the Platform.

---

## 4. Service Discovery

A Platform typically exposes multiple service endpoints: OAuth 2.0 endpoints (Authorization, Token), standard data service endpoints (openEHR REST APIs, FHIR APIs), and possibly other standard or proprietary APIs (e.g., DICOMWeb APIs).

**SMART Service Discovery** extends the [FHIR `.well-known/smart-configuration`](https://hl7.org/fhir/smart-app-launch/STU2.1/conformance.html#using-well-known) endpoint definition. It allows a Platform to advertise authentication endpoints, SMART capabilities, and available services.

### Configuration Endpoint

The configuration endpoint should be always available relative to Platform base URL:

- Base URL: `https://platform.example.com`
- Configuration endpoint: `https://platform.example.com/.well-known/smart-configuration`

For base URL with path segment: `https://platform.example.com/gateway/v1`
- Configuration at: `https://platform.example.com/gateway/v1/.well-known/smart-configuration`

**Key Difference from FHIR:** Unlike FHIR's `.well-known/smart-configuration` (defined relative to FHIR server base URL), this specification defines this endpoint relative to Platform base URL (gateway). This allows Platform to advertise service capabilities beyond FHIR APIs, including openEHR REST APIs and other APIs not part of FHIR server itself.

**Recommendation:** Platform vendors should maintain compatibility with SMART FHIR applications by ensuring consistent `issuer` and exposing FHIR API at same base URL when feasible.

### Response Format

Responses to `/.well-known/smart-configuration` endpoint must be served with `application/json` MIME type.

```json
{
  "issuer": "https://platform.example.com",
  "jwks_uri": "https://platform.example.com/.well-known/jwks.json",
  "authorization_endpoint": "https://platform.example.com/auth/authorize",
  "token_endpoint": "https://platform.example.com/auth/token",
  "services": {
    "org.openehr.rest": {
      "baseUrl": "https://platform.example.com/openehr/rest/v1",
      "description": "The openEHR REST APIs baseUrl",
      "documentation": "https://example.com/openehr/docs",
      "openapi": "https://example.com/openehr/rest/v1/openapi.json"
    },
    "org.fhir.rest": {
      "baseUrl": "https://platform.example.com/",
      "description": "The FHIR APIs baseUrl"
    },
    "com.amazon.aws.s3.rest": {
      "baseUrl": "https://s3.example.com/storage",
      "documentation": "https://example.com/s3/docs",
      "openapi": "https://example.com/s3/openapi.json"
    },
    "com.example.demographics": {
      "baseUrl": "https://demographics.example.com/rest"
    }
  },
  "token_endpoint_auth_methods_supported": [
    "client_secret_basic",
    "private_key_jwt"
  ],
  "grant_types_supported": [
    "authorization_code",
    "client_credentials"
  ],
  "registration_endpoint": "https://platform.example.com/auth/register",
  "scopes_supported": [
    "openid",
    "profile",
    "launch",
    "launch/patient",
    "patient/*.rs",
    "user/*.rs",
    "offline_access"
  ],
  "response_types_supported": ["code"],
  "management_endpoint": "https://platform.example.com/user/manage",
  "introspection_endpoint": "https://platform.example.com/user/introspect",
  "revocation_endpoint": "https://platform.example.com/user/revoke",
  "code_challenge_methods_supported": ["S256"],
  "capabilities": [
    "launch-ehr",
    "permission-patient",
    "permission-v2",
    "client-public",
    "client-confidential-symmetric",
    "context-ehr-patient",
    "sso-openid-connect",
    "context-openehr-ehr",
    "openehr-permission-v1",
    "launch-base64-json"
  ]
}
```

### 4.1. Authentication Endpoints

The following attributes in `.well-known/smart-configuration` must match those defined in OAuth 2.0 + [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig) and [FHIR SMART metadata](https://www.hl7.org/fhir/smart-app-launch/conformance.html#metadata) specifications:

- `issuer`
- `jwks_uri`
- `authorization_endpoint`
- `grant_types_supported`
- `token_endpoint`
- `token_endpoint_auth_methods_supported`
- `registration_endpoint`
- `scopes_supported`
- `management_endpoint`
- `response_types_supported`
- `introspection_endpoint`
- `revocation_endpoint`
- `capabilities`
- `code_challenge_methods_supported`

### 4.2. Services

In addition to FHIR-specific metadata, the configuration endpoint response must include the `services` section describing available service interfaces exposed by the Platform. This section enables Applications to dynamically discover Platform APIs with respective base URLs, descriptions, and documentation links.

The `services` is a hash map where each key is a reverse domain name uniquely identifying a service (e.g., `org.openehr.rest`), and the corresponding value contains service-specific metadata and base URL. This enables flexible, extensible declaration of multiple coexisting APIs.

**Required Services:**
- `org.openehr.rest`: Base URL of openEHR REST APIs **(required)**

**Recommended Services:**
- `org.fhir.rest`: Base URL of FHIR APIs **(recommended)**

**Additional Services:**
- `org.dicomstandard.dicomweb.rest`: DICOMWeb REST API endpoint
- `com.amazon.aws.s3.rest`: AWS S3-compatible REST API
- `com.example.demographics`: Vendor-specific demographic service

**Service Definition Fields:**
- `baseUrl`: Absolute URL to API root **(required)**
- `description`: Human-readable service description
- `version`: Service API version
- `documentation`: Link to service documentation
- `openapi`: Link to OpenAPI (Swagger) definition

**Example Service Definition:**

```json
{
  "org.openehr.rest": {
    "baseUrl": "https://platform.example.com/openehr/rest/v1",
    "description": "The openEHR REST API baseUrl",
    "documentation": "https://platform.example.com/openehr/docs",
    "openapi": "https://platform.example.com/openehr/rest/v1/openapi.json"
  }
}
```

### 4.3. Capabilities

The `capabilities` section advertises supported SMART features as an array value. In addition to those defined in the original [SMART App Launch](https://hl7.org/fhir/smart-app-launch/STU2.1/conformance.html#capabilities) framework, the following capabilities extend the list for openEHR platforms:

| Capability | Description |
|-----------|-------------|
| `context-openehr-ehr` | Supports EHR-level launch context, requested via `launch/patient` scope and conveyed via `ehrId` token claim |
| `context-openehr-episode` | Supports Episode-level context, requested via `launch/episode` scope conveyed via `episodeId` (experimental) |
| `openehr-permission-v1` | Supports fine-grained scopes and authorization scheme over openEHR resources |
| `launch-base64-json` | Supports encoding launch context as base64-encoded JSON object in `launch` parameter |

---

## 5. Application Types

The appropriate authentication flow depends on client Application type, particularly its ability to securely manage credentials and the nature of its interaction with users or backend services. **SMART on openEHR** defines two fundamental client types based on credential handling capabilities, further distinguished by their interaction model.

### 5.1. Classified by Credential Handling

Based on ability to securely manage secrets or secure client authentication using other means:

**Confidential Applications:**
- Can securely hold credentials such as `client_secret` or private keys
- Includes backend services, server-side web applications, and applications using hardware security modules or additional technology for higher security

**Public Applications:**
- Cannot securely store secrets
- Includes native mobile apps and single-page web applications (SPAs) running in browsers
- Must rely on flows not requiring client credentials (e.g., PKCE)

The distinction between public and confidential clients is essential in determining appropriate OAuth2 flow and impacts which tokens can be safely issued and under what conditions.

### 5.2. Classified by User Interaction

Applications are also classified by context and end-user nature:

**Patient-facing Applications:**
- Used directly by patient or launched by practitioner in context of specific patient
- Optionally tied to particular episode of care

**Practitioner-facing Applications:**
- Used by healthcare professionals
- May operate within or outside context of specific patient or episode

**Backend Services:**
- Operate autonomously without direct user interaction
- Typically used for system-to-system communication or background processing
- Examples: synchronization, analytics, alerts

---

## 6. Authentication

In line with the SMART framework, authentication is typically an integral part of the OAuth 2.0 authorization process. For verifying end-user identity, an external identity provider is expected, typically using [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html#Authentication). While OIDC is recommended, exact identity verification mechanisms are implementation-specific and outside this specification's scope.

### 6.1. Supported Authentication Flows

Client Applications may authenticate with the Platform using one of the following OAuth2-compatible flows. The choice depends on [client application type](#5-application-types) (public vs. confidential) and desired security posture.

| Flow | Suitability | Description |
|------|------------|-------------|
| **Authorization Code Grant with PKCE** | Public clients | Recommended for public clients (browser/mobile apps); does not require client secret; mitigates interception risks |
| **Authorization Code Grant with client_secret** | Confidential clients | Suitable for confidential clients (backend web applications) capable of securely storing secrets |
| **Client Credentials Grant** | Backend services | Used when no end-user involved (background system-to-system communication) |
| **JWT Bearer Token Grant** | Confidential clients | Preferred for confidential clients using asymmetric keys (JSON Web Keys) to authenticate via signed JWTs per [JSON Web Signature (JWS)](https://tools.ietf.org/html/rfc7515) |

Platform implementation must clearly advertise which flows are supported in its `.well-known/smart-configuration` metadata document. This allows clients to dynamically determine authentication and token obtaining approaches.

### 6.2. Client Authentication Methods

SMART distinguishes two main authentication methods for confidential clients:

**Asymmetric Authentication (Preferred):**
- Avoids transmitting shared secrets
- Leverages either Client Credentials Grant or JWT Bearer Token Grant
- Uses public/private key pairs (e.g., JSON Web Keys) for authentication

**Symmetric Authentication:**
- Simpler but less secure approach
- Uses pre-shared `client_secret` for authentication
- Typically used with Authorization Code Grant flow

### 6.3. Deprecated Flows

The following OAuth 2.0 flows are discouraged and MUST NOT be used within SMART on openEHR due to security concerns:

| Flow | Reason |
|------|--------|
| **Implicit Grant** | Exposes tokens in URL; lacks proper confidentiality guarantees |
| **Resource Owner Password Credentials Grant** | Involves direct transmission of user credentials; does not support modern identity federation |

### 6.4. Flow Recommendations

**For Public Clients:**
- Must use Authorization Code Grant with PKCE exclusively
- Offers strong security without requiring client secrets

**For Confidential Clients:**
- May use Authorization Code Grant with PKCE, or Authorization Code Grant with `client_secret`
- Choice depends on security infrastructure

**For Backend Services:**
- Must use confidential client
- Recommended to use JWT Bearer Token Grant with JWS (preferred) or Client Credentials Grant
- Choice depends on trust level and identity requirements

### Recommended Flows by Scenario

| Application Example | Client Type | User Interaction Type | Recommended Flow |
|-------|------------|------|----------|
| Single Page Web Application for Patient Portal | Public | Patient-facing | Authorization Code Grant with PKCE |
| Mobile Application for Tracking Heart Rate | Public | Patient-facing | Authorization Code Grant with PKCE |
| Web Application with Backend for Cardiology Management | Confidential | Practitioner-facing | Authorization Code Grant with PKCE or Authorization Code Grant with `client_secret` |
| Realtime Alert System for Hospital | Confidential | Backend service | JWT Bearer Token Grant with JWS or Client Credentials Grant |

---

## 7. Authorization

Both patient-facing and practitioner-facing applications have specific authorization requirements extending beyond core [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749) capabilities. Depending on invocation method, SMART Framework [defines two launch](https://hl7.org/fhir/smart-app-launch/STU2.1/app-launch.html#smart-authorization--fhir-access-overview) contexts, enabling apps to obtain contextual access to clinical data based on user and session:

### Launch Contexts

**Standalone Launch:**
- Application initiated directly by end-user, outside running Platform session context
- User may visit `https://myapp.example.com` and select desired Platform instance
- Application then begins SMART authorization sequence using selected Platform's base URL and `.well-known/smart-configuration` metadata

**Embedded iFrame Launch:**
- Application launched from within Platform's user interface (typically within `iframe` within a Portal)
- Platform passes `iss` (issuer) and `launch` parameters to Application
- Example: `https://myapp.example.com?launch=123&iss=https://platform.example.com`
- `iss` identifies the Platform (FHIR server); `launch` parameter conveys session-specific information

**Note:** To avoid confusion with openEHR Reference Model's `EHR` class, this document refers to **EHR Launch** as **Embedded iFrame Launch**.

### 7.1. SMART Authorization Flow

SMART framework builds on [OAuth 2.0 Authorization Code Flow](https://tools.ietf.org/html/rfc6749#section-4.1) and defines several SMART-specific launch enhancements for [obtaining the authorization code](https://hl7.org/fhir/smart-app-launch/STU2.1/app-launch.html#obtain-authorization-code):

**Flow Steps:**

1. **Redirect to Authorization Endpoint:**
   - Application redirects user to Platform's `authorization_endpoint`
   - Includes SMART-specific query parameters: `aud`, `launch`, `scope`, `state`, `redirect_uri`, etc.

2. **User Authentication and Consent:**
   - Authorization Server authenticates user
   - Validates requested scopes
   - (If allowed) issues authorization `code` to Application via `redirect_uri`

3. **Exchange Code for Tokens:**
   - Application exchanges authorization `code` for `access_token` and optionally `id_token` and `refresh_token`
   - POST to Platform's `token_endpoint`

### 7.2. Context Selection

In **Standalone Launch**, a client Application can request Platform assistance with context selection, provided relevant [capabilities](#43-capabilities) are supported by Platform. Most patient-facing and practitioner-facing applications require Platform to supply additional context during authorization. This contextual data may include:

- openEHR EHR ID
- FHIR Patient ID
- Episode ID
- Other identifiers

Context is typically valid for duration of user session.

**Purpose:** Pre-load or configure Application to operate within relevant clinical scope. Platform may determine context automatically based on authenticated user, or may prompt user (e.g., via selection screen) after consent page if multiple valid contexts are possible.

**Requesting Context:** To explicitly request openEHR-related launch context, Application must include following SMART-defined **scopes** in authorization request:

| Scope | Meaning |
|-------|---------|
| `launch/patient` | Application requires patient context at launch (both FHIR `Patient` resource and corresponding openEHR `EHR` instance). For Standalone Launch, user should be prompted to select openEHR `EHR` |
| `launch/episode` | Application requires episode context at launch (Experimental) |

**Token Response:** Platform returns resolved context information in token response, alongside `access_token` and optionally `id_token`. In addition to standard [SMART App Launch context attributes](https://hl7.org/fhir/smart-app-launch/STU2.1/scopes-and-launch-context.html#launch-context-arrives-with-your-access_token), following openEHR-specific parameters may be included:

| Parameter | Meaning |
|-----------|---------|
| `ehrId` | Unique identifier of openEHR `EHR` instance associated with selected FHIR `Patient` resource |
| `episodeId` | Identifier of selected clinical episode (if applicable; experimental) |

Application may use these parameters to tailor user interface and functionality to selected clinical context.

**Note:** While this specification defines openEHR-specific launch parameters, standard SMART launch scopes and context attributes remain compatible and may be used in parallel for interoperability purposes. These are referenced from [SMART App Launch Framework](https://hl7.org/fhir/smart-app-launch/STU2.1/scopes-and-launch-context.html), but their use is not normative in this specification.

### 7.3. Embedded iFrame Launch

Many practitioner-facing applications, and in some cases patient-facing applications, are integrated directly within web-based front-end (e.g., clinical portal or patient portal) using dedicated component.

In **Embedded iFrame Launch**, Platform initiates application by embedding it in `iFrame` and passing key parameters directly in URL:

- `launch`: Opaque identifier or [token](#91-launch-parameter-as-a-token) encoding relevant launch context (e.g., patient, EHR ID, episode)
- `iss`: Issuer URL representing Platform's base endpoint (for SMART on FHIR compatibility, should also serve as FHIR base URL)

**Example:**
```
https://myapp.example.com?launch=123&iss=https://platform.example.com
```

**Flow Steps:**

1. **Retrieve SMART Configuration:**
   - Application uses `iss` value to retrieve SMART configuration document
   - Endpoint: `{iss}/.well-known/smart-configuration`

2. **Initialize Authorization Flow:**
   - Configuration document provides important endpoints including `authorization_endpoint`
   - Application uses this information to initiate [OAuth 2.0 Authorization Code Flow](https://tools.ietf.org/html/rfc6749#section-1.3.1)
   - Includes `launch` parameter in authorization request

**Supporting Interaction Model:**

To support this interaction pattern, following SMART-defined **scope** must be included in authorization request:

| Scope | Meaning |
|-------|---------|
| `launch` | Permission to obtain launch context when Application is launched from EHR (Embedded iFrame Launch). Must be accompanied by `launch` parameter in authorization request |

---

## 8. Scopes

Authorization is governed by **scopes**, which define the type and extent of access that a client Application is requesting from the Platform.

As specified in [OAuth 2.0 Section 3.3](https://tools.ietf.org/html/rfc6749#section-3.3), scopes are passed during authorization request and evaluated by Platform when issuing access tokens. Platform must validate requested scopes against:

- Application registration metadata
- Applicable access control policies
- Authenticated user's permissions

**SMART on openEHR** aligns with FHIR's [SMART App Launch Framework](https://hl7.org/fhir/smart-app-launch/STU2.1/scopes-and-launch-context.html), where scopes serve three main purposes:

- **Resource Access:** Grant access to specific resource types (e.g., `patient/composition-*.rs`)
- **Context Declaration:** Request specific launch contexts (e.g., `launch/patient`)
- **Identity Claims:** Enable OpenID Connect scopes (e.g., `openid`) to identify user

### 8.1. Resource Scopes

Application can request Platform resource access using scope syntax:

```
<compartment>/<resource>.<permission>
```

Where:

- **`<compartment>`** indicates scope of access delegation:
  - `patient`: Access limited to current EHR; Patient present in context
  - `user`: Access granted based on authenticated user's permissions
  - `system`: Access granted to backend applications acting without user context

- **`<resource>`** identifies openEHR or derived asset being accessed

- **`<permissions>`** specifies allowed operations

### Supported Compartments

| Compartment | Description |
|------------|-------------|
| `patient` | For applications acting in context of specific patient/EHR. Access restricted to data within that patient's EHR |
| `user` | For applications acting on behalf of logged-in user (e.g., practitioner). Access subject to user's security profile, not limited to Patient in context (if any present) |
| `system` | For server-to-server integrations or backend services, typically using client credentials, based on pre-configured client-specific policy. Grants access across all data |

### Supported openEHR REST API Resource Types

Following [openEHR REST APIs](https://specifications.openehr.org/releases/ITS-REST/development) `<resource>` types are supported for use in scopes:

- `template-<templateId>` - Access to operational templates matching `<templateId>` expression
- `composition-<templateId>` - Access to compositions of given template matching `<templateId>` expression
- `aql-<queryName>` - Access to pre-defined (matching `<queryName>` expression) or ad-hoc (wildcard `*`) AQL queries

### Wildcard and Pattern-Based Matching

The `<templateId>` and `<queryName>` support wildcard and pattern-based matching using `*` and `**`:

| Pattern | Matches |
|---------|---------|
| `MyHospital::Template.v0` | Template exact match only |
| `org.openehr::bloodpressure.v1` | Query exact match only |
| `*::Template.v0` | Template.v0 from any namespace |
| `MyHospital::*` | Any template within MyHospital namespace |
| `*` | All available templates or queries |

### Permission Expressions

Following permission expressions are supported:

- `c` - Create
- `r` - Read
- `u` - Update
- `d` - Delete
- `s` - Search or execute (e.g., for AQL queries)

### Scope Examples

| Scope | Description |
|-------|-------------|
| `patient/composition-<templateId>.crud` | Full CRUD access to compositions matching `<templateId>` in current patient's EHR |
| `user/composition-<templateId>.crud` | Full CRUD access to compositions accessible by user |
| `system/composition-<templateId>.crud` | Unrestricted CRUD access to compositions across entire system |
| `user/template-<templateId>.crud` | Create and manage templates accessible to user |
| `system/template-<templateId>.crud` | Full system-wide template management |
| `patient/aql-<queryName>.rs` | Execute and read AQL queries on patient's EHR data |
| `user/aql-<queryName>.cruds` | Full access to user-permitted AQL definitions or ad-hoc queries |
| `system/aql-<queryName>.cruds` | System-wide access to AQL queries and endpoints |

**Note:** Wildcard-based scopes (e.g., `*` or `**`) should be used cautiously and only when absolutely necessary, as they imply broad access. For example, `system/aql-*.rs` would grant access to all registered and ad-hoc AQL queries system-wide.

---

## 9. Experimental Features

The following concepts and aspects are considered experimental.

**Note for Implementers:** Treat use as provisional and subject to change in future versions of this specification.

### 9.1. Launch Parameter as a Token

To support efficient and context-rich embedded launches, it is **recommended** that the `launch` parameter be a **base64-encoded JSON object** containing launch context attributes such as:

- `ehrId` - openEHR EHR identifier
- `patient` - FHIR Patient ID (if available)
- `episodeId` - Clinical episode ID (optional)

This allows Application to initialize its interface with full context and potentially bypass full authorization cycle if already authenticated. This significantly improves user experience, for instance, when switching patients within same embedded session.

**Platforms supporting this optimization** should advertise following capability in `/.well-known/smart-configuration` response:

- `launch-base64-json`: May be used to deliver context (including `episodeId`) in base64-encoded JSON format for embedded iFrame launches

### 9.2. Experimental: Episode Context

The **Episode** concept represents a bounded period of care or clinical workflow, such as:
- Hospital admission
- Treatment course
- Referral

It serves as logical container for grouping related clinical activities, encounters, and observations. Particularly relevant for workflows requiring context maintenance across multiple interactions or systems.

In SMART on openEHR context, Episode selection and usage is considered **experimental**. While openEHR specification outlines Episode concept, formal resource definitions and operational semantics are still evolving. As openEHR specification evolves to formalize Episode as first-class resource, following enhancements may be introduced:

- Standardized resource representation of Episode type or new archetype
- Extended query support for filtering by Episode
- Improved UI/UX support in authorization servers for Episode selection
- FHIR mapping for Episode-related concepts

#### 9.2.1. Scopes and Capabilities

To request Episode context during authorization flow, following scope may be included in authorization request:

| Scope | Description |
|-------|-------------|
| `launch/episode` | Requests Episode context at launch time. If launching outside EHR, prompts Platform to determine or allow selection of Episode relevant to session |

Platforms supporting Episode context should advertise following capability in `/.well-known/smart-configuration` response:

- `context-openehr-episode`: Indicates Platform supports Episode context selection during launch, requested via `launch/episode` scope

#### 9.2.2. Token Response Parameters

When authorization request includes `launch/episode` scope and Platform is capable of resolving Episode, following parameter will be included in token response:

| Parameter | Description |
|-----------|-------------|
| `episodeId` | Identifier of selected or inferred Episode for session. May map to openEHR EHR_STATUS.episode or platform-specific abstraction. Semantics currently implementation-defined |

This value is intended for use by client Application to filter or group clinical data relevant to specific Episode of care.

#### 9.2.3. Launch Scenarios

**Standalone Launch:**
When `launch/episode` scope is included, Platform may prompt user to select Episode or infer it automatically based on session context (e.g., currently admitted case, recent discharge summary, etc.).

**Embedded iFrame Launch:**
Episode context may be embedded in base64-encoded `launch` parameter provided at runtime. This can improve usability by avoiding separate Episode selection prompt during intra-portal navigation.

---

## References

- SMART App Launch - Release 2.1.0 (2021), [https://hl7.org/fhir/smart-app-launch/STU2.1](https://hl7.org/fhir/smart-app-launch/STU2.1)

- The 'About SMART' page on SMART Health IT, [https://smarthealthit.org/about-smart-2/](https://smarthealthit.org/about-smart-2/)

- OAuth 2.0 Authorization Framework, [https://tools.ietf.org/html/rfc6749](https://tools.ietf.org/html/rfc6749)

- OAuth 2.0 Dynamic Client Registration Protocol, [https://tools.ietf.org/html/rfc7591](https://tools.ietf.org/html/rfc7591)

- OpenID Connect (OIDC), [https://openid.net/specs/openid-connect-core-1_0.html#Authentication](https://openid.net/specs/openid-connect-core-1_0.html#Authentication)

- JSON Web Token (JWT) Assertion, [https://tools.ietf.org/html/rfc7523](https://tools.ietf.org/html/rfc7523)

- JSON Web Signature (JWS), [https://tools.ietf.org/html/rfc7515](https://tools.ietf.org/html/rfc7515)

- Best Practices in Authorization for SMART on FHIR EHRs, [https://docs.smarthealthit.org/authorization/best-practices](https://docs.smarthealthit.org/authorization/best-practices)

---

## Document Information

**Issuer:** openEHR Specification Program
**Web:** [specifications.openEHR.org](https://specifications.openehr.org)
**Issues:** [Problem Reports](https://specifications.openehr.org/components/ITS-REST/open_issues)

### License

Creative Commons Attribution-NoDerivs 3.0 Unported.
[https://creativecommons.org/licenses/by-nd/3.0/](https://creativecommons.org/licenses/by-nd/3.0/)

**Copyright (c) 2023 - 2025 The openEHR Foundation**

The openEHR Foundation is an independent, non-profit foundation, facilitating the sharing of health records by consumers and clinicians via open specifications, clinical models and open platform implementations.

---

Last updated 2025-06-18 07:28:52 UTC
