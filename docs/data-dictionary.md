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
