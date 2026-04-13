---
title: LGPD — Health Data Protection
type: concept
sources:
  - raw/market-landscape-research.md
  - raw/sources/ibanet-org-protections-health-data-brazilds.md
  - raw/sources/secureprivacy-ai-blog-lgpd-compliance-requirements.md
  - raw/sources/lgpd-brasil-info-capitulo_02-artigo_11.md
  - raw/sources/portaltelemedicina-com-br-lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes.md
  - raw/sources/gov-br-saude-pt-br-acesso-a-informacao-lgpd.md
  - raw/sources/pixeon-com-blog-lgpd-na-saude.md
created: 2026-04-12
updated: 2026-04-12
---

The **Lei Geral de Proteção de Dados Pessoais (LGPD)** — Law 13.709/2018 — is Brazil's comprehensive personal data protection law, modeled partly on the EU's GDPR. For clinical software, health data triggers the law's most stringent rules: it is classified as **sensitive personal data** (*dados pessoais sensíveis*), activating a restricted set of legal bases and stricter operational obligations.

**Governing instrument:** Law 13.709/2018  
**Enforcement authority:** ANPD (Autoridade Nacional de Proteção de Dados)  
**Effective date:** August 2020 (penalties enforceable from August 2021)

---

## Classification of Health Data

Health data is classified as **dados pessoais sensíveis** under LGPD Articles 5(XII) and 11. This triggers stricter processing rules than apply to ordinary personal data ([LGPD Brasil Info](https://lgpd-brasil.info/capitulo_02/artigo_11)).

The sensitive data classification covers: data on racial or ethnic origin, religious belief, political opinion, trade union membership, health or sexual life, genetic or biometric data.

LGPD establishes **10 principles** in Article 6 governing all processing (compared to GDPR's 6 principles), and provides data subjects with **9 enumerated rights** (vs. GDPR's 8): confirmation of processing, access, correction, anonymization/blocking/deletion, portability, sharing information, consent revocation, review of automated decisions, and complaint to ANPD ([SecurePrivacy](https://secureprivacy.ai/blog/lgpd-compliance-requirements)).

### Medical Record vs. Health Data Distinction

**Medical records (prontuário)** are governed by a separate legal layer: CFM Resolution 1.638/2002 and the Code of Medical Ethics (CME Arts. 73, 85, 87, 89 — professional secrecy). Under CFM Opinion 05/2020, the prontuário belongs to the **patient**, not to the institution. Non-record health data (e.g., aggregated statistics, administrative data) can rely on any Article 11 basis. These two regimes operate in parallel and must both be satisfied when clinical record data is processed ([IBANet](https://ibanet.org/protections-health-data-brazil)).

Health plan auditors may access medical records only through a **medical auditor** bound by professional secrecy. Generic contractual authorizations for record sharing are **void** (CRM-SC Opinion 2418/16) ([IBANet](https://ibanet.org/protections-health-data-brazil)).

---

## Legal Bases for Processing Health Data (Article 11)

Processing of sensitive health data is permitted **only** for specific purposes. The permitted legal bases are:

1. **Explicit consent** of the data subject
2. Performance of a **legal or regulatory obligation** by the controller
3. **Shared processing by public bodies** for legally mandated public policies
4. **Studies by research bodies**, with anonymization wherever possible
5. **Protection of life or physical safety** of the data subject or a third party
6. **Health protection** — exclusively by health professionals, health services, or sanitary authorities
7. **Prevention of fraud** and security of the data subject

**Critical restriction:** Health insurers (*operadoras de planos privados*) are **explicitly prohibited** from using health data for risk selection in contracting or exclusion of beneficiaries (Article 11, §5) ([LGPD Brasil Info](https://lgpd-brasil.info/capitulo_02/artigo_11)).

### Article 11 Layered Structure

Article 11 contains several additional paragraphs with practical significance:

- **§3**: Shared processing of health data for **economic advantage** is subject to ANPD regulation — it is not freely permitted.
- **§4**: Health service providers **may** share data among themselves, but **exclusively** for a specific, ongoing care episode. This sharing is limited in scope and purpose.
- **§5**: Insurer prohibition (see above).

The **"health protection" legal basis** (basis 6 above) is narrow: it applies only to procedures performed by health professionals, health services, or sanitary authorities. **Insurers and employers cannot invoke this basis** ([LGPD Brasil Info](https://lgpd-brasil.info/capitulo_02/artigo_11), [IBANet](https://ibanet.org/protections-health-data-brazil)).

---

## How LGPD Health Data Differs from General LGPD

| Dimension | General Personal Data | Sensitive Health Data |
|---|---|---|
| Legal bases | 10 legal bases available | ~7 restricted bases; narrower |
| Consent requirement | Can rely on legitimate interest | Explicit consent required (or specific health exceptions) |
| Insurer restriction | Not applicable | Explicitly cannot be used for risk selection / exclusion |
| Cross-controller sharing | Allowed with legal basis | Cannot be shared between controllers for **economic advantage**, except for healthcare delivery, pharmacy, and financial/administrative transactions arising from that care |
| Penalties for breach | Up to 2% revenue / R$50M cap | Same penalties; enforcement priority given to health sector breaches |

---

## Key Compliance Requirements for Clinical Software

| Requirement | Detail |
|---|---|
| **Data mapping** | Catalog all personal data flows — including paper records and WhatsApp communications |
| **Legal basis documentation** | Each processing activity must have a documented legal basis |
| **Consent management** | Granular, explicit, revocable consent; timestamp logs required |
| **DPO appointment** | Must appoint a Data Protection Officer (*Encarregado*); small-scale agents (revenue ≤ R$4.8M) are exempt unless high-risk processing — health data likely qualifies as high-risk |
| **Data subject rights** | 15-day response window for detailed data access requests; small-scale agents get 30 days |
| **Breach notification** | Report serious breaches to ANPD within **3 business days**; operationalized by ANPD Resolution CD/ANPD No. 15 (April 2024) |
| **Incident registry** | All security incidents must be recorded for **5 years**, including non-notifiable incidents |
| **Encryption** | All patient data storage and transmission must be encrypted |
| **Cross-controller sharing restriction** | Health data cannot be shared between controllers for economic advantage (see above) |
| **Retention** | Medical records retained ≥20 years (physical) or permanently (digital) per CFM Resolution 1.821/2007 |
| **Third-party processor contracts** | Written data processing agreements with all vendors; controllers share liability for processor failures |
| **DPIA** | Data Protection Impact Assessments recommended (not explicitly mandated) for high-risk processing |

([Portal Telemedicina](https://portaltelemedicina.com.br/lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes), [LGPD Brasil Info](https://lgpd-brasil.info/capitulo_02/artigo_11))

---

## Penalties

| Sanction | Detail |
|---|---|
| **Administrative fine** | Up to **2% of Brazilian revenue, capped at R$50 million per infraction** |
| **Suspension** | Suspension of data processing operations |
| **Public disclosure** | Public naming of the violating organization |

([Portal Telemedicina](https://portaltelemedicina.com.br/lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes), [LGPD Compliance Guide via SecurePrivacy](https://secureprivacy.ai/blog/lgpd-compliance-requirements))

Brazil led global data breach rankings in 2023, intensifying ANPD's focus on the health sector ([Pixeon Blog](https://www.pixeon.com/blog/lgpd-na-saude/)). The **health sector is consistently among the top 5** for ANPD complaints ([SecurePrivacy](https://secureprivacy.ai/blog/lgpd-compliance-requirements)).

### Notable Enforcement Examples

| Case | Year | Outcome |
|---|---|---|
| Telekall | 2023 | Fine ~R$14,400 |
| IAMSPE | 2023 | Enforcement action |
| Meta | July 2024 | Processing **suspension** order |
| X Corp | December 2024 | **5-day** processing suspension |
| Cumulative fines since 2023 | — | ~R$98M (~US$20M) |

([IBANet](https://ibanet.org/protections-health-data-brazil), [SecurePrivacy](https://secureprivacy.ai/blog/lgpd-compliance-requirements))

### ANPD Enforcement Priorities (2025–2026)

ANPD has signaled focus on: AI and facial recognition, children's data, and data scraping ([SecurePrivacy](https://secureprivacy.ai/blog/lgpd-compliance-requirements)).

---

## Healthcare-Specific Practical Considerations

### WhatsApp and Messaging Apps
WhatsApp is permitted for patient communication if encrypted, but uncontrolled persistent message history remains risky. All communications must satisfy LGPD data subject rights requirements ([Portal Telemedicina](https://portaltelemedicina.com.br/lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes)).

### TISS Billing Data
Billing data sent to insurers via [[tiss]] generally does not require separate patient consent. However, detailed clinical data transmitted in reports (beyond claim-processing needs) may require explicit consent ([Portal Telemedicina](https://portaltelemedicina.com.br/lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes)).

### SBIS Certification as Compliance Evidence
[[sbis-certification]] (Sociedade Brasileira de Informática em Saúde) evaluations are a recognized method to validate software security for health data and demonstrate LGPD compliance to regulators and clients ([Portal Telemedicina](https://portaltelemedicina.com.br/lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes)).

### Telemedicine
Law 14.510/2022 (the Telehealth Act) explicitly affirms LGPD compliance obligations for telehealth services. See [[telemedicine-regulation]] for details.

### ICP-Brasil and Data Integrity
Electronic health records must support Level of Security Assurance 2 (NGS2) under ICP-Brasil (see [[sus-integration]]) or another legally accepted standard per CFM Resolution 2.314/2022.

### Applicable Security Standards

**ISO 27001** (information security management) and **ISO 27799** (health informatics — information security management in health using ISO/IEC 27002) are the primary international standards applicable to health data processing under LGPD. ISO 27799 specifically addresses health sector requirements that go beyond the general ISO 27001 framework ([Pixeon Blog](https://www.pixeon.com/blog/lgpd-na-saude/)).

### Notable Incidents

**2017 Cartão Nacional da Saúde (CNS) breach**: Exposed records for 120M+ Brazilians — the largest known Brazilian health data breach. The CNS database exposure underscored the critical need for access controls and encryption on national health registries ([Pixeon Blog](https://www.pixeon.com/blog/lgpd-na-saude/)).

### Government Health Sector DPO and Rights Portal

The Ministry of Health (Ministério da Saúde) has designated **encarregado@saude.gov.br** as its DPO contact. Citizens can exercise LGPD data subject rights against government health entities through the **Fala.BR** platform ([gov.br/saude](https://www.gov.br/saude/pt-br/acesso-a-informacao/lgpd)).

### Sectoral Self-Regulation

The **CNSaúde Code of Good Data Protection Practices** is a voluntary sectoral code providing sector-specific guidance on LGPD implementation for health organizations. Adherence is voluntary but signals good-faith compliance ([IBANet](https://ibanet.org/protections-health-data-brazil)).

### LGPD and SUS Digital

LGPD compliance is a **prerequisite** for participation in the SUS Digital (*Estratégia de Saúde Digital*) program. Providers connecting to RNDS and related federal health infrastructure must demonstrate LGPD alignment as part of onboarding ([gov.br/saude](https://www.gov.br/saude/pt-br/acesso-a-informacao/lgpd)). See [[sus-integration]].

---

## LGPD vs GDPR — Key Differences Relevant to Health Software

| | LGPD (Brazil) | GDPR (EU) |
|---|---|---|
| DPO requirement | Required for all controllers (small-scale agents ≤ R$4.8M exempt unless high-risk) | Required for certain controllers |
| Breach notification | 3 business days (operationalized by ANPD Resolution CD/ANPD No. 15, April 2024) | 72 hours |
| Legal basis for health data | Article 11 restricted list | Article 9 special categories |
| Data subject rights | 9 rights (includes complaint to ANPD) | 8 rights |
| Processing principles | 10 principles (Article 6) | 6 principles |
| Extraterritorial scope | Yes (processes data of persons in Brazil or data collected in Brazil) | Yes |
| Fines | 2% revenue / R$50M cap per infraction | 4% global turnover / €20M (whichever higher) |
| Incident registry | 5-year retention required for all incidents | Not explicitly mandated at same level |

---

## Summary: Regulatory Checklist for Clinical Software

| Area | Action Required |
|---|---|
| Legal basis | Document the legal basis for every category of health data processing |
| Consent flows | Implement granular, timestamped, revocable consent capture |
| DPO | Appoint and register a Data Protection Officer |
| Data subject rights | Build 15-day response workflow for access/correction/deletion |
| Breach response | Implement ANPD 3-day breach notification protocol (ANPD Resolution CD/ANPD No. 15, April 2024) |
| Incident registry | Maintain 5-year registry of all security incidents, including non-notifiable ones |
| Vendor contracts | Ensure all SaaS/cloud vendors have data processing agreements |
| Encryption | Encrypt data at rest and in transit |
| Retention | Implement 20-year (physical) / permanent (digital) retention per CFM 1.821/2007 |
| Security audit | Pursue [[sbis-certification]] or equivalent audit for credibility |

---

## See Also

- [[tiss]] — TISS billing data intersects with LGPD consent rules
- [[telemedicine-regulation]] — Law 14.510/2022 affirms LGPD for telehealth
- [[sbis-certification]] — SBIS evaluation as recognized LGPD compliance evidence
- [[sus-integration]] — ICP-Brasil and RNDS data exchange security requirements
- [[market-overview]] — Market context for Brazil's healthcare data environment
