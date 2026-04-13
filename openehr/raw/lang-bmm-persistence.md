# BMM Persistence Model and Syntax

**Status:** STABLE
**Release:** LANG Release-1.0.0
**Date:** [latest_issue_date]
**Keywords:** reflection, meta-model, UML

**Issuer:** openEHR Specification Program

© 2016 - 2021 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Amendment Record](#amendment-record)
2. [Acknowledgements](#acknowledgements)
3. [Preface](#preface)
4. [Overview](#overview)
5. [Persistence Package](#persistence-package)
6. [BMM Persistence Syntax](#bmm-persistence-syntax)

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| **LANG Release 1.0.0 - 2.3.0** | Add Basic Meta-Model (BMM) spec to BASE component | openEHR SEC | 04 Sep 2019 |
| | Support indexed containers like `Hash<K, V>` | T Beale | 04 Sep 2019 |
| | Add value-set constraint | T Beale | 26 Mar 2019 |
| | Separate from main BMM specification; support generic types as class ancestors; add `P_BMM_BASE_TYPE` | T Beale | 27 Apr 2018 |
| **2.2.2** | Improve introductory text in Overview section | E Sundvall, T Beale | 03 Nov 2017 |
| **2.2.1** | Rename and restructure classes for consistency | C Nanjo, T Beale | 02 Mar 2017 |
| **2.2.0** | Remove `P_BMM_CLASSIFIER`; add inheritance fixes | T Beale | 20 Jun 2016 |
| | Correct naming conventions for methods | T Beale | 18 Apr 2016 |
| **2.1.0** | Initial writing based on ADL Workbench implementation | T Beale | 08 Feb 2016 |

---

## Acknowledgements

### Primary Author

- **Thomas Beale**, Ars Semantica; openEHR Foundation Management Board

### Contributors

- Patrick Langford, NeuronSong LLC, Utah, USA
- Claude Nanjo, Cognitive Medical Systems Inc., California, USA
- Erik Sundvall PhD, Linkoping University, Sweden

### Trademarks

- "openEHR" is a registered trademark of the openEHR Foundation
- "OMG" and "UML" are registered trademarks of the Object Management Group

---

## Preface

### Purpose

This specification describes a persistence model for the Basic Meta-Model (BMM) called `P_BMM`, suitable for serializing BMM models. It functions as an approximate replacement for UML XMI for data-only models, offering human-readability and support for generic types, container types, and multiple inheritance.

### Status

This specification achieves STABLE status. The development version is available at the official openEHR specifications repository.

Known omissions are indicated with "TBD" (To Be Determined) paragraphs.

### Feedback

- **Forum:** openEHR languages specifications forum
- **Issue Tracking:** Specifications Problem Report tracker
- **Change History:** LANG component Change Request tracker

### Conformance

Conformance to openEHR specifications is determined through formal testing against relevant Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

### Tooling

- **ADL Workbench (AWB):** Full implementation in Eiffel, available as open source on Github
- **Archie:** Java-based modeling tool in openEHR Github area
- **BMM Libraries:** Available in EOMF Github repository

---

## Overview

### Conceptual Approach

This specification defines a model for serializing the Basic Meta-Model (BMM). The approach uses `P_BMM_XXX` classes as intermediate representations that enable symbolic referencing via class names and syntactical type names, rather than materializing complex object graphs directly.

The `P_BMM_*` classes serve dual purposes:

1. **Simplified Object Model:** A modified version of `BMM_*` classes enabling human-readable serialization
2. **Schema Framework:** Support for schema inclusion and reuse, analogous to XML schema approaches

A logical BMM model can be expressed as multiple `.bmm` schema files, which are `P_BMM_*` object serializations. Schema readers resolve inclusions to produce final in-memory BMM model instances.

We distinguish between:
- **P_BMM Form:** Model of a BMM schema (with symbolic references)
- **BMM Form:** Model of a compiled BMM model (fully resolved references)

### Concrete Format

BMM models are typically expressed as schema text files supporting inclusion and reuse. The default format has historically been openEHR ODIN syntax, though other formats supporting typed object models are acceptable, including JSON (with type markers), YAML, and XML.

---

## Persistence Package

### Overview

The `org.openehr.lang.bmm_persistence` package defines a simplified persistence form of the main BMM model suitable for serialization and human authoring. Attributes named `_bmm_xxx_` of type `BMM_XXX` are derived from persisted attributes of corresponding `P_BMM_XXX` classes.

### Class Definitions

#### P_BMM_MODEL_ELEMENT Class

**Description:** Persistent form of `BMM_MODEL_ELEMENT`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | documentation | String | Optional documentation of this element |

#### P_BMM_PACKAGE_CONTAINER Class

**Description:** Persisted form of a model component that contains packages

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | packages | Hash<String, P_BMM_PACKAGE> | Package hierarchy structure |

#### P_BMM_SCHEMA Class

**Inherits:** `P_BMM_PACKAGE_CONTAINER`, `BMM_SCHEMA`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | primitive_types | List<P_BMM_CLASS> | Primitive type definitions |
| 0..1 | class_definitions | List<P_BMM_CLASS> | Class definitions |

**Functions:**

| Cardinality | Function | Pre-state | Post-state |
|---|---|---|---|
| 0..1 | validate_created() | state = State_created | state = State_validated_created |
| 0..1 | load_finalise() | state = State_validated_created | state = State_includes_processed or State_includes_pending |
| 0..1 | merge(other: P_BMM_SCHEMA) | state = State_includes_pending | — |
| 0..1 | validate() | — | — |
| 0..1 | create_bmm_model() | state = State_includes_processed | — |
| 1..1 | canonical_packages() | — | P_BMM_PACKAGE |

#### P_BMM_PACKAGE Class

**Inherits:** `P_BMM_PACKAGE_CONTAINER`, `P_BMM_MODEL_ELEMENT`

**Description:** Package as a tree structure with potential subpackages and/or classes

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | name | String | Package name (may be qualified) |
| 0..1 | classes | List<String> | Class names in this package |
| 0..1 | bmm_package_definition | BMM_PACKAGE | Generated BMM_PACKAGE object |

**Functions:**

| Function | Purpose |
|---|---|
| merge(other: P_BMM_PACKAGE) | Merge packages and classes from included schemas |
| create_bmm_package_definition() | Generate BMM_PACKAGE object |

#### P_BMM_TYPE Class

**Description:** Persistent form of `BMM_TYPE` (abstract)

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | bmm_type | BMM_TYPE | Result of create_bmm_type() |

**Functions:**

| Cardinality | Function | Purpose |
|---|---|---|
| 0..1 | create_bmm_type(a_schema, a_class_def) | Create appropriate BMM_XXX object |
| 1..1 | as_type_string() | Formal name for display |

#### P_BMM_CLASS Class

**Inherits:** `P_BMM_MODEL_ELEMENT`

**Description:** Persistent form of `BMM_CLASS` for serialization

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | name | String | Class name |
| 0..1 | ancestors | List<String> | Immediate inheritance parents |
| 0..1 | properties | Hash<String, P_BMM_PROPERTY> | Class attributes |
| 0..1 | is_abstract | Boolean | Abstract type flag |
| 0..1 | is_override | Boolean | Overrides included schema definition |
| 0..1 | generic_parameter_defs | Hash<String, P_BMM_GENERIC_PARAMETER> | Generic parameters |
| 1..1 | source_schema_id | String | Source schema identifier |
| 0..1 | bmm_class | BMM_CLASS | Generated BMM_CLASS object |
| 1..1 | uid | Integer | Unique id for merge comparison |
| 0..1 | ancestor_defs | List<P_BMM_GENERIC_TYPE> | Structured inheritance ancestors |

**Functions:**

| Function | Purpose |
|---|---|
| is_generic() | True if class is generic |
| create_bmm_class() | Create `_bmm_class_definition_` |
| populate_bmm_class(a_bmm_schema) | Add model elements to bmm_class |

#### P_BMM_GENERIC_PARAMETER Class

**Inherits:** `P_BMM_MODEL_ELEMENT`

**Description:** Persistent form of `BMM_GENERIC_PARAMETER`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | name | String | Parameter name (single uppercase letter) |
| 0..1 | conforms_to_type | String | Conformance constraint type name |
| 0..1 | bmm_generic_parameter | BMM_PARAMETER_TYPE | Generated object |

**Invariant:** `name.count = 1 and name.is_upper`

**Functions:**

| Function | Purpose |
|---|---|
| create_bmm_generic_parameter(a_bmm_schema) | Create BMM_GENERIC_PARAMETER |

#### P_BMM_PROPERTY Class

**Inherits:** `P_BMM_MODEL_ELEMENT` (abstract)

**Description:** Persistent form of `BMM_PROPERTY`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | name | String | Property name in class |
| 0..1 | is_mandatory | Boolean | Mandatory flag |
| 0..1 | is_computed | Boolean | Computed property flag |
| 0..1 | is_im_infrastructure | Boolean | Infrastructure property flag |
| 0..1 | is_im_runtime | Boolean | Runtime settable flag |
| 0..1 | type_def | P_BMM_TYPE | Type definition |
| 0..1 | bmm_property | BMM_PROPERTY | Generated object |

**Functions:**

| Function | Purpose |
|---|---|
| create_bmm_property(a_bmm_schema, a_class_def) | Create BMM_PROPERTY from P_BMM parts |

#### P_BMM_BASE_TYPE Class

**Inherits:** `P_BMM_TYPE` (abstract)

**Description:** Persistent form of `BMM_PROPER_TYPE`

| Cardinality | Attribute | Type |
|---|---|---|
| 0..1 | value_constraint | String |

#### P_BMM_SIMPLE_TYPE Class

**Inherits:** `P_BMM_BASE_TYPE`

**Description:** Persistent form of `BMM_SIMPLE_TYPE`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | type | String | Simple class name |
| 0..1 | bmm_type | BMM_SIMPLE_TYPE | Generated object |

#### P_BMM_OPEN_TYPE Class

**Inherits:** `P_BMM_BASE_TYPE`

**Description:** Persistent form of `BMM_PARAMETER_TYPE`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | type | String | Type parameter (single letter) |
| 0..1 | bmm_type | BMM_PARAMETER_TYPE | Generated object |

#### P_BMM_GENERIC_TYPE Class

**Inherits:** `P_BMM_BASE_TYPE`

**Description:** Persistent form of `BMM_GENERIC_TYPE`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | root_type | String | Root type name |
| 1..1 | generic_parameter_defs | List<P_BMM_TYPE> | Non-simple generic parameters |
| 0..1 | generic_parameters | List<String> | Simple type parameters |
| 0..1 | bmm_type | BMM_GENERIC_TYPE | Generated object |

**Functions:**

| Function | Purpose |
|---|---|
| generic_parameter_refs() | Return generic parameters in order |

#### P_BMM_CONTAINER_TYPE Class

**Inherits:** `P_BMM_TYPE`

**Description:** Persistent form of `BMM_CONTAINER_TYPE`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | container_type | String | Container type name |
| 0..1 | type_def | P_BMM_BASE_TYPE | Type definition |
| 0..1 | type | String | Target type name |
| 0..1 | bmm_type | BMM_CONTAINER_TYPE | Generated object |

**Functions:**

| Function | Purpose |
|---|---|
| type_ref() | Return target type |

#### P_BMM_INDEXED_CONTAINER_TYPE Class

**Inherits:** `P_BMM_CONTAINER_TYPE`

**Description:** Support for indexed containers like `Hash<K, V>`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | index_type | String | Key type name |
| 0..1 | bmm_type | BMM_INDEXED_CONTAINER_TYPE | Generated object |

#### P_BMM_SINGLE_PROPERTY Class

**Inherits:** `P_BMM_PROPERTY`

**Description:** Persistent form of `BMM_SINGLE_PROPERTY`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | type | String | Type name if simple |
| 0..1 | type_ref | P_BMM_SIMPLE_TYPE | Generated type reference |
| 0..1 | bmm_property | BMM_UNITARY_PROPERTY | Generated object |

**Functions:**

| Function | Purpose |
|---|---|
| type_def() | Generate type_ref from type |

#### P_BMM_SINGLE_PROPERTY_OPEN Class

**Inherits:** `P_BMM_PROPERTY`

**Description:** Persistent form of single open property with generic parameter type

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | type_ref | P_BMM_OPEN_TYPE | Type definition |
| 0..1 | type | String | Type parameter reference |
| 0..1 | bmm_property | BMM_UNITARY_PROPERTY | Generated object |

**Functions:**

| Function | Purpose |
|---|---|
| type_def() | Generate type_ref from type |

#### P_BMM_GENERIC_PROPERTY Class

**Inherits:** `P_BMM_PROPERTY`

**Description:** Persistent form of `BMM_GENERIC_PROPERTY`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | type_def | P_BMM_GENERIC_TYPE | Type definition |
| 0..1 | bmm_property | BMM_UNITARY_PROPERTY | Generated object |

#### P_BMM_CONTAINER_PROPERTY Class

**Inherits:** `P_BMM_PROPERTY`

**Description:** Persistent form of `BMM_CONTAINER_PROPERTY`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | cardinality | Interval<Integer> | Container cardinality |
| 0..1 | type_def | P_BMM_CONTAINER_TYPE | Type definition |
| 0..1 | bmm_property | BMM_CONTAINER_PROPERTY | Generated object |

**Functions:**

| Function | Purpose |
|---|---|
| create_bmm_property(a_bmm_schema, a_class_def) | Create BMM_CONTAINER_PROPERTY |

#### P_BMM_INDEXED_CONTAINER_PROPERTY Class

**Inherits:** `P_BMM_CONTAINER_PROPERTY`

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | type_def | P_BMM_INDEXED_CONTAINER_TYPE | Type definition |
| 0..1 | bmm_property | BMM_INDEXED_CONTAINER_PROPERTY | Generated object |

#### P_BMM_ENUMERATION Class

**Inherits:** `P_BMM_CLASS`

**Description:** Persistent form of `BMM_ENUMERATION` attributes

| Cardinality | Attribute | Type |
|---|---|---|
| 0..1 | item_names | List<String> |
| 0..1 | item_values | List<Any> |
| 0..1 | bmm_class | BMM_ENUMERATION |

#### P_BMM_ENUMERATION_STRING Class

**Inherits:** `P_BMM_ENUMERATION`

**Description:** Persistent form of `BMM_ENUMERATION_STRING`

| Cardinality | Attribute | Type |
|---|---|---|
| 0..1 | bmm_class | BMM_ENUMERATION_STRING |

#### P_BMM_ENUMERATION_INTEGER Class

**Inherits:** `P_BMM_ENUMERATION`

**Description:** Persistent form of `BMM_ENUMERATION_INTEGER`

| Cardinality | Attribute | Type |
|---|---|---|
| 0..1 | bmm_class | BMM_ENUMERATION_INTEGER |

---

## BMM Persistence Syntax

### Overview

BMM schemas are typically authored in openEHR ODIN syntax, though any format supporting typed object models may be used, including JSON, YAML, and XML. The structures are direct ODIN serializations of the `P_BMM_XXX` classes.

### Header Items

A BMM schema header contains metadata corresponding to persistent attributes of the `P_BMM_SCHEMA` class:

```odin
bmm_version = <"2.3">

-- Schema identification
rm_publisher = <"openehr">
schema_name = <"adltest">
rm_release = <"1.0.2">
model_name = <"TEST_PKG">

-- Schema documentation
schema_revision = <"1.0.36">
schema_lifecycle_state = <"stable">
schema_description = <"openEHR schema to support test archetypes">
```

### Inclusions

Schema files may include other schemas:

```odin
includes = <
    ["1"] = <
        id = <"openehr_basic_types_1.0.2">
    >
>
```

### Package Definition

Packages are defined recursively with class names and subpackages:

```odin
packages = <
    ["org.openehr.test_pkg"] = <
        name = <"org.openehr.test_pkg">
        classes = <"WHOLE", "SOME_TYPE", "BOOK", "CHAPTER", "ENTRY", "CAR", "CAR_BODY">
    >
>
```

**Notes:**
- Only top-level package identifiers can contain dots (.)
- Only same-schema-defined classes can be referenced
- ODIN keys must match `name` attributes

### Class Definitions

#### Classes for Primitive Types

Primitive type definitions appear in a `primitive_types` block as normal class definitions. These typically correspond to primitives in target programming languages or downstream technologies.

```odin
primitive_types = <
    ["Any"] = <
        name = <"Any">
        is_abstract = <True>
    >
    ["Ordered"] = <
        name = <"Ordered">
        is_abstract = <True>
        ancestors = <"Any">
    >
>
```

#### Non-primitive Classes

Main class definitions appear within `class_definitions` blocks as keyed ODIN objects:

```odin
class_definitions = <
    ["ITEM"] = <
        name = <"ITEM">
        ancestors = <"Any">
        is_abstract = <True>
        properties = <
            -- properties defined here
        >
    >
>
```

Class-level meta-properties:

| Property | Type | Purpose |
|---|---|---|
| name | String | Class name |
| ancestors | List<String> | Inheritance parents |
| is_abstract | Boolean | Cannot be instantiated |
| properties | Hash | Attribute definitions |

#### Simple Classes

Simple classes have types matching their names:

```odin
["ELEMENT"] = <
    name = <"ELEMENT">
    ancestors = <"ITEM">
    properties = <
        ["null_flavour"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"null_flavour">
            type = <"DV_CODED_TEXT">
            is_mandatory = <True>
        >
        ["value"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"value">
            type = <"DATA_VALUE">
        >
    >
>
```

##### Class Properties

Properties use ODIN object blocks keyed by property name with ODIN type markers:

| Property | Type | Purpose |
|---|---|---|
| name | String | Property name in class |
| is_mandatory | Boolean | Mandatory flag |

##### Container Properties

Container properties define structured collection types:

```odin
["ELEMENT"] = <
    name = <"ELEMENT">
    ancestors = <"ITEM">
    properties = <
        ["items"] = (P_BMM_CONTAINER_PROPERTY) <
            name = <"items">
            type_def = <
                container_type = <"List">
                type = <"ITEM">
            >
            cardinality = <|>=1|>
            is_mandatory = <True>
        >
    >
>
```

Indexed containers like `Hash<K,V>` and `Dictionary<K,V>` use `P_BMM_INDEXED_CONTAINER_PROPERTY`:

```odin
["CALLBACK_WAIT"] = <
    name = <"CALLBACK_WAIT">
    ancestors = <"...">
    properties = <
        ["custom_actions"] = (P_BMM_INDEXED_CONTAINER_PROPERTY) <
            name = <"custom_actions">
            type_def = <
                container_type = <"Hash">
                index_type = <"String">
                type = <"EVENT_ACTION">
            >
            cardinality = <|>=0|>
        >
    >
>
```

#### Generic Classes

Generic classes contain substitutable type parameters, functioning as type generators:

```odin
["Interval"] = <
    name = <"Interval">
    ancestors = <"Any">
    generic_parameter_defs = <
        ["T"] = <
            name = <"T">
            conforms_to_type = <"Ordered">
        >
    >
    properties = <
        ["lower"] = (P_BMM_SINGLE_PROPERTY_OPEN) <
            name = <"lower">
            type = <"T">
        >
        ["upper"] = (P_BMM_SINGLE_PROPERTY_OPEN) <
            name = <"upper">
            type = <"T">
        >
    >
>
```

Generic types as property types use `P_BMM_GENERIC_PROPERTY`:

```odin
["DV_INTERVAL"] = <
    name = <"DV_INTERVAL">
    ancestors = <"Interval", "DATA_VALUE">
    generic_parameter_defs = <
        ["T"] = <
            name = <"T">
            conforms_to_type = <"DV_ORDERED">
        >
    >
>

["SOME_TYPE"] = <
    name = <"SOME_TYPE">
    ancestors = <"Any">
    properties = <
        ["qty_interval_attr"] = (P_BMM_GENERIC_PROPERTY) <
            name = <"qty_interval_attr">
            type_def = <
                root_type = <"DV_INTERVAL">
                generic_parameters = <"DV_QUANTITY">
            >
        >
    >
>
```

Complex nested types like `List<Reference<Party>>`:

```odin
["Patient"] = <
    name = <"Patient">
    ancestors = <"Any">
    properties = <
        ["careProvider"] = (P_BMM_CONTAINER_PROPERTY) <
            name = <"careProvider">
            type_def = <
                container_type = <"List">
                type_def = (P_BMM_GENERIC_TYPE) <
                    root_type = <"Reference">
                    generic_parameters = <"Party">
                >
            >
            cardinality = <|>=0|>
        >
    >
>
```

Generic parameters themselves can be generic types:

```odin
["REFERENCE_RANGE"] = <
    name = <"REFERENCE_RANGE">
    ancestors = <"Any">
    generic_parameter_defs = <
        ["T"] = <
            name = <"T">
            conforms_to_type = <"DV_ORDERED">
        >
    >
    properties = <
        ["range"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"range">
            type = <"DV_INTERVAL">
            is_mandatory = <True>
        >
    >
>

["RANGE_OF_INTERVAL_OF_QUANTITY"] = <
    name = <"RANGE_OF_INTERVAL_OF_QUANTITY">
    ancestors = <"Any">
    properties = <
        ["range"] = (P_BMM_GENERIC_PROPERTY) <
            name = <"range">
            type_def = <
                root_type = <"REFERENCE_RANGE">
                generic_parameter_defs = <
                    ["T"] = (P_BMM_GENERIC_TYPE) <
                        root_type = <"DV_INTERVAL">
                        generic_parameters = <"DV_QUANTITY">
                    >
                >
            >
        >
    >
>
```

Complex multi-parameter example:

```odin
["CRAZY_TYPE"] = <
    name = <"CRAZY_TYPE">
    ancestors = <"Any">
    properties = <
        ["range"] = (P_BMM_GENERIC_PROPERTY) <
            name = <"range">
            type_def = <
                root_type = <"REFERENCE_RANGE">
                generic_parameter_defs = <
                    ["T"] = (P_BMM_GENERIC_TYPE) <
                        root_type = <"DV_INTERVAL">
                        generic_parameters = <"DV_QUANTITY">
                    >
                    ["U"] = (P_BMM_SIMPLE_TYPE) <
                        type = <"Integer">
                    >
                    ["V"] = (P_BMM_CONTAINER_TYPE) <
                        type = <"DV_QUANTITY">
                        container_type = <"List">
                    >
                    ["W"] = (P_BMM_CONTAINER_TYPE) <
                        type_def = (P_BMM_GENERIC_TYPE) <
                            root_type = <"DV_INTERVAL">
                            generic_parameters = <"DV_QUANTITY">
                        >
                        container_type = <"List">
                    >
                >
            >
        >
    >
>
```

#### Enumerated Types

Enumerated types are constrained forms of standard types, represented using `P_BMM_ENUMERATION_INTEGER` and `P_BMM_ENUMERATION_STRING`:

```odin
["PROPORTION_KIND"] = (P_BMM_ENUMERATION_INTEGER) <
    name = <"PROPORTION_KIND">
    ancestors = <"Integer">
    item_names = <"pk_ratio", "pk_unitary", "pk_percent", "pk_fraction", "pk_integer_fraction">
>

["PROPORTION_KIND_2"] = (P_BMM_ENUMERATION_INTEGER) <
    name = <"PROPORTION_KIND_2">
    ancestors = <"Integer">
    item_names = <"pk_ratio", "pk_unitary", "pk_percent", "pk_fraction", "pk_integer_fraction">
    item_values = <0, 1001, 1002, 1003>
>
```

String enumerations:

```odin
["MAGNITUDE_STATUS"] = (P_BMM_ENUMERATION_STRING) <
    name = <"MAGNITUDE_STATUS">
    ancestors = <"String">
    item_names = <"le", "ge", "eq", "approx_eq">
    item_values = <"<=", ">=", "=", "~">
>

["NAME_PART"] = (P_BMM_ENUMERATION_STRING) <
    name = <"NAME_PART">
    ancestors = <"String">
    item_names = <"FIRST", "MIDDLE", "LAST">
>
```

#### Value-set Constraints

Value-sets constrain standard types to external value sets without explicit enumeration:

```odin
-- Simple form without constraint
["encoding"] = (P_BMM_SINGLE_PROPERTY) <
    name = <"encoding">
    type = <"CODE_PHRASE">
>

-- With value-set constraint
["encoding"] = (P_BMM_SINGLE_PROPERTY) <
    name = <"encoding">
    type_ref = <
        type = <"CODE_PHRASE">
        value_constraint = <"openEHR::languages">
    >
>
```

Container types with value constraints:

```odin
-- Original form
["language"] = (P_BMM_CONTAINER_PROPERTY) <
    name = <"language">
    type_def = <
        container_type = <"List">
        type = <"Coding">
    >
>

-- With value constraint
["language"] = (P_BMM_CONTAINER_PROPERTY) <
    name = <"language">
    type_def = <
        container_type = <"List">
        type_def = (P_BMM_SIMPLE_TYPE) <
            type = <"Coding">
            value_constraint = <"hl7::Languages">
        >
    >
>
```

### Inheritance

Simple class inheritance uses the `ancestors` string list:

```odin
["PARENT"] = <
    name = <"PARENT">
    properties = <
        -- properties
    >
>

["CHILD"] = <
    name = <"CHILD">
    ancestors = <"PARENT">
    properties = <
        -- additional properties
    >
>
```

Generic inheritance uses structured `ancestor_defs` section instead of the `ancestors` list:

```odin
["GENERIC_PARENT"] = <
    name = <"GENERIC_PARENT">
    generic_parameter_defs = <
        ["T"] = <
            name = <"T">
            conforms_to_type = <"SUPPLIER">
        >
        ["U"] = <
            name = <"U">
            conforms_to_type = <"SUPPLIER">
        >
    >
    properties = <
        ["property_a"] = (P_BMM_SINGLE_PROPERTY_OPEN) <
            name = <"property_a">
            type = <"T">
        >
        ["property_b"] = (P_BMM_SINGLE_PROPERTY_OPEN) <
            name = <"property_b">
            type = <"U">
        >
    >
>

["SUPPLIER"] = <
    name = <"SUPPLIER">
    is_abstract = <True>
    properties = <
        ["abstract_prop"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"abstract_prop">
            type = <"String">
        >
    >
>

["SUPPLIER_A"] = <
    name = <"SUPPLIER_A">
    ancestors = <"SUPPLIER">
    properties = <
        ["magnitude"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"magnitude">
            type = <"Double">
            is_mandatory = <True>
        >
        ["units"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"units">
            type = <"String">
            is_mandatory = <True>
        >
    >
>

["SUPPLIER_B"] = <
    name = <"SUPPLIER_B">
    ancestors = <"SUPPLIER">
    properties = <
        ["property"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"property">
            type = <"CODE_PHRASE">
            is_mandatory = <True>
        >
        ["precision"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"precision">
            type = <"Integer">
        >
    >
>

["GENERIC_CHILD_OPEN_T"] = <
    name = <"GENERIC_CHILD_OPEN_T">
    ancestor_defs = <
        ["GENERIC_PARENT<T,SUPPLIER_B>"] = (P_BMM_GENERIC_TYPE) <
            root_type = <"GENERIC_PARENT">
            generic_parameters = <"T", "SUPPLIER_B">
        >
    >
    generic_parameter_defs = <
        ["T"] = <
            name = <"T">
            conforms_to_type = <"SUPPLIER">
        >
    >
    properties = <
        ["gen_child_open_t_prop"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"gen_child_open_t_prop">
            type = <"String">
        >
    >
>

["GENERIC_CHILD_OPEN_U"] = <
    name = <"GENERIC_CHILD_OPEN_U">
    ancestor_defs = <
        ["GENERIC_PARENT<SUPPLIER_A,U>"] = (P_BMM_GENERIC_TYPE) <
            root_type = <"GENERIC_PARENT">
            generic_parameters = <"SUPPLIER_A", "U">
        >
    >
    generic_parameter_defs = <
        ["U"] = <
            name = <"U">
            conforms_to_type = <"SUPPLIER">
        >
    >
    properties = <
        ["gen_child_open_u_prop"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"gen_child_open_u_prop">
            type = <"String">
        >
    >
>

["GENERIC_CHILD_CLOSED"] = <
    name = <"GENERIC_CHILD_CLOSED">
    ancestor_defs = <
        ["GENERIC_PARENT<SUPPLIER_A,SUPPLIER_B>"] = (P_BMM_GENERIC_TYPE) <
            root_type = <"GENERIC_PARENT">
            generic_parameters = <"SUPPLIER_A", "SUPPLIER_B">
        >
    >
    properties = <
        ["gen_child_closed_prop"] = (P_BMM_SINGLE_PROPERTY) <
            name = <"gen_child_closed_prop">
            type = <"String">
        >
    >
>
```

---

**Last Updated:** 2020-07-27 10:29:54 +0100