---
title: Basic Meta-Model (BMM)
type: entity
sources:
  - raw/lang-bmm.md
  - raw/lang-bmm-persistence.md
created: 2026-04-13
updated: 2026-04-13
---

# Basic Meta-Model (BMM)

The Basic Meta-Model (BMM) is a computable representation of object models developed by openEHR as a practical alternative to UML/XMI. It provides a human-readable, machine-processable format for expressing information models, supporting features that UML tools handle poorly in practice: generic types (open and closed), container types, multiple inheritance, enumerated types, and design by contract. BMM is part of the LANG component (Release 1.0.0) and is currently in TRIAL status.

## Motivation and Purpose

Open computing environments require computable model representations for reasoning, validation, code generation, and documentation. In archetype-based frameworks like openEHR, this need is acute: archetypes must be validated against [[reference-model]] definitions, and runtime data must conform to operational templates derived from [[archetype-object-model]] specifications.

While UML theoretically addresses these needs, its XMI serialization has significant practical drawbacks: the UML 2.5.1 specification is approximately 796 pages, type concepts are inadequately formalized, generic types and container properties are problematic, and OCL-based design by contract is constrained by fundamental semantic issues. XML Schema is similarly unsuitable for object modeling due to non-OOP inheritance and absence of generic classes.

BMM addresses these limitations by combining object-oriented and functional programming concepts into a focused meta-model that is both human-authored and computationally processable.

## Key Features

- **OO+FP Foundation**: Directly based on object-oriented class models and functional programming rather than universal meta-models like UML
- **Proper Type Meta-model**: Clear distinction between types and classes, enabling correct representation of typing relationships
- **Full Generic Types**: First-order type entities with support for open, closed, and partially closed generics
- **Container Types**: Dedicated meta-types for `List<T>`, `Set<T>`, `Hash<K,V>`, etc.
- **Enumerated Types**: Range-constrained classes and external value-set references
- **Built-in Expression Language**: Complete meta-model for the [[expression-language]]
- **Design by Contract**: Formal support for invariants and pre/post-conditions
- **Operator/Function Aliasing**: Symbolic operators mapped to function definitions

## Package Organization

```
org.openehr.lang.bmm/
  model_access/         -- Schema load/reload interface
  core/
    model/              -- Models and packages (BMM_MODEL, BMM_PACKAGE)
    entity/             -- Classes and types (BMM_CLASS, BMM_TYPE hierarchies)
    feature/            -- Class features (properties, routines, constants)
    literal_value/      -- Literal values (BMM_LITERAL_VALUE and descendants)
    expression/         -- First-order predicate logic expressions (EL_*)
```

## Model Access Layer

The `model_access` package provides the application interface for loading BMM schemas and converting them to in-memory model form. The central entry point is `BMM_MODEL_ACCESS`, a singleton that manages schema discovery, loading, validation, and retrieval.

### Schema Loading Flow

1. **Schema Loading**: `BMM_SCHEMA_DESCRIPTOR.load()` deserializes a schema file (typically `.bmm` in [[odin]] syntax)
2. **Creation Validation**: `validate_created()` checks structural correctness
3. **Schema Merging**: `BMM_SCHEMA.merge()` recursively merges included schemas
4. **Merge Validation**: `validate_merged()` verifies the merged structure
5. **Model Creation**: `create_model()` generates the final `BMM_MODEL` instance

### Key Classes

- **BMM_MODEL_ACCESS**: Singleton providing access to loaded/validated models. Supports `initialise_all()` to load all schemas from directories, `bmm_model(key)` to retrieve by full or partial key (e.g., `"openEHR_EHR_1.0.4"`, `"openEHR_EHR_1.0"`, or just `"openEHR_EHR"`)
- **BMM_SCHEMA_DESCRIPTOR**: Descriptor holding schema meta-data, processing state, and inclusion lists
- **BMM_SCHEMA**: Abstract parent of persistable schema forms, carrying `bmm_version`, `includes`, lifecycle state, and schema metadata
- **BMM_SCHEMA_STATE**: Enumeration tracking processing state: `State_created` -> `State_validated_created` -> `State_includes_pending` / `State_includes_processed`
- **BMM_INCLUDE_SPEC**: Schema inclusion specification with a single `id` attribute (e.g., `"openehr_primitive_types_1.0.2"`)

