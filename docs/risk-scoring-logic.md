# Risk Scoring Logic

This document describes the simplified site-level risk scoring logic used in CRA-RBM Assistant.

The purpose of this logic is to demonstrate how site monitoring data can be structured and prioritized from a CRA perspective. The scoring model is simplified for portfolio and educational use.

## 1. Risk Indicators

The current MVP uses the following risk indicators:

- Open query count
- Query aging days
- Protocol deviation count
- SAE reporting delay count
- Missing essential document count
- IP accountability issue count
- ICF issue count

## 2. Scoring Criteria

### Open Queries

| Condition               | Score |
| ----------------------- | ----: |
| 0 to 5 open queries     |     0 |
| 6 to 10 open queries    |     1 |
| 11 or more open queries |     2 |

### Query Aging Days

| Condition       | Score |
| --------------- | ----: |
| 0 to 7 days     |     0 |
| 8 to 14 days    |     1 |
| 15 days or more |     2 |

### Protocol Deviations

| Condition            | Score |
| -------------------- | ----: |
| 0 to 1 deviation     |     0 |
| 2 to 3 deviations    |     1 |
| 4 or more deviations |     2 |

### SAE Reporting Delay

| Condition               | Score |
| ----------------------- | ----: |
| No delay                |     0 |
| One or more delay cases |     3 |

### Missing Essential Documents

| Condition                     | Score |
| ----------------------------- | ----: |
| No missing documents          |     0 |
| One or more missing documents |     2 |

### IP Accountability Issues

| Condition               | Score |
| ----------------------- | ----: |
| No issue                |     0 |
| One or more issue cases |     2 |

### ICF Issues

| Condition               | Score |
| ----------------------- | ----: |
| No issue                |     0 |
| One or more issue cases |     3 |

## 3. Risk Level

| Total Score | Risk Level |
| ----------- | ---------- |
| 0 to 2      | Low        |
| 3 to 5      | Medium     |
| 6 or higher | High       |

## 4. Example

If a site has the following metrics:

- Open queries: 16
- Query aging days: 15
- Protocol deviations: 4
- SAE reporting delay: 1
- Missing essential documents: 2
- IP accountability issue: 1
- ICF issue: 1

Then the score is:

```text
Open queries: 2
Query aging: 2
Protocol deviations: 2
SAE delay: 3
Missing documents: 2
IP accountability issue: 2
ICF issue: 3

Total risk score: 16
Risk level: High
```

## 5. Relationship with Site Review Modules

The current risk score is calculated from summarized site-level monitoring metrics.

Detailed site review modules provide supporting context for CRA review:

| Module                               | Relationship to Risk Score                                                   |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| Essential Document Readiness Tracker | Supports interpretation of missing essential document risk                   |
| Protocol Deviation Tracker           | Supports interpretation of protocol deviation risk                           |
| ICF Version Control Check            | Supports interpretation of informed consent-related risk                     |
| Monitoring Report Draft              | Integrates risk score and detailed findings into a CRA-oriented report draft |

In the current MVP, these detailed modules do not dynamically recalculate the risk score. Instead, they provide structured evidence and review context for the summarized risk indicators.

Future versions may calculate risk scores directly from detailed operational records such as essential document statuses, protocol deviation severity, and ICF version check results.

## 6. High-priority Indicators

Some indicators are weighted more heavily because they may have direct implications for subject safety, protocol compliance, or informed consent quality.

| Indicator                   | Reason for Higher Weight                                                           |
| --------------------------- | ---------------------------------------------------------------------------------- |
| SAE reporting delay         | Safety reporting delays may require urgent review and escalation                   |
| ICF issue                   | Informed consent issues may affect subject protection and documentation quality    |
| Missing essential documents | Missing site documents may affect inspection readiness                             |
| IP accountability issue     | IP accountability issues may affect investigational product control and compliance |

The weighting is simplified and rule-based for portfolio demonstration. It is not a validated RBQM model.

## Data Use Notice

This project does not use real patient data, real subject data, confidential sponsor documents, or real site performance data.

Study-level information may be imported from public ClinicalTrials.gov registry data. Site-level operational data, including monitoring metrics, essential documents, protocol deviations, and subject consent records, is synthetic and used only to demonstrate CRA-oriented workflow design.
