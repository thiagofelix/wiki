# Simplified Formats for openEHR Data

**Issuer:** openEHR Specification Program
**Release:** ITS-REST development
**Status:** STABLE
**Revision:** [latest_issue]
**Date:** [latest_issue_date]
**Keywords:** JSON, REST, web template, simplified data, flat, structured

(c) 2019 - 2025 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Acknowledgements](#acknowledgements)
2. [Preface](#preface)
3. [Overview](#overview)
4. [Design Rationale](#design-rationale)
5. [Basic Concepts](#basic-concepts)
6. [RM Mappings](#rm-mappings)
7. [Context Information](#context-information)

---

## Acknowledgements

### Primary Author

The specification builds on Web Template serialization developed by **Better d.o.o.** (formerly Marand, Slovenia) and further documented by the **EHRbase** implementation as "Simplified Data Template."

### Contributors

Notable contributors include Thomas Beale (Ars Semantica), Christian Chevalley (EtherCIS), Borut Fabjan and Bostjan Lah (Better), Ian McNicoll (FreshEHR), Bjorn Naess (DIPS), and others from the openEHR community.

### Trademarks

'openEHR' is a registered trademark of the openEHR Foundation.

---

## Preface

### Purpose

This specification defines **Simplified Formats** as JSON representations for openEHR data instances. These formats offer "a more accessible way to create and manipulate content compared to canonical formats, making it easier for developers new to openEHR."

### Status

The specification is STABLE. Development versions are available at the official specifications repository.

### Feedback

Feedback can be submitted via:
- [openEHR ITS forum](https://discourse.openehr.org/c/specifications/its)
- [Problem Report tracker](https://specifications.openehr.org/components/ITS-REST/open_issues)

### Conformance

Conformance testing follows the same processes as other openEHR serialization formats, with the format indicated via HTTP `Content-Type` headers.

---

## Overview

### Introduction

The serialization format uses **Web Template (WT)** as a JSON representation employing simplified field identifiers instead of canonical archetype paths. Two structural variants exist:

- **Flat** - Flattened key-value structure
- **Structured** - Hierarchical JSON objects

### Scope

**Covered:**
- Flat and Structured format structure and syntax
- Field identifier generation rules
- Context data representation
- RM attributes handling
- Mapping between Simplified Formats and canonical openEHR RM
- Serialization and deserialization requirements

**Not Covered:**
- Web Template as a resource
- Archetype technology
- Storage or indexing strategies

### MIME Types

| Format | MIME Type |
|--------|-----------|
| Flat | `application/openehr.wt.flat+json` |
| Structured | `application/openehr.wt.structured+json` |

### Relationship to Other Specifications

The format relates to:
- **openEHR Reference Model** - Serialized instances represent valid RM structures
- **Operational Templates (OPT)** - Field identifiers generated from OPT definitions
- **AQL** - Instances include AQL paths for query integration
- **Canonical JSON/XML** - Alternative serialization convertible to canonical formats

---

## Design Rationale

### Background

OpenEHR information models operate across multiple layers: the Reference Model (RM) and domain-level models expressed through archetypes and templates. The RM is designed with two computational goals: self-standing data instances and regular, predictable software behavior.

### Canonical Format

"Canonical" means fully expressed instance data with containment structures following the RM, all mandatory fields present, attributes named per the RM, and cardinalities respecting the RM.

#### Canonical JSON Example

```json
{
  "_type": "COMPOSITION",
  "name": {
    "_type": "DV_TEXT",
    "value": "Blood_Pressure_Demo.v0"
  },
  "archetype_details": {
    "archetype_id": {
      "value": "openEHR-EHR-COMPOSITION.encounter.v1"
    },
    "template_id": {
      "value": "Blood_Pressure_Demo.v0"
    },
    "rm_version": "1.0.4"
  },
  "language": {
    "_type": "CODE_PHRASE",
    "terminology_id": {
      "_type": "TERMINOLOGY_ID",
      "value": "ISO_639-1"
    },
    "code_string": "en"
  },
  "territory": {
    "_type": "CODE_PHRASE",
    "terminology_id": {
      "_type": "TERMINOLOGY_ID",
      "value": "ISO_3166-1"
    },
    "code_string": "DE"
  }
}
```

#### The Challenge

Canonical formats present challenges:

1. **Steep learning curve** - Understanding full RM hierarchy required
2. **Verbose structures** - Even simple data needs extensive nesting
3. **Type specifications** - Every object requires `_type` declarations
4. **Boilerplate repetition** - Many fields repeated throughout

These challenges particularly affect form-based applications and limited-scope use cases.

### Historical Formats

**Template Data Schema (TDS):** XSD-based format developed by Ocean Health Systems, transforming `.oet` files into XML Schemas.

**ECISFLAT:** JSON-based alternative from EtherCIS using AQL-style paths based on archetype node codes.

**Web Template (WT):** Developed by Better, representing radical simplification using programmer-friendly paths with JSON expression.

### Simplified JSON Formats

These formats introduce:
- Node IDs generated from human-readable names
- Separation of context data (`ctx/` prefix)
- Elimination of intermediate RM structures
- Direct element-to-value mapping
- Optional RM attributes with underscore prefix

#### Flat Format Example

```json
{
  "blood_pressure_demo.v0/category|value": "event",
  "blood_pressure_demo.v0/category|code": "433",
  "blood_pressure_demo.v0/context/start_time": "2022-02-03T04:05:06",
  "blood_pressure_demo.v0/blood_pressure/any_event:0/systolic|unit": "mm[Hg]",
  "blood_pressure_demo.v0/blood_pressure/any_event:0/systolic|magnitude": 154.0
}
```

#### Structured Format Example

```json
{
  "blood_pressure_demo.v0": {
    "category": [{
      "|value": "event",
      "|code": "433"
    }],
    "blood_pressure": [{
      "any_event": [{
        "systolic": [{
          "|unit": "mm[Hg]",
          "|magnitude": 154.0
        }]
      }]
    }]
  }
}
```

### Requirements

For viability, simplified formats must meet these requirements:

1. **Abstraction capability** - Abstract structural complexity where appropriate
2. **Machine generability** - Completely generated from Operational Templates
3. **Bidirectional conversion** - Routinely convertible to/from canonical format
4. **Template specificity** - Field identifiers derived from and validated against templates
5. **Semantic preservation** - All clinical semantics preserved despite simplification

---

## Basic Concepts

### Web Template Metadata

A Web Template includes:
- Simplified node identifiers
- AQL paths for all elements
- Input type definitions for data entry
- Localized labels and descriptions
- Multiplicity constraints

### Field Identifiers

Hierarchical field identifiers comprise:

1. **Node IDs** - Generated from archetype node names
2. **Path separators** - Forward slash (`/`) between levels
3. **Instance indicators** - Colon notation (`:0`, `:1`) for repeating elements
4. **Attribute suffixes** - Pipe notation (`|magnitude`, `|unit`)
5. **RM attribute prefix** - Underscore (`_`) for optional RM attributes
6. **Raw canonical JSON** - `|raw` attribute for embedding canonical JSON

Example: `vital_signs/body_temperature:0/any_event:0/temperature|magnitude`

#### Node ID Generation Rules

Algorithm for generating node IDs from archetype node names:

1. Replace non-alphanumeric characters (except `_`, `.`, `-`) with underscore
2. Consolidate multiple consecutive underscores to single underscore
3. Convert to lowercase
4. Remove leading and trailing underscores
5. Use "id" if result is empty
6. Prepend "a" if result starts with digit
7. Append numeric suffix if needed for uniqueness

| Original Name | Generated ID |
|---------------|--------------|
| Body temperature | body_temperature |
| Problem/diagnosis | problem_diagnosis |
| Blood Pressure | blood_pressure |
| 1st visit | a1st_visit |

#### Path Construction

Full paths concatenate parent node IDs with forward slashes:

```
composition_id/section_id/observation_id/element_id
```

#### Instance Indexing

Multiple instances use colon notation:

```
node_id:0  # First instance
node_id:1  # Second instance
```

#### Attribute Suffixes

| RM Type | Suffix | Description |
|---------|--------|-------------|
| DV_QUANTITY | `|magnitude` | Numeric value |
| DV_QUANTITY | `|unit` | Unit of measure |
| DV_CODED_TEXT | `|code` | Terminology code |
| DV_CODED_TEXT | `|value` | Display term |
| DV_CODED_TEXT | `|terminology` | Terminology ID |
| PARTY_IDENTIFIED | `|id` | ID value |
| PARTY_IDENTIFIED | `|id_namespace` | Namespace |

#### RM Attributes Prefix

Optional RM attributes use underscore prefix (`_attributeName`):

```json
{
  "path/observation:0/_uid": "9fcc1c70-9349-444d-b9cb-8fa817697f5e"
}
```

Examples with `_link` and `_normal_range`:

```json
{
  "path/observation:0/_link:0|type": "problem",
  "path/observation:0/_link:0|target": "ehr://problem-123",
  "vital_signs/temperature:0/value/_normal_range/lower|magnitude": 36.0
}
```

#### Raw Canonical JSON

The `|raw` attribute embeds pre-serialized openEHR canonical JSON:

```json
{
  "vital_signs/blood_pressure:0/any_event:0/systolic|raw": {
    "_type": "DV_QUANTITY",
    "magnitude": 120,
    "unit": "mm[Hg]"
  }
}
```

### Context

Context information represents composition-level metadata with `ctx/` prefix:

- **Mandatory:** language, territory
- **Optional:** composer, time, setting, participations, facility, workflow identifiers

### Format Variants

#### Flat Format

All elements as key-value pairs at single level:

- Keys are full WT paths (with indices and suffixes)
- Values are primitive types or simple objects
- No distinction between ELEMENT and its value

Syntax rules:
1. All paths fully qualified from root
2. Context fields use `ctx/` prefix
3. Instance indices zero-based
4. Attribute suffixes separated by pipe
5. RM attribute paths use underscore prefix
6. Path segments separated by forward slash

Example:

```json
{
  "ctx/language": "en",
  "ctx/territory": "US",
  "ctx/composer_name": "Dr. Smith",
  "vital_signs/body_temperature:0/any_event:0/temperature|magnitude": 37.5,
  "vital_signs/body_temperature:0/any_event:0/temperature|unit": "C"
}
```

#### Structured Format

Hierarchy preserved as nested JSON objects:

- Each path segment becomes nested property
- Instance indices remain in property names
- Attribute suffixes prefixed with pipe
- Context data grouped under `ctx` object
- Arrays used throughout

Syntax rules:
1. Hierarchy represented by nested objects
2. Instance indices remain in property names
3. Attribute suffixes use pipe prefix
4. Context grouped under `ctx` property
5. Arrays used for data values
6. Empty objects omitted

Example:

```json
{
  "ctx": {
    "language": "en",
    "territory": "US"
  },
  "vital_signs": {
    "body_temperature": [{
      "any_event": [{
        "temperature": [{
          "|magnitude": 37.5,
          "|unit": "C"
        }],
        "time": ["2024-01-15T10:30:00Z"]
      }]
    }]
  }
}
```

### Conversion Between Formats

#### Flat to Structured

Algorithm:
1. Parse each flat key into path segments
2. Separate context fields from composition fields
3. Split on forward slash, create nested objects
4. For final segment, check for attribute suffix
5. If suffix exists, create array with suffix as property
6. Handle RM attributes appropriately
7. Merge nested structures and add context

#### Structured to Flat

Algorithm:
1. Recursively traverse nested object structure
2. Build path by concatenating property names with slash
3. Append pipe-prefixed properties to parent path
4. Unwrap arrays
5. Flatten context with `ctx/` prefix
6. Preserve instance indices and RM attribute prefixes

### Level Removal

#### Always Removed

These node types are omitted from paths:

| Type | Replaced By |
|------|-------------|
| ITEM_TREE | ITEM_TREE.items |
| ITEM_LIST | ITEM_LIST.items |
| ITEM_SINGLE | ITEM_SINGLE.item |
| ITEM_TABLE | ITEM_TABLE.rows |
| HISTORY | HISTORY.events |

#### Conditionally Removed

**EVENT** nodes removed when:
1. Maximum occurrence is 1 (`max = 1`)
2. AND no sibling EVENT nodes exist

**EVENT** nodes retained when:
- Multiple EVENT types exist in same OBSERVATION
- EVENT can occur multiple times

### Validation

Implementations should validate:

- Web Template mapping to input field identifiers
- Pipe presence for attribute suffix identification
- Mandatory context fields (language, territory)
- Field identifiers match WT structure
- Data types match Operational Template expectations
- Cardinality constraints satisfied
- Terminology bindings valid
- RM attribute paths valid

---

## RM Mappings

### COMPOSITION

**Reference:** [COMPOSITION class specification](https://specifications.openehr.org/releases/RM/latest/ehr.html#_composition_class)

Example flat format:

```json
{
  "conformance-ehrbase.de.v0/language|code": "en",
  "conformance-ehrbase.de.v0/language|terminology": "ISO_639-1",
  "conformance-ehrbase.de.v0/territory|code": "US",
  "conformance-ehrbase.de.v0/category|code": "433",
  "conformance-ehrbase.de.v0/context/start_time": "2021-12-21T14:19:31.649613+01:00",
  "conformance-ehrbase.de.v0/composer|name": "Silvia Blake"
}
```

| Flat Path | Type | RM Path | Required | Note |
|-----------|------|---------|----------|------|
| `/language` | CODE_PHRASE | language | Yes | |
| `/territory` | CODE_PHRASE | territory | Yes | |
| `/category` | DV_CODED_TEXT | category | Yes | |
| `/composer` | PARTY_PROXY | composer | Yes | Set to PARTY_SELF via ctx/composer_self:true |
| `/context` | EVENT_CONTEXT | context | Yes | |
| `/_link:i` | LINK | links | No | |
| `/_feeder_audit` | FEEDER_AUDIT | feeder_audit | No | |
| `/_uid` | STRING | uid.value | No | |

### ADMIN_ENTRY

**Reference:** [ADMIN_ENTRY class specification](https://specifications.openehr.org/releases/RM/latest/ehr.html#_admin_entry_class)

Example:

```json
{
  "conformance-ehrbase.de.v0/conformance_section/conformance_admin_entry/dv_text": "DV_TEXT 56",
  "conformance-ehrbase.de.v0/conformance_section/conformance_admin_entry/language|code": "en",
  "conformance-ehrbase.de.v0/conformance_section/conformance_admin_entry/encoding|code": "UTF-8"
}
```

| Flat Path | Type | RM Path | Required | Note |
|-----------|------|---------|----------|------|
| `/language` | CODE_PHRASE | language | Yes | |
| `/territory` | CODE_PHRASE | territory | Yes | |
| `/subject` | PARTY_PROXY | subject | No | Set to PARTY_SELF if not explicit |
| `/_work_flow_id` | OBJECT_REF | workflow_id | No | |
| `/_link:i` | LINK | links | No | |
| `/_feeder_audit` | FEEDER_AUDIT | feeder_audit | No | |
| `/_uid` | STRING | uid.value | No | |

### INSTRUCTION

**Reference:** [INSTRUCTION class specification](https://specifications.openehr.org/releases/RM/latest/ehr.html#_instruction_class)

Example:

```json
{
  "conformance-ehrbase.de.v0/conformance_section/conformance_instruction/current_activity/dv_text": "DV_TEXT 45",
  "conformance-ehrbase.de.v0/conformance_section/conformance_instruction/narrative": "Human readable instruction narrative",
  "conformance-ehrbase.de.v0/conformance_section/conformance_instruction/expiry_time": "2022-01-31T10:33:28.724259+01:00"
}
```

| Flat Path | Type | RM Path | Required | Note |
|-----------|------|---------|----------|------|
| `/language` | CODE_PHRASE | language | Yes | |
| `/territory` | CODE_PHRASE | territory | Yes | |
| `/narrative` | DV_TEXT | narrative | Yes | |
| `/_expiry_time` | DV_DATE_TIME | expiry_time | Yes | |
| `/_wf_definition` | DV_PARSABLE | wf_definition | No | |
| `/subject` | PARTY_PROXY | subject | No | Set to PARTY_SELF if not explicit |
| `/_guideline_id` | OBJECT_REF | guideline_id | No | |
| `/_work_flow_id` | OBJECT_REF | workflow_id | No | |
| `/_link:i` | LINK | links | No | |
| `/_feeder_audit` | FEEDER_AUDIT | feeder_audit | No | |
| `/_uid` | STRING | uid.value | No | |

### ACTION

**Reference:** [ACTION class specification](https://specifications.openehr.org/releases/RM/latest/ehr.html#_action_class)

Example:

```json
{
  "conformance-ehrbase.de.v0/conformance_section/conformance_action/dv_text": "dv_text in description",
  "conformance-ehrbase.de.v0/conformance_section/conformance_action/ism_transition/current_state|code": "532",
  "conformance-ehrbase.de.v0/conformance_section/conformance_action/time": "2022-01-31T10:33:28.72414+01:00"
}
```

| Flat Path | Type | RM Path | Required | Note |
|-----------|------|---------|----------|------|
| `/language` | CODE_PHRASE | language | Yes | |
| `/territory` | CODE_PHRASE | territory | Yes | |
| `/time` | DV_DATE_TIME | time | Yes | |
| `/ism_transition` | ISM_TRANSITION | ism_transition | Yes | |
| `/_instruction_details` | INSTRUCTION_DETAILS | instruction_details | No | |
| `/subject` | PARTY_PROXY | subject | No | Set to PARTY_SELF if not explicit |
| `/_guideline_id` | OBJECT_REF | guideline_id | No | |
| `/_work_flow_id` | OBJECT_REF | workflow_id | No | |
| `/_link:i` | LINK | links | No | |
| `/_feeder_audit` | FEEDER_AUDIT | feeder_audit | No | |
| `/_uid` | STRING | uid.value | No | |

### EVALUATION

**Reference:** [EVALUATION class specification](https://specifications.openehr.org/releases/RM/latest/ehr.html#_evaluation_class)

Example:

```json
{
  "conformance-ehrbase.de.v0/conformance_section/conformance_evaluation/dv_text": "dv_text in data",
  "conformance-ehrbase.de.v0/conformance_section/conformance_evaluation/language|code": "en"
}
```

| Flat Path | Type | RM Path | Required | Note |
|-----------|------|---------|----------|------|
| `/language` | CODE_PHRASE | language | Yes | |
| `/territory` | CODE_PHRASE | territory | Yes | |
| `/subject` | PARTY_PROXY | subject | No | Set to PARTY_SELF if not explicit |
| `/_guideline_id` | OBJECT_REF | guideline_id | No | |
| `/_work_flow_id` | OBJECT_REF | workflow_id | No | |
| `/_link:i` | LINK | links | No | |
| `/_feeder_audit` | FEEDER_AUDIT | feeder_audit | No | |
| `/_uid` | STRING | uid.value | No | |

### OBSERVATION

**Reference:** [OBSERVATION class specification](https://specifications.openehr.org/releases/RM/latest/ehr.html#_observation_class)

Example:

```json
{
  "conformance-ehrbase.de.v0/conformance_section/conformance_observation/any_event:0/dv_quantity|magnitude": 65.9,
  "conformance-ehrbase.de.v0/conformance_section/conformance_observation/any_event:0/time": "2021-12-21T16:02:58.0094262+01:00",
  "conformance-ehrbase.de.v0/conformance_section/conformance_observation/language|code": "en"
}
```

### ELEMENT

ELEMENT values are represented directly without container nesting in simplified formats.

### CLUSTER

CLUSTER structures are preserved as nested hierarchies in both flat and structured formats.

### Additional RM Classes

The specification includes detailed mappings for:
- LINK
- FEEDER_AUDIT
- FEEDER_AUDIT_DETAILS
- ACTIVITY
- ISM_TRANSITION
- INSTRUCTION_DETAILS
- EVENT_CONTEXT
- OBJECT_REF
- INTERVAL_EVENT
- POINT_EVENT
- PARTY_PROXY subtypes (PARTY_SELF, PARTY_IDENTIFIED, PARTY_RELATED)
- Data Value types (DV_TEXT, DV_CODED_TEXT, DV_QUANTITY, DV_DATE_TIME, etc.)

---

## Context Information

Context represents composition-level metadata. Key fields include:

### Composer

The person creating the composition:

```json
{
  "ctx/composer_name": "Dr. Smith",
  "ctx/composer_id": "12345",
  "ctx/composer_id_namespace": "HOSPITAL-NS"
}
```

### ID Namespace and Scheme

Identifiers for persons/facilities:

```json
{
  "ctx/composer_id": "12345",
  "ctx/composer_id_scheme": "UUID",
  "ctx/composer_id_namespace": "EHR.NETWORK"
}
```

### Language and Territory

Required composition-level settings:

```json
{
  "ctx/language": "en",
  "ctx/territory": "US"
}
```

### Workflow ID

Optional workflow reference:

```json
{
  "ctx/_work_flow_id|id": "WF123",
  "ctx/_work_flow_id|type": "WORKFLOW"
}
```

### Participation

Multiple participants with functions:

```json
{
  "ctx/_participation:0|function": "requester",
  "ctx/_participation:0|mode": "face-to-face communication",
  "ctx/_participation:0|name": "Dr. Marcus Johnson"
}
```

### Healthcare Facility

Facility information:

```json
{
  "ctx/_health_care_facility|id": "9091",
  "ctx/_health_care_facility|name": "Hospital"
}
```

### Timestamps

- **time** - Start of context
- **end_time** - End of context
- **history_origin** - Data collection start
- **action_time** - When action occurred

### Activity Timing

For instructions:

```json
{
  "path/instruction/activity/timing": "R4/2022-01-31T10:00:00+01:00/P3M"
}
```

### Provider

Clinical provider information:

```json
{
  "ctx/_provider|name": "Dr. Johnson",
  "ctx/_provider|id": "199"
}
```

### ISM Transition State

Action state information:

```json
{
  "path/action/ism_transition|current_state|code": "532"
}
```

### Instruction Narrative

Human-readable instruction text:

```json
{
  "path/instruction/narrative": "Take twice daily with food"
}
```

### Location

Clinical setting location:

```json
{
  "ctx/_location": "microbiology lab 2"
}
```

### Setting

Care environment:

```json
{
  "ctx/setting|code": "238",
  "ctx/setting|value": "other care"
}
```

### Link

References to related information:

```json
{
  "path/composition/_link:0|type": "problem",
  "path/composition/_link:0|target": "ehr://problem-123"
}
```

---

## Amendment Record

Changes to this specification are tracked through the openEHR Problem Reports and Change Request system.

---

## References

- openEHR Reference Model specifications
- openEHR Operational Template (OPT) specification
- openEHR REST API specification
- openEHR JSON Schema specifications
- Better Web Templates documentation
- EHRbase Simplified Data Template documentation
- EtherCIS ECISFLAT format documentation
- Ocean Health Systems Template Data Schema specification
