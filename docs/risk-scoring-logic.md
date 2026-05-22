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
