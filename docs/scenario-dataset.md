# Scenario-based Synthetic Dataset

## Purpose

This project does not use real patient data, real subject data, confidential sponsor protocol, or real site performance data.

Instead, it uses scenario-based synthetic operational data to demonstrate CRA monitoring review logic.

## Scenario Design Principles

- Reflect common CRA review areas
- Use controlled synthetic issues
- Map each issue to monitoring review workflow
- Avoid real patient/site/sponsor data
- Support dashboard, risk review, and report draft generation

## Scenario Examples

| Scenario                   | Synthetic Data Design                                  | CRA Review Purpose                                 |
| -------------------------- | ------------------------------------------------------ | -------------------------------------------------- |
| Outdated ICF version       | Subject signed ICF v1.0 after v2.0 became effective    | Detect informed consent version consistency issue  |
| Visit window deviation     | Visit performed outside the expected window            | Demonstrate protocol compliance review             |
| Missing essential document | Delegation Log or IP Accountability Log marked Missing | Demonstrate site file readiness review             |
| Expired GCP certificate    | GCP certificate marked Expired                         | Demonstrate training/qualification evidence review |
| SAE reporting delay        | SAE delay count and deviation record added             | Demonstrate safety reporting follow-up             |

## Scenario Profile Generation

Imported studies are assigned a deterministic scenario profile based on their study ID.

This is not random demo data generation. The purpose is to keep the scenario reproducible while allowing different imported studies to demonstrate different CRA monitoring risk patterns.

For example, the same NCT ID will always generate the same scenario profile, but different NCT IDs may generate different profiles.

### Why deterministic profiles are used

Fully random data generation was intentionally avoided because it can make testing, screenshots, documentation, and interview explanations inconsistent.

Deterministic scenario profiles provide:

- Reproducible demo data
- Stable screenshots and portfolio examples
- Different CRA monitoring risk scenarios across imported studies
- Clear explanation of why a specific issue appears in a specific demo site
- Better alignment with scenario-based testing

### Scenario profile assignment

The current MVP assigns a scenario profile using the imported study ID.

Conceptually:

```text
scenario_profile = profile_list[sum(character codes of studyId) % number_of_profiles]
```

This simple deterministic assignment method is used only for portfolio demonstration. It is not intended to represent real clinical trial risk prediction.

### Scenario profiles

| Scenario Profile           | Main Review Focus                                       | Example Signals                                                                    |
| -------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `DOCUMENT_READINESS_RISK`  | Essential document readiness and site file completeness | Missing Delegation Log, expired GCP certificate, pending Approved ICF              |
| `PROTOCOL_DEVIATION_RISK`  | Protocol compliance and deviation follow-up             | Visit window deviation, missing assessment, open major deviation                   |
| `ICF_VERSION_RISK`         | Informed consent version consistency                    | Subject signed outdated ICF version after newer version became effective           |
| `DELEGATION_TRAINING_RISK` | Delegation and training evidence consistency            | Protocol training after delegation start date, missing GCP training evidence       |
| `BALANCED_HIGH_RISK`       | Multiple risk signals across site operations            | Query aging, SAE reporting delay, missing documents, protocol deviation, ICF issue |

### How scenario profiles affect generated data

Each scenario profile can influence the following synthetic operational data:

- Monitoring metrics
- Essential document records
- Protocol deviation records
- ICF version and subject consent records
- Delegation and training records
- Site Review Hub summary
- Monitoring Report Draft findings and follow-up actions

### Important limitation

The scenario profile does not predict real study risk.

It only controls which synthetic operational scenario is generated after a public study is imported. The goal is to demonstrate CRA review logic, not to assess the real-world risk of a ClinicalTrials.gov study.
