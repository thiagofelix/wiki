# Simplified Data Template (SDT)

**Issuer:** openEHR Specification Program
**Release:** ITS-REST Release-1.0.3
**Status:** DEVELOPMENT
**Date:** Latest Issue
**Keywords:** JSON, REST, web template, commit, simplified data, TDS, SDT, ncSDT, simSDT, structSDT

(c) 2019 - 2022 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Preface](#preface)
2. [Overview](#overview)
3. [Conceptual Approach](#conceptual-approach)
4. [sOPT Generation](#sopt-generation)
5. [Simple Template Concrete Formats](#simple-template-concrete-formats)
6. [Instance Conversion](#instance-conversion)

---

## Preface

### Purpose

This specification presents a developer-oriented template format designed for simplified creation of openEHR content. Unlike canonical formats, these simplified approaches aim to reduce complexity for developers with limited openEHR experience, enabling easier Composition instantiation.

### Status

This document remains in DEVELOPMENT state. The current version appears at the official openEHR specifications site. Unresolved items are marked as "to be determined" (TBD) paragraphs throughout.

### Feedback

Community input is encouraged through:
- openEHR ITS forum discussions
- Problem reports via the specifications tracker
- Change request documentation in the ITS-REST history

### Conformance

Conformance testing aligns with standard openEHR-REST API calls using alternate representation formats, specified via HTTP Content-Type headers.

**TBD:** Conformance procedures and Content-Type specifications require further documentation.

---

## Overview

### Requirements

OpenEHR provides three canonical serialization approaches:

- Canonical XML (based on openEHR RM XSDs)
- Canonical JSON (following openEHR JSON schemas)
- Additional canonical formats (potentially YAML)

"Canonical" designation requires:

- Containment following RM structure
- All RM mandatory fields present
- Attributes named per RM specifications
- Cardinalities respecting RM constraints

These formats work well for comprehensive implementations but create barriers for developers focused on specific data sets. Historical alternatives--including TDS, EtherCIS Flat JSON, and Marand formats--addressed this gap through various simplification strategies.

This specification unifies these approaches within a formal framework supporting current variants and future extensions.

---

## Conceptual Approach

### Background

OpenEHR's layered architecture distinguishes between:

- **Reference Model (RM):** Information model foundation
- **Operational Templates (OPT):** Domain-specific data sets derived from archetypes
- **Archetypes:** Constraint models based on RM

The RM supports two design goals:

- Data instances remain complete when shared with non-openEHR partners
- Software implementations function predictably across diverse scenarios

This rigor, while valuable, creates overhead for developers managing limited data types or specific templates (vital signs, lab results, pregnancy plans).

Template-specific simplification offers a practical pathway, allowing each openEHR template to generate simplified commit formats.

### Historical Formats

#### XML Schema Formats

**Template Data Schema (TDS)** emerged from Ocean Health Systems, transforming `.oet` template files and archetypes into single XSD definitions. The transformation flattened RM structures and converted archetype node codes to XSD tags for developer-friendly identification.

Example Portuguese TDD extract:

```xml
<Problema_Diagnostico>
  <name>
    <value>Problema Diagnostico</value>
  </name>
  <language>
    <terminology_id>
      <value>ISO_639-1</value>
    </terminology_id>
    <code_string>pt</code_string>
  </language>
  <subject xsi:type="oe:PARTY_SELF"/>
  <data>
    <Diagnostico>
      <value>
        <oe:value>Hipertensao secundaria</oe:value>
        <oe:defining_code>
          <oe:terminology_id>
            <oe:value>CID-10_1998.v1.0.0</oe:value>
          </oe:terminology_id>
          <oe:code_string>I15</oe:code_string>
        </oe:defining_code>
      </value>
    </Diagnostico>
  </data>
</Problema_Diagnostico>
```

#### JSON Formats

**Near-Canonical SDT (ncSDT)** employs AQL-style paths using archetype codes while simplifying DV_XXX and PARTY_PROXY types:

```json
{
    "/context/health_care_facility|name":"Northumbria Community NHS",
    "/context/health_care_facility|identifier":"999999-345",
    "/context/start_time":"2015-09-28T10:18:17.352+07:00",
    "/composer|identifier":"1345678",
    "/composer|name":"Dr. Marcus Johnson",
    "/category":"openehr::433|event|",
    "/territory":"FR",
    "/language":"fr"
}
```

**Simplified IM SDT (simSDT)** applies radical RM simplification with natural language paths. Also known as "Simplified JSON Format" or "Flat Format," supported by EHRbase:

```json
{
  "laboratory_order/_uid": "23d69330-7790-4394-8abc-1455681f6ffa::ydh.code4health.com::1",
  "laboratory_order/language|code": "en",
  "laboratory_order/language|terminology": "ISO_639-1",
  "laboratory_order/territory|code": "GB",
  "laboratory_order/territory|terminology": "ISO_3166-1",
  "laboratory_order/context/_health_care_facility|name": "Northumbria Community NHS",
  "laboratory_order/laboratory_test_request/_uid": "b8c17799-457d-4583-8d85-c369dffacc21",
  "laboratory_order/laboratory_test_request/lab_request/service_requested|code": "444164000",
  "laboratory_order/laboratory_test_request/lab_request/service_requested|value": "Urea, electrolytes and creatinine measurement",
  "laboratory_order/laboratory_test_request/lab_request/service_requested|terminology": "SNOMED-CT",
  "ctx/language": "en",
  "ctx/territory": "GB"
}
```

**Structured IM SDT (structSDT)** represents data in JSON structures based on Web Template paths, avoiding flattening:

```json
{
  "ctx": {
    "language": "en",
    "territory": "SI",
    "composer_name": "matijak_test"
  },
  "vitals": {
    "vitals": [
      {
        "body_temperature": [
          {
            "any_event": [
              {
                "temperature": [
                  {
                    "|magnitude": 37.2,
                    "|unit": "C"
                  }
                ],
                "time": [
                  "2014-01-22T15:18:07.339+01:00"
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### General Form of an Algorithm

**Developer Note:** Users implementing simplified formats via examples need not understand detailed conversion algorithms. Platform services typically generate example instances automatically, with algorithmic details reserved for openEHR platform developers handling complex scenarios.

Three critical requirements enable simplified formats:

- Abstract away structural complexity through reduced self-containment and increased schema reliance
- Permit complete machine generation from canonical definitions (OPTs)
- Support routine machine conversion to canonical formats at execution

#### Template Definition Generation Scheme

```
Operational Template (OPT)
         |
    RM Flattening
         |
    +--------------------+
    |   JSON Template    |
    |   Definitions      |
    +--------------------+
         / \
  Near-Canonical  Simplified
```

Both near-canonical and simplified template definitions derive from OPT transformations. The simplified variant requires an additional step: the **sOPT transformer** converts an OPT into a simplified OPT using a Simplified Information Model (SIM)--a logical subset of RM classes relevant to commitable EHR content.

SIM simplifications include:

- **De-normalization:** Merging Composition relationships, reducing path depth
- **Stringification:** Replacing complex low-level types with String for simplified representation

The SIM enables generating simplified OPTs (sOPTs) from any Operational Template, producing various JSON Data Templates (JDTs) including hierarchical and flat formats. Paths may use AQL format or simplified conversion algorithms.

#### Instance Conversion Flow

```
Simplified Template Instance
         |
    sOPT Instance Converter
         |
Canonical RM Format
(committed to persistence layer)
```

Developers create instances in simplified JSON formats, which server-side converters transform to canonical RM format during data commitment.

---

## sOPT Generation

This section describes machine-derivation of Simplified OPTs from canonical OPT definitions using the Simplified Reference Model.

### Visitor Algorithm

#### C_COMPLEX_OBJECT Processing

```pseudocode
SOptVisitor:: OptVisitor {

    public enterCComplexObject (CComplexObject cObj) {
        // Obtain or synthesize SIM class name for cObj.rmTypeName
        simClassName = xxx;

        // Create sOPT CComplexObject
        CComplexObject SCobj = new CComplexObject(simClassName);

        // Process attributes
        for (CAttribute cAttr in cCObj.attributes) {

            // Find applicable rules
            if (rules.hasPathRule (cObj.rmTypeName, CAttr.rmAttributeName)) {
                attrRule = rules.pathRule (cObj.rmTypeName, CAttr.rmAttributeName);

                // Handle collapse cases
                if (attrRule.collapse) {
                    // Create output C_ATTRIBUTE with SIM attribute name
                    CAttribute sCAttr = new CAttribute (baseName(attrRule.simPath));

                    // Attach new C_OBJECT
                    for (collapseRule in rules.matchingPathRules (cCObj.rmTypeName, CAttr.rmAttributeName)
                        sCAttr.appendChildren (makeCCObjects (collapseRule));
                }
                else
                    sCAttr.appendChildren (makeCCObjects (attrRule));
            }
        }
    }

    private List<CObject> makeCCObjects (CAttribute cAttr, SOptRule aRule) {
        List<CObject> sChildCObjList = new List<CObject>;
        CObject sChildCObj;

        // For primitive SIM targets, apply constraint conversion rules
        if (PrimitiveTypes.has (aRule.sim_type)) {
            for (cChildObj in cAttr.children) {
                sChildCObj = rules.execute (aRule.constraintConvRule (cChildObj));
                sChildCObjList.append (cChildObj)
            }
        }
        // Otherwise execute visitor on sub-tree
        else
            sChildCObjList.extend (visit (aRule.rmPath));

        return sChildCObjList;
    }
}
```

---

## Simple Template Concrete Formats

*Currently under development; notes follow.*

### Sparse JSON

*Additional documentation in progress.*

---

## Instance Conversion

This section describes converting simplified template instances to canonical format at execution time, enabling system persistence.

---

## Amendment Record

| Issue | Details | Completed |
|-------|---------|-----------|
| **ITS_REST Release 1.0.3** | Current release | -- |
| **1.0.2** | SPECITS-57: Updating simplified JSON format information and links | 13 Mar 2021 |
| **0.7.0** | SPECITS-33: Initial simplified data template specification; adapted from Marand Web Templates, EtherCIS documentation, Ocean Health Systems Template Data Schema | 17 Jul 2019 |

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica (UK); openEHR Foundation Management Board

### Contributors

Recognizing contributions from:
- Christian Chevalley (EtherCIS)
- Borut Fabjan (Better)
- Bostjan Lah (Better)
- Ian McNicoll (FreshEHR)
- Bjorn Naess (DIPS)
- Matija Polajnar (Marand)

Design informed by Marand Web Templates, EtherCIS ECISFLAT format, and Ocean Health Systems TDS.

### Trademarks

- openEHR -- openEHR Foundation registered trademark
- OMG, UML -- Object Management Group registered trademarks

---

**Support:**
- Issues: [Problem Reports](https://specifications.openehr.org/components/ITS-REST/open_issues)
- Web: [specifications.openEHR.org](https://specifications.openehr.org)
