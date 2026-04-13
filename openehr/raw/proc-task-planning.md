# Task Planning (TP) Specification - Markdown Conversion

## Document Header

**Issuer**: openEHR Specification Program

**Release**: PROC Release-1.7.0

**Status**: RETIRED

**Keywords**: workflow, task, planning, EHR, EMR, reference model, openehr

© 2017 - 2024 The openEHR Foundation

**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported
https://creativecommons.org/licenses/by-nd/3.0/

---

## Table of Contents

1. [Acknowledgements](#acknowledgements)
2. [Preface](#preface)
3. [Background](#background)
4. [Technical Requirements](#technical-requirements)
5. [Design Principles](#design-principles)
6. [Task Planning Model Overview](#task-planning-model-overview)
7. [Definition Model](#definition-model)
8. [Global Semantics](#global-semantics)
9. [Execution](#execution)
10. [Materialised Model](#materialised-model)
11. [Plan Execution History](#plan-execution-history)
12. [Transactional Service Model](#transactional-service-model)
13. [Relationship with other openEHR EHR Artefacts](#relationship-with-other-openehr-ehr-artefacts)

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica (UK); openEHR Foundation Management Board

### Contributors

The following individuals contributed formal and informal input:

- Danielle Santos Alves, RN, midwife, Federal University of Pernambuco (UFPE), Brazil
- Borut Fabjan, Program Manager, Better, Slovenia
- Matija Kejžar, Software Engineer, Better, Slovenia
- Bostjan Lah, Senior Architect, Marand, Slovenia
- Eugeny Leonov, Solit Clouds, Moscow, Russia
- Vladimir V Makarov, Department of Information Technologies, City of Moscow
- Ian McNicoll MD, FreshEHR, UK
- Bjørn Næss, DIPS, Norway
- Pablo Pazos Gutierrez, Senior engineer, CaboLabs, Uruguay
- Pekka Pesola, Engineer, Tieto, Finland
- Matija Polajnar, PhD, Software Engineer, Better, Slovenia

### Support

Funded by:

- City of Moscow
- Better d.o.o., Slovenia (formerly Marand)
- DIPS, Norway
- Ars Semantica, UK

### Intellectual Origins

Design ideas derived from:

- Industry use cases provided by Marand and DIPS implementers
- Activity-Based Design (ABD) project at Intermountain Healthcare (2015-)
- YAWL (Yet Another Workflow Language) research and standards review
- OMG BPMN (Business Process Modelling Notation)
- OMG CMMN (Case Management Modelling Notation)

### Trademarks

- 'openEHR' is a trademark of the openEHR Foundation
- 'OMG' is a trademark of the Object Management Group

---

## Preface

### Purpose

This specification defines openEHR Task Planning facilities addressing clinical process automation requirements. Central concepts include plans designed to achieve goals relating to an active subject. Plans incorporate decision logic and require access to subject data from backend systems.

**Intended Audience:**

- Standards bodies producing health informatics standards
- Academic groups using openEHR
- Open source healthcare community
- Solution vendors
- Medical informaticians and clinicians
- Health data managers

### Related Documents

**Prerequisite Documents:**

- The openEHR Architecture Overview
- The openEHR Process and Planning Overview

**Related Documents:**

- Task Planning Visual Modelling Language (TP-VML)
- openEHR Decision Language
- openEHR Process Examples
- openEHR EHR Information Model

### Status

This specification is in the **RETIRED** state.

### Feedback

- **Forum**: Process specifications forum
- **Issues**: Specifications Problem Report tracker
- **Changes**: PROC component Change Request tracker

### Conformance

Conformance to openEHR specifications is determined by formal testing against relevant Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

---

## Background

### Scope

#### Representation of Care Management Artefacts

This specification defines a model of structured plans that, when executed in an engine, provide notifications to workers relating to tasks. Plans require decision logic and subject data access.

Task Plans can represent:

- **Care pathways**: complex, condition-specific, outcome-oriented
- **Guidelines**: condition-specific, activity-oriented
- **Order set administration plans**: condition-specific
- **Patient plans**: subject-specific, derived from published pathways and guidelines or locally created

**Reference**: The openEHR Process and Planning Overview provides comprehensive overview.

#### Limitations of the openEHR Standard Entry Model

Task Planning addresses the inability of the openEHR EHR architecture to directly represent fine-grained tasks.

The openEHR Entry model defines representations for clinical statements (observations, decisions, orders, performed actions). Instructions represent orders for Actions such as "administer 3 times a day, for 7 days, with meals"—converted mentally by humans to individual tasks.

Task Planning provides concrete representation of planned Actions and Observations ahead of time as individual tasks that can be:

- Displayed
- Verified
- Performed (or not)
- Signed off by workers

A task set need not relate to a single order, or any order at all. A task plan corresponds to any self-standing healthcare job.

### What Task Planning Does Not Do

#### Task Lists (TODO Lists)

Task Planning centers on work plans designed to achieve goals for a subject. Task lists (worker-centric) must be derived from concurrently executing work plans.

- **Task list**: worker-centric; derived from plan execution for personal calendar views (days/weeks)
- **Work plan**: subject-centric; may correspond to any duration (minutes to years)

This specification does not cover worker task lists or extracted calendar views, though provides guidance.

#### Appointment Booking and Management

The planning paradigm does not address concrete creation and management of appointment bookings (complex administrative work). The system assumes existing systems manage administrative activity.

A task may request appointment creation for a visit at nominal time for a purpose. Plan waits for patient arrival via trigger events. Administrative activity to ensure patient appearance is external to task planning.

#### Clinical Decision Support (CDS)

This specification covers computable representation of decisions in work plans but does not replace CDS systems performing complex decision analysis via specialist knowledge bases.

Plans may request CDS system answers for specific queries (e.g., medication interactions, treatment proposals for hypertensive patients).

### Relationship to Existing Workflow Formalisms

Task Planning incorporates concepts from standard workflow languages including YAWL and OMG standards (BPMN, CMMN, DMN).

**Key Differences:**

The subject is assumed to be:

- An intentional agent (human patient) making choices
- An active biological organism reacting to interventions
- Not a passive object (unlike logistic workflows)

Other departures:

- Declarative rather than prescriptive plan graph structure definition
- Formalization of all plan elements and execution
- Non-deterministic design recognizing unknowable exceptions
- Self-standing task and group specification with preconditions rather than logical join/split operators

---

## Technical Requirements

### Overview

The openEHR Process and Planning Overview describes general requirements summarized as:

- Long term clinical plans
- Reminders/checklist items for often-missed actions
- Complex action sets from clinical pathways
- Decision points determining alternative paths
- Actions requiring sign-off
- Worker coordination in distributed teams
- Actions recording EHR information
- Actions with varying granularity for training modes

**Applicable Scenarios:**

- Routine medication administration (post-operative pain)
- Complex drug administration (multi-drug chemotherapy)
- Physiotherapy rehabilitation (recurrent procedure with endpoint)
- Dialysis (recurrent procedure)
- Diet and physical activity plans (patient performer)
- Surgery planning (one-time event)
- Acute stroke management (multiple coordinated performers)

### Flexible Allocation of Workers

Worker availability must be accommodated. Specific workers can leave and be replaced:

- During active work periods
- Between tasks within plans
- Due to shift changes, vacations, or unforeseen unavailability

### Coordinated Teamwork

Plans often require team execution with specialized performers:

- Each performer handles their work portion
- Control passes between team members
- Workers may operate in parallel with real-time communication
- If physically separated, notifications alert workers when to commence and callback notifications alert when other work completes

**Example**: Acute stroke management involving multiple specialists.

### Planned Tasks for an Order

The simplest requirement is posting a full action plan in advance, resulting in Tasks for each planned openEHR ACTION.

An openEHR INSTRUCTION (e.g., "Amoxicillin 500mg oral tablet 3 times/day x 7 days") is interpreted by agents into separate tasks (21 administrations). These can be represented as plan Tasks for performance and sign-off.

**Challenge**: Some work is open-ended with no known completion date (e.g., chronic diabetes insulin treatment).

### Tracking Orders from Plans

Standard clinic activity includes raising orders (lab tests, radiology) and awaiting results, commonly within protocol-based plans.

Plans should enable:

- Creating orders
- Executing (sending) orders
- Waiting on results
- Managing multiple simultaneous orders in the same plan

### Order Sets and Protocols

Plans typically encompass multiple orders following protocols or regimens.

**Example**: Multi-drug chemotherapy (R-CHOP protocol):

| Drug | Standard R-CHOP-14/21 | R-Maxi-CHOP | Mode | Days |
|------|---|---|---|---|
| Rituximab | 375 mg/m² | 375 mg/m² | IV infusion | Day 1 |
| Cyclophosphamide | 750 mg/m² | 1200 mg/m² | IV infusion | Day 1 |
| Hydroxydaunorubicin | 50 mg/m² | 75 mg/m² | IV bolus | Day 1 |
| Oncovin | 1.4 mg/m² (max 2 mg) | 2 mg | IV bolus | Day 1 |
| Prednisone/Prednisolone | 40 mg/m² | 100 mg | PO qd | Days 1-5 |

Plans must support protocols with multiple order components and actions without orders (observations, checks).

### Lookahead Plan

Flexible planning posts tasks for moving time windows (one day, few days, nursing rotations).

Rather than planning complete execution, tasks are executed and more added. Planned task timing may change, resulting in different overall task unfolding than complete pre-execution planning.

**Required for**: Open-ended cases where completion date is unknown or unclear.

### Recurring/Repeatable Tasks

Many clinical plans involve time-based repetition:

- Multi-iteration treatment (CHOP-14: 5-day treatment every 14 days for 3 iterations)
- Permanently recurring lifelong therapy (asthma)

### Checklist & Sign-off

Posted task plans viewed as checklists are signed off as performed or not done. Utility includes:

- Correspondence between planned tasks and performed actions established
- Planned Action A1 marked as intentionally performed (even if at time T' rather than T)
- Picture emerging of planned actions performed and signed off
- Identification of missed, unnecessary, or externally-done tasks

### Sub-plans

Plans vary by detail level depending on worker experience requirements.

- One institution may describe cannulation atomically
- Another may require guideline-based step-by-step execution

**General Case**: Any task representable as single plan item could also be represented as reference to separate detailed plan.

### Task Grouping, Optionality and Execution Basis

Task sets achieving defined goals may be executed:

- Sequentially or in parallel
- With sub-groups executing together
- With optional or conditional execution

**Example**: Sequential plan with parallel sub-group step.

Designate tasks as optional, executed conditionally.

### Decision Pathways

Care pathway or guideline-derived plans contain decision points:

- **Decision point**: Variable assignment (e.g., `$v := expression`)
- **Subordinate decision paths**: Task groups with variable tests (e.g., `$v rel_op value`)

**Example**: Intermountain Healthcare Ischemic Stroke Care Process Module classifying symptom onset time with subsequent path decisions.

### Different Types of Cancellation

Tasks may be cancelled before execution for two reasons:

- **Cancellation**: Task cannot be performed (resource lack); equivalent to task failure
- **Unnecessary cancellation**: Task isn't needed, already done externally; equivalent to task success

System must distinguish flavors to reliably determine plan success/failure.

### Changes and Abandonment

Plans may require midway changes or abandonment due to unexpected patient situation changes.

**Supported Abandonment Types:**

- Entire plan cancellation
- Particular task cancellation with reason
- Task marked "did not perform" after planned time with reason

**Implementation**: Planned tasks initially exist in 'planning buffer', committed to EHR when performed, explicitly marked not done, or included in not-done action list upon abandonment.

### Rationalising Unrelated Work Plans

Multiple concurrent plans for different problems and timelines may exist for same subject (chemotherapy, hypertension, ante-natal care).

Support needed for:

- Locating existing plans
- Scanning times, states, resources
- Avoiding clashes
- Finding rationalisation opportunities (grouping tasks into single visit, coordinating blood draws)
- Processing multiple plans for 'patient diary' construction (rationalised work list)

### Support Process Analytics

Differences typically exist between planned tasks and actual performed actions:

- **Execution time**: Planned time T vs. actual T'
- **Performer**: Intended vs. actual performer type
- **Order details**: Modifications (e.g., medication dose adjustments)

These differences provide analytics resources via EHR representation of both planned tasks and performed actions.

### Support for Costing and Billing Information

System should record:

- **Internal costing**: Against plans and individual tasks (inventory consumption, time, resources)
- **External billing**: Using nationally agreed code systems (ICD10 etc.)

---

## Design Principles

### Conceptual Model

Plans are not standalone, requiring decision logic and subject data access.

**Key Consequence**: Plans use symbolic references (rather than inline expressions) to:

- Proxy values (patient state, diagnoses)
- Decision logic functions

All expressions are represented externally via decision logic modules or proxies, maintained as independent knowledge artefacts used by plans.

### Computational Basis

Plans are executable, with objective computational meaning enabling execution per specification semantics.

This ensures:

- No ambiguous plan meaning
- Conversion of dispersed workers with weak communication into integrated coordinated teams
- Following YAWL approach

### Computation Context

A Task Planning execution engine executes Plans and related Decision support modules, obtaining patient information via Subject proxy (converting EHR data to virtual patient view).

**External Communication**: Plans communicate with other systems via:

- openEHR EHR systems
- External organizations (email, phone)
- Communication/notification systems

**User Connection**: Performers connect via applications communicating with TP Engine API. Plan designers connect via dedicated designer applications.

#### Separation of Definition and Execution

Clear separation of Plan definition and execution is fundamental, distinguishing multiple representation levels:

| Level | Type | Purpose |
|-------|------|---------|
| **Design time** | Plan template (archetyped) | Reusable plan components |
| **Planning** | Plan definition (instantiated) | Concrete patient-specific plan |
| **Execution** | Plan execution (materialized) | Runtime plan execution |
| **Task execution** | Runtime instantiation | Current user session tasks |

---

### Conceptual Elements

#### Work Plan

The top-level formal concept is the Work Plan, consisting of one or more Task Plans.

**Definition**: A definition of work performed by one or more workers achieving a defined goal for a single subject of care.

**Structure**: Within a Work Plan:

- Each Task Plan defines work in single work context by principal performer and possibly other participants
- Multiple Task Plans occur due to:
  - Distinct performers in different contexts (requiring managed hand-offs)
  - Sub-plans subordinate to parent Task Plan

**Execution Scope**: Entirety of Work Plan executes within single computational context (Task Planning engine).

**Geographic Scope**: Usually single enterprise, though may span organizations if all Task Plans communicate within same execution context.

#### Task Plan

Work definition in one context with principal performer consists of Tasks.

**Basic Structuring**: 

- Sequential task lists (linear workflows)
- Hierarchical structure enabling fractal subdivision
- **Formal construct**: Task Group containing Tasks and more Task Groups

**Task Definition**: A separately performable item of work for a performer.

**Business Correspondence**:

- Explicit clinical responsibility level
- Explicit reimbursement/billing level
- Protocol single items designed for sign-off
- Particular planned execution time

##### Parallel and Sequential Execution

Hierarchy and sequential execution enable representation of most work types.

**Additional Feature**: Parallel execution—tasks performable without regard to order.

**Execution Type Indicator**: At Task Group level indicating sequential or parallel performance.

**Effect**: Enables multiple execution paths during plan execution.

##### Conditional Structures

Task Groups augmented with conditions create conditional structures representing:

- **if/elseif/else**: Multi-branch logic chain with conditions evaluated in order
- **switch**: Multi-way structure based on single condition with multiple value branches
- **rule-set**: Chained event-driven rules firing on specific event types

**Human/System Interaction Levels**:

1. **Fully automated**: Formal conditions fully express criteria for alternate paths
2. **Decision support**: Formal conditions provide support but may be overridden by users
3. **Ad hoc**: Alternate pathways defined with user-provided runtime criteria

##### Summary

Reverse hierarchy of structures:

- **Task**: Separately performable unit at any granularity; inline or sub-plan defined
- **Task Group**: Group of Tasks/more Groups executed on same basis (sequential, parallel)
- **Conditional Group types**: Special Task Groups enabling conditional logic
- **Task Plan**: Logical task set for single performer context achieving defined result
- **Work Plan**: Top-level structure with related Task Plans implementing intended outcome

#### Graph Structure

Task Group replaces traditional workflow node references, defining static graph structure by implication.

**Advantage**: Only exceptions to normal flow represented with explicit node references.

**Power**: Task Groups with attached rules (e.g., sequential/parallel indicator) rather than explicit links.

#### Work Context

Fundamental concept: work context distinguishes Task Plans.

**Definition**: A single, contiguous cognitive flow in the real world (not computation) in which work is performed seamlessly by one or more performers on a single subject.

**Characteristics**:

- Unbroken cognitive activity flow
- Single or multiple persons working as one with real-time communication
- Different context = different cognitive actors
- Communications via notifications at checkpoints (typically beginning and end)

**Parallelism**: A performer may work on multiple items concurrently within same context.

#### Context Switch and Fork

Two types of control changes:

**Context Switch**: Work stops in one context and passes to different context; original worker waits for response.
- Within same Work Plan = **hand-off** (Task Plan switch)
- Different environment = external request

**Context Fork**: Current performer signals another context to start work but continues own work.

**Terminology**:
- Context switch = synchronous/block-and-wait processing
- Context fork = asynchronous/parallel processing

**Hand-off Scenarios**:

1. **Inputs immediately available**: Notify next performer; they begin immediately (e.g., radiologist after images ready)
2. **Performer-availability dependent**: Add to performer's work queue (e.g., doctor seeing patients in turn)
3. **Subject-availability dependent**: Start when subject available (e.g., transfusion unit upon patient arrival)

#### Context Continuity over Worker Shifts

Work extending over hours or days involves worker shift changes.

**Model Position**: Not treated as context switch.

**Assumption**: Task Planning runtime maintains all relevant context information for new workers.

**Requirement**: De-allocation and re-allocation to replacement performers only.

#### Principal Performer

Following work context concept, a Task Plan has a principal performer—single logical executing actor.

**Types**:

- Single person
- Device
- Software service
- Personnel group (e.g., ward nurses across shifts) working as "single mind"

**Other Participations**: Additional participants specified for individual Tasks within plan.

**Responsibility**: Principal performer is responsible for all actions and notification of completions/cancellations.

**Specification**: Principal performer and participants specified as professional roles, optionally with specific agent (possibly patient).

**Work Plan Coordination**: Where multiple actors in different contexts required, separate Task Plans each with own principal performers; coordination via context switching and notification.

**Allocation**: During execution, particular physical actor assigned as principal performer, changing over time due to shifts, vacations, out-of-hours contacts.

#### Time and Wait States

Many tasks executable only when events occur or conditions become true, treated as wait states.

**Time Understanding**:

- **Relative offset**: From plan timeline start upon activation
- **Absolute time**: Calendar markings
- **Event moment**: When event occurs

**First two converted to artificial events**: Execution system internal clock reaching timeline/calendar markers.

**Real Event Types**:

- **Timer event**: Timer expiration
- **State trigger**: Watched variable conditions (subject variables, clinical process variables)
- **Task transition**: Prior task state transitions
- **Callback notification**: Dispatched task completion in different plan/external system
- **System notification**: External event notified by user
- **Manual notification**: User-signaled external event

**Task Definition**: Tasks may wait on one or more events.

### Levels of Definition and Representation

Task Plans defined, refined, and used in various phases:

| Phase | Representation | Purpose |
|-------|---|---|
| Design | Definition model (archetyped templates) | Reusable models at increasing specialization |
| Planning | Instantiated definition (subject instance) | Concrete patient-specific plan; adjustable |
| Execution | Materialised definition (execution run) | Published, persisted reference model |
| Task execution | Runtime instantiation (session subset) | Current user/performer session |

#### Phases of Work

**Design Phase**: Archetype and template-based modeling creates progressive specialization hierarchy enabling:

- Reusable model generation
- Object-oriented-like flexibility

**Planning Phase**: Work Plan template instantiated by clinical planner creating definition instances stored in patient EHR Composition.

- Multiple workers may perform modifications over time
- Patient EHR may contain multiple Work Plan definitions simultaneously

**Execution Phase**: Work Plan materialized from EHR into TP Engine for execution.

- Materialised Plan expression records all plan-related performer actions
- Plan execution may be long-lived (extending beyond single worker session)
- Execution state persisted

**Runtime Execution**: Multiple executions within execution phase, during individual application invocations with performers and applications.

**EHR Recording**: Work results documented via openEHR Entries (Actions, Observations).

### Execution Concepts

#### Plan Execution Lifecycle

Work Plan definition execution involves three states:

**1. Materialised State**:
- Post-creation, plan may be modified by users
- Pre-allocations of performers possible

**2. Activated State**:
- Materialised plan activated when users proceed
- Connections established between plan execution context and performer allocation/communication channels
- Execution clock zero point established
- Initial performer allocations generate notifications as time moves forward
- Tasks become available as earlier tasks complete/cancel
- Performers may: do work, cancel task (not needed), complete, abort, abandon plan

**3. Terminated State**:
- Occurs when materialized task graph path terminates
- Either finishing or abandonment at intermediate task
- Returns termination status (success/fail) controlling downstream behavior in context-switch chains

#### Allocation

Worker allocation connects Plan system representation to real-world actors performing work.

**Worker Resource Types**:

- **Individuals**: Specified in plan as role/function (e.g., 'cardiologist')
- **Worker pool**: Group of equivalent workers (e.g., ward nurses); any can perform task; may swap over time

**Runtime Resolution**:

- Plan/Task assigned to real individual or worker pool
- Appropriate worker claims plan (if posted awaiting workers) or accepts task (if invitations sent)
- Organization and TP Engine determine resolution

**Allocation Strategies**: Sophisticated implementations may offer first-available, quickest-to-complete, least-frequently-used, etc.

#### Task Lifecycle

Every Task has lifecycle state machine representing real-world work state as known by plan execution system.

**States**:

| State | Meaning |
|-------|---------|
| `planned` | Initial state |
| `available` | Ready to perform |
| `completed` | Successful completion |
| `cancelled` | Not needed (benign cancellation) |
| `abandoned` | Cannot complete; plan abandonment |

**Success Path**: `planned` ⇒ `available` ⇒ `completed`

**Terminal States**: `cancelled`, `abandoned`

**Special Transition**: `override` forces Task into `available` state despite preconditions.

**Plan Impact**:

- Task `completed` or `cancelled` = success; plan remains `active`
- Task `abandoned` = failure; plan terminates with failure status

#### Availability

Task becomes available when three conditions met:

1. **Execution control flow reaches task**: Preceding tasks completed (local flow) or previously dispatched external task completing with restart at current task
2. **Waited-on external events occur**: Scheduled time reached or event notification received
3. **Subject preconditions met**: If specified, conditions satisfied (e.g., systolic BP < 160 mmHg)

**Override Exception**: Performer always allowed to override external and subject preconditions (better real-world knowledge); control flow requirement still holds.

**Performer Allocation**: Nothing happens until available worker allocated; allocation triggers commencement and further lifecycle states.

#### Adaptive Modification and Exception-handling

Key model assumption: human/other performer always knows best.

**Consequence**: System-posted tasks are advisory; details (such as time) are advisory.

**Support for Execution-time Adaptation**:

- **Logical deletion**: Tasks skipped via two cancellation types: `cancelled` (not needed—benign), `abandoned` (abandon plan—fails)
- **Logical addition**: Unplanned work items always performable (extra observations, unplanned actions); recorded via normal Entries
- **Overrides**: Runtime override of plan aspects (task time, subject preconditions); represented as alternative lifecycle transition

### Relationship of Tasks with existing openEHR Entry Types

Task Plans not standalone; existing openEHR Entry types represent orders (INSTRUCTION) and performed activities (ACTION).

**Hierarchy**:

- INSTRUCTION: Formal "what is to be done" (concise, order-suitable)
- Task Plan: Detailed step-by-step plan
- ACTION/OBSERVATION/EVALUATION/ADMIN_ENTRY: Records of "what was done"

**Not Every Task Equals Order**: General case has Work Plan corresponding to clinical goal implicating multiple orders; some plan tasks lack orders.

**Task Correspondence Variations**:

- Typically: Task = unrecorded openEHR ACTION (with driving INSTRUCTION)
- Also: ACTION without INSTRUCTION, OBSERVATION, EVALUATION, ADMIN_ENTRY

**Plan Driver**: Usually care plan or guideline (including orders), or ad hoc planning.

### Order Semantics versus Plan Semantics

**Key Difference**: Semantic expression level.

**INSTRUCTION** (Order): Algorithmic form expressing interpreted program mentally.

- Example: "Amoxicillin 3 times a day, orally, for 7 days"
- Human-interpreted to resultant actions

**Task Plan**: Interpreted order form—"unfolded" list of single tasks in time.

- Example: "Give 1 Amoxicillin oral tab at lunch"
- Suitable for work lists, check-off, mistake prevention
- Task performance generates appropriate openEHR Entry (e.g., "gave 1 Amoxicillin tab at 13:37")

---

## Task Planning Model Overview

### Identification and Referencing

Various elements require runtime referencing:

- Tasks and Task Groups identified via `_uid_` attribute (inherited from LOCATABLE via PLAN_ITEM)
- Populated with Guid
- References via UID_BASED_ID instances carrying Guid

### Plan Data Context

**TBD**: Section needs upgrade to latest Expression Language and Business Model Management model. Type `EXPR_TYPE_DEF` to be replaced by BMM equivalent.

Task Plan contains logical symbolic values:

- Constants
- Variable references
- Expressions

Globally tracked at Work Plan level (common to all Task Plans).

**Tracking**: Each context value has:
- Symbolic name (`CONTEXT_VALUE._name_`)
- Type from openEHR type system (`EXPR_TYPE_DEF`)

**Representation Classes**:

- `CONTEXT_VARIABLE<T>`: Atomic variables
- `CONTEXT_CONSTANT<T>`: Constants
- `CONTEXT_EXPRESSION<T>`: Expressions referencing variables

Generic classes with type parameter.

**Variable Types**:

- **Subject state**: Patient vital signs, demographics
- **Clinical care process**: Time since stroke event, etc.

**Expression Types**: Logical expressions (e.g., `$bp_systolic - $bp_diastolic`)

**Expression Syntax**: Defined by openEHR Expression Language

**Variable Distinction**: External vs. Local

#### External Variables

Represent outside-environment entity values.

- Written via `_populating_request_` using EHR queries, API calls
- Not writable from within Work Plan

**Subtypes**:

- **Event variable**: Watched for changes; value updates on change
- **State variable**: Standard external variable
- **Continuous event variable**: For continuous-valued variables (real numbers) with threshold-based updates (e.g., changes < 2% ignored)

#### Local Variables

Internal to Work Plan.

- Readable and writable by expressions within Tasks

#### Class Descriptions

##### PLAN_DATA_CONTEXT Class

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `variables` | `0..1 List<CONTEXT_VARIABLE>` | All tracked plan variables |
| `expressions` | `0..1 List<CONTEXT_EXPRESSION>` | All plan expressions based on variables |
| `constants` | `0..1 List<CONTEXT_CONSTANT>` | All plan constants |

##### CONTEXT_VALUE Class (Abstract)

**Generic**: `CONTEXT_VALUE<T>`

**Type Parameter**: Formal value type (Boolean, Integer, etc.)

**Type Representation**: `EXPR_TYPE_DEF`

**Attributes**:

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `name` | `1..1 String` | Symbolic name |
| `type` | `1..1 EXPR_TYPE_DEF` | Formal type |

##### CONTEXT_CONSTANT Class

Subclass of `CONTEXT_VALUE<T>`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `value` | `1..1 T` | Constant value |

##### CONTEXT_VARIABLE Class

Subclass of `CONTEXT_VALUE<T>`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `initial_value` | `0..1 T` | Initial value |

##### EXTERNAL_VARIABLE Class

Subclass of `CONTEXT_VARIABLE<T>`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `populating_request` | `1..1 SYSTEM_CALL` | Method obtaining external value |

##### LOCAL_VARIABLE Class

Subclass of `CONTEXT_VARIABLE<T>`

No additional attributes.

##### EVENT_VARIABLE Class

Subclass of `EXTERNAL_VARIABLE<T>`

Watched variable; updated on change detection.

##### CONTINUOUS_EVENT_VARIABLE Class

Subclass of `EVENT_VARIABLE<T>`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `update_threshold` | `0..1 Real` | Percentage threshold for updates (e.g., 2% = 0.02) |

##### STATE_VARIABLE Class

Subclass of `EXTERNAL_VARIABLE<T>`

Standard external variable; updated by periodic polling or push notifications.

##### CONTEXT_EXPRESSION Class

Subclass of `CONTEXT_VALUE<T>`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `expression` | `1..1 String` | Expression text (openEHR Expression Language) |

##### BOOLEAN_CONTEXT_EXPRESSION Class

Subclass of `CONTEXT_EXPRESSION<Boolean>`

Boolean expression for conditions and decisions.

### System Calls

#### Generic API Calls

Plans reference external system capabilities via generic API calls for:

- Computing values
- Checking conditions
- Initiating external processes

#### Query Calls

Specialized system calls querying external systems (particularly EHR).

#### Class Descriptions

##### SYSTEM_CALL Class (Abstract)

Base class for system calls.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `name` | `1..1 String` | Call name/identifier |
| `description` | `0..1 String` | Human-readable description |
| `parameters` | `0..1 List<PARAMETER_DEF>` | Call parameters |
| `return_type` | `1..1 EXPR_TYPE_DEF` | Return value type |

##### PARAMETER_DEF Class

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `name` | `1..1 String` | Parameter name |
| `type` | `1..1 EXPR_TYPE_DEF` | Parameter type |
| `description` | `0..1 String` | Parameter description |

##### PARAMETER_MAPPING Class

Binds call parameters to variable/expression values.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `parameter_name` | `1..1 String` | Parameter to bind |
| `value_source` | `1..1 String` | Variable/expression providing value |

##### API_CALL Class

Subclass of `SYSTEM_CALL`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `service_id` | `1..1 String` | External system identifier |
| `parameter_mappings` | `0..1 List<PARAMETER_MAPPING>` | Parameter bindings |

##### QUERY_CALL Class

Subclass of `SYSTEM_CALL`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `query_specification` | `1..1 String` | Query (AQL, SQL, etc.) |
| `result_binding` | `0..1 String` | Variable receiving result |

### Variable Referencing

Variables referenced in expressions and conditions using `$variable_name` syntax.

Type consistency checked at definition time; runtime type mismatch handling implementation-defined.

### Specifying Time

#### Class Descriptions

##### TIME_SPECIFIER Class (Abstract)

Base class for time specifications.

Subclasses represent different time forms.

##### CLOCK_TIME Class

Subclass of `TIME_SPECIFIER`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `hour` | `0..1 Integer` | 0-23 |
| `minute` | `0..1 Integer` | 0-59 |
| `second` | `0..1 Integer` | 0-59 |

Represents time of day.

##### CUSTOMARY_TIME Class

Subclass of `TIME_SPECIFIER`

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `customary_time` | `1..1 String` | Customary designation (e.g., "breakfast time", "afternoon") |

Allows culturally familiar time references.

### Enumerated Types

#### RESUME_TYPE Enumeration

Controls task resumption after interruption.

**Values**:

- `AT_TIME`: Resume at specified time
- `IMMEDIATE`: Resume immediately
- `MANUAL`: Await manual notification

#### TEMPORAL_RELATION Enumeration

Temporal relationships for time specifications.

**Values**:

- `BEFORE`: Before specified time
- `AT`: At specified time
- `AFTER`: After specified time
- `WITHIN`: Within time range

#### EXECUTION_TYPE Enumeration

Task group execution mode.

**Values**:

- `SEQUENTIAL`: Execute in defined order
- `PARALLEL`: Execute in any order concurrently

#### PLAN_TIME_ORIGIN Enumeration

Time origin for relative time specifications.

**Values**:

- `PLAN_START`: Relative to plan activation
- `TASK_START`: Relative to task commencement
- `EVENT_TIME`: Relative to event occurrence

---

## Definition Model

### Overview

The definition model represents a Work Plan and Task Plans as designed for execution.

Classes divided into:

- **Plan Structure**: Work Plan, Task Plans, temporal aspects
- **Task Composition**: Task Groups, individual Tasks
- **Task Actions**: Performable and Dispatchable actions
- **Data Interaction**: Dataset specifications
- **Decision Logic**: Conditional structures
- **Order Tracking**: Order references and tracking
- **Events**: Temporal, state, and callback events
- **Costing**: Cost tracking information

### Plan Structure

#### The Plan Calendar

A Work Plan may optionally define a calendar marking significant moments (e.g., clinic dates, medication review dates).

**Use**: Reference in time specifications within plans.

#### Plan Items

Plan Items are containers for timed or conditionally-executed work elements (Tasks, Task Groups).

##### Wait States

Tasks may be defined with wait states indicating preconditions for availability.

**Wait State Types**:

- **Task wait**: Awaits completion of another task
- **Event wait**: Awaits specified event (timer, state change, callback)
- **Timer wait**: Awaits time-based event

##### Repetition

Tasks/Task Groups may repeat based on:

- **Count**: Fixed repetition number
- **Interval**: Time-based (e.g., daily for 7 days)
- **Until condition**: Repeat until condition satisfied
- **Unbounded**: Repeat indefinitely (for chronic conditions)

##### Other Attributes

| Attribute | Purpose |
|-----------|---------|
| Lifecycle state | Track execution progress |
| Availability state | Track readiness conditions |
| Optional marker | Designate optional tasks |
| Training level | Specify training detail level |

#### Lifecycle State

##### TASK_LIFECYCLE Enumeration

Task states through execution:

| State | Meaning |
|-------|---------|
| `planned` | Defined but not available |
| `available` | Ready for performance |
| `underway` | Active performance |
| `completed` | Successfully finished |
| `cancelled` | Not needed |
| `abandoned` | Cannot perform |

##### Task Availability

Tasks become available when:

- Control flow reaches task
- Wait condition satisfied
- Subject preconditions met

##### Aggregate Process State

Determines plan-level status based on contained tasks:

- Sequential groups: Status progresses through tasks
- Parallel groups: Status reflects group completion semantics

#### References to Clinical Quality Artefacts

Tasks may reference:

- Guidelines
- Care pathways
- Protocols
- Quality measures

For traceability and compliance documentation.

#### Class Definitions

##### WORK_PLAN Class

Top-level plan structure.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `subject_id` | `1..1 OBJECT_REF` | Subject of care reference |
| `identifier` | `1..1 OBJECT_ID` | Unique plan identifier |
| `name` | `1..1 String` | Plan name/title |
| `description` | `0..1 String` | Plan description |
| `goal` | `0..1 String` | Clinical goal |
| `task_plans` | `1..* List<TASK_PLAN>` | Contained task plans |
| `data_context` | `0..1 PLAN_DATA_CONTEXT` | Variables and expressions |
| `calendar` | `0..1 PLAN_CALENDAR` | Optional timeline calendar |
| `start_condition` | `0..1 BOOLEAN_CONTEXT_EXPRESSION` | Condition for plan start |
| `completion_condition` | `0..1 BOOLEAN_CONTEXT_EXPRESSION` | Condition for plan completion |
| `root_task_group` | `1..1 TASK_GROUP` | Root task group |

##### PLAN_CALENDAR Class

Defines significant plan timeline moments.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `calendar_entries` | `1..* List<CALENDAR_ENTRY>` | Timeline moments |

##### PLAN_TIMELINE Class

Timeline within plan defining relative or absolute times.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `origin` | `1..1 PLAN_TIME_ORIGIN` | Time origin specification |
| `entries` | `0..* List<CALENDAR_ENTRY>` | Timeline entries |

##### CALENDAR_ENTRY Class

Single calendar moment.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `name` | `1..1 String` | Entry name/label |
| `time` | `1..1 TIME_SPECIFIER` | Time specification |
| `description` | `0..1 String` | Entry description |

##### TASK_PLAN Class

Work definition for single context with principal performer.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `identifier` | `1..1 OBJECT_ID` | Unique identifier |
| `name` | `1..1 String` | Plan name |
| `principal_performer` | `1..1 TASK_PARTICIPATION` | Primary performer specification |
| `other_participations` | `0..* List<TASK_PARTICIPATION>` | Additional participants |
| `root_group` | `1..1 TASK_GROUP` | Root task group |
| `start_condition` | `0..1 BOOLEAN_CONTEXT_EXPRESSION` | Start condition |
| `completion_condition` | `0..1 BOOLEAN_CONTEXT_EXPRESSION` | Completion condition |

##### TASK_PARTICIPATION Class

Specifies performer role and details.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `performer_role` | `1..1 String` | Role name/code |
| `specific_performer_id` | `0..1 OBJECT_REF` | Specific performer reference |
| `substitute_performers_allowed` | `1..1 Boolean` | Allow substitutions |

##### PLAN_ITEM Class

Abstract base for timed/conditional plan elements.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `name` | `1..1 String` | Item name |
| `description` | `0..1 String` | Item description |
| `optional` | `1..1 Boolean` | Optional marker |
| `wait_condition` | `0..1 TASK_WAIT` | Wait preconditions |
| `subject_precondition` | `0..1 SUBJECT_PRECONDITION` | Subject conditions |
| `lifecycle_state` | `1..1 TASK_LIFECYCLE` | Current state |

##### TASK_REPEAT Class

Repetition specification.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `repetition_type` | `1..1 String` | Fixed count, interval, until, unbounded |
| `repetition_count` | `0..1 Integer` | Fixed repetitions |
| `repetition_interval` | `0..1 Duration` | Time between repetitions |
| `termination_condition` | `0..1 BOOLEAN_CONTEXT_EXPRESSION` | Until condition |

### Task Group Structure

#### Sequential Task Groups

Tasks execute in defined order; one must complete before next available.

#### Parallel Task Groups and Concurrency

Multiple tasks execute concurrently; no ordering requirement.

**Concurrency Modes**:

| Mode | Semantics |
|------|-----------|
| `PARALLEL_ALL` | All members must complete |
| `PARALLEL_FIRST` | First completion terminates group |
| `PARALLEL_N` | N completions terminate group |

#### Hierarchical Nesting

Task Groups may contain other Task Groups enabling arbitrary hierarchy.

#### Generic Execution-time Semantics

Group execution semantics defined via rules allowing extensibility.

#### Well-formedness

Groups must satisfy structural constraints:

- No circular references
- All referenced tasks reachable
- Type consistency

#### Training Level

Task Groups may specify training detail level (novice, intermediate, expert), enabling flexible presentation.

#### Class Definitions

##### TASK_GROUP Class

Container for tasks/subtasks.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `members` | `0..* List<PLAN_ITEM>` | Contained tasks/groups |
| `execution_type` | `1..1 EXECUTION_TYPE` | Sequential/parallel |
| `concurrency_mode` | `0..1 CONCURRENCY_MODE` | Concurrency semantics |
| `execution_rule` | `0..1 EXECUTION_RULE` | Advanced execution rules |
| `training_level` | `0..1 Integer` | Training detail level |

##### EXECUTION_TYPE Enumeration

| Value | Meaning |
|-------|---------|
| `SEQUENTIAL` | Execute in order |
| `PARALLEL` | Execute concurrently |

##### CONCURRENCY_MODE Enumeration

| Value | Meaning |
|-------|---------|
| `PARALLEL_ALL` | All complete required |
| `PARALLEL_FIRST` | First completion ends group |
| `PARALLEL_N` | N completions end group |

##### EXECUTION_RULE Class

Advanced execution rules.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `rule_type` | `1..1 String` | Rule category |
| `rule_expression` | `1..1 String` | Rule specification |

### General Task Semantics

#### Dispatchable and Performable Tasks

Two fundamental task categories:

**Performable Task**: Work performed within current context; performer does work directly.

**Dispatchable Task**: Work performed in different context; requires handoff/external request.

#### Class Definitions

##### TASK Class (Abstract)

Base task class.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `name` | `1..1 String` | Task name |
| `description` | `0..1 String` | Task description |
| `optional` | `1..1 Boolean` | Optional marker |
| `wait_condition` | `0..1 TASK_WAIT` | Wait preconditions |
| `subject_precondition` | `0..1 SUBJECT_PRECONDITION` | Subject conditions |
| `planned_time` | `0..1 TIME_SPECIFIER` | Planned execution time |
| `estimated_duration` | `0..1 Duration` | Expected duration |

##### DISPATCHABLE_TASK Class

Subclass of TASK for external/handoff work.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `action` | `1..1 DISPATCHABLE_ACTION` | Action to dispatch |

##### PERFORMABLE_TASK Class

Subclass of TASK for direct performer work.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `action` | `1..1 PERFORMABLE_ACTION` | Action to perform |

### Task Actions

#### Performable Actions

Work performed directly by principal performer.

##### Sub-plans and Re-use

A task may reference separate detailed plan (sub-plan).

**Use Cases**:

- Detailed procedure specifications
- Reusable plan components
- Training-level flexibility

##### Inline Defined Actions

Actions specified inline within task.

**Types**:

- Clinical observations
- Procedure steps
- Assessments
- Documentation

#### Dispatchable Actions

Work performed by different context (handoff, external request, system request).

##### Hand-offs and Coordinated Teamwork

Pass work control to another performer in same Work Plan.

**Scenarios**:

- Specialist referrals
- Multi-stage procedures
- Department handoffs

##### External Request

Request work from external organization.

**Examples**:

- Laboratory tests
- Radiology imaging
- External consultations

##### System Request

Request work from IT system or service.

**Examples**:

- Report generation
- Data processing
- Automated procedures

#### Class Definitions

##### TASK_ACTION Class (Abstract)

Base action class.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `name` | `1..1 String` | Action name |
| `description` | `0..1 String` | Action description |

##### SUBJECT_PRECONDITION Class

Conditions on subject for action appropriateness.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `condition_expression` | `1..1 BOOLEAN_CONTEXT_EXPRESSION` | Precondition expression |
| `message` | `0..1 String` | User message if condition false |

##### PERFORMABLE_ACTION Class

Subclass of TASK_ACTION for direct performance.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `action_definition` | `1..1 DEFINED_ACTION` | Inline or sub-plan action |
| `archetype_id` | `0..1 String` | Associated archetype |
| `prototype_entry` | `0..1 COMPOSITION` | Prototype EHR entry |
| `resource_participations` | `0..* List<RESOURCE_PARTICIPATION>` | Resource requirements |

##### RESOURCE_PARTICIPATION Class

Specifies required resources (not performers).

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `resource_type` | `1..1 String` | Resource category |
| `quantity` | `0..1 Real` | Required amount |
| `unit` | `0..1 String` | Measurement unit |
| `resource_id` | `0..1 String` | Specific resource identifier |

##### DEFINED_ACTION Class

Abstract base for defined actions.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `name` | `1..1 String` | Action name |

##### SUB_PLAN Class

Subclass of DEFINED_ACTION referencing sub-plan.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `sub_plan_id` | `1..1 OBJECT_REF` | Referenced plan identifier |
| `plan_timeline` | `0..1 PLAN_TIMELINE` | Sub-plan timing |

##### DISPATCHABLE_ACTION Class

Subclass of TASK_ACTION for work dispatch.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `action_type` | `1..1 String` | Handoff, external, system |
| `request` | `1..1 DISPATCHABLE_ACTION` | Actual action subclass |

##### HAND_OFF Class

Subclass of DISPATCHABLE_ACTION for performer handoff.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `target_task_plan_id` | `1..1 OBJECT_REF` | Handoff destination plan |
| `input_parameters` | `0..* List<PARAMETER_MAPPING>` | Data passed to destination |
| `output_parameters` | `0..* List<PARAMETER_MAPPING>` | Expected results |
| `callback_location` | `0..1 OBJECT_REF` | Resumption point on completion |

##### EXTERNAL_REQUEST Class

Subclass of DISPATCHABLE_ACTION for external organization request.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `external_organization_id` | `1..1 String` | Organization identifier |
| `request_specification` | `1..1 String` | What to request |
| `expected_response_type` | `0..1 EXPR_TYPE_DEF` | Response type |
| `timeout_period` | `0..1 Duration` | Response timeout |

##### SYSTEM_REQUEST Class

Subclass of DISPATCHABLE_ACTION for system/IT service request.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `system_call` | `1..1 SYSTEM_CALL` | API/query call |
| `result_variable` | `0..1 String` | Variable receiving result |

##### LINKED_PLAN Class

Plan reference supporting multiple execution instances.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `plan_id` | `1..1 OBJECT_REF` | Referenced plan identifier |
| `version` | `0..1 String` | Plan version |
| `instantiation_id` | `1..1 UID` | Unique instantiation identifier |

### Data-sets and Application Interaction

#### Overview

Tasks may specify data display, capture, and review specifications for performer interaction.

#### Display and Capture Data-sets

**Display Data-set**: Information displayed to performer (patient history, measurements, etc.).

**Capture Data-set**: Information entered by performer during task performance.

**Review Data-set**: Information reviewed by performer before task sign-off.

#### Progressive Data Capture

Data captured in phases:

1. Initial data collection
2. Intermediate updates
3. Final sign-off data

Each phase may have different data requirements.

#### Class Definitions

##### DATASET_SPEC Class (Abstract)

Base dataset specification.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `dataset_id` | `1..1 String` | Unique dataset identifier |
| `name` | `1..1 String` | Dataset name |
| `archetype_ids` | `0..* List<String>` | Associated archetypes |
| `template_id` | `0..1 String` | Associated template |

##### CAPTURE_DATASET_SPEC Class

Subclass of DATASET_SPEC for data entry.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `required_elements` | `0..* List<String>` | Mandatory data items |
| `optional_elements` | `0..* List<String>` | Optional data items |
| `dataset_commit_groups` | `0..* List<DATASET_COMMIT_GROUP>` | Commit phases |

##### REVIEW_DATASET_SPEC Class

Subclass of DATASET_SPEC for sign-off review.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `reviewed_elements` | `0..* List<String>` | Items reviewed |
| `sign_off_required` | `1..1 Boolean` | Signature required |

##### DATASET_COMMIT_GROUP Class

Groups data capture into phases.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `group_id` | `1..1 String` | Group identifier |
| `group_name` | `1..1 String` | Group name |
| `data_items` | `1..* List<String>` | Data items in group |
| `commit_timing` | `0..1 STRING` | When to commit (immediate, end-of-task, etc.) |

### Decision Structures

#### Overview

Conditional structures enable decision pathways in plans.

#### Condition Group (if/elseif/else chain)

Multiple conditions evaluated in order.

**Structure**:

```
if condition_1 then
  execute branch_1
elseif condition_2 then
  execute branch_2
else
  execute default_branch
```

#### Decision Group (case)

Single condition with multiple value-based branches.

**Structure**:

```
case $variable of
  value_1 → branch_1
  value_2 → branch_2
  ...
  default → default_branch
```

#### Event Group

Event-driven conditional structure.

**Structure**:

```
on event_1 do branch_1
on event_2 do branch_2
...
```

#### Class Definitions

##### CHOICE_GROUP Class (Abstract)

Base class for conditional structures.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `name` | `1..1 String` | Group name |
| `branches` | `1..* List<CHOICE_BRANCH>` | Decision branches |
| `override_type` | `0..1 OVERRIDE_TYPE` | Override behavior |

##### OVERRIDE_TYPE Enumeration

Controls runtime override ability.

| Value | Meaning |
|-------|---------|
| `NONE` | No override allowed |
| `WARN` | Override with warning |
| `ALLOW` | Override without restriction |

##### CHOICE_BRANCH Class (Abstract)

Base branch class.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `task_group` | `1..1 TASK_GROUP` | Branch task group |

##### CONDITION_GROUP Class

Subclass of CHOICE_GROUP for if/elseif/else.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `condition_branches` | `1..* List<CONDITION_BRANCH>` | Condition branches |
| `default_branch` | `0..1 TASK_GROUP` | Default tasks |

##### CONDITION_BRANCH Class

Subclass of CHOICE_BRANCH for single condition.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `condition` | `1..1 BOOLEAN_CONTEXT_EXPRESSION` | Branch condition |
| `task_group` | `1..1 TASK_GROUP` | Tasks if condition true |

##### DECISION_GROUP Class

Subclass of CHOICE_GROUP for case/switch.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `decision_variable` | `1..1 String` | Variable to test |
| `decision_branches` | `1..* List<DECISION_BRANCH>` | Value branches |
| `default_branch` | `0..1 TASK_GROUP` | Default tasks |

##### DECISION_BRANCH Class

Subclass of CHOICE_BRANCH for value range.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `value_range` | `1..1 String` | Value specification |
| `task_group` | `1..1 TASK_GROUP` | Tasks for value range |

##### ADHOC_GROUP Class

Subclass of CHOICE_GROUP for runtime user-determined paths.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `branches` | `1..* List<ADHOC_BRANCH>` | Available options |
| `description` | `0..1 String` | Path selection guidance |

##### ADHOC_BRANCH Class

Subclass of CHOICE_BRANCH for ad hoc option.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `option_description` | `1..1 String` | User-facing option description |
| `task_group` | `1..1 TASK_GROUP` | Tasks for option |

##### EVENT_GROUP Class

Subclass of CHOICE_GROUP for event-driven logic.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `event_branches` | `1..* List<EVENT_BRANCH>` | Event branches |
| `timeout_task_group` | `0..1 TASK_GROUP` | Tasks on timeout |

##### EVENT_BRANCH Class

Subclass of CHOICE_BRANCH for event condition.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `event_trigger` | `1..1 EVENT` | Triggering event |
| `task_group` | `1..1 TASK_GROUP` | Tasks on event |

### Order Tracking

#### Tracking an Existing Order

A task may reference an existing openEHR INSTRUCTION order and track its execution.

#### Creating and Tracking an Order

A task may create an order and subsequently track its progress.

#### Class Definitions

##### ORDER_REF Class

Reference to openEHR order (INSTRUCTION).

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `order_id` | `1..1 OBJECT_REF` | Order reference |
| `order_archetype` | `0..1 String` | Order archetype |
| `tracking_purpose` | `0..1 String` | Why tracked |

### Events

#### Overview

Events trigger task transitions and wait condition completions.

#### Event Types

##### TIMELINE_MOMENT

Specific point in time on plan calendar.

#### General Facilities

##### Event Wait State

Task waits for event occurrence.

##### Timers

Time-based delays triggering task availability.

##### Reminder

Notification upon event or time.

#### Task Wait State

Task waits for completion event.

##### Time-outs

Maximum wait duration before forced transition.

##### Reminder

User notification of pending task.

##### Lifecycle Transition Override

Force task state transition despite unmet conditions.

#### Callbacks

Notification callbacks on task completion in different context.

##### Callback Processing for Blocking Tasks

Dispatched task blocks current plan until completion.

##### Callback Processing for Non-blocking Tasks

Dispatched task doesn't block current plan.

##### Callback with Custom Resume Behaviour

Resume behavior specified beyond standard.

##### Manually-notified Pseudo-callback

Manual user notification of external event.

#### Class Definitions

##### TASK_WAIT Class

Task waits for condition(s).

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `wait_conditions` | `1..* List<TASK_WAIT>` | Conditions awaited |
| `timeout` | `0..1 Duration` | Maximum wait time |
| `timeout_action` | `0..1 RESUME_ACTION` | Action on timeout |
| `reminder` | `0..1 REMINDER` | Reminder specification |

##### EVENT_WAIT Class

Subclass of TASK_WAIT for event condition.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `event_trigger` | `1..1 EVENT` | Awaited event |

##### TIMER_WAIT Class

Subclass of TASK_WAIT for time-based wait.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `timer_event` | `1..1 TIMER_EVENT` | Timer specification |

##### REMINDER Class

Reminder notification specification.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `reminder_timing` | `1..1 TIME_SPECIFIER` | When to remind |
| `reminder_method` | `0..1 String` | How to remind (email, SMS, etc.) |
| `reminder_message` | `0..1 String` | Message content |

##### CALLBACK_WAIT Class

Subclass of TASK_WAIT for dispatched task completion.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `callback_event` | `1..1 CALLBACK_NOTIFICATION` | Callback source |
| `blocking` | `1..1 Boolean` | Blocks current plan |
| `resume_action` | `0..1 RESUME_ACTION` | Resumption behavior |

##### EVENT_ACTION Class

Action triggered by event.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `target_task` | `1..1 OBJECT_REF` | Task to act upon |
| `action_type` | `1..1 String` | Action type |

##### RESUME_ACTION Class

Specifies task resumption behavior.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `resume_type` | `1..1 RESUME_TYPE` | How to resume |
| `resume_time` | `0..1 TIME_SPECIFIER` | Time to resume |

##### EVENT Class (Abstract)

Base event class.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `name` | `1..1 String` | Event name |

##### PLAN_EVENT Class

Subclass of EVENT for plan-internal events.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `event_type` | `1..1 String` | Event category |

##### TIMER_EVENT Class

Subclass of EVENT for time-based events.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `delay` | `1..1 Duration` | Delay duration |
| `time_origin` | `0..1 PLAN_TIME_ORIGIN` | Origin for delay |

##### CALENDAR_EVENT Class

Subclass of EVENT for calendar moments.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `calendar_entry_name` | `1..1 String` | Referenced calendar moment |

##### TIMELINE_MOMENT Class

Calendar entry specification.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `offset` | `1..1 Duration` | Offset from origin |
| `fixed_time` | `0..1 TIME_SPECIFIER` | Absolute time |

##### TASK_TRANSITION Class

Subclass of EVENT for task state changes.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `task_id` | `1..1 OBJECT_REF` | Task reference |
| `transition_state` | `1..1 TASK_LIFECYCLE` | State to trigger on |

##### MANUAL_NOTIFICATION Class

Subclass of EVENT for manual user notification.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `notification_type` | `1..1 String` | Notification category |
| `notification_message` | `0..1 String` | User message |

##### SYSTEM_NOTIFICATION Class

Subclass of EVENT for system-generated notifications.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `system_id` | `1..1 String` | Source system identifier |
| `notification_content` | `0..1 String` | Notification content |

##### STATE_TRIGGER Class

Subclass of EVENT for watched state changes.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `state_variable` | `1..1 String` | Variable to watch |
| `trigger_condition` | `1..1 BOOLEAN_CONTEXT_EXPRESSION` | Trigger condition |

##### CALLBACK_NOTIFICATION Class

Subclass of EVENT for external task completion notification.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `callback_task_id` | `1..1 OBJECT_REF` | Task completing |
| `callback_status` | `0..1 String` | Completion status |

### Cost Tracking

#### Class Definitions

##### TASK_COSTING Class

Cost information for task.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `cost_type` | `1..1 String` | Cost category |
| `cost_amount` | `1..1 Real` | Amount |
| `cost_currency` | `0..1 String` | Currency code |
| `billing_code` | `0..1 String` | External billing code |
| `billing_description` | `0..1 String` | Billing description |

---

## Global Semantics

### Control Flow

#### Graph Structure

Plan graph structure defined implicitly via Task Group organization.

#### General Scheme

Normal flow proceeds through Task Group members in execution order.

#### Conditional Nodes

Conditional Groups (if/elseif/else, switch, ad hoc) create multiple paths.

### Task Dispatching

#### Hand-offs

Control passes to another Task Plan within Work Plan.

- Current plan waits for completion
- Results may be passed to resumed task
- Enables performer coordination

#### External Requests

Control passes to external organization.

- Communication via external channel
- Current plan continues or waits
- Results integrated on receipt

#### System Requests

Call to IT system or service.

- Synchronous or asynchronous
- Results integrated into plan execution
- May store in context variables

#### Resume Semantics

Post-dispatch resumption continues:

- At specified location
- At next sequential task
- On condition satisfaction
- At specified time

### Aggregate Lifecycle State

Plan state determined by contained tasks.

#### Sequential Groups

Progress through tasks in order:

- `planned`: All tasks planned
- `underway`: Current task underway
- `completed`: All tasks complete

#### Parallel Groups

Concurrent task execution:

- `planned`: All tasks planned
- `underway`: Any task underway
- `completed`: All tasks complete (semantics vary)

#### Work Plan

Overall status reflects all contained Task Plans.

---

## Execution

### Phases of Processing

#### Materialisation

Work Plan definition converted to executable form:

- Decision paths simplified
- Repetitive sections unfolded
- Unreachable code removed
- Execution-tracking structures created

#### Activation

Materialised plan prepared for execution:

- Connections established
- Worker allocations made
- Initial notifications generated
- Execution timeline begun

#### Termination

Plan execution ends:

- All paths completed
- Plan abandoned midway
- Terminal status recorded

#### Allowed Plan Modifications

During execution:

- Task cancellations
- Task reordering (within control flow constraints)
- Worker reallocations
- Condition overrides
- Repetition changes
- Task timing adjustments

### Execution Processing

#### Worker Allocation

Assign workers to Task Plans and Tasks.

**Process**:

1. Identify required roles
2. Find available workers
3. Notify allocation
4. Track assignment

#### Worker De-allocation

Remove worker assignment.

**Triggers**:

- Task completion
- Plan termination
- Worker unavailability
- Shift changes

#### Resource Allocation

Assign non-human resources.

**Resources**:

- Equipment
- Materials
- Facilities
- Time slots

### Persistence

Execution state persisted to enable:

- Interruption and resumption
- Worker shift transitions
- Crash recovery
- Audit trail

---

## Materialised Model

### Overview

The materialised model represents executable form of Work Plan.

Created from definition model prior to execution.

Persists throughout plan execution.

### Class Descriptions

#### M_WORK_PLAN Class

Materialised Work Plan instance.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition reference |
| `subject_id` | `1..1 OBJECT_REF` | Subject reference |
| `instantiation_id` | `1..1 UID` | Unique instantiation identifier |
| `materialised_task_plans` | `1..* List<M_TASK_PLAN>` | Materialised task plans |
| `performer_allocations` | `0..* List<M_PERFORMER_ALLOCATION>` | Current allocations |
| `start_time` | `0..1 DateTime` | Actual start time |
| `end_time` | `0..1 DateTime` | Actual end time |
| `state` | `1..1 String` | Current execution state |

#### M_TASK_PLAN Class

Materialised Task Plan instance.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition reference |
| `principal_performer` | `0..1 String` | Assigned performer |
| `materialised_root_group` | `1..1 M_TASK_GROUP` | Root task group |
| `start_time` | `0..1 DateTime` | Actual start time |
| `end_time` | `0..1 DateTime` | Actual end time |
| `state` | `1..1 String` | Current state |

#### M_PERFORMER_ALLOCATION Class

Current worker allocation.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `performer_id` | `1..1 OBJECT_REF` | Allocated worker |
| `task_plan_id` | `1..1 OBJECT_REF` | Assigned Task Plan |
| `allocation_time` | `1..1 DateTime` | Allocation time |
| `available_from` | `0..1 DateTime` | Worker availability start |
| `available_until` | `0..1 DateTime` | Worker availability end |

#### M_PLAN_ITEM Class

Materialised plan item.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition |
| `uid` | `1..1 UID` | Unique identifier |
| `state` | `1..1 TASK_LIFECYCLE` | Current state |
| `created_time` | `1..1 DateTime` | Creation time |
| `available_time` | `0..1 DateTime` | Available time |
| `start_time` | `0..1 DateTime` | Start time |
| `end_time` | `0..1 DateTime` | End time |

#### M_TASK_GROUP Class

Materialised task group.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition |
| `members` | `0..* List<M_PLAN_ITEM>` | Materialised members |
| `execution_type` | `1..1 EXECUTION_TYPE` | Sequential/parallel |
| `state` | `1..1 String` | Current state |

#### M_TASK Class

Materialised task.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition |
| `materialised_action` | `1..1 M_TASK_ACTION` | Materialised action |
| `assigned_performer` | `0..1 OBJECT_REF` | Assigned performer |
| `state` | `1..1 TASK_LIFECYCLE` | Lifecycle state |
| `planned_time` | `0..1 DateTime` | Planned time |
| `estimated_duration` | `0..1 Duration` | Expected duration |
| `actual_start_time` | `0..1 DateTime` | Actual start |
| `actual_end_time` | `0..1 DateTime` | Actual end |

#### M_TASK_ACTION Class

Materialised task action.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition |
| `action_detail` | `1..1 M_TASK_ACTION` | Action subclass |
| `state` | `1..1 String` | Current state |

#### M_DISPATCHABLE_ACTION Class

Materialised dispatchable action.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition |
| `dispatch_status` | `1..1 String` | Dispatched, completed, failed |
| `dispatch_time` | `1..1 DateTime` | Dispatch time |
| `callback_status` | `0..1 String` | Callback status |
| `callback_time` | `0..1 DateTime` | Callback time |

#### M_PERFORMABLE_ACTION Class

Materialised performable action.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `definition_id` | `1..1 OBJECT_REF` | Source definition |
| `performer_id` | `1..1 OBJECT_REF` | Assigned performer |
| `captured_data` | `0..1 COMPOSITION` | Captured data during performance |

---

## Plan Execution History

### Overview

Audit and execution record of Work Plan execution.

Persisted throughout plan lifetime.

Enables:

- Execution tracking
- Variance analysis
- Compliance audit
- Research

### Class Descriptions

#### TASK_PLAN_EXECUTION_HISTORY Class

Execution history for Task Plan.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `task_plan_id` | `1..1 OBJECT_REF` | Task Plan reference |
| `execution_id` | `1..1 UID` | Unique execution identifier |
| `start_time` | `1..1 DateTime` | Execution start |
| `end_time` | `0..1 DateTime` | Execution end |
| `status` | `1..1 String` | Final status |
| `event_records` | `0..* List<EVENT_RECORD>` | Recorded events |

#### EVENT_RECORD Class (Abstract)

Base event record.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `uid` | `1..1 UID` | Unique identifier |
| `timestamp` | `1..1 DateTime` | Event time |
| `event_type` | `1..1 String` | Event category |

#### TASK_PLAN_EVENT_RECORD Class

Subclass of EVENT_RECORD for plan-level events.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `event_type` | `1..1 String` | Started, completed, abandoned, etc. |
| `event_details` | `0..1 String` | Additional information |

#### TASK_EVENT_RECORD Class

Subclass of EVENT_RECORD for task-level events.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `task_id` | `1..1 OBJECT_REF` | Task reference |
| `task_state` | `1..1 TASK_LIFECYCLE` | State transitioned to |
| `performer_id` | `0..1 OBJECT_REF` | Performing agent |
| `event_details` | `0..1 String` | Additional information |

#### TASK_NOTIFICATION_RECORD Class

Subclass of EVENT_RECORD for notifications.

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| `notification_type` | `1..1 String` | Notification category |
| `recipient_id` | `1..1 OBJECT_REF` | Recipient agent |
| `notification_content` | `0..1 String` | Message content |
| `delivery_status` | `0..1 String` | Delivery outcome |

---

## Transactional Service Model

### Overview

API for task planning system interaction.

Covers plan definition and execution phases.

### Definition Interface

Design and planning phase services.

### Execution-time Interface

Execution phase services.

### Class Descriptions

#### I_WORK_PLAN_DEFINITION Interface

Work Plan definition interface.

Methods:

- `create_work_plan()`: Create new plan
- `modify_work_plan()`: Alter plan
- `delete_work_plan()`: Remove plan
- `publish_work_plan()`: Finalize for execution
- `get_work_plan()`: Retrieve plan

#### I_TASK_PLAN_MATERIALISED Interface

Materialised Task Plan interface.

Methods:

- `activate_task_plan()`: Activate for execution
- `get_task_status()`: Query task state
- `allocate_performer()`: Assign worker
- `update_task_state()`: Change task state
- `get_execution_history()`: Retrieve audit trail

#### I_WORK_PLAN_DEFINITION Interface (Repeated)

Documentation placeholder.

#### I_TASK_PLAN_MATERIALISED Interface (Repeated)

Documentation placeholder.

---

## Relationship with other openEHR EHR Artefacts

### Overview

Task Planning integrates with standard openEHR EHR information model.

- INSTRUCTION: Orders
- ACTION: Performed activities
- OBSERVATION: Measurements
- EVALUATION: Assessments
- ADMIN_ENTRY: Administrative records

### Execution-time EHR Structures

During Task Plan execution:

- Tasks correspond to planned openEHR entries
- Completion generates ACTION entries
- Observations generate OBSERVATION entries
- Results create appropriate entry types

All connected via:

- Archetype references
- Prototype entry specifications
- Data capture specifications

---

## Amendment Record

| Issue | Date | Author | Notes |
|-------|------|--------|-------|
| [Document amendment table would continue here] | | | |

---

## References

[References section would list cited works including YAWL, BPMN, CMMN, DMN, and other standards and research materials]

---

*End of Task Planning (TP) Specification Document*