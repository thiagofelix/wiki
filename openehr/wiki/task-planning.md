---
title: Task Planning
type: entity
sources:
  - raw/proc-task-planning.md
created: 2026-04-13
updated: 2026-04-13
---

# Task Planning (PROC)

The Task Planning specification defines a model for clinical workflow and process management. It enables structured care plans, order sets, and clinical pathways to be defined and executed.

**Release**: PROC 1.7.0 (RETIRED — being superseded)

## Purpose

Task Planning bridges the gap between individual clinical entries (observations, instructions, actions) and the higher-level care processes they belong to. It provides:

- Structured definition of multi-step care plans
- Execution tracking with state management
- Support for parallel and sequential task coordination
- Integration with clinical decision support
- Temporal constraints and scheduling

## Model Layers

### Definition Model

Defines the plan template — what tasks should be performed:

- **WORK_PLAN** — top-level plan definition
- **TASK_PLAN** — a sequence of tasks for one performer
- **TASK_GROUP** — grouping of related tasks (sequential or parallel)
- **TASK** — individual unit of work
  - **PERFORMABLE_TASK** — task to be performed by a human/system
  - **DISPATCHABLE_TASK** — task delegated to another system

Tasks can define:
- Pre-conditions and wait conditions
- Timing constraints (earliest/latest)
- Repeat specifications
- Subject and performer requirements

### Materialised Model

Represents a plan instantiated for a specific patient/context:

- **MATERIALISED_WORK_PLAN** — instantiated work plan
- **MATERIALISED_TASK_PLAN** — instantiated task plan
- **MATERIALISED_TASK** — individual task instance with execution state

### Execution Model

Tracks plan execution:

- Task lifecycle: `planned` → `available` → `active` → `completed`/`cancelled`/`aborted`
- Each task transition is recorded
- Supports pause/resume, skip, and override workflows

### Plan Execution History

All execution events are recorded for audit and analysis:
- Task state transitions
- Performer actions
- System events (timer expirations, condition evaluations)

## Task Types

| Task Type | Description |
|-----------|-------------|
| **DEFINED_ACTION** | Perform a clinical action (links to an INSTRUCTION archetype) |
| **SYSTEM_REQUEST** | Request from external system |
| **HAND_OFF** | Transfer responsibility to another performer |
| **SUB_PLAN** | Nested sub-plan |
| **CONDITION_GROUP** | Conditional branching based on data/state |
| **DECISION_GROUP** | Decision point requiring human choice |
| **EVENT_GROUP** | Wait for external event |

## Coordination

### Sequential Execution
Tasks executed in order within a TASK_GROUP:
```
Task A → Task B → Task C
```

### Parallel Execution
Multiple TASK_PLANs can execute concurrently:
```
Task Plan 1: Order medication → Administer → Monitor
Task Plan 2: Order labs → Collect sample → Report results
```

### Synchronization
Parallel plans can synchronize at:
- **Timeline markers** — named synchronization points
- **Wait conditions** — data-driven gates
- **Callbacks** — notifications from other tasks/systems

## Integration with EHR

Task Planning connects to the EHR data model:
- Tasks reference INSTRUCTION archetypes (what to do)
- Task completion creates ACTION entries (what was done)
- Pre-conditions query EHR data via [[archetype-query-language|AQL]]
- Plan state is tracked independently of clinical data
