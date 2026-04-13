---
title: OpenEHR Overview
type: overview
sources:
  - raw/architecture-overview.md
created: 2026-04-13
updated: 2026-04-13
---

# OpenEHR Overview

OpenEHR is an open standard for electronic health records (EHR) developed by the openEHR Foundation. It provides a specification-driven approach to building interoperable, future-proof health information systems.

## What is OpenEHR?

OpenEHR defines a complete platform for electronic health records through:

- A stable **Reference Model** (RM) — the only part implemented in software
- **Archetypes** — reusable, vendor-independent clinical content definitions
- **Templates** — use-case-specific data set definitions composed from archetypes
- **Archetype Query Language (AQL)** — portable queries against archetype paths
- **REST APIs** — standardized platform service interfaces

## Core Design Principles

### Multi-Level Modelling

The central innovation of openEHR. Instead of encoding all domain knowledge directly in software/database schemas (which creates brittle, unmaintainable systems), openEHR separates models into three levels:

1. **Reference Model (RM)** — stable information model (~50-100 classes). Implemented in software. Defines generic clinical structures (compositions, entries, data types) without domain specifics.
2. **Archetypes** — formal definitions of clinical content (blood pressure, lab result, medication order). Authored by domain experts in [[archetype-definition-language|ADL]], not software developers. Reusable across contexts.
3. **Templates** — combine archetype elements into context-specific data sets (e.g., "diabetic patient encounter form"). Used for deployment in actual systems.

Only level 1 is in software. Levels 2 and 3 are consumed at runtime, making systems self-adapting as new archetypes are developed.

### Ontological Separation

Three distinct semantic categories, each developed and maintained independently:

| Category | Examples | Authors |
|----------|----------|---------|
| **Information models** | Data types, structures, identifiers | IT architects |
| **Domain content models** | "Microbiology result", "blood pressure" | Clinicians, domain experts |
| **Terminologies** | SNOMED CT, ICD, LOINC | Terminology organizations |

This separation is critical — terminologies describe real-world phenomena (types of infections), while archetypes describe information structures (how to record a microbiology result). They are complementary, not competing.

### Separation of Responsibilities

The architecture follows SOA principles with services at three deployment levels:
- **Healthcare delivery** (provider enterprise — clinic, hospital)
- **Continuity of care** (care network — regional health service)
- **Healthcare system** (national — public health, quality reporting)

## Specification Components

The openEHR specifications are organized into components:

### Abstract Specifications (Platform-Independent)

| Component | Description | Key Specs |
|-----------|-------------|-----------|
| **[[base-component\|BASE]]** | Foundation types, identifiers, definitions | Foundation Types, Base Types |
| **LANG** | Generic languages: ODIN, BMM, Expression Language | |
| **[[reference-model\|RM]]** | Core information model: EHR, demographics, data types | See [[reference-model]] |
| **[[archetype-model\|AM]]** | Archetype formalism: ADL, AOM, templates | See [[archetype-model]] |
| **[[archetype-query-language\|QUERY]]** | Archetype Query Language (AQL) | See [[archetype-query-language]] |
| **TERM** | openEHR support terminology | |
| **[[task-planning\|PROC]]** | Process model / Task Planning | See [[task-planning]] |
| **CDS** | Clinical Decision Support (GDL) | |
| **SM** | Service Model — abstract platform APIs | |

### Implementation Technology Specifications (ITS)

| Component | Description |
|-----------|-------------|
| **[[rest-api\|ITS-REST]]** | REST API definitions (OpenAPI 3.0) |
| **ITS-JSON** | JSON Schema definitions |
| **ITS-XML** | XML Schema (XSD) definitions |
| **ITS-BMM** | BMM schema definitions |

### Other

| Component | Description |
|-----------|-------------|
| **CNF** | Conformance / certification criteria |

## The Problem OpenEHR Solves

### The Scale Problem

Healthcare domain semantics are vast:
- Tens of thousands of clinical observations (systolic BP, visual acuity, etc.)
- ~10^4 laboratory analyte types
- 10^5 to 10^6 terminology concepts (SNOMED CT, ICD, LOINC)

A traditional information model of 50-100 classes technically allows an astronomical number of possible data instances (~10^10+), but meaningful clinical data patterns number only in the tens of thousands. The "meaningful instance space" is a tiny fraction of what the model permits.

### The Traditional Approach Fails

Expanding the information model to accommodate all meaningful patterns means:
- Constant model changes → continuous system instability
- Systems running 24/365 generating terabytes/year cannot tolerate this
- Domain semantics must be authored by clinicians, not software developers

### OpenEHR's Answer

Archetypes define the meaningful instance space separately from software. The RM stays stable (implemented once), while archetypes evolve independently. This means:
- Software is smaller, more maintainable
- Domain experts author content models in their own formalism
- Systems are self-adapting — they consume new archetypes at runtime
- Archetypes are vendor-independent and reusable across products

## Key Resources

- **Published specifications**: specifications.openehr.org/releases
- **GitHub organization**: github.com/openEHR
- **Clinical Knowledge Manager (CKM)**: openehr.org/ckm — the archetype repository
- **Discourse forum**: discourse.openehr.org

## History

OpenEHR incorporates 20+ years of research:
- **1992-1995**: EU FP3 Good European Health Record (GEHR) project
- **1997-2001**: GEHR Australia — introduced archetypes, XML-enabling
- **2003+**: openEHR Foundation established, specifications formalized
- Influenced and was influenced by ISO 13606 (2005 revision)
- Architecture designed to be compatible with ISO 13606, HL7, and other standards
