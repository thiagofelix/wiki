# Index

## Overviews
- [[openehr-overview]] — High-level introduction to OpenEHR architecture, design principles, and specification structure

## Entities
- [[reference-model]] — The stable core information model (RM 1.1.0): EHR structure, entries, data types, demographics
- [[ehr-information-model]] — EHR package: EHR root object, compositions, folders, versioning, event context
- [[common-information-model]] — Common IM: LOCATABLE, PARTY_PROXY, versioning, change control, folders
- [[data-types]] — Clinical data types: DV_TEXT, DV_QUANTITY, DV_DATE_TIME, DV_CODED_TEXT, etc.
- [[data-structures]] — Data structures: ITEM_TREE, ITEM_LIST, HISTORY, EVENT, ELEMENT, CLUSTER
- [[demographic-model]] — Demographic IM: PARTY, PERSON, ORGANISATION, ROLE, relationships
- [[archetype-model]] — Archetype formalism: three-layer architecture, identification, specialisation, templates
- [[archetype-definition-language]] — ADL 2 syntax: cADL constraints, terminology section, specialisation, slots
- [[archetype-object-model]] — AOM 2: constraint model classes, validation, flattening, operational templates
- [[archetype-query-language]] — AQL: SQL-like queries using archetype paths, CONTAINS operator, functions
- [[rest-api]] — ITS-REST: EHR, Query, and Definition API endpoints (OpenAPI 3.0)
- [[task-planning]] — PROC: Task Planning for clinical workflows, care plans, execution tracking
- [[base-component]] — BASE: foundation types, identification hierarchy, terminology types

## Concepts
- [[multi-level-modelling]] — Core design paradigm: separating stable RM from variable archetypes/templates

## Sources

### AA_GLOBAL
- raw/architecture-overview.md — Architecture Overview (BASE 1.2.0)

### BASE
- raw/base-foundation-types.md — BASE Foundation Types (BASE 1.2.0)
- raw/base-types.md — BASE Base Types (BASE 1.2.0)
- raw/base-resource.md — Resource Model: AUTHORED_RESOURCE, RESOURCE_DESCRIPTION, translations (BASE 1.2.0)

### RM
- raw/rm-ehr.md — EHR Information Model (RM 1.1.0)
- raw/rm-common.md — Common Information Model (RM 1.1.0)
- raw/rm-data-types.md — Data Types Information Model (RM 1.1.0)
- raw/rm-data-structures.md — Data Structures Information Model (RM 1.1.0)
- raw/rm-demographic.md — Demographic Information Model (RM 1.1.0)
- raw/rm-support.md — Support Information Model (RM 1.1.0)
- raw/rm-integration.md — Integration Information Model (RM 1.1.0)
- raw/rm-ehr-extract.md — EHR Extract Information Model (RM 1.1.0)

### AM
- raw/am-overview.md — Archetype Technology Overview (AM 2.3.0)
- raw/am-adl2.md — Archetype Definition Language 2 (AM 2.3.0)
- raw/am-aom2.md — Archetype Object Model 2 (AM 2.3.0)
- raw/am-adl14.md — Archetype Definition Language 1.4 (AM 2.3.0, legacy)
- raw/am-aom14.md — Archetype Object Model 1.4 (AM 2.3.0, legacy)
- raw/am-identification.md — Archetype Identification: HRID, versioning, lifecycle, governance (AM 2.3.0)
- raw/am-opt2.md — Operational Template 2: flattening, terminology handling (AM 2.3.0, development)

### LANG
- raw/lang-bmm.md — Basic Meta-Model: formal meta-model for expressing RM and other models (LANG)
- raw/lang-bmm-persistence.md — BMM Persistence: serialization format for BMM schemas (LANG)
- raw/lang-odin.md — Object Data Instance Notation: serialization format used in ADL and BMM (LANG)
- raw/lang-el.md — Expression Language: formal expression syntax for archetypes and rules (LANG)
- raw/lang-bel.md — Basic Expression Language: simplified expression sub-language (LANG)

### QUERY
- raw/query-aql.md — Archetype Query Language (QUERY 1.1.0)

### ITS-REST
- raw/its-rest-overview.md — ITS-REST Overview: design principles, authentication, error handling
- raw/its-rest-ehr.md — ITS-REST EHR API
- raw/its-rest-query.md — ITS-REST Query API
- raw/its-rest-definition.md — ITS-REST Definition API
- raw/its-rest-definitions.md — ITS-REST Definitions API (variant of definition)
- raw/its-rest-demographic.md — ITS-REST Demographic API (development)
- raw/its-rest-admin.md — ITS-REST Admin API (development)
- raw/its-rest-system.md — ITS-REST System API
- raw/its-rest-simplified-data-template.md — ITS-REST Simplified Data Template format (development)
- raw/its-rest-simplified-formats.md — ITS-REST Simplified Formats: flat/structured representations
- raw/its-rest-smart-app-launch.md — ITS-REST SMART on openEHR: SMART App Launch integration (development)

### CDS
- raw/cds-gdl.md — Guideline Definition Language v1 (CDS, retired)
- raw/cds-gdl2.md — Guideline Definition Language v2 (CDS, stable)

### SM
- raw/sm-platform.md — Service Model Platform

### PROC
- raw/proc-task-planning.md — Task Planning (PROC 1.7.0)

### TERM
- raw/term-support-terminology.md — Support Terminology (TERM 3.0.0)

### CNF
- raw/cnf-platform-conformance.md — Platform Conformance (CNF)

### Community / Research
- raw/aql-parser-ecosystem.md — AQL parser implementations survey
- raw/cdr-implementations-survey.md — CDR implementations comparison
- raw/ehrbase-architecture.md — EHRbase architecture deep-dive
- raw/ethercis-architecture.md — EtherCIS architecture deep-dive
- raw/openehr-persistence-patterns.md — Persistence patterns for openEHR data
- raw/AqlLexer.g4 — AQL ANTLR4 lexer grammar
- raw/AqlParser.g4 — AQL ANTLR4 parser grammar

## Syntheses
