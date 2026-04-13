# Guideline Definition Language (GDL) Specification

**Status:** RETIRED
**Release:** CDS Release-2.0.1
**Revision:** [latest_issue]
**Date:** [latest_issue_date]
**Keywords:** decision support, GDL, archetype

---

## Table of Contents

1. [Acknowledgements](#acknowledgements)
2. [Preface](#preface)
3. [Overview](#overview)
4. [Design](#design)
5. [Implementation](#implementation)
6. [Amendment Record](#amendment-record)

---

## Acknowledgements

Funding for this work has been provided by:
- Cambio Healthcare Systems, Sweden

### Trademarks

- "openEHR" is a trademark of the openEHR Foundation
- "Java" is a registered trademark of Oracle Corporation
- "Microsoft" and ".Net" are trademarks of the Microsoft Corporation

---

## 1. Preface

### 1.1. Purpose

This specification presents the design of the Guideline Definition Language (GDL), a formal language for expressing decision support logic. GDL remains independent of specific natural languages and reference terminologies by leveraging openEHR Reference Model and Archetype Model designs.

### 1.2. Related Documents

Prerequisite reading includes:
- openEHR Reference Model specifications

### 1.3. Status

This specification carries **RETIRED** status. To Be Determined (TBD) paragraphs indicate areas needing clarification.

### 1.4. Feedback

- **Feedback:** [technical mailing list](https://discourse.openehr.org/c/specifications)
- **Issues:** [specifications Problem Report tracker](https://specifications.openehr.org/components/CDS/open_issues)
- **Changes:** [CDS component Change Request tracker](https://specifications.openehr.org/components/CDS/history)

---

## 2. Overview

### 2.1. Background

Sharing computerized clinical decision support across languages and platforms has faced persistent challenges. Key barriers include insufficient standardized clinical information models and limited terminology resource flexibility across sites.

### 2.2. Scope

GDL expresses clinical logic as production rules. Individual GDL rules contain if-then statements and function as building blocks supporting single and complex decision-making. These rules enable point-of-care decision support and retrospective population analytics.

### 2.3. An Example

Below is a simplified GDL implementation calculating the CHA2DS2-VASc Score for stroke risk stratification in atrial fibrillation:

#### Guide Header
```
(GUIDE) <
    gdl_version = <"0.1">
    id = <"CHA2DS2VASc_Score_calculation.v1-Revised function">
    concept = <"gt0036">
    language = (LANGUAGE) <
        original_language = <[ISO_639-1::en]>
    >
    description = (RESOURCE_DESCRIPTION) <
        details = <
            ["en"] = (RESOURCE_DESCRIPTION_ITEM) <
                copyright = <"">
                keywords = <"Atrial Fibrillation", "Stroke", "CHA2DS2-VASc">
                misuse = <"">
                purpose = <"Calculates stroke risk for patients with atrial fibrillation.">
                use = <"Calculates stroke risk for patients with atrial fibrillation.">
            >
        >
        lifecycle_state = <"Author draft">
        original_author = <
            ["date"] = <"2012/12/03">
            ["email"] = <"rong.chen@cambio.se">
            ["name"] = <"Rong Chen">
            ["organisation"] = <"Cambio Healthcare Systems">
        >
        other_contributors = <"Carlos Valladares",...>
    >
>
```

#### Archetype Binding
```
definition = (GUIDE_DEFINITION) <
    archetype_bindings = <
        [1] = (ARCHETYPE_BINDING) <
            archetype_id = <"openEHR-EHR-EVALUATION.problem-diagnosis.v1">
            domain = <"EHR">
            elements = <
                ["gt0107"] = (ELEMENT_BINDING) <
                    path = <"/data[at0001]/items[at0002.1]">
                >
            >
        >
    >
>
```

#### Pre-conditions
```
definition = (GUIDE_DEFINITION) <
    archetype_bindings = <
        [1] = (ARCHETYPE_BINDING) <
            archetype_id = <"openEHR-EHR-EVALUATION.problem-diagnosis.v1">
            domain = <"EHR">
            elements = <
                ["gt0107"] = (ELEMENT_BINDING) <
                    path = <"/data[at0001]/items[at0002.1]">
                >
            >
            predicates = <"/data[at0001]/items[at0002.1] is_a local::gt0105|Atrial fibrillation|",...>
            template_id = <"diagnosis_chadvas_icd10">
        >
    >
    pre_conditions = <"$gt0107!=null",...>
>
```

#### Rules
```
rules = <
    ["gt0018"] = (RULE) <
        when = <"$gt0108!=null",...>
        then = <"$gt0014=1|local::at0031|Present|",...>
        priority = (11)
    >
    ["gt0019"] = (RULE) <
        when = <"$gt0109!=null",...>
        then = <"$gt0010=1|local::at0034|Present|",...>
        priority = (9)
    >
    ["gt0026"] = (RULE) <
        then = <"$gt0016.magnitude=( ( ( ( ( (gt0009.value+$gt0010.value)+$gt0011.value)+$gt0015.value)+$gt0012.value)+$gt0013.value)+$gt0014.value)",...>
        priority = (1)
    >
>
```

#### Term Definitions
```
term_definitions = <
    ["en"] = (TERM_DEFINITION) <
        terms = <
            ["gt0003"] = (TERM) <
                text = <"Diagnosis">
            >
            ["gt0014"] = (TERM) <
                text = <"Hypertension">
            >
            ["gt0102"] = (TERM) <
                text = <"Diabetes">
            >
            ["gt0105"] = (TERM) <
                text = <"Atrial fibrillation">
            >
            ["gt0018"] = (TERM) <
                text = <"Set hypertension">
            >
            ["gt0019"] = (TERM) <
                text = <"Set diabetes">
            >
            ["gt0026"] = (TERM) <
                text = <"Calculate total score">
            >
        >
    >
>
```

#### Terminology Bindings
```
term_definitions = <
    ["ICD10"] = (TERM_BINDING) <
        bindings = <
            ["gt0105"] = (BINDING) <
                codes = <[ICD10::I48],...>
                uri = <"">
            >
        >
    >
>
```

---

## 3. Design

### 3.1. Requirements

#### 3.1.1. Clinical Information Models

- Clinical logic expression using archetypes as rule input and output
- Support for archetypes based on different reference information models

#### 3.1.2. Natural Language Support

- Meta-data authorship in any natural language
- Rule expressions independent of natural language
- Individual rule naming independent of natural language
- Multiple language translations without logical rule modifications

#### 3.1.3. Reference Terminology Support

- Binding locally-defined terms to single external reference terminology concepts
- Binding locally-defined terms to multiple external reference terminology concepts
- Binding locally-defined terms to external terminology ref-sets

#### 3.1.4. Identification and Meta-data

- Unique rule identification within a given namespace
- Explicit version information in rule identification
- Sufficient authorship, purpose, version, and clinical reference meta-data

#### 3.1.5. Rule Execution

- Chainable execution of multiple CDS rules for complex decision-making
- Rule reusability across different decision support applications and clinical contexts

### 3.2. Guide Object Model

#### 3.2.1. Design Background

openEHR archetypes function as both GDL input and output, enabling natural language and reference terminology independence. This design choice requires substantial reuse of openEHR specifications.

#### 3.2.2. Packages Structure

The Guide Object Model comprises two packages:
1. **Guide Package** - structures for guide definition and archetype binding
2. **Expressions Package** - structures for rule expressions and operations

---

### 3.3. Guide Package

#### 3.3.1. Overview

The guide package contains core classes shown in the following relational model. Blue-colored classes derive loosely from original openEHR specifications.

#### 3.3.2. Class Definitions

##### 3.3.2.1. GUIDE

Main class representing a discrete guide, defining archetype bindings, rules, and meta-information.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | gdl_version | String | GDL version the guide is written in |
| 1..1 | id | String | Guide identification |
| 1..1 | concept | String | Normative guide meaning as local guide code |
| 1..1 | language | Language | Natural language resources (original + translations) |
| 1..1 | description | RESOURCE_DESCRIPTION | Authorship, use/misuse, lifecycle, references |
| 1..1 | definition | GUIDE_DEFINITION | Archetype bindings and rule definitions |
| 1..1 | ontology | GUIDE_ONTOLOGY | Guide ontology |

##### 3.3.2.2. GUIDE_DEFINITION

Encompasses archetype bindings and rule definitions.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | archetype_bindings | List<ARCHETYPE_BINDING> | Archetype-to-variable bindings |
| 1..1 | rules | Map<String, Rule> | Rules indexed by local gt codes |
| 0..1 | pre_conditions | List<EXPRESSION_ITEM> | Pre-execution conditions |

##### 3.3.2.3. ARCHETYPE_BINDING

Binds selected archetype elements to local gt codes.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | archetype_id | String | Source archetype ID |
| 0..1 | template_id | String | Optional template ID for element selection |
| 0..1 | domain | String | Variable space ("EHR" or "CDS") |
| 1..1 | Elements | Map<String, ELEMENT_BINDING> | Element bindings by gt code |
| 0..1 | predicate_statements | List<EXPRESSION_ITEM> | Constraint expressions |

##### 3.3.2.4. ELEMENT_BINDING

Maps specific archetype elements to local variables.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | id | String | Local gt code |
| 1..1 | path | String | Path to archetype element |

##### 3.3.2.5. RULE

Single rule within a guide.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | id | String | Local gt code |
| 1..1 | when_statements | List<EXPRESSION_ITEM> | Firing conditions |
| 1..1 | then_statements | List<ASSIGNMENT_EXPRESSION> | Output expressions |

#### 3.3.3. Syntax Specification

GDL grammar and lexical specification derive entirely from dADL and follow the guide object model.

---

### 3.4. Expressions Package

#### 3.4.1. Overview

The expressions package provides models for rule expressions, operators, and functions.

#### 3.4.2. Class Definitions

##### 3.4.2.1. EXPRESSION_ITEM

Abstract model for rule expressions.

##### 3.4.2.2. UNARY_EXPRESSION

Extends EXPRESSION_ITEM.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | operand | EXPRESSION_ITEM | Unary expression operand |
| 1..1 | operator | OPERATOR_KIND | Unary operator |

##### 3.4.2.3. BINARY_EXPRESSION

Extends EXPRESSION_ITEM.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | left | EXPRESSION_ITEM | Left operand |
| 1..1 | right | EXPRESSION_ITEM | Right operand |
| 1..1 | operator | OPERATOR_KIND | Binary operator |

##### 3.4.2.4. ASSIGNMENT_EXPRESSION

Extends EXPRESSION_ITEM.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | variable | String | Target gt code |
| 1..1 | assignment | EXPRESSION_ITEM | Value expression |

##### 3.4.2.5. FUNCTIONAL_EXPRESSION

Extends EXPRESSION_ITEM.

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | function | Kind | Function type |
| 1..1 | items | List<EXPRESSION_ITEM> | Function parameters |

##### 3.4.2.6. OPERATOR_KIND

Enumeration of operators:

**Arithmetic Operators**

| Operator | Symbol |
|---|---|
| Addition | + |
| Subtraction | - |
| Multiplication | * |
| Division | / |
| Exponent | ^ |

**Logical Operators**

| Operator | Symbol |
|---|---|
| And | && |
| Or | \|\| |
| Not | ! |

**Relational Operators**

| Operator | Symbol |
|---|---|
| Equal | == |
| Unequal | != |
| Less than | < |
| Less than or equal | <= |
| Greater than | > |
| Greater than or equal | >= |

**Assignment Operator**

| Operator | Symbol |
|---|---|
| Assignment | = |

**Terminological Reasoning Operators**

| Operator | Symbol |
|---|---|
| Is a | is_a |
| Is not a | !is_a |

#### Function Kinds

| Function | Description |
|---|---|
| abs | Absolute value of a double |
| ceil | Smallest double ≥ argument (integer equivalent) |
| exp | Euler's number e raised to power |
| floor | Largest double ≤ argument (integer equivalent) |
| log | Natural logarithm (base e) |
| log10 | Base 10 logarithm |
| log1p | Natural logarithm of (argument + 1) |
| round | Closest long value |
| sqrt | Positive square root |
| max | Maximum element value |
| min | Minimum element value |

#### 3.4.3. Syntax Specification

GDL expression grammar derives loosely from ADL assertion syntax. This grammar is implemented via JavaCC specifications. The complete Java GDL parser source code is provided in the grammar section.

---

## 4. Implementation

### 4.1. Drools

GDL remains technology-agnostic and supports multiple rule engine implementations. JBoss Drools (open source) provides the primary execution engine, translating GDL to Drools Rule Language (DRL).

**Implementation Considerations:**

- Each GDL rule generates a new DRL rule
- Rule titles combine guide ID and GT code
- Rule priority maps to DRL salience
- All rules employ no-loop attribute
- Current time uses DvDateTime class
- Pre-execution element validation required
- Element modification propagates via modify method
- General definition elements declared within rule scope
- Pre-conditions duplicated across applicable rules

### 4.2. GDL Editor

An open-source authoring tool enables GDL guideline creation, editing, and execution. This multiplatform desktop application generates archetype-based forms for user input and rule triggering.

**Resources:**
- GitHub: [https://github.com/openEHR/gdl-tools](https://github.com/openEHR/gdl-tools)
- Downloads: [http://sourceforge.net/projects/gdl-editor](http://sourceforge.net/projects/gdl-editor)

### 4.3. Appendix A: Grammar

```java
/**
 * Expression parser
 *
 * @author rong.chen
 */
options
{
  JDK_VERSION = "1.5";
  LOOKAHEAD= 1;
  DEBUG_PARSER = false;
  DEBUG_TOKEN_MANAGER = false;
  DEBUG_LOOKAHEAD = false;
  UNICODE_INPUT = true;
  static = false;
}

PARSER_BEGIN(ExpressionParser)
package se.cambio.cds.gdl.parser;
import java.io.*;
import java.util.*;
import se.cambio.cds.gdl.model.expression.*;
import org.openehr.rm.datatypes.text.CodePhrase;
import org.openehr.rm.datatypes.quantity.*;
import org.openehr.rm.datatypes.basic.DataValue;

public class ExpressionParser
{
  private static final String CHARSET = "UTF-8";

  /* Public interface */
  public List < ExpressionItem > parseBooleanExpressions()
    throws ParseException
  {
    return expressions();
  }

  public List < ExpressionItem > parseArithmeticExpressions()
    throws ParseException
  {
    return expressions();
  }

  public ExpressionItem parse() throws ParseException
  {
    return expression_item();
  }

  public void reInit(File file) throws IOException
  {
    ReInit(new FileInputStream(file), CHARSET);
  }

  public void reInit(InputStream input) throws IOException
  {
    ReInit(new BufferedInputStream(input));
  }

  public static void main(String args []) throws ParseException
  {}
}

PARSER_END(ExpressionParser)

/* WHITE SPACE */
SKIP : { " " | "\t" | "\n" | "\r" | "\f" }

/* COMMENTS */
SPECIAL_TOKEN :
{
  < SINGLE_LINE_COMMENT : "--" (~[ "\n", "\r" ])* >
}

/* SYMBOLS - COMMON */
TOKEN :
{
  < SYM_MINUS : "-" >
| < SYM_PLUS : "+" >
| < SYM_STAR : "*" >
| < SYM_SLASH : "/" >
| < SYM_CARET : "^" >
| < SYM_DOT : "." >
| < SYM_SEMICOLON : ";" >
| < SYM_COMMA : "," >
| < SYM_TWO_COLONS : "::" >
| < SYM_COLON : ":" >
| < SYM_EXCLAMATION : "!" >
| < SYM_L_PARENTHESIS : "(" >
| < SYM_R_PARENTHESIS : ")" >
| < SYM_DOLLAR : "$" >
| < SYM_QUESTION : "?" >
| < SYM_L_BRACKET : "[" >
| < SYM_R_BRACKET : "]" >
| < SYM_INTERVAL_DELIM : "|" >
| < SYM_EQ : "==" >
| < SYM_GE : ">=" >
| < SYM_LE : "<=" >
| < SYM_LT : "<" >
| < SYM_GT : ">" >
| < SYM_NE : "!=" >
| < SYM_NOT : "not" >
| < SYM_AND : "and" | "&&" >
| < SYM_OR : "or" | "||" >
| < SYM_FALSE : "false" >
| < SYM_TRUE : "true" >
| < SYM_NULL : "null" >
| < SYM_IS_A : "is_a" >
| < SYM_IS_NOT_A : "!is_a" >
| < SYM_FOR_ALL : "for_all" >
| < SYM_MAX : "max" >
| < SYM_MIN : "min" >
| < SYM_CURRENT_DATETIME : "currentDateTime" >
| < SYM_ASSIGNMENT : "=" >
| < SYM_MODULO : "\\" >
| < SYM_DIV : "//" >
| < SYM_ELLIPSIS : ".." >
| < SYM_LIST_CONTINUE : "..." >
}

/* VALUE TOKENS */
TOKEN :
{
  < #V_LOCAL_CODE_CORE : "g" [ "c", "t" ] ([ "0"-"9", "." ])+ [ "0"-"9" ] >
| < V_LOCAL_CODE : < V_LOCAL_CODE_CORE > >
| < V_QUANTITY : (< V_REAL > | < V_INTEGER >) ","
    ([ "a"-"z", "A"-"Z", "µ", "°", "%", "*", "0"-"9", "[", "]", "/" ])+ >
| < V_PROPORTION : (< V_REAL > | < V_INTEGER >) ","
    (< V_REAL > | < V_INTEGER >) "," (["0"-"4"]) >
| < V_INTEGER : (< DIG >)+ | "(-" (< DIG >)+ ")"
    | (< DIG >){1, 3}("," (< DIG >){3})+ >
| < V_ISO8601_DURATION: ("-")? "P"((<DIG>)+["y","Y"])? ... >
| < V_DATE: (["0"-"9"]){4} "-" ... >
| < V_TIME: <HOUR_MINUTE> <SECOND> >
| < V_DATE_TIME: "("<DATE_TIME> ")" >
| < V_CODE_PHRASE : "[" (< LET_DIG_DUDSLR >)+ "::" (< LET_DIG_DUDS >)+ "]" >
| < V_CODE_PHRASE_RAW : (< LET_DIG_DUDSLR >)+ "::" (< LET_DIG_DUDS >)+ >
| < V_ORDINAL : < V_INTEGER > "|" < V_CODE_PHRASE_RAW > < V_LABEL > >
| < V_ATTRIBUTE_IDENTIFIER : [ "a"-"z" ] (< LET_DIG_U >)* >
| < V_LABEL : "|" (~[ "|" ])* "|" >
| < V_REAL : ... >
| < V_STRING : "'" ... "'" >
}

/* LOCAL TOKENS */
TOKEN :
{
  < #DIG : [ "0"-"9" ] >
| < #LET_DIG : [ "a"-"z", "A"-"Z", "0"-"9" ] >
| < V_ABSOLUTE_PATH : < SYM_SLASH > < PATH_SEGMENT >
    (< SYM_SLASH > < PATH_SEGMENT >)* >
}

/* PARSING RULES */
List < ExpressionItem > expressions() :
{ ... }

ExpressionItem expression_item() :
{ ... }

ExpressionItem expression_node() :
{ ... }

ExpressionItem expression_leaf() :
{ ... }

Variable variable() :
{ ... }

ConstantExpression constant_expression() :
{ ... }
```

---

## 5. Amendment Record

| Issue | Details | Raiser | Completed |
|---|---|---|---|
| CDS Release 2.0.1 | |
| 2.0.1 | [SPECCDS-6](https://specifications.openehr.org/tickets/SPECCDS-6): Retire GDL v1 specifications | SEC | 31 Jul 2024 |
| CDS Release 2.0.0 | |
| 2.0.0 | [SPECCDS-2](https://specifications.openehr.org/tickets/SPECCDS-2): Add GDL and GDL2 specifications to CDS release | SEC | 20 May 2019 |
| 1.0.0 | Initial Writing | Rong Chen, Iago Corbal | 29 July 2015 |

---

**Copyright © 2013 - 2024 The openEHR Foundation**

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
[https://creativecommons.org/licenses/by-nd/3.0/](https://creativecommons.org/licenses/by-nd/3.0/)

**Support:**
- Issues: [Problem Reports](https://specifications.openehr.org/components/CDS/open_issues)
- Web: [specifications.openEHR.org](https://specifications.openehr.org)

---

*Last updated 2024-07-31 09:56:12 UTC*
