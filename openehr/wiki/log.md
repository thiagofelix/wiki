# Log

## [2026-04-13] ingest | Fetched 20 additional openEHR specification documents

Completed full coverage of official openEHR GitHub specification repos. Raw sources now total 49 files.

**New sources added:**
- LANG (5): BMM, BMM Persistence, ODIN, Expression Language, Basic Expression Language
- ITS-REST (8): Overview, Admin API, Demographic API, Definitions API, System API, Simplified Data Template, Simplified Formats, SMART App Launch
- AM (4): ADL 1.4, AOM 1.4, Archetype Identification, OPT2
- CDS (2): GDL v1 (retired), GDL2 (stable)
- BASE (1): Resource Model

**Index updated:** Sources section reorganized by component, community/research sources listed separately.

**Not yet ingested into wiki pages** — raw sources saved only. Wiki pages pending for: LANG specs (BMM, ODIN, EL, BEL), additional ITS-REST APIs, AM 1.4 legacy specs, archetype identification, OPT2, CDS/GDL, and resource model.

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
