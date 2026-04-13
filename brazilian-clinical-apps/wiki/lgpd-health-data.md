---
title: LGPD — Health Data Protection
type: concept
sources:
  - raw/market-landscape-research.md
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
| **DPO appointment** | Must appoint a Data Protection Officer (*Encarregado*) |
| **Data subject rights** | 15-day response window for access, correction, and deletion requests |
| **Breach notification** | Report serious breaches to ANPD within **3 business days** |
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

Brazil led global data breach rankings in 2023, intensifying ANPD's focus on the health sector ([Pixeon Blog](https://www.pixeon.com/blog/lgpd-na-saude/)).

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

---

## LGPD vs GDPR — Key Differences Relevant to Health Software

| | LGPD (Brazil) | GDPR (EU) |
|---|---|---|
| DPO requirement | Required for all controllers | Required for certain controllers |
| Breach notification | 3 business days | 72 hours |
| Legal basis for health data | Article 11 restricted list | Article 9 special categories |
| Extraterritorial scope | Yes (processes data of persons in Brazil or data collected in Brazil) | Yes |
| Fines | 2% revenue / R$50M cap per infraction | 4% global turnover / €20M (whichever higher) |

---

## Summary: Regulatory Checklist for Clinical Software

| Area | Action Required |
|---|---|
| Legal basis | Document the legal basis for every category of health data processing |
| Consent flows | Implement granular, timestamped, revocable consent capture |
| DPO | Appoint and register a Data Protection Officer |
| Data subject rights | Build 15-day response workflow for access/correction/deletion |
| Breach response | Implement ANPD 3-day breach notification protocol |
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
