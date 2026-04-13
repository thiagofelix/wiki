# Demographic Information Model

**Issuer**: openEHR Specification Program
**Release**: RM Release-1.1.0
**Status**: STABLE
**Source**: https://specifications.openehr.org/releases/RM/latest/demographic.html
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## 1. Preface

### 1.1 Purpose

This document describes the openEHR Demographic Information Model architecture. Semantics derive from GEHR, ISO 13606, HL7v3 RIM, and work from Australia.

### 1.2 Related Documents

**Prerequisite documents**:
- The openEHR Architecture Overview

**Related model documents**:
- The openEHR Support Information Model
- The openEHR Data Types Information Model

---

## 2. Demographic Package

### 2.1 Overview

The demographic model presents a generalized representation of facts expected in a demographic server, functioning as either standalone or a wrapper service for existing systems (e.g., patient master index). In wrapper implementations, it adds required openEHR semantics, particularly versioning, to existing services.

Design is based on the party and accountability scheme described by Fowler (1997), influenced by clinical adaptations including work from Australia and HL7v3.

**Primary design criteria**:
1. Express attributes and relationships of demographic entities independent of particular clinical involvements
2. Ensure instances serialize unambiguously into EHR Extract
3. Treat each PARTY as self-contained hierarchy (like COMPOSITION objects)
4. Implement PARTY_RELATIONSHIPs correctly to prevent endless traversal during serialization

#### 2.1.1 Archetyping

The model is designed for archetype use, providing generic entities. Every class containing a `_details_:STRUCTURE` attribute is fully archetypable. Archetypes can define:
- Particular kinds of PERSON, ORGANISATION
- Actual ROLE types (healthcare practitioner, nurse)
- PARTY_IDENTITY and ADDRESS variants

#### 2.1.2 Names and Addresses

PARTY_IDENTITY and ADDRESS classes contain only links to details via STRUCTURE class. PARTY_IDENTITY instances (via `_identities_` attribute) express party-owned names: self-declared names (institutions/companies) or socially-derived names (parental/tribal attribution).

Organization-assigned or state-assigned identifiers are recorded in PARTY._details_ structure, not PARTY_IDENTITY.

#### 2.1.3 Party Identification

Organization or state-assigned party identifiers are treated as standard party attributes, recorded in PARTY._details_ structure.

System-level party identifiers are provided via the `_uid_` attribute (type OBJECT_VERSION_ID) of the containing VERSION object.

#### 2.1.4 Party Relationships

Real-world party relationships expressed using PARTY_RELATIONSHIP objects. Relationships are directional via `source` and `target` attributes.

Each involved party includes the relationship in:
- Its `relationships` list (if at source end)
- Its `_reverse_relationships_` list (if at target end)

**Storage semantics**:
- PARTY_RELATIONSHIPs stored as part of source PARTY data
- `relationships` attribute is by-value
- `reverse_relationships`, `source`, and `target` are by-reference
- References use OBJECT_REFs containing HIER_OBJECT_IDs (denoting version containers)

#### 2.1.5 Versioning Semantics

Classes PARTY and descendants ACTOR and ROLE are potentially versioned. A PARTY version includes all compositional parts: identities, contacts, and source party relationships. Each party stored in its own version container.

### 2.2 Class Definitions

#### 2.2.1 PARTY Class

**Class**: `PARTY` (abstract)
**Description**: Ancestor of all party types, including real-world entities and roles. A party is any entity capable of activity participation.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | identities | List<PARTY_IDENTITY> | Identities used by the party (legal name, aliases, nicknames) |
| 0..1 | contacts | List<CONTACT> | Contacts for this party |
| 0..1 | details | ITEM_STRUCTURE | All other details for this party |
| 0..1 | reverse_relationships | List<LOCATABLE_REF> | References to relationships where party is target |
| 0..1 | relationships | List<PARTY_RELATIONSHIP> | Relationships where party is source |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | type(): DV_TEXT | Type of party from inherited `_name_` |

**Invariants**:
- `Type_valid`: `type = name`
- `Contacts_valid`: `contacts /= Void implies not contacts.is_empty`
- `Relationships_validity`: `relationships /= Void implies (not relationships.is_empty and then relationships.for_all (r | r.source = self)`
- `Is_archetype_root`: `is_archetype_root`
- `Uid_mandatory`: `uid /= Void`

#### 2.2.2 VERSIONED_PARTY Class

**Class**: `VERSIONED_PARTY`
**Description**: Static type formed by binding generic parameter of `VERSIONED_OBJECT<T>` to `PARTY`.
**Inheritance**: VERSIONED_OBJECT

