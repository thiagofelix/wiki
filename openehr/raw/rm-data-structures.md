# Data Structures Information Model

**Issuer**: openEHR Specification Program
**Release**: RM Release-1.1.0
**Status**: STABLE
**Source**: https://specifications.openehr.org/releases/RM/latest/data_structures.html
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## 1. Preface

### 1.1 Purpose

This document describes common data structures used in the openEHR reference model, including lists, tables, trees, and history structures.

### 1.2 Related Documents

Prerequisite: openEHR Architecture Overview

---

## 2. Background

### 2.1 Requirements

Structured data in EHR and related systems requires standard representations for:

- Single values (e.g., weight, height, blood sugar)
- Lists of named/numbered elements (e.g., blood test results)
- Tables with named columns and/or rows (e.g., visual acuity results)
- Tree structures (e.g., biochemistry, microbiology results)
- Histories of values in any of the above forms (e.g., time series of blood pressures, glucose levels)

### 2.2 Design Principles

The design principle emphasizes providing explicit specifications for logical structures using generic representations such as hierarchy. Reasons:

1. **Interoperability**: Ensures all parties encode logical structures identically
2. **Software Implementation**: Developers can create explicit functional interfaces for logical structures
3. **Data Processing**: Receiver software can reliably process incoming information in its intended form

The model removes ambiguity from previous EHR specifications regarding structure and time representation.

---

## 3. Overview

The `rm.data_structures` package contains two sub-packages:

- **item_structure package**: Describes generic, path-addressable data structures
- **history package**: Describes generic linear history for recording past events

### 3.1 Class Descriptions

#### 3.1.1 DATA_STRUCTURE Class

**Class**: `DATA_STRUCTURE` (abstract)
**Description**: Abstract parent class of all data structure types. Includes the `as_hierarchy()` function which generates the equivalent CEN EN13606 single hierarchy for each subtype's physical representation.
**Inheritance**: LOCATABLE

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `as_hierarchy(): ITEM` | Hierarchical equivalent of the physical representation, compatible with CEN EN 13606 structures |

---

## 4. Item Structure Package

### 4.1 Overview

Subtypes of `ITEM_STRUCTURE` explicitly model logical data structure types commonly found in health records:

- **ITEM_SINGLE**: Single values (e.g., patient weight)
- **ITEM_LIST**: Lists (e.g., address parts)
- **ITEM_TREE**: Hierarchically structured data (e.g., microbiology reports)
- **ITEM_TABLE**: Tabular data (e.g., visual acuity, reflex test results)

Data values connect to spatial structures via the `_value_` attribute of the `ELEMENT` class. The `_null_flavour_` attribute indicates how to interpret the `_value_` contents, using openEHR null flavours vocabulary: `253|unknown|`, `271|no information|`, `272|masked|`, `273|not applicable|`.

The optional `_null_reason_` field records specific reasons for lack of data when medico-legal or reporting contexts require it.

### 4.2 ISO 13606 Encoding Rules

#### 4.2.1 ITEM_SINGLE

An `ITEM_SINGLE` object encodes in ISO 13606 as a single `ELEMENT` object.

#### 4.2.2 ITEM_LIST

An `ITEM_LIST` object encodes in ISO 13606 as a `CLUSTER` object containing the set of `ELEMENT` instances from the openEHR list.

#### 4.2.3 ITEM_TABLE

Each row encodes as a `CLUSTER` containing `ELEMENT` instances. Empty/void column values are represented by `ELEMENT` instances with no value and `_null_flavour_` set. `ELEMENT` names in a row are the column names.

#### 4.2.4 ITEM_TREE

`ITEM_TREE` data are replicated as-is to produce the correct ISO 13606 hierarchical form.

### 4.3 Class Descriptions

#### 4.3.1 ITEM_STRUCTURE Class

**Class**: `ITEM_STRUCTURE` (abstract)
**Description**: Abstract parent class of all spatial data types.
**Inheritance**: DATA_STRUCTURE

#### 4.3.2 ITEM_SINGLE Class

**Class**: `ITEM_SINGLE`
**Description**: Logical single value data structure. Represents any data which is logically a single value, such as a person's height or weight.
**Inheritance**: ITEM_STRUCTURE

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 1..1 | `item` | ELEMENT |

#### 4.3.3 ITEM_LIST Class