## Type System

BMM makes a fundamental distinction between _class_ (definitional entity) and _type_ (formal generator of instances). The type hierarchy uses several key meta-type divisions:

### BMM_TYPE Hierarchy

```
BMM_TYPE (abstract)
  BMM_UNITARY_TYPE (abstract) -- singular instance types
    BMM_PARAMETER_TYPE         -- formal generic parameters (e.g., T in List<T>)
    BMM_EFFECTIVE_TYPE (abstract) -- concrete types
      BMM_MODEL_TYPE (abstract)   -- class-based types
        BMM_SIMPLE_TYPE            -- non-generic (e.g., String, ENTRY)
        BMM_GENERIC_TYPE           -- generic (e.g., Interval<Quantity>)
      BMM_TUPLE_TYPE              -- tuple types
      BMM_SIGNATURE               -- routine signatures
  BMM_CONTAINER_TYPE            -- collection types (List<T>, Set<T>)
    BMM_INDEXED_CONTAINER_TYPE  -- keyed collections (Hash<K,V>)
```

### Type Semantics

- **Simple types** are based on non-generic classes. Conformance follows the class inheritance hierarchy.
- **Generic types** may be _closed_ (all parameters substituted, e.g., `Interval<Quantity>`), _partially closed_ (some substituted), or _open_ (none substituted, e.g., `Document<T, U>`). Generic parameter types are restricted to `BMM_UNITARY_TYPE`, preventing containers as generic arguments.
- **Container types** distinguish collections from singular generics. Ordered+unique = `Set<T>`, ordered+not-unique = `List<T>`. Indexed containers like `Hash<K,V>` add an `index_type`.
- **Signatures** capture formal type structure: `T_result` for properties, `<[T_arg1, T_arg2], T_result>` for functions, `<[T_arg1, T_arg2]>` for procedures.
- **Tuple types** enable typing arrays of heterogeneously-typed objects, primarily used in signature argument lists.

### Type Conformance

Type conformance algorithms determine valid substitution. The general approach: parse both type names, compare base classes, and recursively check generic parameters. For container types, both the container class and member types must conform.

## Class Hierarchy

### BMM_CLASS and Descendants

```
BMM_MODULE (abstract)
  BMM_CLASS (abstract)
    BMM_SIMPLE_CLASS          -- no generic parameters
      BMM_ENUMERATION (abstract)
        BMM_ENUMERATION_STRING   -- String-valued enumerations
        BMM_ENUMERATION_INTEGER  -- Integer-valued enumerations
    BMM_GENERIC_CLASS         -- has formal type parameters
```

`BMM_CLASS` is the central meta-class, carrying:

- **properties**: `Hash<String, BMM_PROPERTY>` (flattened class properties)
- **functions**: `Hash<String, BMM_FUNCTION>` (class functions)
- **procedures**: `Hash<String, BMM_PROCEDURE>` (class procedures)
- **invariants**: `List<EL_BOOLEAN_EXPRESSION>` (class invariants)
- **ancestors**: `List<BMM_EFFECTIVE_TYPE>` (inheritance parents)
- **is_abstract** / **is_primitive**: boolean markers

Key operations include `all_ancestors()`, `all_descendants()`, `flattened_properties()` (including inherited), and `type_definition()`.

### Enumerations

Enumeration types use `BMM_ENUMERATION_STRING` and `BMM_ENUMERATION_INTEGER` to represent types with explicitly defined value sets. External value-set references use `BMM_VALUE_SET_SPEC` with a `value_set_id` and optional `value_set_url`.

### The Any Class

