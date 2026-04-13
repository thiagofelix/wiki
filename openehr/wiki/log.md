# Log

## [2026-04-13] ingest | Initial crawl of OpenEHR specification documents

Crawled 22 specification documents from specifications.openehr.org and saved as raw markdown sources.

**Sources crawled:**
- BASE: Architecture Overview, Foundation Types, Base Types
- RM: EHR, Common, Data Types, Data Structures, Demographic, Support, Integration, EHR Extract
- AM: Overview, ADL2, AOM2
- QUERY: AQL
- ITS-REST: EHR API, Query API, Definition API
- SM: Platform Service Model
- PROC: Task Planning
- TERM: Support Terminology
- CNF: Platform Conformance

**Wiki pages created (14):**
- Overview: [[openehr-overview]]
- Entities: [[reference-model]], [[ehr-information-model]], [[common-information-model]], [[data-types]], [[data-structures]], [[demographic-model]], [[archetype-model]], [[archetype-definition-language]], [[archetype-object-model]], [[archetype-query-language]], [[rest-api]], [[task-planning]], [[base-component]]
- Concepts: [[multi-level-modelling]]

**Key findings:**
- OpenEHR uses multi-level modelling: stable RM (in software) + archetypes (domain content) + templates (use-case specific)
- The RM has 8 specifications covering EHR, demographics, data types/structures, common patterns, integration, and EHR extract
- Entry types map to clinical problem-solving: OBSERVATION → EVALUATION → INSTRUCTION → ACTION
- AQL queries are portable across all openEHR implementations via archetype paths
- Built-in versioning and audit trail for all EHR content
- Task Planning (PROC 1.7.0) is RETIRED status — being superseded