**Class**: `ITEM_LIST`
**Description**: Logical list data structure where each item has a value and can be referred to by name and positional index. The list may be empty.
**Inheritance**: ITEM_STRUCTURE

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 0..1 | `items` | List<ELEMENT> |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `item_count(): Integer` | Count of all items |
| 0..1 | `names(): List<DV_TEXT>` | Retrieve the names of all items |
| 1..1 | `named_item(a_name: String): ELEMENT` | Retrieve item with name 'a_name' |
| 1..1 | `ith_item(i: Integer): ELEMENT` | Retrieve the i-th item |
| 1..1 | `as_hierarchy(): CLUSTER` | Generate CEN EN13606-compatible hierarchy |

**Invariants**:
- `Valid_structure`: `items.forall (i:ITEM | i.type = "ELEMENT")`

#### 4.3.4 ITEM_TABLE Class

**Class**: `ITEM_TABLE`
**Description**: Logical relational database-style table data structure with named and ordered columns. Implemented using cluster-per-row encoding.
**Inheritance**: ITEM_STRUCTURE

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 0..1 | `rows` | List<CLUSTER> |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `row_count(): Integer` | Number of rows |
| 1..1 | `column_count(): Integer` | Number of columns |
| 0..1 | `row_names(): List<DV_TEXT>` | Return set of row names |
| 0..1 | `column_names(): List<DV_TEXT>` | Return set of column names |
| 1..1 | `ith_row(i: Integer): CLUSTER` | Return i-th row |
| 1..1 | `has_row_with_name(a_key: String): Boolean` | True if row with name exists |
| 1..1 | `has_column_with_name(a_key: String): Boolean` | True if column with name exists |
| 1..1 | `named_row(a_key: String): CLUSTER` | Return row with name |
| 1..1 | `element_at_cell_ij(i: Integer, j: Integer): ELEMENT` | Return cell at location |
| 1..1 | `as_hierarchy(): CLUSTER` | Generate CEN EN13606-compatible hierarchy |

**Invariants**:
- `Valid_structure`: `rows.for_all (items.for_all (instance_of ("ELEMENT")))`

#### 4.3.5 ITEM_TREE Class

**Class**: `ITEM_TREE`
**Description**: Logical tree data structure. Used for representing logically tree-structured data such as audiology results, microbiology results, and biochemistry results.
**Inheritance**: ITEM_STRUCTURE

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 0..1 | `items` | List<ITEM> |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `has_element_path(a_path: String): Boolean` | True if path is a valid leaf path |
| 1..1 | `element_at_path(a_path: String): ELEMENT` | Return leaf element at the path |
| 1..1 | `as_hierarchy(): CLUSTER` | Generate CEN EN13606-compatible hierarchy |

---

## 5. Representation Package

### 5.1 Overview

This package contains classes for simple hierarchical representation of any data structure. Compatible with ISO 13606-1 classes of the same names.

### 5.2 Class Descriptions

#### 5.2.1 ITEM Class

**Class**: `ITEM` (abstract)
**Description**: Abstract parent of `CLUSTER` and `ELEMENT` representation classes.
**Inheritance**: LOCATABLE

#### 5.2.2 CLUSTER Class

**Class**: `CLUSTER`
**Description**: The grouping variant of `ITEM`, which may contain further instances of `ITEM` in an ordered list.
**Inheritance**: ITEM

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 1..1 | `items` | List<ITEM> |

#### 5.2.3 ELEMENT Class

**Class**: `ELEMENT`
**Description**: The leaf variant of `ITEM`, to which a `DATA_VALUE` instance is attached.
**Inheritance**: ITEM

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 0..1 | `null_flavour` | DV_CODED_TEXT |
| 0..1 | `value` | DATA_VALUE |
| 0..1 | `null_reason` | DV_TEXT |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `is_null(): Boolean` | True if value logically not known |

**Invariants**:
- `Inv_is_null_valid`: `is_null() = (value = Void)`
- `Inv_null_flavour_indicated`: `is_null() xor null_flavour = Void`
- `Inv_null_flavour_valid`: `is_null implies terminology(Terminology_id_openehr).has_code_for_group_id(Group_id_null_flavour, null_flavour.defining_code)`
- `Inv_null_reason_valid`: `null_reason /= Void implies is_null()`

---

## 6. History Package

### 6.1 Overview

The `history` package defines classes which formalize past, linear time, enabling historical data of any structural complexity to be recorded. It supports both instantaneous and interval event samples within periodic and aperiodic series.

