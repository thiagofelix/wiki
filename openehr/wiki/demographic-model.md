---
title: Demographic Model
type: entity
sources:
  - raw/rm-demographic.md
  - raw/its-rest-demographic.md
created: 2026-04-13
updated: 2026-04-13
---

# Demographic Information Model

The Demographic IM defines a generalized representation of people, organizations, and their relationships. It operates separately from the EHR, either as a standalone demographic server or as a wrapper over existing systems (e.g., patient master index).

**Release**: RM 1.1.0 (STABLE)

## Class Hierarchy

```
PARTY (abstract) ─── LOCATABLE
├── ACTOR (abstract)
│   ├── PERSON
│   ├── ORGANISATION
│   ├── GROUP
│   └── AGENT
└── ROLE
```

Supporting classes:
- PARTY_IDENTITY — names owned by a party
- PARTY_RELATIONSHIP — directional relationships
- CONTACT — contact means
- ADDRESS — specific address
- CAPABILITY — what a role can do

## PARTY

Abstract ancestor of all demographic entities. Attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `identities` | List\<PARTY_IDENTITY\> | Names: legal name, aliases, nicknames |
| `contacts` | List\<CONTACT\> | Contact information |
| `details` | ITEM_STRUCTURE | All other archetypable details |
| `relationships` | List\<PARTY_RELATIONSHIP\> | Relationships where party is source |
| `reverse_relationships` | List\<LOCATABLE_REF\> | Relationships where party is target |

Key invariant: `uid` is mandatory (unlike most LOCATABLE descendants).

## ACTOR Subtypes

| Class | Description | Examples |
|-------|-------------|----------|
| **PERSON** | Individual human being | Patient, clinician, administrator |
| **ORGANISATION** | Formal organizational entity | Hospital, clinic, health authority |
| **GROUP** | Group of actors | Care team, department |
| **AGENT** | Software agent or device | Automated system, monitoring device |

ACTOR adds:
- `roles` — List\<PARTY_REF\> referencing ROLE objects
- `languages` — languages the actor can communicate in

## ROLE

Responsibilities undertaken by an ACTOR:
- `performer` — PARTY_REF to the actor playing the role
- `capabilities` — List\<CAPABILITY\> defining what the role can do
- `time_validity` — when the role is active

Archetypes define specific role types: healthcare practitioner, nurse, general practitioner, patient, etc.

## Relationships

PARTY_RELATIONSHIP models directional relationships:
- `source` — PARTY_REF to the source party
- `target` — PARTY_REF to the target party
- `details` — ITEM_STRUCTURE for relationship specifics
- `time_validity` — when the relationship holds

Storage: relationships are stored as part of the **source** party's data.

## Names and Addresses

### PARTY_IDENTITY

Party-owned names (not assigned identifiers):
- Person: legal name, maiden name, nickname, tribal name
- Organisation: official name, trading name

Details stored in an ITEM_STRUCTURE, fully archetypable.

### CONTACT and ADDRESS

Contact means for a party:
- CONTACT groups addresses by purpose (home, work, vacation)
- ADDRESS contains the actual address details in an ITEM_STRUCTURE
- Both have optional `time_validity` for temporal scoping

### Identification

Organization/state-assigned identifiers (medical record number, SSN) go in `PARTY.details`, **not** in PARTY_IDENTITY. System-level identifiers come from the VERSION object's `uid`.

## Versioning

PARTY and its descendants are versioned via VERSIONED_PARTY. A party version includes all compositional parts: identities, contacts, and source relationships. Each party lives in its own version container.

## EHR Integration

The EHR references demographics via PARTY_PROXY objects in the [[common-information-model]]:
- PARTY_SELF — the record subject (patient)
- PARTY_IDENTIFIED — other parties (clinicians, organizations)
- PARTY_RELATED — parties with stated relationship to patient

This separation enables anonymous EHRs (no demographic link) and flexible identity management.

## REST API

The openEHR Demographic REST API (currently in DEVELOPMENT status) provides RESTful endpoints for managing demographic entities under the `/demographic/` path. Each party type -- AGENT, GROUP, ORGANISATION, PERSON, and ROLE -- supports full CRUD operations (POST, GET, PUT, DELETE) with identical request/response patterns.

Key capabilities include:

- **Version history**: Retrieve the full revision history of any party, or get the version active at a specific point in time.
- **Contributions**: Record batches of demographic changes as a single contribution for auditability.
- **ITEM_TAG metadata**: Associate, retrieve, and remove metadata tags on demographic records and their versions.
- **Optimistic locking**: Concurrent modification protection via `If-Match`/`ETag` headers.
- **Simplified formats**: Supports `application/openehr.wt.flat+json` and `application/openehr.wt.structured+json` in addition to standard JSON and XML.

See [[rest-api]] for the full endpoint listing and details on content negotiation.