Every BMM model must possess a top class named `Any`. If not explicitly defined, `BMM_MODEL` generates a standard one. All classes without explicit inheritance gain `Any` as parent, ensuring a unified inheritance graph.

## Features

Features are stored or computed elements of classes. BMM supports:

### Properties (BMM_PROPERTY)

Stored data within classes, split into:

- **BMM_UNITARY_PROPERTY**: Singular (non-container) typed property
- **BMM_CONTAINER_PROPERTY**: Multi-valued container property with `BMM_CONTAINER_TYPE`
- **BMM_INDEXED_CONTAINER_PROPERTY**: Keyed container (e.g., `Hash<String, EVENT_ACTION>`)

Properties carry flags: `is_nullable`, `is_computed`, `is_composition`, `is_mandatory`.

### Constants (BMM_CONSTANT)

Fixed values, optionally computed from expressions. Inherit from both `BMM_INSTANTIABLE` and `BMM_TYPED_FEATURE`.

### Routines

- **BMM_FUNCTION**: Value-returning routine with a `BMM_RESULT` return value
- **BMM_PROCEDURE**: Work-performing routine with no return value
- **BMM_OPERATOR**: Symbolic function (e.g., `+`, `*`) with operator position (prefix, infix, postfix)

Routines carry `signature` (`BMM_SIGNATURE`), optional `preconditions`/`postconditions`, optional `body` (`BMM_ROUTINE_BODY`), and boolean markers `is_creator` / `is_converter`.

### Feature Visibility

Features support `Public`, `Protected`, and `Private` visibility via `BMM_VISIBILITY`. Feature groups categorize as `Constant`, `Property`, `Function`, or `Procedure`.

## Expression Meta-Model

The BMM includes a full expression meta-model (the `EL_*` classes) supporting first-order predicate logic. This meta-model provides the structural foundation for the [[expression-language]].

### Terminal Entities (EL_TERMINAL)

- **EL_LITERAL**: Literal value wrapping a `BMM_LITERAL_VALUE`
- **EL_INSTANCE_REF**: Named instance reference
- **EL_SELF_REF**: Reference to current instance (like `this`/`self`)
- **EL_TYPE_REF**: Reference to a type by name
- **EL_SCOPED_REF**: Reference to scoped entity (scope path + item name)
- **EL_INSTANTIABLE_REF**: Reference to instantiable entity

### Predicates (EL_PREDICATE)

- **EL_ATTACHED**: Tests whether a reference is non-null
- **EL_DEFINED**: Tests whether a value is defined

### Operators (EL_OPERATOR)

- **EL_UNARY_OPERATOR**: Prefix operations (e.g., `NOT`)
- **EL_BINARY_OPERATOR**: Infix operations (e.g., `AND`, `+`, `>`)

### Decision Structures

- **EL_DECISION_TABLE**: Multi-branch decision with condition/result branches and optional default
- **EL_CONDITION_CHAIN**: Chained if/then/else
- **EL_CONDITIONAL_EXPRESSION**: Ternary conditional
- **EL_CASE_TABLE**: Switch/case expression

### Agents

- **EL_FUNCTION_AGENT**: Delayed function call (lambda/closure returning a value)
- **EL_PROCEDURE_AGENT**: Delayed procedure call
- **EL_AGENT_CALL**: Agent invocation with arguments

## Statement Meta-Model

The BMM includes basic statement support for routine implementations:

- **BMM_STATEMENT_BLOCK**: Sequence of statements
- **BMM_ASSIGNMENT**: Variable assignment (`target := value`)
- **BMM_PROCEDURE_CALL**: Procedure invocation statement
- **BMM_ASSERTION**: Constraint-checking statement with optional failure message
- **BMM_ACTION_TABLE**: Multi-branch action execution (conditional action dispatch)

## Persistence Model (P_BMM)

The persistence model, defined in the `bmm_persistence` package, provides a simplified serialization form of BMM suitable for human authoring. The `P_BMM_*` classes serve as intermediate representations that use symbolic referencing (class names, type name strings) rather than materialized object graphs.

