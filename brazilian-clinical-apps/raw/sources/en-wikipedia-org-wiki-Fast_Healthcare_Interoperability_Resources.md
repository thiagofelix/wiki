---
source_url: https://en.wikipedia.org/wiki/Fast_Healthcare_Interoperability_Resources
title: "Fast Healthcare Interoperability Resources - Wikipedia"
type: web-page
fetched: 2026-04-12
---

# Fast Healthcare Interoperability Resources - Wikipedia

Source: https://en.wikipedia.org/wiki/Fast_Healthcare_Interoperability_Resources

---

Fast Healthcare Interoperability Resources - Wikipedia

- 

Jump to content

Search

				Search

Donate

- Create account

- Log in

Personal tools

- 

Donate

- 

Create account

- 

Log in

## Fast Healthcare Interoperability Resources

10 languages

- Deutsch
- Français
- עברית
- Bahasa Indonesia
- Italiano
- 日本語
- 한국어
- Română
- Русский
- 中文
			
			Edit links

						From Wikipedia, the free encyclopedia

Standard for exchanging electronic health records

Fast Healthcare Interoperability Resources (FHIR)AbbreviationFHIROrganizationHL7Base standardsJSON, XML, RDFDomainElectronic health recordsLicenseCC0Websitefhir.org

The Fast Healthcare Interoperability Resources (FHIR, /faɪər/, like fire) is a technical standard by HL7 International for health information exchange. It is designed for a wide range of settings and with different health care information systems. The standard describes data formats and elements (known as "resources") and an API for exchanging electronic health records (EHR).

FHIR builds on previous data format standards from HL7, like HL7 version 2.x and HL7 version 3.x.  But it is easier to implement because it uses a modern web-based suite of API technology, including a REST protocol, and a choice of JSON, XML or RDF for data representation.&#91;1&#93; One of its goals is to facilitate interoperability between legacy health care systems, to make it easier to provide health care information to health care providers and individuals on a wide variety of devices from computers to tablets to cell phones, and to allow third-party application developers to provide medical applications which can be easily integrated into existing systems.&#91;2&#93;

FHIR provides an alternative to document-centric approaches by directly exposing discrete data elements as services. For example, basic elements of healthcare like patients, admissions, diagnostic reports and medications can each be retrieved and manipulated via their own resource URLs.

## Standardization
[edit]

Major Milestones in FHIR Standardization

Date
Version
Description

2011-08-18
-
The initial draft of FHIR, then known as Resources For Healthcare (RFH), was published on Grahame Grieve's blog in Australia&#91;3&#93;&#91;4&#93;

2011-09-11
-
The standard was adopted by Health Level Seven International (HL7) as a work item&#91;4&#93;

2014-09-30
0.082
DSTU1 (First Draft Standard for Trial Use) official version published&#91;5&#93;&#91;6&#93;

2015-10-24
1.0.2
DSTU2 (Second Draft Standard for Trial Use) official version published&#91;5&#93;

2019-10-24
3.0.1
STU3 (Third Standard for Trial Use)&#91;5&#93; included coverage of a variety of clinical workflows, a Resource Description Framework format, and a variety of other updates&#91;7&#93;

2019-10-30
4.0.1
Release 4 has the First Normative Content and Trial Use Developments&#91;5&#93;&#91;8&#93;

2023-03-26
5.0.0
Release 5 &#91;5&#93;&#91;9&#93;

## Architecture
[edit]
Depiction of a set of interrelated FHIR resources. Each resource consists of data elements that describe the healthcare concept.

FHIR is organized by resources (e.g., patient, observation).&#91;10&#93; Such resources can be specified further by defining FHIR profiles (for example, binding to a specific terminology). A collection of profiles can be published as an implementation guide (IG), such as The U.S. Core Data for Interoperability (USCDI).&#91;11&#93; The ONC anticipates finalizing USCDI v4 in July 2023.&#91;12&#93;

Because FHIR is implemented on top of HTTPS, FHIR resources can be retrieved and parsed by analytics platforms for real-time data gathering. In this concept, healthcare organizations would be able to gather real-time data from specified resource models. FHIR resources can be streamed to a data store where they can be correlated with other informatics data. Potential use cases include epidemic tracking, prescription drug fraud, adverse drug interaction warnings, and the reduction of emergency room wait times.&#91;13&#93;

## Implementations
[edit]

Globally, a number of high-profile players in the health care informatics field are showing interest in and experimenting with FHIR, including CommonWell Health Alliance and SMART (Substitutable Medical Applications, Reusable Technologies).&#91;14&#93;