Generic types: `HISTORY<T: ITEM_STRUCTURE>`, `EVENT<T: ITEM_STRUCTURE>`, `POINT_EVENT<T>`, `INTERVAL_EVENT<T>`.

#### 6.1.1 Basic Semantics

The History model represents time-based data where every sample measures the same phenomenon using the same measurement method.

Two major safeguards:
1. **Generic types** force identical data types at each Event
2. **Archetyping** ensures identical structure for every sample

#### 6.1.2 Timing

`HISTORY._origin_: DV_DATE_TIME` indicates time series '0-point'. `EVENT._time_: DV_DATE_TIME` represents absolute event time. Relative offset computed via `EVENT._offset_()`.

For Interval events, `_time_` refers to the event end time.

History origin time need not be the first sample time (e.g., reference event like childbirth with Apgar scores at offsets).

#### 6.1.3 Point Events

Point events represent instantaneous values via `POINT_EVENT` class instances.

#### 6.1.4 Interval Events

`INTERVAL_EVENT` class instances express values corresponding to time intervals. The `_width_` attribute defines interval duration; the inherited `_time_` value corresponds to the trailing edge.

Mathematical meaning given by `_math_function_` attribute: `145|minimum|`, `144|maximum|`, `146|mean|`, `147|change|`.

#### 6.1.5 Change Data

Sub-category of interval data using three event math function terms:
- **`147|change|`**: Difference between current and previous value (positive or negative)
- **`522|increase|`**: Positive change value
- **`521|decrease|`**: Positive value representing negative change

#### 6.1.6 Summary Event Data

Summary events via optional `HISTORY._summary_` attribute, archetypable separately from main data.

#### 6.1.7 Efficient Representation of Fine-grained Device Data

Interval Events enable efficient representation of long stable data periods as single events. `INTERVAL_EVENT._sample_count_` records original sample numbers.

#### 6.1.8 State

'State' in time-based recording represents information about the whole entity from which recorded values originate. Example: heart rate (primary datum) with exertion level (state).

Two approaches:
1. Separate `HISTORY` structure within `OBSERVATION` class
2. State attribute in the `EVENT` class itself

### 6.2 Class Descriptions

#### 6.2.1 HISTORY Class

**Class**: `HISTORY<T>` where T: ITEM_STRUCTURE
**Description**: Root object of linear history (time series structure).
**Inheritance**: DATA_STRUCTURE

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 1..1 | `origin` | DV_DATE_TIME |
| 0..1 | `period` | DV_DURATION |
| 0..1 | `duration` | DV_DURATION |
| 0..1 | `summary` | ITEM_STRUCTURE |
| 0..1 | `events` | List<EVENT> |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `is_periodic(): Boolean` | Whether history is periodic |

**Invariants**:
- `Events_valid`: `(events /= Void and then not events.is_empty) or summary /= Void`
- `Periodic_validity`: `is_periodic xor period = Void`
- `Period_consistency`: `is_periodic implies events.for_all(e: EVENT | e.offset.to_seconds.mod(period.to_seconds) = 0)`

#### 6.2.2 EVENT Class

**Class**: `EVENT<T>` (abstract) where T: ITEM_STRUCTURE
**Description**: Defines abstract notion of a single series event.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 1..1 | `time` | DV_DATE_TIME |
| 0..1 | `state` | ITEM_STRUCTURE |
| 1..1 | `data` | T |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `offset(): DV_DURATION` | Offset from origin, computed as `time.diff(parent.origin)` |

#### 6.2.3 POINT_EVENT Class

**Class**: `POINT_EVENT<T>`
**Description**: Defines a single point event in a series.
**Inheritance**: EVENT

#### 6.2.4 INTERVAL_EVENT Class

**Class**: `INTERVAL_EVENT<T>`
**Description**: Defines a single interval event in a series.
**Inheritance**: EVENT

**Attributes**:

| Cardinality | Name | Type |
|---|---|---|
| 1..1 | `width` | DV_DURATION |
| 0..1 | `sample_count` | Integer |
| 1..1 | `math_function` | DV_CODED_TEXT |

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `interval_start_time(): DV_DATE_TIME` | Start time of the interval |

**Invariants**:
- `Math_function_validity`: `terminology(Terminology_id_openehr).has_code_for_group_id(Group_id_event_math_function, math_function.defining_code)`
- `Interval_start_time_valid`: `interval_start_time = time - width`