### Design Approach

A logical BMM model can be expressed as multiple `.bmm` schema files. Each file is an [[odin]] serialization of `P_BMM_*` class instances. Schema readers resolve inclusions to produce final in-memory `BMM_MODEL` instances.

Two forms are distinguished:

- **P_BMM Form**: Model of a BMM schema (symbolic references, human-readable)
- **BMM Form**: Compiled BMM model (fully resolved references, in-memory)

### Key P_BMM Classes

- **P_BMM_SCHEMA**: Top-level schema container with `primitive_types` and `class_definitions` lists, plus schema metadata and inclusion support
- **P_BMM_PACKAGE**: Package tree structure with name, sub-packages, and class name lists
- **P_BMM_CLASS**: Persistent class with `name`, `ancestors`, `properties`, `generic_parameter_defs`, and `ancestor_defs` (for generic inheritance)
- **P_BMM_PROPERTY** subtypes: `P_BMM_SINGLE_PROPERTY`, `P_BMM_SINGLE_PROPERTY_OPEN`, `P_BMM_GENERIC_PROPERTY`, `P_BMM_CONTAINER_PROPERTY`, `P_BMM_INDEXED_CONTAINER_PROPERTY`
- **P_BMM_TYPE** subtypes: `P_BMM_SIMPLE_TYPE`, `P_BMM_OPEN_TYPE`, `P_BMM_GENERIC_TYPE`, `P_BMM_CONTAINER_TYPE`, `P_BMM_INDEXED_CONTAINER_TYPE`
- **P_BMM_ENUMERATION** subtypes: `P_BMM_ENUMERATION_STRING`, `P_BMM_ENUMERATION_INTEGER`

### Schema Lifecycle

`P_BMM_SCHEMA` progresses through states via operations:

1. `validate_created()`: State_created -> State_validated_created
2. `load_finalise()`: -> State_includes_processed or State_includes_pending
3. `merge(other)`: Merge included schemas
4. `validate()`: Final validation
5. `create_bmm_model()`: Generate `BMM_MODEL`

### ODIN Serialization Syntax

BMM schemas are typically authored in [[odin]] syntax. A schema file contains:

- **Header**: `bmm_version`, `rm_publisher`, `schema_name`, `rm_release`, lifecycle state
- **Inclusions**: References to other schema files by id
- **Packages**: Recursive package definitions with class name lists
- **Primitive types**: Class definitions for primitives (`Any`, `Ordered`, `Integer`, etc.)
- **Class definitions**: Full class definitions with properties, generics, and inheritance

Properties use ODIN type markers to indicate their P_BMM class, e.g., `(P_BMM_SINGLE_PROPERTY)`, `(P_BMM_CONTAINER_PROPERTY)`, `(P_BMM_GENERIC_PROPERTY)`.

## Relationship to Archetypes

BMM provides the computable information model layer that archetype tools depend on. The [[archetype-object-model]] uses BMM to validate that archetype constraints are consistent with the [[reference-model]]. In tools like the ADL Workbench, BMM models enable class closure views showing all reachable properties of flattened classes, and archetype nodes are colored by their BMM class.

The [[archetype-definition-language]] uses [[odin]] sections whose structure aligns with BMM class definitions. The expression meta-model (`EL_*` classes) underpins assertions in AOM2 archetypes.

## Tooling

Two primary implementations exist:

- **openEHR Archie Library**: Full Java implementation (open source on GitHub)
- **openEHR ADL Workbench**: Complete reference implementation in Eiffel with BMM libraries available in the EOMF GitHub repository

## Model Semantics

### Inheritance Rules

- **Simple inheritance**: Child classes gain all parent features and conform to parent types
- **Generic inheritance**: Parameters may be constrained; constraints propagate to children
- **Multiple inheritance**: Supported; conflicts resolved through explicit redefinition in descendant classes using inheritance order
- **Contract inheritance**: Preconditions may be weakened in children; postconditions may not be weakened; invariants must be maintained by all descendants