#### 2.2.3 ROLE Class

**Class**: `ROLE`
**Description**: Generic description of a role performed by an actor. Roles define responsibilities undertaken by a party for a purpose.
**Inheritance**: PARTY

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | time_validity | DV_INTERVAL<DV_DATE> | Valid time interval for this role |
| 1..1 | performer | PARTY_REF | Reference to actor playing the role |
| 0..1 | capabilities | List<CAPABILITY> | Capabilities of this role |

#### 2.2.4 PARTY_RELATIONSHIP Class

**Class**: `PARTY_RELATIONSHIP`
**Description**: Generic description of a relationship between parties.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | details | ITEM_STRUCTURE | Detailed description of the relationship |
| 1..1 | target | PARTY_REF | Target of relationship |
| 0..1 | time_validity | DV_INTERVAL<DV_DATE> | Valid time interval for this relationship |
| 1..1 | source | PARTY_REF | Source of relationship |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | type(): DV_TEXT | Type of relationship (employment, authority, health provision) |

**Invariants**:
- `Type_validity`: `type = name`

#### 2.2.5 PARTY_IDENTITY Class

**Class**: `PARTY_IDENTITY`
**Description**: An identity owned by a party, such as person name or company name.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | details | ITEM_STRUCTURE | The value of the identity |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | purpose(): DV_TEXT | Purpose of identity (legal, stagename, nickname, tribal name) |

**Invariants**:
- `Purpose_valid`: `purpose = name`

#### 2.2.6 CONTACT Class

**Class**: `CONTACT`
**Description**: Description of a means of contact for a party.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | addresses | List<ADDRESS> | Address alternatives for this contact |
| 0..1 | time_validity | DV_INTERVAL<DV_DATE> | Valid time interval |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | purpose(): DV_TEXT | Purpose for which this contact is used |

#### 2.2.7 ADDRESS Class

**Class**: `ADDRESS`
**Description**: Address of contact, which may be electronic or geographic.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | details | ITEM_STRUCTURE | Archetypable structured address |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | type(): DV_TEXT | Type of address (electronic, locality) |

#### 2.2.8 CAPABILITY Class

**Class**: `CAPABILITY`
**Description**: Capability of a role, such as EHR modifier or healthcare provider.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | credentials | ITEM_STRUCTURE | Qualifications of the role performer |
| 0..1 | time_validity | DV_INTERVAL<DV_DATE> | Valid time interval for credentials |

#### 2.2.9 ACTOR Class

**Class**: `ACTOR` (abstract)
**Description**: Ancestor of all real-world types, including people and organizations. An actor is any real-world entity capable of taking on a role.
**Inheritance**: PARTY

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | languages | List<DV_TEXT> | Languages which can be used to communicate |
| 0..1 | roles | List<PARTY_REF> | Identifiers of version containers for each role |

#### 2.2.10 PERSON Class

**Class**: `PERSON`
**Description**: Generic description of persons.
**Inheritance**: ACTOR

#### 2.2.11 ORGANISATION Class

**Class**: `ORGANISATION`
**Description**: Generic description of organizations. A legally constituted body whose existence generally outlives existence of parties considered part of it.
**Inheritance**: ACTOR

#### 2.2.12 GROUP Class

**Class**: `GROUP`
**Description**: A real-world group of parties created by another party, usually an organization, for specific purpose. Typical clinical example: specialist care team.
**Inheritance**: ACTOR

#### 2.2.13 AGENT Class

**Class**: `AGENT`
**Description**: Generic concept of any kind of agent, including devices and software systems, but not humans or organizations.
**Inheritance**: ACTOR

---

## 2.3 Instance Examples

### 2.3.1 Parties

#### 2.3.1.1 Person

A PERSON with home and work contact information. Separate archetypes exist for PERSON, each ADDRESS, and each PARTY_IDENTITY.

#### 2.3.1.2 Health Care Facility

A healthcare facility with organizational identity and contact information.

#### 2.3.1.3 Group

A cardiac surgery team in a hospital. The group includes head surgeon, anesthetist, assistant surgeon and others. Each team member has employment relationship with hospital.

### 2.3.2 Relationships

#### 2.3.2.1 Patient

A patient relationship between person (source) and healthcare organization (target). Can be represented with both parties acting through roles with associated credentials.

---

## References

- Fowler, M. (1997). _Analysis Patterns: Reusable Object Models_. Addison Wesley.
