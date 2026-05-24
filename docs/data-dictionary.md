# Data Dictionary

## Study

| Field               | Description                                        |
| ------------------- | -------------------------------------------------- |
| studyId             | Unique study identifier                            |
| title               | Study title                                        |
| phase               | Clinical trial phase                               |
| indication          | Target disease or condition                        |
| sponsor             | Sponsor name, synthetic in this project            |
| studyDesign         | Structured study design information                |
| intervention        | Investigational product and comparator information |
| population          | Target population and enrollment information       |
| endpoints           | Primary and secondary endpoints                    |
| eligibilityCriteria | Inclusion and exclusion criteria                   |
| visitSchedule       | Study visit schedule and key assessments           |
| safetyReporting     | AE/SAE reporting-related information               |
| craFocusAreas       | CRA-oriented monitoring focus areas                |

## Site

| Field                 | Description                            |
| --------------------- | -------------------------------------- |
| siteId                | Unique site identifier                 |
| studyId               | Related study identifier               |
| siteName              | Synthetic site name                    |
| principalInvestigator | Synthetic investigator name            |
| country               | Site country                           |
| status                | Site activation status                 |
| activationDate        | Site activation date                   |
| targetEnrollment      | Planned enrollment target for the site |
| currentEnrollment     | Current enrollment count               |

## MonitoringMetric

| Field                     | Description                                |
| ------------------------- | ------------------------------------------ |
| metricId                  | Unique metric identifier                   |
| siteId                    | Related site identifier                    |
| studyId                   | Related study identifier                   |
| openQueries               | Number of unresolved queries               |
| queryAgingDays            | Maximum or representative query aging days |
| protocolDeviations        | Number of protocol deviation cases         |
| saeReportingDelayCount    | Number of delayed SAE reporting cases      |
| missingEssentialDocuments | Number of missing essential documents      |
| ipAccountabilityIssues    | Number of IP accountability-related issues |
| icfIssues                 | Number of informed consent-related issues  |
| lastMonitoringVisitDate   | Date of the most recent monitoring visit   |

## ChecklistTemplate

| Field         | Description                                         |
| ------------- | --------------------------------------------------- |
| checklistType | Checklist type such as SIV or IMV                   |
| category      | Checklist category                                  |
| item          | Checklist review item                               |
| rationale     | Reason why this item is relevant for CRA monitoring |
| displayOrder  | Display order in the checklist                      |

## EssentialDocument

| Field        | Description                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| documentId   | Unique essential document identifier                                                                      |
| studyId      | Related study identifier                                                                                  |
| siteId       | Related site identifier                                                                                   |
| documentType | Type of essential document, such as IRB Approval Letter, Approved ICF, Delegation Log, or GCP Certificate |
| required     | Whether the document is required for site readiness review                                                |
| status       | Document readiness status: Ready, Missing, Pending, or Expired                                            |
| version      | Document version, if applicable                                                                           |
| documentDate | Document issue, approval, or confirmation date                                                            |
| expiryDate   | Expiry date, if applicable                                                                                |
| comment      | CRA-oriented review comment or follow-up note                                                             |

## ProtocolDeviation

| Field            | Description                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| deviationId      | Unique protocol deviation identifier                                                           |
| studyId          | Related study identifier                                                                       |
| siteId           | Related site identifier                                                                        |
| subjectCode      | Synthetic subject code                                                                         |
| category         | Deviation category, such as Visit Window Deviation, Missing Assessment, or SAE Reporting Delay |
| severity         | Deviation severity: Minor, Major, or Critical                                                  |
| status           | Deviation status: Open, In Review, or Resolved                                                 |
| description      | Description of the protocol deviation                                                          |
| detectedDate     | Date when the deviation was detected                                                           |
| rootCause        | Root cause identified for the deviation                                                        |
| correctiveAction | Corrective action taken or planned                                                             |
| preventiveAction | Preventive action to reduce recurrence                                                         |

## IcfVersion

| Field           | Description                                |
| --------------- | ------------------------------------------ |
| icfVersionId    | Unique ICF version identifier              |
| studyId         | Related study identifier                   |
| version         | ICF version number                         |
| irbApprovalDate | IRB approval date for the ICF version      |
| effectiveDate   | Date when the ICF version became effective |
| status          | Version status: Active or Superseded       |

## SubjectConsent

| Field              | Description                                          |
| ------------------ | ---------------------------------------------------- |
| consentId          | Unique subject consent identifier                    |
| studyId            | Related study identifier                             |
| siteId             | Related site identifier                              |
| subjectCode        | Synthetic subject code                               |
| signedIcfVersion   | ICF version signed by the subject                    |
| consentDate        | Date when the subject signed the ICF                 |
| consentProcessNote | Synthetic note describing the consent review context |

## AuditLog

| Field       | Description                                        |
| ----------- | -------------------------------------------------- |
| id          | Unique audit log identifier                        |
| actorUserId | Authenticated user ID, nullable in the current MVP |
| tableName   | Name of the changed database table                 |
| action      | Database action: INSERT, UPDATE, or DELETE         |
| recordId    | Identifier of the changed record                   |
| oldData     | Previous row data as JSONB, for UPDATE or DELETE   |
| newData     | New row data as JSONB, for INSERT or UPDATE        |
| createdAt   | Timestamp when the change was logged               |

## ImportedClinicalTrial

ClinicalTrials.gov study data is mapped into the internal Study structure.

| Source Field        | Internal Field              | Description                              |
| ------------------- | --------------------------- | ---------------------------------------- |
| nctId               | studyId                     | Public ClinicalTrials.gov NCT identifier |
| title               | title                       | Public study title                       |
| phases              | phase                       | Clinical trial phase                     |
| conditions          | indication                  | Target disease or condition              |
| interventions       | intervention                | Public intervention information          |
| primaryOutcomes     | endpoints                   | Primary outcome measures                 |
| secondaryOutcomes   | endpoints                   | Secondary outcome measures               |
| eligibilityCriteria | eligibilityCriteria.rawText | Public eligibility criteria text         |

## API-derived Review Objects

The following objects are generated by backend services and are not stored as separate primary tables in the current MVP.

### SiteReviewSummary

| Field                 | Description                                 |
| --------------------- | ------------------------------------------- |
| study                 | Study summary                               |
| site                  | Site risk summary                           |
| essentialDocuments    | Essential document readiness summary        |
| protocolDeviations    | Protocol deviation summary                  |
| icfVersionCheck       | ICF version consistency check summary       |
| monitoringReportDraft | Enhanced monitoring report draft            |
| modules               | Navigation metadata for site review modules |

### MonitoringReportDraft

| Field                    | Description                                         |
| ------------------------ | --------------------------------------------------- |
| riskSummary              | Site-level risk score, risk level, and risk factors |
| essentialDocumentSummary | Document readiness summary                          |
| protocolDeviationSummary | Protocol deviation status and severity summary      |
| icfSummary               | ICF consent consistency summary                     |
| findings                 | Generated monitoring findings                       |
| followUpActions          | CRA-oriented follow-up action plan                  |
| limitations              | Prototype and data-use limitations                  |

## Data Use Notice

This project does not use real patient data, real subject data, confidential sponsor documents, or real site performance data.

Study-level information may be imported from public ClinicalTrials.gov registry data. Site-level operational data, including monitoring metrics, essential documents, protocol deviations, and subject consent records, is synthetic and used only to demonstrate CRA-oriented workflow design.
