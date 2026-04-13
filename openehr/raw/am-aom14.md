# Archetype Object Model 1.4 (AOM1.4) Specification

**Issuer:** openEHR Specification Program
**Release:** AM Release-2.3.0
**Status:** STABLE
**Date:** See amendment record
**Keywords:** EHR, ADL, AOM, health records, archetypes, constraint language, ISO 13606, openehr

---

## Table of Contents

1. [Amendment Record](#amendment-record)
2. [Acknowledgements](#acknowledgements)
3. [Preface](#preface)
4. [The Archetype Object Model](#the-archetype-object-model)
5. [The Archetype Package](#the-archetype-package)
6. [Constraint Model Package](#constraint-model-package)
7. [The Assertion Package](#the-assertion-package)
8. [Primitive Package](#primitive-package)
9. [Terminology Package](#terminology-package)
10. [Appendices](#appendices)

---

## Amendment Record

| Issue | Details | Completed |
|-------|---------|-----------|
| AM Release 2.3.0: 1.4.6 | Fix typos in AOM, ADL 1.4. SPECAM-84 | 03 Apr 2023 |
| AM Release 2.3.0: 1.4.5 | Support negative durations. SPECAM-69 | 09 Sep 2020 |
| AM Release 2.3.0: 1.4.4 | Convert citations to bibtex form. SPECPUB-7 | 15 Dec 2019 |
| AM Release 2.1.0: 1.4.3 | Adjust references to BASE packages. SPECAM-42 | 22 Sep 2017 |

---

## Acknowledgements

### Primary Author

Thomas Beale, Ars Semantica, UK

### Supporters

- University College London (CHIME)
- Ocean Informatics

### Trademarks

- 'openEHR' is a trademark of the openEHR Foundation
- 'Java' is a registered trademark of Oracle Corporation
- 'Microsoft' is a trademark of Microsoft Corporation

---

## Preface

### Purpose

This document provides authoritative specification of archetype semantics as an object model for archetype processing. The model serves dual purposes: as a foundation for software development and as an API specification for archetype systems.

Key characteristics include:

- Language-independent object model representation
- Foundation for parser output generation
- Basis for archetype manipulation tools
- Standard reference for implementation

### Related Documents

**Prerequisites:**
- openEHR Architecture Overview
- openEHR Archetypes Technical Overview

**Related specifications:**
- openEHR Definition Language (ADL1.4)
- openEHR Archetype Profile

### Nomenclature

In this specification, "attribute" encompasses all stored properties: primitive attributes and relationships (associations, aggregations, compositions). References to XML attributes are explicitly qualified.

### Status

This specification maintains STABLE status. Current development versions are available at the openEHR specifications website. The document represents a reformatted version of the original AOM 1.4 specification with corrections and modern publishing standards applied.

### Feedback

Feedback channels:
- **Forum:** openEHR ADL discussion forum
- **Issues:** Specifications Problem Report tracker
- **History:** AM component Change Request tracker

### Conformance

Artifact conformance to openEHR specifications is determined through formal testing against Implementation Technology Specifications (ITSs), including IDL interfaces and XML schemas. ITS conformance indicates underlying model conformance.

---

## Background

### What is an Archetype?

Archetypes represent constraint-based models of domain entities, functioning as structured business rules. Each archetype constrains configurations of data instances from reference model classes, establishing valid exemplars of specific domain concepts.

Key characteristics:
- Constraint-based modeling approach
- Composition and specialization support
- Template-compatible structure
- Domain concept expression

### Context

The AOM relates to linguistic archetype forms through object-oriented semantics equivalent to the ADL BNF language definition. The diagram below illustrates this relationship:

```
ADL Text Documents
        |
    [Parser]
        |
AOM Instance Objects <-> Reference Model
        |
Runtime Archetypes
```

### Tools

Available resources:
- **ADL Workbench:** Reference compiler, visualizer, and editor
- **openEHR Tools:** Full development environment
- **GitHub:** Source projects and community implementations

---

## The Archetype Object Model

### Design Background

The openEHR architecture employs dual formal systems:

**1. Reference Model (RM)**
- Defines information structure and semantics
- Represents ISO RM/ODP information viewpoint
- Long-term invariant design
- Minimizes software and schema updates

**2. Archetype Model (AM)**
- Defines archetype and template structure
- Comprises ADL, AOM, and openEHR Archetype Profile
- Provides formal constraint expression
- Enables generic archetyping across reference models

### Package Structure

The AOM defines the `am.archetype` package hierarchy:

```
am.archetype
├── archetype (core structures)
├── constraint_model (constraints)
├── assertion (logical expressions)
├── primitive (basic types)
└── ontology (terminology)
```

### Model Overview

#### Archetypes as Objects

An archetype object structure originates from multiple sources:

1. **Parsing process:** Syntax conversion (ADL, XML, OWL) to objects
2. **Database retrieval:** Reconstruction from persistent storage
3. **GUI editing:** Interactive in-memory creation and modification

The resulting structure consists of alternating layers:
- **Object constraint nodes** (`C_COMPLEX_OBJECT`, `C_PRIMITIVE_OBJECT`)
- **Attribute constraint nodes** (`C_ATTRIBUTE` and subtypes)

Leaf nodes contain primitive type constraints (`C_STRING`, `C_INTEGER`, etc.).

Special node types:
- `ARCHETYPE_INTERNAL_REF`: Reference to other nodes in same archetype
- `CONSTRAINT_REF`: Reference to external constraints in ontology
- `ARCHETYPE_SLOT`: Composition point for other archetypes

#### The Archetype Ontology

The ontology section provides language-independent specification of linguistic entities. Four major components:

1. **Term definitions:** Identified by 'atNNNN' codes
2. **Constraint definitions:** Identified by 'acNNNN' codes
3. **Term bindings:** External terminology mappings
4. **Constraint bindings:** External resource references

This structure enables translation and multi-language support while maintaining neutral definition structure.

#### Archetype Specialisation

Archetypes support specialisation relationships where:
- Specialised archetypes mention parent archetype
- Changes restrict constraints (narrowing only)
- Created data conforms to both specialised and parent archetypes
- Specialisation depth measures hierarchy level

#### Archetype Composition

Composition enables:
- Modular definition structure
- Archetype reuse across multiple parent archetypes
- Semantic equivalence to larger single archetypes

**Mechanism:** Archetype slots define composition points through constraint expressions.

---

## The Archetype Package

### Overview

The archetype model mirrors ADL archetype document structure. An archetype consists of:

- **Identifying metadata:** Via `AUTHORED_RESOURCE` inheritance
- **Definition:** Root `C_COMPLEX_OBJECT` constraint
- **Ontology:** `ARCHETYPE_ONTOLOGY` instance

### ARCHETYPE Class

```
Class: ARCHETYPE
Inherits: AUTHORED_RESOURCE

Attributes:
- definition : C_COMPLEX_OBJECT [1..1]
    Root constraint node of archetype definition

- ontology : ARCHETYPE_ONTOLOGY [1..1]
    Ontology section

- adl_version : String [0..1]
    ADL version if parsed from sharable archetype

- archetype_id : ARCHETYPE_ID [1..1]
    Multi-axial identifier in archetype space

- concept : String [1..1]
    Normative meaning as local archetype code (typically "at0000")

- parent_archetype_id : ARCHETYPE_ID [0..1]
    Specialisation parent identifier

- invariants : List<ASSERTION> [0..1]
    Archetype-level constraint statements

- uid : HIER_OBJECT_ID [0..1]
    OID identifier
```

**Key Functions:**

| Function | Returns | Purpose |
|----------|---------|---------|
| `concept_name(lang)` | String | Concept name in specified language |
| `physical_paths()` | List<String> | Language-independent paths |
| `logical_paths(lang)` | List<String> | Language-dependent paths |
| `specialisation_depth()` | Integer | Depth in specialisation hierarchy |
| `is_specialised()` | Boolean | Whether has parent archetype |
| `is_valid()` | Boolean | Overall validity test |
| `node_ids_valid()` | Boolean | All node_ids in ontology |
| `internal_references_valid()` | Boolean | All internal references valid |
| `constraint_references_valid()` | Boolean | All constraint references valid |
| `short_concept_name()` | String | Short concept from archetype_id |

**Invariants:**

```
- concept_valid: ontology.has_term_code(concept_code)
- specialisation_validity: is_specialised implies specialisation_depth > 0
- invariants_valid: invariants != Void implies not invariants.is_empty
- uid_validity: uid != Void implies not uid.is_empty
- version_validity: version = archetype_id.version_id
- description_valid: description != Void
- original_language_valid: original_language != Void and language != Void
```

---

## Constraint Model Package

### Overview

The constraint model provides generic expressions of constraints on object-oriented class instances. Major abstractions include:

- **Object constraints:** Variations representing different constraint types
- **Attribute constraints:** Constraints on class properties
- **Semantic correspondence:** Direct mapping to OO formalisms

### Semantics

#### All Node Types

Common properties across all constraint nodes:

| Property | Purpose |
|----------|---------|
| `path()` | Path to node from archetype root |
| `has_path(a_path)` | Tests whether path exists |
| `is_valid()` | Node and sub-nodes validity |
| `is_subset_of(other)` | Tests constraint narrowness for specialisation |

#### Attribute Node Types

Attributes are constrained by `C_ATTRIBUTE` subtypes:

**C_SINGLE_ATTRIBUTE**
- Constrains single-valued attributes
- Children represent alternative object constraints
- Example: `Person.date_of_birth : Date`

**C_MULTIPLE_ATTRIBUTE**
- Constrains container-valued attributes
- Children represent co-existing container members
- Includes cardinality constraints
- Example: `Person.contacts : List<Contact>`

The distinction between `existence` and `cardinality`:

| Constraint | Applies To | Meaning |
|-----------|-----------|---------|
| Existence | All attributes | Whether container/value exists |
| Cardinality | Container attributes only | Valid membership count/properties |

#### Object Node Types

##### Node_id and Paths

The `node_id` attribute serves dual functions:

1. **Individual identification:** Guarantees sibling uniqueness
2. **Ontology linking:** Connects to term codes in ontology section

Paths are constructed from alternating node_ids and rm_attribute_names following Xpath-like syntax.

##### Defined Object Nodes (C_DEFINED_OBJECT)

Objects defined by inline archetype constraints. Properties:

**any_allowed**
- Indicates complete absence of constraints
- True when no further structure specified
- Simplifies "open" constraint expression

**assumed_value**
- Defines implicit value for optional items
- Example: Patient position "sitting" in general practice context
- Appears in leaf nodes only
- Distinct from default values (local only)

**valid_value**
- Tests reference model object conformance
- Designed for recursive implementation
- Basis for runtime validation

**default_value**
- Generates reasonable prototype values
- Supports initial object creation
- Typically uses reflection mechanisms

##### Complex Objects (C_COMPLEX_OBJECT)

Key structuring type alongside `C_ATTRIBUTE`. Structure:

```
C_COMPLEX_OBJECT
├── rm_type_name : String
│   Reference model type being constrained
│
└── attributes : List<C_ATTRIBUTE>
    Constraints on reference model properties
    ├── rm_attr_name : String
    ├── existence : Interval<Integer>
    └── children : List<C_OBJECT>
```

##### Primitive Types

Constraints on primitive types (`C_STRING`, `C_INTEGER`, etc.):

- Do not inherit from `ARCHETYPE_CONSTRAINT`
- Related by association to `C_PRIMITIVE_OBJECT`
- Enables independent definition
- Simplified interface

##### Domain-specific Extensions (C_DOMAIN_TYPE)

Allows specialized constraint semantics for specific reference model types. Example: `C_QUANTITY` providing custom constraints for measurement quantities.

Benefits:
- Standard generic approach for general types
- Specialized semantics for domain concepts
- Integrated into standard constraint model
- Extensible via inheritance

##### Reference Objects (C_REFERENCE_OBJECT)

**ARCHETYPE_SLOT**
- Composition point for additional archetypes
- Constraints define allowable slot fillers
- Include/exclude constraint specifications

**ARCHETYPE_INTERNAL_REF**
- Proxy reference to archetype node
- Eliminates constraint duplication
- Uses path-based references

**CONSTRAINT_REF**
- References external constraint definitions
- Points to ontology binding
- Delegates to external services (terminology)

#### Assertions

Complementary constraint mechanism for:
- Multi-attribute constraints
- Archetype slot filtering
- Expressed in first-order predicate logic
- Supports structured invariants

Example: "systolic_pressure >= diastolic_pressure" in blood pressure archetype.

### Class Definitions

#### ARCHETYPE_CONSTRAINT Class (Abstract)

```
Class: ARCHETYPE_CONSTRAINT (abstract)

Functions:
- is_subset_of(other) : Boolean
    Comparison for specialisation validation

- is_valid() : Boolean
    Node validity assessment

- path() : String
    Relative path from archetype root

- has_path(a_path) : Boolean
    Path existence test
```

#### C_ATTRIBUTE Class (Abstract)

```
Class: C_ATTRIBUTE (abstract)
Inherits: ARCHETYPE_CONSTRAINT

Attributes:
- rm_attribute_name : String [1..1]
    Reference model attribute name

- existence : Interval<Integer> [1..1]
    Optionality constraint (0..1 or 1..1)

- children : List<C_OBJECT> [0..1]
    Child object constraint nodes

Functions:
- any_allowed() : Boolean
    True if no value restrictions

Invariants:
- rm_attribute_name_valid: not rm_attribute_name.is_empty
- existence_set: existence.lower >= 0 and existence.upper <= 1
- children_validity: any_allowed xor children != Void
```

#### C_SINGLE_ATTRIBUTE Class

```
Class: C_SINGLE_ATTRIBUTE
Inherits: C_ATTRIBUTE

Functions:
- alternatives() : List<C_OBJECT>
    Alternative constraints for single attribute value

Invariants:
- members_valid: alternatives != Void and
    all(co: C_OBJECT | co.occurrences.upper <= 1)
```

#### C_MULTIPLE_ATTRIBUTE Class

```
Class: C_MULTIPLE_ATTRIBUTE
Inherits: C_ATTRIBUTE

Attributes:
- cardinality : CARDINALITY [1..1]
    Container cardinality constraint

Functions:
- members() : List<C_OBJECT>
    Container member constraints
```

#### CARDINALITY Class

```
Class: CARDINALITY

Attributes:
- interval : Interval<Integer> [1..1]
    Membership count constraint

- is_ordered : Boolean [1..1]
    True if order is significant

- is_unique : Boolean [1..1]
    True if members must be unique

Functions:
- is_bag() : Boolean
    Unordered, non-unique semantics

- is_list() : Boolean
    Ordered, non-unique semantics

- is_set() : Boolean
    Unordered, unique semantics
```

#### C_OBJECT Class (Abstract)

```
Class: C_OBJECT (abstract)
Inherits: ARCHETYPE_CONSTRAINT

Attributes:
- rm_type_name : String [1..1]
    Reference model type name

- occurrences : Interval<Integer> [1..1]
    Data occurrence constraint

- node_id : String [1..1]
    Semantic identifier (at-code or Primitive_node_id)
```

#### C_DEFINED_OBJECT Class (Abstract)

```
Class: C_DEFINED_OBJECT (abstract)
Inherits: C_OBJECT

Attributes:
- assumed_value : Any [0..1]
    Default value if absent from data

Functions:
- valid_value(a_value) : Boolean
    Value conformance test

- prototype_value() : Any
    Generate prototype instance

- has_assumed_value() : Boolean
    Assumed value existence check

- default_value() : Any
    Generate default value

- any_allowed() : Boolean
    Complete constraint absence

Invariants:
- assumed_value_valid:
    has_assumed_value implies valid_value(assumed_value)
```

#### C_COMPLEX_OBJECT Class

```
Class: C_COMPLEX_OBJECT
Inherits: C_DEFINED_OBJECT

Attributes:
- attributes : List<C_ATTRIBUTE> [0..1]
    Constraints on reference model attributes

Functions:
- any_allowed() : Boolean [effected]
    True if attributes.is_empty

Invariants:
- attributes_valid:
    any_allowed xor (attributes != Void and not attributes.is_empty)
```

#### C_PRIMITIVE_OBJECT Class

```
Class: C_PRIMITIVE_OBJECT
Inherits: C_DEFINED_OBJECT

Attributes:
- item : C_PRIMITIVE [1..1]
    Constraint definition object

Functions:
- any_allowed() : Boolean [effected]
    True if item = Void

Invariants:
- item_valid: any_allowed xor item != Void
```

#### C_DOMAIN_TYPE Class (Abstract)

```
Class: C_DOMAIN_TYPE (abstract)
Inherits: C_DEFINED_OBJECT

Functions:
- standard_equivalent() : C_COMPLEX_OBJECT
    Standard constraint form
```

#### C_REFERENCE_OBJECT Class (Abstract)

```
Class: C_REFERENCE_OBJECT (abstract)
Inherits: C_OBJECT
```

#### ARCHETYPE_SLOT Class

```
Class: ARCHETYPE_SLOT
Inherits: C_REFERENCE_OBJECT

Attributes:
- includes : List<ASSERTION> [0..1]
    Archetype inclusion constraints

- excludes : List<ASSERTION> [0..1]
    Archetype exclusion constraints

Invariants:
- includes_valid: includes != Void implies not includes.is_empty
- excludes_valid: excludes != Void implies not excludes.is_empty
- validity: any_allowed xor (includes != Void or excludes != Void)
```

#### ARCHETYPE_INTERNAL_REF Class

```
Class: ARCHETYPE_INTERNAL_REF
Inherits: C_REFERENCE_OBJECT

Attributes:
- target_path : String [1..1]
    Archetype path reference

Note: Local occurrences always take precedence. If unspecified
on deserialization, target occurrences should be inherited.

Invariants:
- consistency: not any_allowed
- target_path_valid: target_path != Void and not target_path.is_empty
```

#### CONSTRAINT_REF Class

```
Class: CONSTRAINT_REF
Inherits: C_REFERENCE_OBJECT

Attributes:
- reference : String [1..1]
    Ontology constraint reference (ac-code)

Invariants:
- consistency: not any_allowed
```

---

## The Assertion Package

### Overview

Assertions express constraints in first-order predicate logic for use in:
- Archetype slot filtering
- Complex object constraints (invariants)

Expressed in typed FOL as expression trees.

### Semantics

Assertions support:

**Variables:** Inbuilt, path-based, external query results

**Constants:** Primitive types including date/time values

**Operators:**
- Arithmetic: `+`, `-`, `*`, `/`, `^`, `%`
- Relational: `>`, `<`, `>=`, `<=`, `=`, `!=`, `matches`
- Boolean: `not`, `and`, `or`, `xor`
- Quantifiers: `for_all`, `exists`

### Class Definitions

#### ASSERTION Class

```
Class: ASSERTION

Attributes:
- tag : String [0..1]
    Expression tag for differentiation

- string_expression : String [0..1]
    String form of expression

- expression : EXPR_ITEM [1..1]
    Expression tree root

- variables : List<ASSERTION_VARIABLE> [0..1]
    Variable definitions

Invariants:
- tag_valid: tag != Void implies not tag.is_empty
- expression_valid: expression != Void and expression.type = "BOOLEAN"
```

#### EXPR_ITEM Class (Abstract)

```
Class: EXPR_ITEM (abstract)

Attributes:
- type : String [1..1]
    Primitive type name or reference model type
    Relational/boolean operators return "Boolean"
    Arithmetic operators return "Real" or "Integer"
```

#### EXPR_LEAF Class

```
Class: EXPR_LEAF
Inherits: EXPR_ITEM

Attributes:
- reference_type : String [1..1]
    Reference category:
    "constant" | "attribute" | "function" | "constraint"

- item : Any [1..1]
    Manifest constant, attribute path, or constraint
```

#### EXPR_OPERATOR Class (Abstract)

```
Class: EXPR_OPERATOR (abstract)
Inherits: EXPR_ITEM

Attributes:
- precedence_overridden : Boolean [0..1]
    True if natural precedence overridden
    (indicates parentheses needed)

- operator : OPERATOR_KIND [1..1]
    Operator code
```

#### EXPR_UNARY_OPERATOR Class

```
Class: EXPR_UNARY_OPERATOR
Inherits: EXPR_OPERATOR

Attributes:
- operand : EXPR_ITEM [1..1]
    Single operand
```

#### EXPR_BINARY_OPERATOR Class

```
Class: EXPR_BINARY_OPERATOR
Inherits: EXPR_OPERATOR

Attributes:
- left_operand : EXPR_ITEM [1..1]
    Left operand

- right_operand : EXPR_ITEM [1..1]
    Right operand
```

#### ASSERTION_VARIABLE Class

```
Class: ASSERTION_VARIABLE

Attributes:
- name : String [1..1]
    Variable name

- definition : String [1..1]
    Formal variable definition
```

#### OPERATOR_KIND Enumeration

```
Enumeration: OPERATOR_KIND

Values:
op_eq           Equals (= or ==)
op_ne           Not equals (!= or /=)
op_le           Less-than or equals (<=)
op_lt           Less-than (<)
op_ge           Greater-than or equals (>=)
op_gt           Greater-than (>)
op_matches      Matches/is_in
op_not          Logical NOT
op_and          Logical AND
op_or           Logical OR
op_xor          Logical XOR
op_implies      Logical implication
op_for_all      Universal quantifier
op_exists       Existential quantifier
op_plus         Addition (+)
op_minus        Subtraction (-)
op_multiply     Multiplication (*)
op_divide       Division (/)
op_exponent     Exponentiation (^)
op_modulo       Modulo (%)
```

---

## Primitive Package

### Overview

Leaf-level constraints on primitive types. Most types support multiple constraint representations (pattern and interval).

### Class Definitions

#### C_PRIMITIVE Class (Abstract)

```
Class: C_PRIMITIVE (abstract)

Attributes:
- assumed_value : Any [0..1]
    Value assumed if absent from data

Functions:
- default_value() : Any
    Generate default value

- has_assumed_value() : Boolean
    Assumed value existence check

- valid_value(a_value) : Boolean
    Value conformance test

Invariants:
- assumed_value_valid:
    has_assumed_value implies valid_value(assumed_value)
```

#### C_BOOLEAN Class

```
Class: C_BOOLEAN
Inherits: C_PRIMITIVE

Attributes:
- true_valid : Boolean [1..1]
    True if True value allowed

- false_valid : Boolean [1..1]
    True if False value allowed

- assumed_value : Boolean [0..1]
    Default assumption

Note: Both cannot be False simultaneously.
```

#### C_STRING Class

```
Class: C_STRING
Inherits: C_PRIMITIVE

Attributes:
- pattern : String [0..1]
    Regular expression pattern

- list : List<String> [0..1]
    Explicit string list

- list_open : Boolean [1..1]
    True if list non-exhaustive

- assumed_value : String [0..1]
    Default assumption

Functions:
- valid_value(a_value) : Boolean
    Pattern/list conformance test
```

#### C_INTEGER Class

```
Class: C_INTEGER
Inherits: C_PRIMITIVE

Attributes:
- list : List<Integer> [0..1]
    Explicit integer list

- range : Interval<Integer> [0..1]
    Integer range constraint

- assumed_value : Integer [0..1]
    Default assumption
```

#### C_REAL Class

```
Class: C_REAL
Inherits: C_PRIMITIVE

Attributes:
- list : List<Real> [0..1]
    Explicit real number list

- range : Interval<Real> [0..1]
    Real range constraint

- assumed_value : Real [0..1]
    Default assumption
```

#### C_DATE Class

```
Class: C_DATE
Inherits: C_PRIMITIVE

Attributes:
- day_validity : VALIDITY_KIND [0..1]
    Day constraint (mandatory/optional/disallowed)

- month_validity : VALIDITY_KIND [0..1]
    Month constraint

- timezone_validity : VALIDITY_KIND [0..1]
    Timezone constraint

- range : Interval<Iso8601_date> [0..1]
    Date range constraint

- assumed_value : Iso8601_date [0..1]
    Default assumption

Example patterns: "YYYY-??-??" (year required, month/day optional)

Invariants:
- month_optional implies day in {optional, disallowed}
- month_disallowed implies day_disallowed
```

#### C_TIME Class

```
Class: C_TIME
Inherits: C_PRIMITIVE

Attributes:
- minute_validity : VALIDITY_KIND [0..1]
    Minute constraint

- second_validity : VALIDITY_KIND [0..1]
    Second constraint

- millisecond_validity : VALIDITY_KIND [0..1]
    Millisecond constraint

- timezone_validity : VALIDITY_KIND [0..1]
    Timezone constraint

- range : Interval<Iso8601_time> [0..1]
    Time range constraint

- assumed_value : Iso8601_time [0..1]
    Default assumption

Functions:
- validity_is_range() : Boolean
    Range form constraint indicator

Invariants:
- minute_optional implies second in {optional, disallowed}
- minute_disallowed implies second_disallowed
- second_optional implies millisecond in {optional, disallowed}
- second_disallowed implies millisecond_disallowed
```

#### C_DATE_TIME Class

```
Class: C_DATE_TIME
Inherits: C_PRIMITIVE

Attributes:
- month_validity : VALIDITY_KIND [0..1]
- day_validity : VALIDITY_KIND [0..1]
- hour_validity : VALIDITY_KIND [0..1]
- minute_validity : VALIDITY_KIND [0..1]
- second_validity : VALIDITY_KIND [0..1]
- millisecond_validity : VALIDITY_KIND [0..1]
- timezone_validity : VALIDITY_KIND [0..1]

- range : Interval<Iso8601_date_time> [0..1]
    DateTime range constraint

- assumed_value : Iso8601_date_time [0..1]
    Default assumption

Functions:
- validity_is_range() : Boolean
    Range form constraint indicator

Invariants:
- month_optional implies day in {optional, disallowed}
- month_disallowed implies day_disallowed
- day_optional implies hour in {optional, disallowed}
- day_disallowed implies hour_disallowed
- hour_optional implies minute in {optional, disallowed}
- hour_disallowed implies minute_disallowed
- minute_optional implies second in {optional, disallowed}
- minute_disallowed implies second_disallowed
- second_optional implies millisecond in {optional, disallowed}
- second_disallowed implies millisecond_disallowed
```

#### C_DURATION Class

```
Class: C_DURATION
Inherits: C_PRIMITIVE

Attributes:
- years_allowed : Boolean [0..1]
- months_allowed : Boolean [0..1]
    True if months allowed

- weeks_allowed : Boolean [0..1]
- days_allowed : Boolean [0..1]
    True if days allowed

- hours_allowed : Boolean [0..1]
    True if hours allowed

- minutes_allowed : Boolean [0..1]
    True if minutes allowed

- seconds_allowed : Boolean [0..1]
- fractional_seconds_allowed : Boolean [0..1]
    True if fractional seconds allowed

- range : Interval<Iso8601_duration> [0..1]
    Duration range constraint

- assumed_value : Iso8601_duration [0..1]
    Default assumption

ISO 8601 Extensions (openEHR):
- Week designator ('W') can mix with other units
- Negative durations supported via leading minus sign
- Allowed patterns: P[Y|y][M|m][D|d][T[H|h][M|m][S|s]] and P[W|w]

Example: "PWD/|P0W..P50W|" combines pattern and range constraint
```

---

## Terminology Package

### Overview

All linguistic entities reside in the ontology section. The ontology package specifies terminology representation.

### Semantics

#### Specialisation Depth

Archetypes occur at specialisation lineage positions. Depth indicators:

- **Depth 0:** No specialisation parent
- **Depth N:** N steps from root parent

Term code naming convention uses period markers:
- `at0.0.1` -- New term at depth 2
- `at0001.0.1` -- Specialises `at0001` from parent (depth 2)
- `at0001.1.1` -- Specialises `at0001.1` from immediate parent

Constraint codes use flat naming without depth markers.

#### Term and Constraint Definitions

Represented as `ARCHETYPE_TERM` instances (code + name/value pairs).

Required pairs:
- `"text"` -- Term display
- `"description"` -- Detailed meaning

Optional pairs:
- `"provenance"` -- External source indicator
- Domain-specific attributes

The `term_attribute_names` list catalogs all attribute names used throughout the archetype.

### Class Definitions

#### ARCHETYPE_ONTOLOGY Class

```
Class: ARCHETYPE_ONTOLOGY

Attributes:
- term_codes : List<String> [1..1]
    All "at" codes from definition (node_ids)

- constraint_codes : List<String> [1..1]
    All "ac" codes from definition

- parent_archetype : ARCHETYPE [1..1]
    Owner archetype reference

- terminologies_available : List<String> [0..1]
    External terminology identifiers with bindings

- specialisation_depth : Integer [1..1]
    Depth in specialisation hierarchy (0 for root)

- term_attribute_names : List<String> [1..1]
    All attribute names used in term/constraint definitions

Functions:
- has_language(a_lang) : Boolean
    Language presence test

- has_terminology(a_terminology_id) : Boolean
    External terminology presence test

- has_term_code(a_code) : Boolean
    Term code existence test

- has_constraint_code(a_code) : Boolean
    Constraint code existence test

- term_definition(a_lang, a_code) : ARCHETYPE_TERM
    Retrieve term definition
    Pre: has_language(a_lang)
    Pre: has_term_code(a_code)

- constraint_definition(a_code, a_lang) : ARCHETYPE_TERM
    Retrieve constraint definition
    Pre: has_language(a_lang)
    Pre: has_constraint_code(a_code)

- term_binding(a_terminology, a_code) : CODE_PHRASE
    External terminology binding
    Pre: has_term_binding(a_terminology_id, a_code)

- constraint_binding(a_terminology_id, a_code) : String
    External constraint binding (usually query expression)

Invariants:
- original_language_validity: language_codes.has_concept_id(original_language)
- concept_code_validity: id_codes.has(concept_code)
- term_bindings_validity: bindings != Void implies not bindings.is_empty
- parent_archetype_valid: parent_archetype.ontology = self
```

#### ARCHETYPE_TERM Class

```
Class: ARCHETYPE_TERM

Attributes:
- code : String [1..1]
    Term/constraint code identifier

- items : Hash<String, String> [0..1]
    Name/value pairs ("text", "description", etc.)

Functions:
- keys() : List<String>
    All attribute names in this term

Invariants:
- code_valid: not code.is_empty
```

---

## Appendices

### Appendix A: Domain-specific Extension Example

#### Overview

Domain-specific constraint classes inherit from `C_DOMAIN_TYPE`. This appendix exemplifies adding specialized constraints for scientific/clinical computing.

#### Scientific/Clinical Computing Types

Common concepts requiring special constraint semantics:

1. **Ordinal:** Discrete ranked values (pathology scales)
2. **Coded Term:** Terminology-constrained text
3. **Quantity:** Scientific measurements

#### Class Definitions

##### C_ORDINAL Class

```
Class: C_ORDINAL
Inherits: C_DOMAIN_TYPE

Attributes:
- list : List<ORDINAL> [0..1]
    Allowed ordinal values
```

##### ORDINAL Class

```
Class: ORDINAL

Attributes:
- symbol : CODE_PHRASE [1..1]
    Terminology code for symbol

- value : Integer [1..1]
    Ordinal numeric value
```

##### C_QUANTITY Class

```
Class: C_QUANTITY
Inherits: C_DOMAIN_TYPE

Attributes:
- property : String [1..1]
    Physical property name

- list : List<C_QUANTITY_ITEM> [0..1]
    Allowed quantity item constraints
```

##### C_QUANTITY_ITEM Class

```
Class: C_QUANTITY_ITEM

Attributes:
- magnitude : Interval<Real> [1..1]
    Numeric value range

- units : String [0..1]
    Optional unit constraint
```

##### C_CODED_TEXT Class

```
Class: C_CODED_TEXT
Inherits: C_DOMAIN_TYPE

Attributes:
- terminology : String [1..1]
    Terminology identifier

- code_list : List<String> [0..1]
    Allowed codes (Void = any from terminology)
```

### Appendix B: Using Archetypes with Diverse Reference Models

#### Overview

The AOM provides generic constraint expression applicable across reference models expressed in UML or similar object-oriented formalisms. This appendix addresses multi-model application.

#### Clinical Computing Use

The archetype model successfully applies across:
- Different RM versions
- Domain-specific RMs
- Custom extensions

Flexibility is achieved through:
- Generic constraint mechanisms
- Domain-specific extension points
- Model-agnostic semantics

---

## References

### Standards
- ISO 8601-1: Date and time representations
- ISO 13606: Electronic health record architecture
- OMG: Unified Modeling Language (UML)

### openEHR Specifications
- openEHR Architecture Overview
- openEHR Archetype Definition Language 1.4
- openEHR Archetypes Technical Overview
- openEHR Archetype Profile
- openEHR Release 1.0.3 Support Information Model
- openEHR Release 1.0.3 Data Types Information Model
- openEHR Release 1.0.3 Common Information Model

### Related Work
- Beale, T. (2000). "Archetypes: Constraint-based Domain Models"
- Beale, T. (2002). "Archetype Semantics"
- Rector, A. (2000). "Terminology and Ontology"

---

## Copyright and Licensing

(c) 2004 - 2024 The openEHR Foundation

The openEHR Foundation is an independent, non-profit organization facilitating health record sharing through open specifications, clinical models, and platform implementations.

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
https://creativecommons.org/licenses/by-nd/3.0/

**Support Resources:**
- Problem Reports: https://specifications.openehr.org/components/AM/open_issues
- Web: https://specifications.openehr.org
- Forum: https://discourse.openehr.org/c/specifications/adl
