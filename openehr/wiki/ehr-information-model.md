---
title: EHR Information Model
type: entity
sources:
  - raw/rm-ehr.md
created: 2026-04-13
updated: 2026-04-13
---

# EHR Information Model

The EHR IM defines the logical structure of an openEHR Electronic Health Record — the primary clinical data repository.

**Release**: RM 1.1.0 (STABLE)

## EHR Structure

```
EHR
├── ehr_id: HIER_OBJECT_ID          # Globally unique (recommended UUID)
├── system_id: HIER_OBJECT_ID       # System where EHR was created
├── time_created: DV_DATE_TIME      # Creation timestamp
│
├── ehr_status → VERSIONED_EHR_STATUS
│   └── EHR_STATUS
│       ├── subject: PARTY_SELF     # Record subject (may be anonymous)
│       ├── is_queryable: Boolean   # Include in population queries?
│       ├── is_modifiable: Boolean  # Allow content changes?
│       └── other_details: ITEM_STRUCTURE  # Archetyped extensions
│
├── ehr_access → VERSIONED_EHR_ACCESS
│   └── EHR_ACCESS
│       ├── scheme: String          # Access control scheme name
│       └── settings: ACCESS_CONTROL_SETTINGS
│
├── compositions → VERSIONED_COMPOSITION[]
│   └── COMPOSITION
│       ├── composer: PARTY_PROXY   # Who authored the content
│       ├── context: EVENT_CONTEXT  # Healthcare event context
│       ├── category: DV_CODED_TEXT # persistent/event/episodic
│       └── content: List<CONTENT_ITEM>  # Sections and Entries
│
├── folders → VERSIONED_FOLDER[]    # Optional organizational indexes
│
└── contributions → CONTRIBUTION[]  # Change-set audit trail
```

## Compositions

The COMPOSITION is the fundamental data container — the unit of committal, integrity, and versioning.

### Temporal Categories

| Category | Description | Update Pattern | Examples |
|----------|-------------|----------------|----------|
| **Persistent** | Ongoing patient state | Updated in-place (new versions of same instance) | Problem list, medications, allergies, family history, vaccination history |
| **Event** | Healthcare activity records | New instance per event | Encounter notes, lab results, procedure records |
| **Episodic** | Time-bounded ongoing state | Like persistent but for a defined period | Pregnancy record, post-surgery recovery |

### ACID-Inspired Properties

- **Durability**: Persistent unit of information committal
- **Atomicity**: Minimal unit of clinical integrity
- **Consistency**: Contributions leave record consistent
- **Isolation**: Simultaneous changes don't interfere
- **Indelibility**: Committed information cannot be destroyed
- **Traceability**: Adequate audit at committal

### Event Context

EVENT_CONTEXT documents the healthcare event:
- `start_time` / `end_time` — when the event occurred
- `health_care_facility` — where (PARTY_IDENTIFIED)
- `setting` — care setting code (primary care, emergency, etc.)
- `participations` — who was involved and how
- `location` — physical care delivery location

### Composer vs Committer

| | Composer | Committer |
|-|----------|-----------|
| **What** | Person responsible for content | System user who committed |
| **Where** | COMPOSITION.composer | VERSION.audit.committer |
| **Example** | "RN Jane Williams" | "jane.williams@hospital.au" |

## Content Structure

```
COMPOSITION
└── content: List<CONTENT_ITEM>
    ├── SECTION (navigation/headings)
    │   └── items: List<CONTENT_ITEM>  # nested Sections or Entries
    └── ENTRY (clinical statements)
        ├── ADMIN_ENTRY
        ├── OBSERVATION
        ├── EVALUATION
        ├── INSTRUCTION
        │   └── activities: List<ACTIVITY>
        └── ACTION
            └── ism_transition: ISM_TRANSITION
```

See [[reference-model#entry-types-clinical-statements]] for Entry type details.

## Versioning

Each Composition lives in a VERSIONED_COMPOSITION container. Versioning scenarios:

| Case | Description | Result |
|------|-------------|--------|
| New content | Authored locally | New ORIGINAL_VERSION |
| Correction | Error fix | New ORIGINAL_VERSION with change_type="correction" |
| Feeder data | From external system | IMPORTED_VERSION + ORIGINAL_VERSION |
| EHR Extract | From another openEHR system | ORIGINAL_VERSION received |

## Folders

Optional hierarchical indexes into Compositions:
- Folders **reference** Compositions (via OBJECT_REF), they don't **contain** them
- Multiple folders can reference the same Composition
- Use cases: "hospital episodes", "diabetes monitoring", "patient-entered data"

## EHR Creation

### Type 1 — New patient
New EHR with fresh globally unique ehr_id (UUID recommended).

### Type 2 — Logical clone
New EHR created as logical copy of patient's EHR from another system.

At creation, the system generates: root EHR object, EHR_STATUS, EHR_ACCESS, and housekeeping data.

## EHR Lifecycle

`EHR_STATUS.is_modifiable` controls whether content can be changed. Deactivation reasons:
- Patient death
- Duplicate record discovered
- Patient opt-out
- EHR moved to another system

## Time in the EHR

Multiple temporal dimensions:
- **Sample/collection time** — when specimen/observation taken
- **Measurement time** — when measurement performed
- **Healthcare event time** — EVENT_CONTEXT.start_time
- **Committal time** — VERSION.audit.time_committed
