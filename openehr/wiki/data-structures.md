---
title: Data Structures
type: entity
sources:
  - raw/rm-data-structures.md
created: 2026-04-13
updated: 2026-04-13
---

# Data Structures Information Model

The Data Structures package defines generic, path-addressable data structures for clinical content and time-series history.

**Release**: RM 1.1.0 (STABLE)

## Sub-packages

- **item_structure** — spatial data structures (single, list, table, tree)
- **history** — temporal data structures (time series)

## Item Structure Package

All subtypes of `ITEM_STRUCTURE` (abstract, inherits DATA_STRUCTURE → LOCATABLE).

### ITEM_SINGLE

Single value. Used for atomic measurements like weight or height.

```
ITEM_SINGLE
  └── item: ELEMENT (exactly one)
```

### ITEM_LIST

Named list of elements. Used for address parts, lab result panels.

```
ITEM_LIST
  └── items: List<ELEMENT> (0..*)
```

Functions: `item_count()`, `names()`, `named_item(name)`, `ith_item(i)`

### ITEM_TABLE

Tabular data with named columns. Used for visual acuity, reflex tests.

```
ITEM_TABLE
  └── rows: List<CLUSTER> (each row is a CLUSTER of ELEMENTs)
```

Each ELEMENT in a row takes its column name. Empty cells have no value with `null_flavour` set.

Functions: `row_count()`, `column_count()`, `row_names()`, `column_names()`, `element_at_cell_ij(i,j)`

### ITEM_TREE

Hierarchical data. The most general structure — used for microbiology results, biochemistry, complex forms.

```
ITEM_TREE
  └── items: List<ITEM> (ELEMENT or CLUSTER, nested arbitrarily)
```

Functions: `has_element_path(path)`, `element_at_path(path)`

## Representation Classes

### ELEMENT

Leaf node containing a data value:
- `value` — a DATA_VALUE (any DV_* type)
- `null_flavour` — why value is absent: `unknown` (253), `no information` (271), `masked` (272), `not applicable` (273)
- `null_reason` — specific reason for absence (medico-legal contexts)

### CLUSTER

Grouping node containing ELEMENTs or nested CLUSTERs:
- `items` — List\<ITEM\> (mix of ELEMENT and CLUSTER)

## History Package

Time-series data for recording observations over time.

### HISTORY

Container for temporal data:
- `origin` — time origin (DV_DATE_TIME)
- `period` — sampling period for regular series (DV_DURATION, optional)
- `duration` — total duration (DV_DURATION, optional)
- `events` — List\<EVENT\> (the actual observations)
- `summary` — optional ITEM_STRUCTURE summarizing the series

### EVENT (abstract)

Base class for temporal observations:
- `time` — when the observation occurred (DV_DATE_TIME)
- `data` — the observed data (ITEM_STRUCTURE)
- `state` — patient state during observation (ITEM_STRUCTURE, optional)

### POINT_EVENT

An instantaneous observation at a single time point.

### INTERVAL_EVENT

An observation over a time interval:
- `width` — duration of the interval (DV_DURATION)
- `math_function` — how the value relates to the interval: `mean`, `minimum`, `maximum`, `total`, `actual`, `mode`, `median`, `change`, `increase`, `decrease`
- `sample_count` — number of samples in the interval (optional)

**Example**: "Mean blood pressure over 24 hours" is an INTERVAL_EVENT with width=P1D and math_function=mean.

## ISO 13606 Compatibility

Each ITEM_STRUCTURE subtype has an `as_hierarchy()` function generating CEN EN 13606-compatible hierarchical form:
- ITEM_SINGLE → single ELEMENT
- ITEM_LIST → CLUSTER containing ELEMENTs
- ITEM_TABLE → CLUSTER containing row CLUSTERs
- ITEM_TREE → direct hierarchy (already compatible)