Open source implementations of FHIR data structures, servers, clients and tools include reference implementations from HL7 in a variety of languages, SMART on FHIR,&#91;15&#93; HAPI-FHIR in Java, and many others (see reference).&#91;16&#93;

A variety of applications were demonstrated at the FHIR Applications Roundtable in July 2016.&#91;17&#93; The Sync for Science (S4S) profile builds on FHIR to help medical research studies ask for (and if approved by the patient, receive) patient-level electronic health record data.&#91;18&#93;

In January, 2018, Apple announced that its iPhone Health App would allow viewing a user's FHIR-compliant medical records when providers choose to make them available. Johns Hopkins Medicine, Cedars-Sinai, Penn Medicine, NYU-Langone Medical Center, Dignity Health and other large hospital systems participated at launch.&#91;19&#93;

## United States
[edit]

In 2014, the U.S. Health IT Policy and the Health IT Standards committees endorsed recommendations for more public (open) APIs.
The U.S. JASON task force report on "A Robust Health Data Infrastructure" says that FHIR is currently the best candidate API approach, and that such APIs should be part of stage 3 of the "meaningful use" criteria of the U.S. Health Information Technology for Economic and Clinical Health Act.&#91;20&#93;&#91;21&#93;&#91;22&#93;&#91;23&#93;
In December 2014, a broad cross-section of US stakeholders committed to the Argonaut Project&#91;24&#93;
which will provide acceleration funding and political will to publish FHIR implementation guides and profiles for query/response interoperability and document retrieval by May 2015.&#91;25&#93;  It would then be possible for medical records systems to migrate from the current practice of exchanging complex Clinical Document Architecture (CDA) documents, and instead exchange sets of simpler, more modular and interoperable FHIR JSON objects.&#91;26&#93;  The initial goal was to specify two FHIR profiles that are relevant to the Meaningful Use requirements, along with an implementation guide for using OAuth 2.0 for authentication.
&#91;27&#93;

A collaboration agreement with Healthcare Services Platform Consortium (now called Logica) was announced in 2017.&#91;28&#93; Experiences with developing medical applications using FHIR to link to existing electronic health record systems clarified some of the benefits and challenges of the approach, and with getting clinicians to use them.&#91;29&#93;

In 2020, the U.S. Centers for Medicare & Medicaid Services (CMS) issued their Interoperability and Patient Access final rule, (CMS-9115-F), based on the 21st Century Cures Act. The rule requires the use of FHIR by a variety of CMS-regulated payers, including Medicare Advantage organizations, state Medicaid programs, and qualified health plans in the Federally Facilitated Marketplace by 2021.&#91;30&#93; Specifically, the rule requires FHIR APIs for Patient Access, Provider Directory and Payer-to-Payer exchange.

Proposed rules from CMS, such as the patient burden and prior authorization proposed rule (CMS-9123-P),&#91;31&#93; further specify FHIR adoption for payer-to-payer exchange. The CMS rules and Office of the National Coordinator for Health IT (ONC) Cures Act Final rule (HHS-ONC-0955-AA01)&#91;32&#93; work in concert to drive FHIR adoption within their respective regulatory authorities.

Further, other agencies are using existing rule-making authority, not derived from the Cures Act, to harmonize the regulatory landscape and ease FHIR adoption. For example, the U.S. Department of Health and Human Services (HHS) Office of Civil Rights (OCR) has proposed to update the HIPAA privacy rule (HHS–OCR–0945–AA00)&#91;33&#93; with an expanded right of access for personal health apps and disclosures between providers for care coordination. Unlike the CMS and ONC final rules, the OCR HIPAA privacy proposed rule is not specific to FHIR; however, OCR's emphasize on standards-based APIs clearly benefits FHIR adoption.

## Brazil
[edit]

In 2020, Brazil's Ministry of Health, by the IT Department of the SUS, started one of the world's largest platforms for national health interoperability, called the National Health Data Network, which uses HL7 FHIR r4 as a standard in all its information exchanges.&#91;34&#93;

## Israel
[edit]

