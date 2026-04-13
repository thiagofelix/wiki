# openEHR Platform Conformance Test Schedule

## Document Overview

This specification defines conformance testing procedures for openEHR platform products. The document outlines methodologies for assessing API conformance and data validation compliance with published openEHR specifications.

## Key Document Information

- **Status**: Development
- **Release**: CNF development
- **Issuer**: openEHR Specification Program
- **License**: Creative Commons Attribution-NoDerivs 3.0 Unported

## Scope and Testing Aspects

The conformance assessment framework evaluates two primary dimensions:

### 1. API Conformance Testing
Tests verify that implemented APIs conform to published specifications using regression testing with reference result comparisons.

### 2. Data Validation Conformance Testing
Tests verify the platform correctly validates data against semantic models (archetypes, templates).

## Test Case Documentation Structure

Each test case follows a standardized format:
- **Description**: Purpose of the test
- **Pre-conditions**: Required system state before execution
- **Post-conditions**: Expected system state after execution
- **Flow**: Step-by-step test execution procedures

## Test Suites Covered

### Definition Service (Section 4)
Tests for Operational Templates (OPT) 1.4/2 management:
- Template validation
- Template upload/retrieval
- Version management
- Template deletion

Operations tested:
- `I_DEFINITION_ADL14.validate_opt()`
- `I_DEFINITION_ADL14.upload_opt()`
- `I_DEFINITION_ADL14.get_opt()`
- `I_DEFINITION_ADL14.get_opts()`
- `I_DEFINITION_ADL14.delete_opt()`

### EHR Service (Section 6)
Tests for Electronic Health Record management:
- EHR creation and retrieval
- EHR status management
- Composition operations
- Contribution tracking
- Directory/folder management
- Demographic data management

Key operations:
- `I_EHR_SERVICE.has_ehr()`
- `I_EHR_SERVICE.create_ehr()`
- `I_EHR_SERVICE.get_ehr()`
- `I_EHR_STATUS` operations
- `I_EHR_COMPOSITION` operations
- `I_EHR_CONTRIBUTION` operations
- `I_EHR_DIRECTORY` operations

### Additional Services
- **Query Service** (Section 11): AQL query execution
- **Demographic Service** (Section 10): Party management
- **Admin Service** (Section 12): System administration
- **Message Service** (Section 13): EHR extract/export operations

## Data Validation Test Cases (Section 14)

Comprehensive testing of data type validation including:

**Structural Elements**:
- Composition constraints
- Observation structure
- History/event structures
- Item structures (tree, list, table, single)

**Data Types - Basic Package**:
- DV_BOOLEAN
- DV_IDENTIFIER
- DV_STATE

**Data Types - Text Package**:
- DV_TEXT
- DV_CODED_TEXT
- DV_PARAGRAPH

**Data Types - Quantity Package**:
- DV_ORDINAL
- DV_SCALE
- DV_COUNT
- DV_QUANTITY
- DV_PROPORTION
- DV_INTERVAL variants

**Data Types - Date/Time Package**:
- DV_DURATION
- DV_TIME
- DV_DATE
- DV_DATE_TIME

**Data Types - Encapsulated Package**:
- DV_PARSABLE
- DV_MULTIMEDIA

**Data Types - URI Package**:
- DV_URI
- DV_EHR_URI

## Test Environment Requirements

Systems under test should support:
- OPT 1.4 format (minimum); OPT 2 optional
- XML representation of compositions
- Full OPT lifecycle management
- Template versioning
- Data validation against archetypes

## Implementation Notes

Key considerations for test implementation:

1. **Pre/Post-condition Execution**: Tests run completely for each data set, with conditions re-established between iterations
2. **Version Management**: Systems may implement versioning through version parameters, OPT metadata, or template ID encoding
3. **OPT Deletion**: Only permitted when no associated data exists or newer revisions are available
4. **EHR Status Defaults**: Systems should assign `is_modifiable=true`, `is_queryable=true`, and `subject=PARTY_SELF` by default
5. **Validation Results**: Services should return error details when validation fails

## Related Normative References

- openEHR Platform Service Model
- ADL 1.4 and 2 specifications
- AOM 1.4 and 2 specifications
- EHR Information Model
- Common and Support Information Models
- AQL specification
- OpenEHR REST API specifications

## Amendment and Feedback

Issues and feedback are managed through:
- openEHR Conformance forum (Discourse)
- Specifications Problem Report tracker
- Component Change Request tracker

---

**Note**: This document is under development. Sections marked "TBD" (To Be Determined) indicate incomplete specifications requiring future definition.

**Source URL**: https://specifications.openehr.org/releases/CNF/development/platform_test_schedule.html (original requested URL https://specifications.openehr.org/releases/CNF/latest/platform_conformance.html returned 404)
