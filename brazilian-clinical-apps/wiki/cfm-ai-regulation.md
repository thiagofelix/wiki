---
title: CFM AI Regulation (Resolution 2.454/2026)
type: concept
sources:
  - raw/sources/jdsupra-com-legalnews-brazilian-cfm-issues-resolution-on-the-6731720.md
  - raw/sources/machadomeyer-com-br-pt-inteligencia-juridica-publicacoes-ij-life-sciences-e-saude-cfm-regulamenta-o-uso-de-int-ff72649d.md
  - raw/sources/medicinasa-com-br-eval-ia-corporativa.md
created: 2026-04-12
updated: 2026-04-12
---

## Overview

CFM Resolution 2.454/2026 was published on February 27, 2026, making it the first comprehensive regulation of artificial intelligence in Brazilian medicine. The resolution establishes governance, liability, and technical standards for AI use across healthcare institutions and clinical practice.

Compliance deadline: **August 10, 2026** (180 days from publication).

Core principle (verbatim): *"em nenhum momento os modelos, sistemas e aplicações de IA na medicina poderão restringir ou substituir a autoridade final do médico."* No AI model, system, or application in medicine may at any point restrict or replace the physician's final authority.

---

## Risk Classification

The resolution establishes four risk tiers for medical AI systems:

| Risk Level | Definition | Examples |
|---|---|---|
| **Low** | AI providing information or suggestions that do not directly influence clinical decisions | Administrative AI, scheduling tools |
| **Medium** | AI directly involved in clinical decision support; mandatory physician review required | Clinical decision support systems |
| **High** | AI making diagnostic, prognostic, or therapeutic recommendations with significant patient impact | Diagnostic imaging AI, treatment recommendation engines |
| **Unacceptable** | Mentioned in the resolution but not formally defined | — |

---

## Governance Requirements

Healthcare institutions deploying AI must establish a **Comissão de IA e Telemedicina** (AI and Telemedicine Commission) that:

- Is under **medical coordination** (not IT or administrative leadership)
- Is formally **subordinate to the institution's diretoria técnica** (technical directorship)

Additional institutional obligations:

- **Interoperability**: Institutions must prioritize interoperable AI systems over closed proprietary platforms.
- **Bias monitoring**: Continuous monitoring is required — a one-time validation at deployment is insufficient.
- **Audit logs**: Full logs of AI prompts and responses must be maintained.
- **External audit access**: CRM (Regional Medical Council) and CFM (Federal Medical Council) must be granted access to audit AI systems.

---

## Liability Rules

The resolution creates an explicit liability framework that departs from default Brazilian law on technology use:

- **Physician liability is excluded** for failures that are exclusively attributable to the AI system, provided the physician can demonstrate diligent use.
- **Institutions cannot penalize** physicians who decline to follow AI recommendations.
- **Contract clauses** that subordinate a physician's clinical conduct to AI outputs are **void and unenforceable**.

---

## Prohibited Acts

- AI systems **cannot communicate** diagnoses, prognoses, or therapeutic decisions **directly to patients**. All clinical communication to patients must pass through a physician.
- **"Shadow AI"** — the informal or personal use of AI tools (e.g., consumer LLMs) in clinical settings outside institutional governance — carries **catastrophic institutional liability risk**. Institutions are responsible for AI use occurring within their walls, even if unsanctioned.

---

## Technical Recommendations

- **RAG (Retrieval-Augmented Generation)** architecture is explicitly recommended for clinical AI applications, as it grounds model outputs in controlled, auditable knowledge bases rather than relying solely on parametric model knowledge.
- **Privacy by design** is adopted as a governing principle for AI system architecture.

See also [[lgpd-health-data]] for data protection requirements that apply in tandem with this resolution.

---

## Legislative Context

CFM Resolution 2.454/2026 is a regulatory act by the medical profession's self-governing body, not a federal statute. However, it sits within a broader legislative trajectory:

- **PL 2.338/2023** (the pending Brazilian AI Law, currently in the Senate) uses the same Low / Medium / High risk classification structure. The alignment between the resolution and the draft law suggests these tiers are likely to be codified into federal statute, creating continuity for institutions that comply now.
- **INAEP** (Instância Nacional de Ética em Pesquisa) has been designated as the governing body responsible for AI research ethics oversight under this framework.

---

## Implications for Software Vendors

Clinical AI software vendors operating in Brazil face concrete compliance requirements stemming from this resolution:

- **Audit log APIs**: Products must expose structured logs of prompts and AI responses that can be surfaced for CRM/CFM audits.
- **Risk tier documentation**: Vendors should formally classify their products under the Low/Medium/High framework and document that classification for institutional customers.
- **No direct-to-patient outputs**: Any product that surfaces AI-generated clinical content must route it through a physician workflow, not directly to a patient-facing interface.
- **Interoperability posture**: Closed, proprietary integrations face institutional headwinds — vendors should invest in open, interoperable APIs.
- **Contractual exposure**: Vendor contracts that include language requiring customers to follow AI outputs may be challenged as void under the liability provisions.
- **Governance collateral**: Institutions will need vendor support (documentation, data sheets, validation evidence) to stand up their Comissão de IA e Telemedicina. Vendors who provide this proactively will have a competitive advantage.

---

## Cross-references

- [[telemedicine-regulation]] — CFM rules on telemedicine, which the AI commission is jointly responsible for
- [[lgpd-health-data]] — LGPD data protection obligations that apply to AI audit logs and patient data processed by AI systems