In 2020, Israel's Ministry of Health began working towards the goal of promoting accessibility of information to patients and caregivers through the adoption of the FHIR standard in health organizations in Israel. Its first act was to create the IL-CORE work team to adapt the necessary components for localization and regulation in the health system in Israel. The ministry, in cooperation with the Nonprofit Organization 8400, created the FHIR IL community, whose purpose is to encourage the adoption of the standard in the Israeli healthcare system while cooperating with healthcare organizations and the industry.&#91;35&#93; As part of a joint activity of the Ministry and 8400, a number of projects were launched for the implementation of FHIR in health management organizations (HMO) and hospitals, alongside other projects that are being independently promoted by healthcare organizations.&#91;36&#93; In addition, the Ministry of Health allocated budgets to the HMOs and other organizations for the purpose of establishing organizational FHIR infrastructure.
In the 2020 Eli Hurvitz Conference on Economy and Society, run by the Israel Democracy Institute it was estimated that the cost of implementing central FHIR modules of in the Israeli healthcare system is estimated at about 400 million NIS over 5 years.&#91;37&#93; In 2023, the Israeli government began a legislative process to promote the sharing of information between organizations in the Israeli health ecosystem for the benefit of the patient, with an emphasis on patient empowerment and reduced information blocking.&#91;38&#93; The proposed legislation also refers to the need to standardize the data by adopting the FHIR standard and utilizing standard terminologies, such as SNOMED-CT, both in source systems and in the data exchange process. The sharing of information will be with the patient's consent, and this consent will be given according to data buckets.&#91;39&#93;

## References
[edit]

- ^ "Welcome to FHIR". HL7.org. 1 November 2019. Retrieved 12 February 2021.

- ^ Kryszyn, Jacek; Smolik, Waldemar T.; Wanta, Damian; Midura, Mateusz; Wróblewski, Przemysław (2023). "Comparison of OpenEHR and HL7 FHIR Standards". International Journal of Electronics and Telecommunications. 69 (1): 47–52. doi:10.24425/ijet.2023.144330. Retrieved 8 January 2024.

- ^ Grahame Grieve (18 August 2011). "Resources For Health: A Fresh Look Proposal". Health Intersections. Archived from the original on 3 March 2023. Retrieved 22 August 2019.

- ^ a b René Spronk (11 August 2016). "Five years of FHIR". Ringholm. Retrieved 22 August 2019.

- ^ a b c d e "All Published Versions of FHIR". hl7.org. Retrieved 17 December 2022.

- ^ "HL7 Fast Healthcare Interoperability Resources Specification 'FHIR™', Release 1". HL7 International. 2 February 2014. Archived from the original on 28 December 2014. Retrieved 26 December 2014.

- ^ "HL7 publishes a new version of its FHIR specification". Healthcare IT News. 22 March 2017. Retrieved 30 March 2017.

- ^ "History - FHIR v4.0.1". hl7.org. Retrieved 17 December 2022.

- ^ "Directory of published versions". hl7.org. Retrieved 10 October 2023.

- ^ "Fast Healthcare Interoperability Resources® (FHIR)". eCQI Resource Center.

- ^ "Draft U.S. Core Data for Interoperability (USCDI) and Proposed Expansion Process" (PDF). USA HHS. Retrieved 27 November 2019.

- ^ "USCDI ONDEC". www.healthit.gov. Archived from the original on 30 May 2023. Retrieved 30 May 2023.

- ^ "What is FHIR? And what does it mean for Healthcare IT Monitoring?". 28 August 2015. Retrieved 28 August 2015.

- ^ Dan Munro (30 March 2014). "Setting Healthcare Interop On Fire". Forbes. Retrieved 22 November 2014.

- ^ "Geisinger moves to mobilize its EHR platform". mHealthNews. 11 November 2014. Retrieved 6 December 2014.

- ^ "Open Source FHIR implementations - HL7Wiki". Retrieved 27 September 2024.

- ^ "Mix of Applications at Showcase to Demonstrate FHIR's Potential | David Raths | Healthcare Blogs". www.healthcare-informatics.com. Retrieved 13 September 2016.

- ^ "Precision medicine: Analytics, data science and EHRs in the new age". 15 August 2016. Retrieved 13 September 2016.

- ^ "Apple announces solution bringing health records to iPhone". Apple Newsroom. Retrieved 9 August 2018.

- ^ "EHR interoperability solution offered by key IT panels". Modern Healthcare. 16 October 2014. Archived from the original on 21 May 2016. Retrieved 8 November 2014.

- ^ "Proposed interoperability overhaul finds boosters, doubters". Modern Healthcare. 21 October 2014. Archived from the original on 25 October 2014. Retrieved 8 November 2014.

- ^ "Federal HIT Committees OK Public API Recommendations to ONC". Healthcare Informatics. 15 October 2014. Retrieved 8 November 2014.

- ^ "Teams Make their Pitch for Defense EHR Contract". Health Data Management. 7 November 2014. Retrieved 8 November 2014.

