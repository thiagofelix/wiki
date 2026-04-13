# Basic Meta-Model (BMM) Specification

**Document Status:** TRIAL  
**Release:** LANG Release-1.0.0  
**Issuer:** openEHR Specification Program  
**Latest Revision:** [\[latest\_issue\]](#)  
**Date:** [\[latest\_issue\_date\]](#)  
**Keywords:** reflection, meta-model, UML

---

## Table of Contents

1. [Preface](#preface)
2. [Overview](#overview)
3. [Model Access Package](#model-access-package)
4. [Model Structure](#model-structure)
5. [Types](#types)
6. [Classes](#classes)
7. [Class Features](#class-features)
8. [Literal Values](#literal-values)
9. [Expressions](#expressions)
10. [Functional Elements](#functional-elements)
11. [Statements](#statements)
12. [Model Semantics](#model-semantics)
13. [BMM Extensions](#bmm-extensions)

---

## Preface

### Purpose

This document presents the Basic Meta-Model (BMM), which serves as a computable representation of object models. The BMM functions as an alternative to UML XMI, offering human-readability alongside support for generic types (both open and closed), container types, and multiple inheritance.

### Status

This specification is in TRIAL state. The development version is available at the openEHR specifications repository.

**Note on Usage:** While BMM provides a formal framework, it is not mandatory for implementing openEHR. Alternative approaches, including UML and direct software implementations, remain viable options.

### Feedback and Conformance

Feedback is welcome via the [openEHR languages specifications forum](https://discourse.openehr.org/c/specifications/bmm-el). Issues may be reported through the [specifications Problem Report tracker](https://specifications.openehr.org/components/LANG/open_issues).

Conformance to openEHR specifications is determined through formal testing against relevant Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas.

### Previous Versions

**Version 3.0.0** introduced major restructuring of the `BMM_TYPE` hierarchy and semantics, enabling proper representation of generic inheritance patterns.

**Version 3.1.0** added meta-classes for computational elements:
- Routines, variables, and constants
- Expression language constructs
- Statement representations

### Language Note

This specification employs precise terminology to avoid confusion:

- **class**: Refers to a class defined within a BMM-expressed model
- **meta-class**: Refers to classes within the BMM itself (e.g., `BMM_CLASS`)
- **feature**: Any stored or computed element of a class
- **property**: A stored class feature; also called "attribute"
- **routine**: A computed feature that may return values (function) or perform work (procedure)
- **generic**: A class or type with parameters of other types
- **type**: A type defined within a BMM-expressed model
- **meta-type**: A type within the BMM itself

### Tooling

Two primary implementations support this specification:

- **[openEHR Archie Library](https://github.com/openEHR/archie)**: Full Java implementation suitable for building UI tools
- **[openEHR ADL Workbench](https://www.openehr.org/downloads/ADLworkbench)**: Complete reference implementation in Eiffel with open-source availability on GitHub

---

## Overview

### Introduction

Open computing environments require computable representations of their models to enable reasoning, validation, consistency checking, code generation, and documentation. This necessity is particularly acute in archetype-based frameworks like openEHR, where validation of archetypes against reference models and runtime data against operational templates becomes essential.

The openEHR project maintains two primary computable model representations: UML and BMM. While UML serves primarily in specification publishing, BMM addresses the limitations of UML/XMI by providing a format that is both human-readable and computationally processable.

### Key Features

The BMM combines object-oriented and functional programming concepts:

- **OO+FP Foundation**: Directly based on object-oriented class models, functional programming, and expression languages rather than universal meta-models like UML
- **Proper Type Meta-model**: Clear distinction between types and classes, enabling proper representation of typing
- **Full Generic Types**: First-order type entities enabling correct representation of generic typing and inheritance
- **Container Types**: Dedicated meta-types for collections like `List<T>` and `Hash<K,V>`
- **Enumerated Types**: Supported via range-constrained classes and external value set references
- **Built-in Expression Language**: Complete meta-model for literals, properties, variables, function calls, and agents
- **Design by Contract**: Formal support for invariants and pre/post-conditions
- **Operator/Function Aliasing**: Support for mapping symbolic operators to function definitions

### State of the Art Comparison

#### UML Limitations

While UML 2.x and XMI 2.x theoretically provide comprehensive machine-processable representations, significant practical limitations persist:

**Specification Complexity:**  
UML 2.5.1 specification comprises approximately 796 pages across multiple documents, while the corresponding XMI specification matches this complexity level.

**Semantic Weaknesses:**
- Type concept is not adequately formalized
- Generic types and container properties are problematic
- Design by Contract support through OCL is constrained by fundamental semantic issues
- No direct support for functional entities (lambdas/routine-as-objects)

**Tool Implementation Issues:**
- Poor OCL and design-by-contract support in most tools
- Inconsistent generic class handling
- Qualified attribute problems
- Highly variable XSD generation
- Tool-specific programming language profiles limiting abstract modeling

#### XML Schema Limitations

While W3C XML Schema offers serialization capabilities, it proves semantically unsuitable for object modeling due to problematic non-OOP inheritance, absence of generic classes, lack of non-data member representation, and marginal design-by-contract support.

### Computational Model

The BMM functions as a structural model representing an abstract syntax tree (AST), whether constructed in-memory (by authoring tools) or parsed from serialized representations. While the specification does not prescribe a concrete syntax, multiple syntaxes could parse to valid BMM instances.

*Note: Throughout this specification, an abstract syntax borrowing from mainstream modeling and programming languages provides illustration without prescriptive intent.*

### Uses of BMM

#### Class Model Representation

From version 3.0.0 onward, BMM represents full interface-level class models including classes, types, and feature types (properties, constants, functions, operators, procedures) without implementation code.

#### Expression Language Basis

The BMM provides meta-types forming the foundation for typed expression languages, including references to static entities, literal values, agent construction, and function calls.

#### Information Model Representation

Tools using BMM can present particularly useful information-modeling views, such as class closure views showing computed reachability graphs of flattened classes and all properties.

#### Archetype Modeling

In tools like the openEHR ADL Workbench, BMM provides computable information models for use with domain-level models such as archetypes, with nodes colored by their class and displaying non-archetyped attributes.

### Specification Structure

This specification defines the BMM object model—the in-memory object structure. The related [BMM Persistence Specification](https://specifications.openehr.org/releases/LANG/Release-1.0.0/bmm_persistence.html) defines serialization formats.

**Package Organization:**

```
org.openehr.lang.bmm/
├── model_access/
│   └── Schema load/reload interface
└── core/
    ├── model/
    │   └── Models and packages
    ├── entity/
    │   └── Classes and types
    ├── feature/
    │   └── Class features
    ├── literal_value/
    │   └── Literal values
    └── expression/
        └── First-order predicate logic expressions
```

---

## BMM Definitions Class

| Aspect | Details |
|--------|---------|
| **Class Name** | `BMM_DEFINITIONS` |
| **Description** | Definitions used across all BMM packages |
| **Inheritance** | `BASIC_DEFINITIONS` |

### Constants

| Name | Type | Value | Meaning |
|------|------|-------|---------|
| `Bmm_internal_version` | String | — | Current BMM meta-model version for schema compatibility assessment |
| `Schema_name_delimiter` | String | `"::"` | Separates schema id from package path |
| `Package_name_delimiter` | String | `"."` | Separates package names in paths |
| `Bmm_schema_file_extension` | String | `".bmm"` | Standard file extension for BMM files |
| `Type_delimiter` | Character | `':'` | Separates names from types in declarations |
| `Generic_left_delimiter` | Character | `'<'` | Generic type opening delimiter |
| `Generic_right_delimiter` | Character | `'>'` | Generic type closing delimiter |
| `Generic_separator` | Character | `','` | Separator within generic type parameters |
| `Generic_constraint_delimiter` | Character | `':'` | Delimiter between parameter and constraint |
| `Tuple_left_delim` | Character | `'['` | Tuple type/instance opening delimiter |
| `Tuple_right_delim` | Character | `']'` | Tuple type/instance closing delimiter |
| `Tuple_separator` | Character | `','` | Separator within tuple definitions |
| `Constraint_left_delim` | Character | `'«'` | Instance constrained enumeration opening |
| `Constraint_right_delim` | Character | `'»'` | Instance constrained enumeration closing |

### Metadata Keys

Schema metadata is accessed via the following string constants:

- `Metadata_bmm_version`: `"bmm_version"`
- `Metadata_schema_name`: `"schema_name"`
- `Metadata_rm_publisher`: `"rm_publisher"`
- `Metadata_rm_release`: `"rm_release"`
- `Metadata_schema_revision`: `"schema_revision"`
- `Metadata_schema_lifecycle_state`: `"schema_lifecycle_state"`
- `Metadata_schema_description`: `"schema_description"`
- `Metadata_schema_path`: `"schema_path"`

### Functions

| Signature | Returns | Purpose |
|-----------|---------|---------|
| `Any_class()` | `BMM_SIMPLE_CLASS` | Obtain built-in `Any` class definition |
| `Any_type()` | `BMM_SIMPLE_TYPE` | Obtain built-in `Any` type definition |
| `create_schema_id(a_model_publisher, a_schema_name, a_model_release)` | `String` | Create schema identifier formatted as `publisher-name-release` |

---

## Model Access Package

### Overview

The `org.openehr.lang.bmm.model_access` package provides application interfaces for loading BMM schemas and converting them to BMM model form. A _schema_ represents the serialized form of a model or model component; one or more schema files are parsed, validated, and merged to create a single `BMM_MODEL` instance.

The package supports multiple serialization formats, each with format-specific subclasses of `BMM_SCHEMA_DESCRIPTOR` and `BMM_SCHEMA`. The `.bmm` file format uses `P_BMM` 2.x persistence classes.

#### Load and Validation Flow

1. **Schema Loading**: `BMM_SCHEMA_DESCRIPTOR._load()` deserializes a schema file
2. **Creation Validation**: `_validate_created()` checks structural correctness
3. **Schema Merging**: `BMM_SCHEMA._merge()` recursively merges included schemas
4. **Merge Validation**: `_validate_merged()` verifies merged structure
5. **Model Creation**: `_create_model()` generates the `BMM_MODEL` instance

#### Model Access

Successfully loaded models are instantiated as `BMM_MODEL` instances and retrieved via `BMM_MODEL_ACCESS._bmm_model()` using a model key. Keys may include full, partial, or no version information—partial keys match the most recent version.

**Example**: Keys `"openEHR_EHR_1.0.4"`, `"openEHR_EHR_1.0"`, `"openEHR_EHR_1"`, and `"openEHR_EHR"` all match version `1.0.4` if it is the most recent available.

### Class Definitions

#### BMM_MODEL_ACCESS

| Aspect | Details |
|--------|---------|
| **Description** | Provides access to loaded and validated BMM models |
| **Visibility** | Singleton pattern |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `schema_directories` | `List<String>` | 0..1 | Directories containing loaded schemas |
| `all_schemas` | `Hash<String, BMM_SCHEMA_DESCRIPTOR>` | 0..1 | All loaded schemas, keyed by schema id |
| `bmm_models` | `Hash<String, BMM_MODEL>` | 0..1 | Top-level (root) models, keyed by model id |
| `matching_bmm_models` | `Hash<String, BMM_MODEL>` | 0..1 | Validated models with partial and full version keys |

**Functions:**

| Signature | Returns | Purpose |
|-----------|---------|---------|
| `initialise_with_load_list(a_schema_dirs, a_schema_load_list)` | void | Initialize with specific subset of available schemas |
| `initialise_all(a_schema_dirs)` | void | Load all schemas from specified directories |
| `reload_schemas()` | void | Reload all BMM schemas |
| `bmm_model(a_model_key)` | `BMM_MODEL` | Retrieve model by full or partial key |
| `has_bmm_model(a_model_key)` | `Boolean` | Check model availability |

#### BMM_SCHEMA_DESCRIPTOR

| Aspect | Details |
|--------|---------|
| **Description** | Descriptor for a BMM schema with meta-data and processing state |
| **Accessibility** | Abstract class |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `bmm_schema` | `BMM_SCHEMA` | 0..1 | Persistent form of model |
| `bmm_model` | `BMM_MODEL` | 0..1 | Computable form of model |
| `schema_id` | `String` | 1..1 | Unique identifier formed from publisher, name, and release |
| `meta_data` | `Hash<String, String>` | 1..1 | Schema meta-data table with keys from `BMM_DEFINITIONS` |
| `includes` | `List<String>` | 0..1 | Identifiers of schemas included by this schema |

**Functions:**

| Signature | Returns | Purpose |
|-----------|---------|---------|
| `is_top_level()` | `Boolean` | True if schema is not included by another |
| `is_bmm_compatible()` | `Boolean` | True if BMM version is compatible with implementation |
| `load()` | void | Load schema into in-memory form |
| `validate_merged()` | void | Validate merged schema structure |
| `validate_includes(all_schemas_list)` | void | Verify included schemas exist |
| `create_model()` | void | Create `BMM_MODEL` from schema |

#### BMM_MODEL_METADATA

| Aspect | Details |
|--------|---------|
| **Description** | Core properties appearing in both persistent and computable forms |

**Attributes:**

| Name | Type | Cardinality |
|------|------|-------------|
| `rm_publisher` | `String` | 1..1 |
| `rm_release` | `String` | 1..1 |

#### BMM_SCHEMA

| Aspect | Details |
|--------|---------|
| **Description** | Abstract parent of persistable BMM model forms |
| **Inheritance** | `BMM_MODEL_METADATA` |
| **Accessibility** | Abstract class |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `bmm_version` | `String` | 1..1 | BMM model version for schema evolution reasoning |
| `includes` | `Hash<String, BMM_INCLUDE_SPEC>` | 0..1 | Inclusion specifications with namespace mapping |
| `bmm_model` | `BMM_MODEL` | 0..1 | Generated computable form |
| `state` | `BMM_SCHEMA_STATE` | 1..1 | Current processing state |
| `model_name` | `String` | 0..1 | Model name for root-point schemas |
| `schema_name` | `String` | 1..1 | Name of model expressed in schema |
| `schema_revision` | `String` | 1..1 | Schema revision identifier |
| `schema_lifecycle_state` | `String` | 1..1 | Development lifecycle state |
| `schema_author` | `String` | 1..1 | Primary schema author |
| `schema_description` | `String` | 1..1 | Schema description |
| `schema_contributors` | `List<String>` | 0..1 | Contributing authors |

**Functions:**

| Signature | Pre-condition | Post-condition | Purpose |
|-----------|---------------|----------------|---------|
| `validate_created()` | state = State_created | passed implies state = State_validated_created | Perform initial validation checks |
| `load_finalise()` | state = State_validated_created | state = State_includes_processed \| State_includes_pending | Convert packages to canonical form |
| `merge(other)` | state = State_includes_pending | — | Merge included schema definitions |
| `validate()` | — | — | Main validation prior to model generation |
| `create_bmm_model()` | state = State_includes_processed | — | Populate BMM_MODEL from schema |
| `read_to_validate()` | — | state = State_includes_processed | True when validation may commence |
| `schema_id()` | — | — | Return unique schema identifier |

#### BMM_SCHEMA_STATE (Enumeration)

| State | Meaning |
|-------|---------|
| `State_created` | Initial state after schema instantiation |
| `State_validated_created` | State after initial validation pass |
| `State_includes_pending` | State with remaining included schemas to process |
| `State_includes_processed` | State after all includes processed |

#### BMM_INCLUDE_SPEC

| Aspect | Details |
|--------|---------|
| **Description** | Schema inclusion specification |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `id` | `String` | 1..1 | Full identifier of included schema (e.g., `"openehr_primitive_types_1.0.2"`) |

---

## Model Structure

### Overview

The `core.model` sub-package defines the top-level structure of a BMM model. Models contain packages and modules (with classes being the most common module type) arranged in hierarchical namespaces.

### Naming Convention

Names in BMM models follow case-sensitive conventions used by model authors (camelCase, snake_case, etc.). During computational processing, case-insensitive matching applies. Thus `"Hashable"` and `"HASHABLE"` reference the same class, while `"HashMap"` and `"HASH_MAP"` remain distinct.

*Future versions may support automated style transformation across imported schemas.*

### Model Semantics

#### Packages

Packages serve as non-semantic organizational containers mirroring UML structure. Every class must reside in exactly one package. Unlike UML, **packages are not namespaces**—all classes within a BMM model must have unique names. Package paths optimize serialization efficiency but are not used for namespace qualification.

#### Use of Other Models

A model may depend on ("use" or "import") other models, declared once in the using model rather than per-class. This relationship populates the `BMM_CLASS._scope_` attribute with a reference to the used model. Serialized syntax typically appears as `other_model_name::Class`.

#### Documentation

The `_documentation_` attribute inherited into classes, properties, packages, and models accepts a keyed table of values. Recommended keys and types include:

- `"purpose": String`
- `"keywords": List<String>`
- `"use": String`
- `"misuse": String`
- `"references": String`

Additional keys and value types may be freely added.

#### Other Meta-data

The `_extensions_` attribute of type `Hash<String, Any>` enables representation of arbitrary meta-data on any model node, providing extensibility mechanisms.

### The Any Class and Type

While BMM models define classes explicitly, they must possess a top class named `Any` from which all others inherit. If not explicitly defined, `BMM_MODEL` generates a standard `Any` class including:

- Default package structure
- Standard `Any` type definition
- Inherits as parent for all unparented classes

Every class without explicit inheritance gains `Any` as its parent, ensuring a unified inheritance graph with `Any` as root.

### Class Definitions

#### BMM_DECLARATION (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type of BMM declared model elements—author-specified elements within model definitions |
| **Accessibility** | Abstract |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `name` | `String` | 1..1 | Element name |
| `documentation` | `Hash<String, Any>` | 0..1 | Optional keyed documentation |
| `scope` | `BMM_DECLARATION` | 1..1 | Declaration context/container |
| `extensions` | `Hash<String, Any>` | 0..1 | Optional extensibility meta-data |

**Functions:**

| Signature | Post-condition | Purpose |
|-----------|----------------|---------|
| `is_root_scope()` | Result = (scope = self) | True if declaration is hierarchy root |

#### BMM_PACKAGE_CONTAINER (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | BMM component containing packages and classes |
| **Inheritance** | `BMM_DECLARATION` |
| **Accessibility** | Abstract |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `packages` | `Hash<String, BMM_PACKAGE>` | 0..1 | Child packages (keys upper-cased) |
| `scope` | `BMM_PACKAGE_CONTAINER` | 1..1 | Referenceable element context (redefined) |

**Functions:**

| Signature | Purpose |
|-----------|---------|
| `package_at_path(a_path)` | Retrieve package by path |
| `do_recursive_packages(action)` | Execute procedure on all packages recursively |
| `has_package_path(a_path)` | Check package existence at path |

#### BMM_PACKAGE

| Aspect | Details |
|--------|---------|
| **Description** | Tree structure node containing packages and/or classes |
| **Inheritance** | `BMM_PACKAGE_CONTAINER` |
| **Name Qualification** | Permitted for top-level packages only |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `classes` | `List<BMM_CLASS>` | 0..1 | Classes declared in this package |

**Functions:**

| Signature | Purpose |
|-----------|---------|
| `root_classes()` | Obtain top-level classes (first level found through recursion) |
| `path()` | Full path back to root package |

#### BMM_MODEL

| Aspect | Details |
|--------|---------|
| **Description** | Root of BMM model structure |
| **Inheritance** | `BMM_PACKAGE_CONTAINER`, `BMM_MODEL_METADATA` |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `class_definitions` | `Hash<String, BMM_CLASS>` | 0..1 | All classes keyed by type name |
| `used_models` | `List<BMM_MODEL>` | 0..1 | Imported models available for reference |

**Functions:**

| Signature | Returns | Purpose |
|-----------|---------|---------|
| `model_id()` | `String` | Lower-case identifier: `<publisher>_<name>_<release>` |
| `class_definition(a_name)` | `BMM_CLASS` | Retrieve class definition by name |
| `type_definition(a_type_name)` | `BMM_CLASS` | Retrieve type including generic components |
| `has_class_definition(a_class_name)` | `Boolean` | Check class existence |
| `has_type_definition(a_type_name)` | `Boolean` | Check type availability |
| `enumeration_definition(a_name)` | `BMM_ENUMERATION` | Retrieve enumeration by name |
| `primitive_types()` | `List<String>` | List primitive type class names |
| `enumeration_types()` | `List<String>` | List enumeration type class names |
| `property_definition(a_type_name, a_prop_name)` | `BMM_PROPERTY` | Retrieve property in flattened class |
| `ms_conformant_property_type(a_bmm_type_name, a_bmm_property_name, a_ms_property_name)` | `Boolean` | Check model-semantic conformance |
| `property_definition_at_path(a_type_name, a_property_path)` | `BMM_PROPERTY` | Retrieve property along path |
| `class_definition_at_path(a_type_name, a_prop_path)` | `BMM_CLASS` | Retrieve owning class of terminal attribute |
| `all_ancestor_classes(a_class)` | `List<String>` | Return all ancestors up to root |
| `is_descendant_of(a_class_name, a_parent_class_name)` | `Boolean` | Check inheritance relationship |
| `type_conforms_to(a_desc_type, an_anc_type)` | `Boolean` | Check type conformance including generics |
| `subtypes(a_type)` | `List<String>` | Generate type substitutions |
| `any_class_definition()` | `BMM_SIMPLE_CLASS` | Obtain `Any` class (defined or default) |
| `any_type_definition()` | `BMM_SIMPLE_TYPE` | Obtain `Any` type definition |
| `boolean_type_definition()` | `BMM_SIMPLE_TYPE` | Obtain `Boolean` type definition |

**Invariants:**

- `Inv_top_level_scope`: scope = self

#### BMM_MODULE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Generalized module concept—ancestor for modules like classes |
| **Inheritance** | `BMM_DECLARATION` |
| **Accessibility** | Abstract |

**Attributes:**

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `scope` | `BMM_MODEL` | 1..1 | Model containing module (redefined) |

---

## Types

### Overview

The BMM distinguishes between _class_ (definitional entities) and _type_ (formal generators of instances and basis for typing). This taxonomy of types, illustrated in the metatype taxonomy diagram, uses several key distinctions:

**Primary Distinction**: `BMM_UNITARY_TYPE` (singular instances) vs. `BMM_CONTAINER_TYPE` (collections)

**Unitary Type Division**: `BMM_PARAMETER_TYPE` (formal generic parameters) vs. `BMM_EFFECTIVE_TYPE` (concrete types)

**Effective Type Division**: `BMM_MODEL_TYPE` (class-based) vs. `BMM_TUPLE_TYPE` (tuple) vs. `BMM_SIGNATURE` (routine signatures)

**Model Type Division**: `BMM_SIMPLE_TYPE` (non-generic classes) vs. `BMM_GENERIC_TYPE` (generic classes)

### Simple Type

A simple type bases on a simple class with no formal generic parameters. Instances are fully described by the class, with polymorphic attachment following standard OOP principles.

#### Conformance Rules

- **Meta-rule**: Simple types only conform to Model types
- **Concrete rule**: Simple type A conforms to Simple type B iff the base class of A has B in its ancestors

### Generic Type

A generic type bases on a generic class with one or more formal type parameters substituted by actual types.

**Parameter Characteristics**:
- Substitution of formal parameters with concrete types (including other generics)
- Unsubstituted formal parameters in feature contexts with open generic types

**Generic Type Categories**:
- **Closed**: All parameters substituted (e.g., `Interval<Quantity>`)
- **Partially Closed**: At least one parameter substituted (e.g., `Document<ClinicalContent, U>`)
- **Open**: No parameters substituted (e.g., `Document<T, U>`)

The meta-type of `BMM_GENERIC_TYPE._generic_parameters_` is `BMM_UNITARY_TYPE`, preventing container types as generic parameters. This enforces expressing containment _where parameters are used_, not where declared.

#### Conformance Rules

- **Meta-rule**: Generic types only conform to other generic types
- **Concrete rules**: `Ga<Tai, …>` conforms to `Gb<Tbi, …>` iff:
  - Base class of Ga has Gb in ancestors
  - Generic parameter counts equal
  - Each Tai either conforms to unconstrained Tbi or satisfies Tbi's constraint

### Tuple Meta-type

`BMM_TUPLE_TYPE` enables typing of tuples—arrays of objects with potentially different types. Primarily used in `BMM_SIGNATURE` for argument lists, standalone tuple types provide anonymous-class-like functionality.

The `Tuple` type is treated as BMM built-in, not model-defined.

#### Conformance Rules

- **Meta-rule**: Tuple types only conform to other tuple types
- **Concrete rule**: `Tuple[Tai, …]` conforms to `Tuple[Tbi, …]` iff each Tai conforms to corresponding Tbi

### Signature Meta-type

Every typed entity carries a signature—the formal construct capturing its type structure. Property and constant signatures express return types; routine signatures capture argument and return type structure.

**Signature Notation**:

```
T_result                                    -- Property/constant
<[T_arg1, T_arg2, ...], T_result>          -- Function
<[T_arg1, T_arg2, ...]>                    -- Procedure
```

**Examples**:

```
<[], Date>                    -- 0-order function
<[Real, Real], Real>          -- 2nd-order function
<[String, Integer]>           -- 1st-order procedure
Function                      -- Any function
Procedure                     -- Any procedure
```

The `BMM_SIGNATURE` meta-type treats signatures as first-order entities. Instances contain `_argument_types_` (`BMM_TUPLE_TYPE`) and optional `_result_type_`.

#### Conformance Rules

- **Meta-rule**: Signature types only conform to other signature types
- **Concrete rules**:
  - All specific Function signatures conform to `Function`
  - All specific Procedure signatures conform to `Procedure`
  - Specific signature conformance requires matching argument counts and component conformance

### Container Meta-types

Container types distinguish collections (like `List<T>`, `Set<T>`) from singular generics. This allows BMM to represent containers directly without enumerating concrete implementations.

**Container Semantics**:

| Combination | Type |
|-------------|------|
| ordered and unique | `Set<T>` |
| ordered and not unique | `List<T>` |
| not ordered and not unique | `Bag<T>` |

**Indexed Containers** like `Hash<K,V>` use `BMM_INDEXED_CONTAINER_TYPE`, adding `_index_type_` for key typing.

#### Conformance Rules

- **Meta-rule**: Container types only conform to other container types
- **Concrete rules**:
  - `Ca<Va>` conforms to `Cb<Vb>` iff base class Ca has Cb as ancestor and Va conforms to Vb
  - Indexed `Ca<Ka, Va>` conforms to `Cb<Kb, Vb>` iff bases conform and both parameter types conform

### Type Conformance

Type conformance algorithms determine whether one type validly substitutes for another. The algorithm checks:

1. Parse both type names
2. Compare base class names
3. For base class equality or inheritance conformance:
   - Non-generic types conform via class hierarchy
   - Generic types require parameter count match and recursive parameter conformance
   - Open parameters conform to constraints

---

## Class Definitions Detail

### BMM_TYPE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Common meta-type for all type definitions |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `is_abstract` | `Boolean` | 1..1 | Type based on abstract class |
| `is_primitive` | `Boolean` | 1..1 | Derived from primitive class |
| `type_name` | `String` | 1..1 | Effective type name |
| `type_signature` | `String` | 1..1 | Fully-defined type signature |

### BMM_UNITARY_TYPE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for singular instance types |
| **Inheritance** | `BMM_TYPE` |
| **Accessibility** | Abstract |

### BMM_EFFECTIVE_TYPE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for concrete unitary types |
| **Inheritance** | `BMM_UNITARY_TYPE` |
| **Accessibility** | Abstract |

### BMM_PARAMETER_TYPE

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for formal generic parameters (e.g., `T` in `List<T>`) |
| **Inheritance** | `BMM_UNITARY_TYPE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `name` | `String` | 1..1 | Parameter name (typically single uppercase letter) |
| `type_constraint` | `BMM_EFFECTIVE_TYPE` | 0..1 | Constraint type if constrained |

### BMM_MODEL_TYPE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for class-based types |
| **Inheritance** | `BMM_EFFECTIVE_TYPE` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `base_class` | `BMM_CLASS` | 1..1 | Defining class |

### BMM_SIMPLE_TYPE

| Aspect | Details |
|--------|---------|
| **Description** | Type based on simple (non-generic) class |
| **Inheritance** | `BMM_MODEL_TYPE` |

### BMM_GENERIC_TYPE

| Aspect | Details |
|--------|---------|
| **Description** | Type based on generic class with parameter substitutions |
| **Inheritance** | `BMM_MODEL_TYPE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `generic_parameters` | `List<BMM_UNITARY_TYPE>` | 1..1 | Parameter type substitutions |

**Functions**:

| Signature | Returns | Purpose |
|-----------|---------|---------|
| `is_closed()` | `Boolean` | True if all parameters substituted |
| `is_partially_closed()` | `Boolean` | True if some parameters substituted |

### BMM_TUPLE_TYPE

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for tuple (multi-typed collection) types |
| **Inheritance** | `BMM_EFFECTIVE_TYPE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `member_types` | `List<BMM_UNITARY_TYPE>` | 0..1 | Tuple component types |

### BMM_SIGNATURE

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for routine signatures |
| **Inheritance** | `BMM_EFFECTIVE_TYPE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `argument_types` | `BMM_TUPLE_TYPE` | 0..1 | Function/procedure argument types |
| `result_type` | `BMM_UNITARY_TYPE` | 0..1 | Function return type (procedures: absent) |

### BMM_CONTAINER_TYPE

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for collection types with containment semantics |
| **Inheritance** | `BMM_TYPE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `base_class` | `BMM_GENERIC_CLASS` | 1..1 | Defining generic class |
| `container_type` | `BMM_UNITARY_TYPE` | 1..1 | Member type |
| `is_ordered` | `Boolean` | 1..1 | Elements are sequentially ordered |
| `is_unique` | `Boolean` | 1..1 | Elements are unique (set-like) |

### BMM_INDEXED_CONTAINER_TYPE

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for keyed collection types (e.g., `Hash<K,V>`) |
| **Inheritance** | `BMM_CONTAINER_TYPE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `index_type` | `BMM_UNITARY_TYPE` | 1..1 | Key type for indexing |

---

## Classes

### Overview

Classes define the structure of types. The BMM represents classes through several meta-classes enabling expression of simple classes, generic classes, enumeration types, and value-set-constrained types.

### Simple Classes

Simple classes are those without formal generic parameters. They form the basis for simple types and may inherit from other simple classes or generic types (with parameters fully specified).

### Generic Classes

Generic classes have one or more formal type parameters (typically named with single letters like `T`, `U`, `K`, `V`). These parameters may be constrained via type constraints (e.g., `T: Ordered`).

### Range-Constrained Classes

Range-constrained classes represent types whose instances are limited to specific value ranges, including enumeration types and external value-set references.

#### Enumerated Types

Enumeration types use the meta-classes `BMM_ENUMERATION`, `BMM_ENUMERATION_STRING`, and `BMM_ENUMERATION_INTEGER` to represent types with explicitly defined value sets.

#### Value-Set Types

Value-set types reference external terminologies or value sets via `BMM_VALUE_SET_SPEC`, enabling constraint to terminology-managed values.

### Class Qualifiers

#### Abstract Classes

Classes marked as abstract cannot be directly instantiated and serve as bases for inheritance hierarchies.

#### Primitive Type Classes

Classes marked primitive receive special visualization treatment. Primitive status has no semantic impact on BMM operations.

### Class Invariants

Classes may include invariants—predicates that must hold for all valid instances. Invariants appear in design-by-contract patterns.

### Inheritance

Classes inherit from parent classes, creating inheritance hierarchies. Multiple inheritance is permitted, with conflicts resolved through explicit ordering.

### Class Definitions

#### BMM_CLASS (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for all class definitions |
| **Inheritance** | `BMM_MODULE` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `properties` | `Hash<String, BMM_PROPERTY>` | 0..1 | Class properties (flattened) |
| `functions` | `Hash<String, BMM_FUNCTION>` | 0..1 | Class functions (flattened) |
| `procedures` | `Hash<String, BMM_PROCEDURE>` | 0..1 | Class procedures (flattened) |
| `invariants` | `List<EL_BOOLEAN_EXPRESSION>` | 0..1 | Class invariants |
| `ancestors` | `List<BMM_EFFECTIVE_TYPE>` | 0..1 | Inheritance parent types |
| `immediate_descendants` | `List<BMM_CLASS>` | 0..1 | Direct child classes |
| `is_abstract` | `Boolean` | 1..1 | Cannot be directly instantiated |
| `is_primitive` | `Boolean` | 1..1 | Primitive type marker |

**Functions**:

| Signature | Returns | Purpose |
|-----------|---------|---------|
| `all_ancestors()` | `List<BMM_EFFECTIVE_TYPE>` | All inheritance parents recursively |
| `all_descendants()` | `List<BMM_CLASS>` | All inheritance children recursively |
| `flattened_properties()` | `Hash<String, BMM_PROPERTY>` | Properties including inherited |
| `type_definition()` | `BMM_SIMPLE_TYPE` | Corresponding type instance |

#### BMM_SIMPLE_CLASS

| Aspect | Details |
|--------|---------|
| **Description** | Class without formal generic parameters |
| **Inheritance** | `BMM_CLASS` |

#### BMM_GENERIC_CLASS

| Aspect | Details |
|--------|---------|
| **Description** | Class with formal generic type parameters |
| **Inheritance** | `BMM_CLASS` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `generic_parameters` | `List<BMM_PARAMETER_TYPE>` | 1..1 | Formal type parameters |

#### BMM_ENUMERATION (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for enumeration type classes |
| **Inheritance** | `BMM_SIMPLE_CLASS` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `item_names` | `List<String>` | 1..1 | Enumeration value names |

#### BMM_ENUMERATION_STRING

| Aspect | Details |
|--------|---------|
| **Description** | Enumeration with String values |
| **Inheritance** | `BMM_ENUMERATION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `item_values` | `List<String>` | 1..1 | String enumeration values |

#### BMM_ENUMERATION_INTEGER

| Aspect | Details |
|--------|---------|
| **Description** | Enumeration with Integer values |
| **Inheritance** | `BMM_ENUMERATION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `item_values` | `List<Integer>` | 1..1 | Integer enumeration values |

#### BMM_VALUE_SET_SPEC

| Aspect | Details |
|--------|---------|
| **Description** | Reference to external value set for constraint |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value_set_id` | `String` | 1..1 | External value set identifier |
| `value_set_url` | `String` | 0..1 | Optional URL reference |

---

## Class Features

### Overview

Features are the stored or computed elements of classes. The BMM supports several feature types:

- **Constants**: Static values
- **Properties**: Stored attributes
- **Functions**: Value-returning routines
- **Procedures**: Work-performing routines
- **Operators**: Overloaded symbolic operations

#### Feature Groups

Features organize by type and visibility, supporting clear interface definition.

#### Feature Visibility

Visibility qualifiers (public, private, protected) control feature access from outside the class.

#### Feature Declarations

Features appear in two forms:

- **Differential Form**: Only features defined/redefined in class
- **Flat Form**: All features including inherited, fully resolved

#### Typed Entities

Features that carry types define their value/parameter structure.

#### Multiple Inheritance Note

While BMM supports multiple inheritance, conflicts must be explicitly resolved through feature redefinition in descendant classes. Features inherited from multiple paths use inheritance order for resolution.

#### Synthesis from Generic Parameters

When a generic class is instantiated with specific parameters, features are synthesized reflecting parameter substitution.

#### Signatures

Features define signatures capturing their formal type structure.

### Constants

Constants are fixed values, optionally computed from expressions.

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `BMM_LITERAL_VALUE` \| `EL_EXPRESSION` | 0..1 | Constant value or computing expression |

### Properties

Properties represent stored data within classes.

#### Unitary versus Container Properties

Properties may be singular (unitary) or multi-valued (containers).

**Semantic Levels**: Properties may have semantic annotations (composition, association, etc.).

### Functions and Procedures

Routines are computed features defined by signature, optional pre/post-conditions, and implementations.

#### Pre- and Post-conditions

Design-by-contract preconditions and postconditions define routine semantics and constraints.

#### Creators and Converters

Special routine types support object construction (creators) and type conversion (converters).

#### Routine Body

Routines may include implementation code or reference external implementations.

---

## Class Feature Definitions

### BMM_TYPED (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for typed entities |
| **Inheritance** | `BMM_DECLARATION` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `type` | `BMM_UNITARY_TYPE` | 1..1 | Entity type |

### BMM_FEATURE_GROUP (Enumeration)

| Value | Meaning |
|-------|---------|
| `Constant` | Static constant |
| `Property` | Stored attribute |
| `Function` | Value-returning routine |
| `Procedure` | Work-performing routine |

### BMM_VISIBILITY (Enumeration)

| Value | Meaning |
|-------|---------|
| `Public` | Accessible outside class |
| `Protected` | Accessible in class and descendants |
| `Private` | Accessible only in class |

### BMM_CLASS_ENTITY (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for class members |
| **Inheritance** | `BMM_TYPED` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `visibility` | `BMM_VISIBILITY` | 1..1 | Feature access level |
| `feature_group` | `BMM_FEATURE_GROUP` | 1..1 | Feature category |

### BMM_CLASS_FEATURE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for class-level referenceable entities |
| **Inheritance** | `BMM_CLASS_ENTITY` |
| **Accessibility** | Abstract |

### BMM_TYPED_FEATURE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for typed features |
| **Inheritance** | `BMM_CLASS_FEATURE` |
| **Accessibility** | Abstract |

### BMM_INSTANTIABLE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for instantiable features |
| **Inheritance** | `BMM_CLASS_FEATURE` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `is_mandatory` | `Boolean` | 1..1 | Required at instantiation |

### BMM_CONSTANT

| Aspect | Details |
|--------|---------|
| **Description** | Constant feature with optional computed value |
| **Inheritance** | `BMM_INSTANTIABLE`, `BMM_TYPED_FEATURE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `BMM_LITERAL_VALUE` \| `EL_EXPRESSION` | 0..1 | Static or computed value |

### BMM_PROPERTY (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for stored properties |
| **Inheritance** | `BMM_INSTANTIABLE`, `BMM_TYPED_FEATURE` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `is_nullable` | `Boolean` | 1..1 | May be unset/null |
| `is_computed` | `Boolean` | 1..1 | Computed versus stored (deprecated) |
| `is_composition` | `Boolean` | 1..1 | Whole/part relationship |

### BMM_UNITARY_PROPERTY

| Aspect | Details |
|--------|---------|
| **Description** | Property with singular (non-container) type |
| **Inheritance** | `BMM_PROPERTY` |

### BMM_CONTAINER_PROPERTY

| Aspect | Details |
|--------|---------|
| **Description** | Property with container type |
| **Inheritance** | `BMM_PROPERTY` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `type` | `BMM_CONTAINER_TYPE` | 1..1 | Container type (redefined) |

### BMM_INDEXED_CONTAINER_PROPERTY

| Aspect | Details |
|--------|---------|
| **Description** | Property with indexed container type |
| **Inheritance** | `BMM_CONTAINER_PROPERTY` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `type` | `BMM_INDEXED_CONTAINER_TYPE` | 1..1 | Indexed container type (redefined) |

### BMM_ROUTINE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for routine features |
| **Inheritance** | `BMM_CLASS_FEATURE` |
| **Accessibility** | Abstract |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `signature` | `BMM_SIGNATURE` | 1..1 | Routine signature |
| `preconditions` | `List<EL_BOOLEAN_EXPRESSION>` | 0..1 | Pre-conditions |
| `postconditions` | `List<EL_BOOLEAN_EXPRESSION>` | 0..1 | Post-conditions |
| `body` | `BMM_ROUTINE_BODY` | 0..1 | Implementation |
| `is_creator` | `Boolean` | 1..1 | Object creation routine |
| `is_converter` | `Boolean` | 1..1 | Type conversion routine |

### BMM_FUNCTION

| Aspect | Details |
|--------|---------|
| **Description** | Value-returning routine |
| **Inheritance** | `BMM_ROUTINE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `result` | `BMM_RESULT` | 1..1 | Return value definition |

### BMM_OPERATOR

| Aspect | Details |
|--------|---------|
| **Description** | Operator (symbolic function) |
| **Inheritance** | `BMM_FUNCTION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `operator_symbol` | `String` | 1..1 | Symbolic operator (e.g., `+`, `*`) |
| `operator_position` | `BMM_OPERATOR_POSITION` | 1..1 | Prefix, infix, or postfix |

### BMM_OPERATOR_POSITION (Enumeration)

| Value | Meaning |
|-------|---------|
| `Prefix` | Unary prefix (e.g., `-x`) |
| `Infix` | Binary infix (e.g., `a + b`) |
| `Postfix` | Unary postfix (e.g., `x!`) |

### BMM_PROCEDURE

| Aspect | Details |
|--------|---------|
| **Description** | Work-performing routine (no return value) |
| **Inheritance** | `BMM_ROUTINE` |

### BMM_VARIABLE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for named storage locations |
| **Inheritance** | `BMM_TYPED` |
| **Accessibility** | Abstract |

### BMM_LOCAL

| Aspect | Details |
|--------|---------|
| **Description** | Local variable within routine |
| **Inheritance** | `BMM_VARIABLE` |

### BMM_PARAMETER

| Aspect | Details |
|--------|---------|
| **Description** | Routine formal parameter |
| **Inheritance** | `BMM_VARIABLE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `direction` | `BMM_PARAMETER_DIRECTION` | 1..1 | In, out, or in/out parameter |

### BMM_RESULT

| Aspect | Details |
|--------|---------|
| **Description** | Function return value |
| **Inheritance** | `BMM_VARIABLE` |

### BMM_PARAMETER_DIRECTION (Enumeration)

| Value | Meaning |
|-------|---------|
| `In` | Input parameter |
| `Out` | Output parameter |
| `InOut` | Bidirectional parameter |

### BMM_ROUTINE_BODY (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for routine implementation |
| **Accessibility** | Abstract |

### BMM_ROUTINE_EXTERNAL

| Aspect | Details |
|--------|---------|
| **Description** | Reference to external routine implementation |
| **Inheritance** | `BMM_ROUTINE_BODY` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `language` | `String` | 1..1 | Language identifier |
| `notation` | `String` | 0..1 | Language dialect/notation |

---

## Literal Values

### Overview

Literal values represent constant values in various forms. The BMM supports primitives, containers, tuples, and type extensions.

### General Model

Literal values inherit from `BMM_LITERAL_VALUE`, providing base semantics.

### Container Literals

Container literals represent fixed collections with specified members.

### Literal Tuples

Tuple literals represent multi-typed value arrays.

### Type Extensions

Literals may be extended with additional type information for semantics preservation.

### Literal Value Classes

#### BMM_LITERAL_VALUE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for literal values |
| **Accessibility** | Abstract |

#### BMM_CONTAINER_VALUE

| Aspect | Details |
|--------|---------|
| **Description** | Container literal value |
| **Inheritance** | `BMM_LITERAL_VALUE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `List<BMM_UNITARY_VALUE>` | 0..1 | Container member values |

#### BMM_INDEXED_CONTAINER_VALUE

| Aspect | Details |
|--------|---------|
| **Description** | Indexed container literal value |
| **Inheritance** | `BMM_CONTAINER_VALUE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `Hash<BMM_PRIMITIVE_VALUE, BMM_UNITARY_VALUE>` | 0..1 | Key-value pairs |

#### BMM_UNITARY_VALUE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for singular literal values |
| **Inheritance** | `BMM_LITERAL_VALUE` |
| **Accessibility** | Abstract |

#### BMM_PRIMITIVE_VALUE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for primitive values |
| **Inheritance** | `BMM_UNITARY_VALUE` |
| **Accessibility** | Abstract |

#### BMM_STRING_VALUE

| Aspect | Details |
|--------|---------|
| **Description** | String literal value |
| **Inheritance** | `BMM_PRIMITIVE_VALUE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `String` | 1..1 | String value |

#### BMM_INTEGER_VALUE

| Aspect | Details |
|--------|---------|
| **Description** | Integer literal value |
| **Inheritance** | `BMM_PRIMITIVE_VALUE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `Integer` | 1..1 | Integer value |

#### BMM_BOOLEAN_VALUE

| Aspect | Details |
|--------|---------|
| **Description** | Boolean literal value |
| **Inheritance** | `BMM_PRIMITIVE_VALUE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `Boolean` | 1..1 | Boolean value |

#### BMM_INTERVAL_VALUE

| Aspect | Details |
|--------|---------|
| **Description** | Interval literal value |
| **Inheritance** | `BMM_UNITARY_VALUE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `lower` | `BMM_PRIMITIVE_VALUE` | 0..1 | Lower bound |
| `upper` | `BMM_PRIMITIVE_VALUE` | 0..1 | Upper bound |
| `lower_unbounded` | `Boolean` | 1..1 | Lower bound infinite |
| `upper_unbounded` | `Boolean` | 1..1 | Upper bound infinite |
| `lower_included` | `Boolean` | 1..1 | Lower bound inclusive |
| `upper_included` | `Boolean` | 1..1 | Upper bound inclusive |

---

## Expressions

### Overview

The BMM includes an expression meta-model supporting first-order predicate logic for expressing assertions, class invariants, and pre/post-conditions.

### Terminal Entities

#### Literals

Literal values as expression operands.

#### Tuples

Multi-typed value collections as expressions.

#### Feature References

References to class properties, constants, and variables.

#### Self Reference

Reference to the current instance (`Current` in Eiffel, `this`/`self` in other languages).

#### Type Reference

Reference to a type by name for isinstance-like operations.

#### Agents

First-class routine references (lambdas/closures).

#### Predicates

Binary predicates testing value attachment and definition:

**attached(x)**: Tests whether x is attached (not null)  
**defined(x)**: Tests whether x is defined (in contracted form)

### Constrained Expressions

Expressions with quantified constraints (for all, exists).

### Operator Expressions

Binary and unary operations on typed expressions.

### Decision Tables

Structured multi-branch decision expressions.

### Usage in BMM Models

#### Simple Assertions

Boolean expressions in class invariants and routine contracts.

#### Quantifier Invariants

Existential and universal quantifier expressions for collection assertions.

### Expression Classes

#### EL_EXPRESSION (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for all expressions |
| **Accessibility** | Abstract |

#### EL_CONSTRAINED

| Aspect | Details |
|--------|---------|
| **Description** | Constrained expression |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `expression` | `EL_EXPRESSION` | 1..1 | Base expression |
| `constraint` | `EL_EXPRESSION` | 1..1 | Constraining predicate |

#### EL_BOOLEAN_EXPRESSION

| Aspect | Details |
|--------|---------|
| **Description** | Boolean-valued expression |
| **Inheritance** | `EL_EXPRESSION` |

#### EL_OPERATOR (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for operator expressions |
| **Inheritance** | `EL_BOOLEAN_EXPRESSION` |
| **Accessibility** | Abstract |

#### EL_UNARY_OPERATOR

| Aspect | Details |
|--------|---------|
| **Description** | Unary operator expression |
| **Inheritance** | `EL_OPERATOR` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `operator` | `String` | 1..1 | Operator symbol |
| `operand` | `EL_EXPRESSION` | 1..1 | Target expression |

#### EL_BINARY_OPERATOR

| Aspect | Details |
|--------|---------|
| **Description** | Binary operator expression |
| **Inheritance** | `EL_OPERATOR` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `operator` | `String` | 1..1 | Operator symbol |
| `left_operand` | `EL_EXPRESSION` | 1..1 | Left expression |
| `right_operand` | `EL_EXPRESSION` | 1..1 | Right expression |

#### EL_SIMPLE

| Aspect | Details |
|--------|---------|
| **Description** | Simple expression (terminal or operator) |
| **Inheritance** | `EL_EXPRESSION` |
| **Accessibility** | Abstract |

#### EL_TERMINAL (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for terminal expressions |
| **Inheritance** | `EL_SIMPLE` |
| **Accessibility** | Abstract |

#### EL_PREDICATE (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for predicate expressions |
| **Inheritance** | `EL_BOOLEAN_EXPRESSION` |
| **Accessibility** | Abstract |

#### EL_DEFINED

| Aspect | Details |
|--------|---------|
| **Description** | Definition test predicate |
| **Inheritance** | `EL_PREDICATE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `expression` | `EL_EXPRESSION` | 1..1 | Expression to test |

#### EL_ATTACHED

| Aspect | Details |
|--------|---------|
| **Description** | Attachment test predicate |
| **Inheritance** | `EL_PREDICATE` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `expression` | `EL_EXPRESSION` | 1..1 | Expression to test |

#### EL_INSTANCE_REF

| Aspect | Details |
|--------|---------|
| **Description** | Reference to named instance |
| **Inheritance** | `EL_TERMINAL` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `instance_name` | `String` | 1..1 | Referenced instance name |

#### EL_SELF_REF

| Aspect | Details |
|--------|---------|
| **Description** | Reference to current instance |
| **Inheritance** | `EL_TERMINAL` |

#### EL_TYPE_REF

| Aspect | Details |
|--------|---------|
| **Description** | Reference to type by name |
| **Inheritance** | `EL_TERMINAL` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `type_name` | `String` | 1..1 | Referenced type name |

#### EL_LITERAL

| Aspect | Details |
|--------|---------|
| **Description** | Literal value expression |
| **Inheritance** | `EL_TERMINAL` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `value` | `BMM_LITERAL_VALUE` | 1..1 | Literal value |

#### EL_SCOPED_REF

| Aspect | Details |
|--------|---------|
| **Description** | Reference to scoped entity |
| **Inheritance** | `EL_TERMINAL` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `scope` | `String` | 1..1 | Scope path |
| `item` | `String` | 1..1 | Referenced item name |

#### EL_INSTANTIABLE_REF

| Aspect | Details |
|--------|---------|
| **Description** | Reference to instantiable entity |
| **Inheritance** | `EL_TERMINAL` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `item_name` | `String` | 1..1 | Referenced item name |

#### EL_AGENT_CALL

| Aspect | Details |
|--------|---------|
| **Description** | Agent/lambda invocation |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `agent` | `EL_AGENT` | 1..1 | Agent expression |
| `arguments` | `List<EL_EXPRESSION>` | 0..1 | Call arguments |

#### EL_FUNCTION_CALL

| Aspect | Details |
|--------|---------|
| **Description** | Function invocation |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `function_name` | `String` | 1..1 | Function identifier |
| `arguments` | `List<EL_EXPRESSION>` | 0..1 | Call arguments |

#### EL_AGENT (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for agent (lambda) expressions |
| **Inheritance** | `EL_TERMINAL` |
| **Accessibility** | Abstract |

#### EL_FUNCTION_AGENT

| Aspect | Details |
|--------|---------|
| **Description** | Value-returning agent |
| **Inheritance** | `EL_AGENT` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `function` | `EL_EXPRESSION` | 1..1 | Function to invoke |

#### EL_PROCEDURE_AGENT

| Aspect | Details |
|--------|---------|
| **Description** | Work-performing agent |
| **Inheritance** | `EL_AGENT` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `procedure` | `EL_EXPRESSION` | 1..1 | Procedure to invoke |

#### EL_TUPLE

| Aspect | Details |
|--------|---------|
| **Description** | Tuple expression |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `items` | `List<EL_TUPLE_ITEM>` | 0..1 | Tuple member values |

#### EL_TUPLE_ITEM

| Aspect | Details |
|--------|---------|
| **Description** | Single tuple member |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `name` | `String` | 0..1 | Optional member name |
| `expression` | `EL_EXPRESSION` | 1..1 | Member expression |

#### EL_DECISION_TABLE

| Aspect | Details |
|--------|---------|
| **Description** | Multi-branch decision structure |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `branches` | `List<EL_DECISION_BRANCH>` | 1..1 | Decision branches |
| `default_branch` | `EL_EXPRESSION` | 0..1 | Default result |

#### EL_DECISION_BRANCH

| Aspect | Details |
|--------|---------|
| **Description** | Single decision branch |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `condition` | `EL_BOOLEAN_EXPRESSION` | 1..1 | Branch condition |
| `result` | `EL_EXPRESSION` | 1..1 | Branch result |

#### EL_CONDITION_CHAIN

| Aspect | Details |
|--------|---------|
| **Description** | Chained conditional structure |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `condition` | `EL_BOOLEAN_EXPRESSION` | 1..1 | Condition to test |
| `then_result` | `EL_EXPRESSION` | 1..1 | True branch result |
| `else_result` | `EL_EXPRESSION` | 0..1 | False branch result |

#### EL_CONDITIONAL_EXPRESSION

| Aspect | Details |
|--------|---------|
| **Description** | Ternary conditional expression |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `condition` | `EL_BOOLEAN_EXPRESSION` | 1..1 | Condition |
| `true_expression` | `EL_EXPRESSION` | 1..1 | True result |
| `false_expression` | `EL_EXPRESSION` | 0..1 | False result |

#### EL_CASE_TABLE

| Aspect | Details |
|--------|---------|
| **Description** | Switch/case expression |
| **Inheritance** | `EL_EXPRESSION` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `cases` | `List<EL_CASE>` | 1..1 | Case branches |
| `default_result` | `EL_EXPRESSION` | 0..1 | Default result |

#### EL_CASE

| Aspect | Details |
|--------|---------|
| **Description** | Single case branch |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `conditions` | `List<EL_EXPRESSION>` | 1..1 | Case conditions |
| `result` | `EL_EXPRESSION` | 1..1 | Case result |

---

## Functional Elements

### Overview

The BMM treats routine calls and functional constructs as first-class entities through agents and signatures.

### Agents

Agents represent delayed routine invocations, similar to function pointers or closures. They bind to either functions or procedures.

### Calls

Agent invocations (calls) execute delayed functions with specified arguments.

---

## Statements

### Overview

The BMM includes basic statement support for expressing routine implementations.

### Assignment

Statements assigning expressions to variables.

### Procedure Call

Statements invoking procedures.

### Action Tables

Structured multi-branch action execution.

### Assertions

Constraint-checking statements.

### Statement Classes

#### BMM_STATEMENT_ITEM (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for statement items |
| **Accessibility** | Abstract |

#### BMM_STATEMENT_BLOCK

| Aspect | Details |
|--------|---------|
| **Description** | Sequence of statements |
| **Inheritance** | `BMM_STATEMENT_ITEM` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `statements` | `List<BMM_STATEMENT>` | 0..1 | Statement sequence |

#### BMM_STATEMENT

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for executable statements |
| **Inheritance** | `BMM_STATEMENT_ITEM` |
| **Accessibility** | Abstract |

#### BMM_SIMPLE_STATEMENT (Abstract)

| Aspect | Details |
|--------|---------|
| **Description** | Meta-type for non-compound statements |
| **Inheritance** | `BMM_STATEMENT` |
| **Accessibility** | Abstract |

#### BMM_PROCEDURE_CALL

| Aspect | Details |
|--------|---------|
| **Description** | Procedure invocation statement |
| **Inheritance** | `BMM_SIMPLE_STATEMENT` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `procedure` | `EL_EXPRESSION` | 1..1 | Procedure to invoke |
| `arguments` | `List<EL_EXPRESSION>` | 0..1 | Call arguments |

#### BMM_ASSIGNMENT

| Aspect | Details |
|--------|---------|
| **Description** | Variable assignment statement |
| **Inheritance** | `BMM_SIMPLE_STATEMENT` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `target` | `String` | 1..1 | Target variable |
| `value` | `EL_EXPRESSION` | 1..1 | Value expression |

#### BMM_ASSERTION

| Aspect | Details |
|--------|---------|
| **Description** | Assertion statement |
| **Inheritance** | `BMM_SIMPLE_STATEMENT` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `assertion` | `EL_BOOLEAN_EXPRESSION` | 1..1 | Predicate to assert |
| `message` | `String` | 0..1 | Failure message |

#### BMM_ACTION_TABLE

| Aspect | Details |
|--------|---------|
| **Description** | Multi-branch action structure |
| **Inheritance** | `BMM_STATEMENT` |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `actions` | `List<BMM_CONDITIONAL_ACTION>` | 1..1 | Conditional actions |
| `default_action` | `BMM_STATEMENT` | 0..1 | Default statement |

#### BMM_CONDITIONAL_ACTION

| Aspect | Details |
|--------|---------|
| **Description** | Conditional action branch |

**Attributes**:

| Name | Type | Cardinality | Meaning |
|------|------|-------------|---------|
| `condition` | `EL_BOOLEAN_EXPRESSION` | 1..1 | Branch condition |
| `action` | `BMM_STATEMENT` | 1..1 | Branch statement |

---

## Model Semantics

### Inheritance

Model semantics define how inheritance relationships function across simple, generic, multiple, and constrained inheritance scenarios.

#### Simple Inheritance

Basic inheritance from a single parent class or type.

**Rules:**
- Child classes gain all parent features
- Child class conforms to parent type
- Multiple inheritance resolution via feature redefinition

#### Generic Inheritance

Inheritance involving generic classes with parameter substitution.

**Rules:**
- Generic parameters may be constrained by parent
- Parameter constraints propagate to children
- Substitution types must satisfy constraints

#### Multiple Inheritance

Inheritance from multiple parents.

**Conflict Resolution:**
- Features inherited from multiple paths use inheritance order
- Explicit redefinition in child class required for disambiguation
- Type conformance follows all parent paths

#### Inheritance with Contracts

Pre-conditions, post-conditions, and invariants follow contract inheritance rules:

**Preconditions:** May be weakened (relaxed) in child routines  
**Postconditions:** May not be weakened (must maintain or strengthen)  
**Invariants:** Must be maintained by all descendants

---

## BMM Extensions

### Overview

The BMM supports extension mechanisms for model-specific meta-data and feature annotations.

### General Extensions

The `_extensions_` attribute on `BMM_DECLARATION` enables arbitrary keyed meta-data attachment to any model element.

### Feature Extensions

Feature-specific extensions support specialized annotations on properties, routines, and other features without BMM modification.

---

## Copyright and License

© 2016 - 2021 The openEHR Foundation

[The openEHR Foundation](https://www.openehr.org) is an independent, non-profit foundation facilitating health record sharing by consumers and clinicians via open specifications, clinical models, and open platform implementations.

**License**: Creative Commons Attribution-NoDerivs 3.0 Unported. [https://creativecommons.org/licenses/by-nd/3.0/](https://creativecommons.org/licenses/by-nd/3.0/)

**Support**:
- Issues: [Problem Reports](https://specifications.openehr.org/components/LANG/open_issues)
- Web: [specifications.openEHR.org](https://specifications.openehr.org)