- ^ "HL7 Launches Joint Argonaut Project to Advance FHIR" (PDF). HL7 International. 4 December 2014. Archived from the original (PDF) on 28 December 2014. Retrieved 26 December 2014.

- ^ "Kindling FHIR". Healthcare IT News. 4 December 2014. Archived from the original on 7 December 2020. Retrieved 6 December 2014.

- ^ "Can Argonaut Project Make Exchanging Health Data Easier?". InformationWeek. 26 January 2015. Retrieved 28 February 2015.

- ^ "Halamka: Expect Argonaut Deliverables by May". healthcare-informatics.com. 19 February 2015. Retrieved 28 February 2015.

- ^ "HL7 Teams with Healthcare Services Platform Consortium on FHIR Development | Healthcare Informatics Magazine | Health IT | Information Technology". www.healthcare-informatics.com. Retrieved 30 March 2017.

- ^ "Top Ten Tech Trends 2017: Slow FHIR: Will a Much-Hyped Standard Turbo-Charge Interoperability—Or Maybe Not Quite? | Healthcare Informatics Magazine | Health IT | Information Technology". www.healthcare-informatics.com. Retrieved 30 March 2017.

- ^ "CMS Interoperability and Patient Access final rule | CMS". www.cms.gov. Retrieved 22 September 2020.

- ^ "CMS Proposes New Rules to Address Prior Authorization and Reduce Burden on Patients and Providers". www.cms.gov. Retrieved 21 May 2021.

- ^ "ONC 21st Century Cures Act Final Rule". www.healthit.gov. Retrieved 21 May 2021.

- ^ "HHS Proposes Modifications to the HIPAA Privacy Rule to Empower Patients, Improve Coordinated Care, and Reduce Regulatory Burdens". www.hhs.gov. 10 December 2020. Archived from the original on 10 December 2020. Retrieved 21 May 2021.

- ^ "RNDS – Ministério da Saúde" (in Brazilian Portuguese). Retrieved 10 November 2020.

- ^ "Israel Core". fhir-il-community.org. 7 August 2022. Archived from the original on 7 August 2022. Retrieved 7 August 2022.

- ^ "FHIR In Israel – An Overview". outburn.co.il. 28 February 2022. Retrieved 7 August 2022.

- ^ "מוכנות מערכת הבריאות למצבי משבר" (PDF). idi.org.il. 16 December 2020. Retrieved 7 August 2022.

- ^ "תזכיר חוק ניוד מידע בריאות, התשפ"ג-2023". www.tazkirim.gov.il. 24 January 2023. Retrieved 14 February 2023.

- ^ "Everything You Need To Know About The Health Data Mobility Law". outburn.co.il. 2 February 2023. Retrieved 14 February 2023.

## Further reading
[edit]

- Braunstein, Mark L. (11 February 2022). Health Informatics on FHIR: How HL7's API is Transforming Healthcare. Springer Cham. p.&#160;470. doi:10.1007/978-3-030-91563-6. ISBN&#160;978-3-030-91563-6. S2CID&#160;246705195. Retrieved 8 August 2022.

## External links
[edit]

- Official website

- v
- t
- eHealth informaticsSubdisciplines

- Medical image computing and imaging informatics

- Artificial intelligence in healthcare

- Neuroinformatics in healthcare

- Behavior informatics in healthcare

- Computational biology in healthcare

- Translational bioinformatics

- Translational medicine

- health information technology

- Telemedicine

- Public health informatics

- Health information management

- Consumer health informatics
Medical classification

- Continuity of Care Record

- HRHIS

- ICD

- ISO 27799

- LOINC
Professional organizations

- American Association for Medical Systems and Informatics

- American Medical Informatics Association

- Australian Society / Australasian College (to merge from 2020)

- Brazilian Society

- European Federation

- Indian Association

- International Association

- American College of Medical Informatics
Other concepts

- Electronic health record

- Health Level 7

- Remote manipulator

- Personalized medicine / precision medicine

- List of medical and health informatics journals

- openEHR

Retrieved from "https://en.wikipedia.org/w/index.php?title=Fast_Healthcare_Interoperability_Resources&oldid=1344969218"
					Categories: 
- Standards for electronic health records
- Industry-specific XML-based standards
- JSONHidden categories: 
- CS1 Brazilian Portuguese-language sources (pt-br)
- Articles with short description
- Short description matches Wikidata
- Use dmy dates from June 2023
- Official website different in Wikidata and Wikipedia

Search

						Search

				Fast Healthcare Interoperability Resources

10 languages

Add topic
