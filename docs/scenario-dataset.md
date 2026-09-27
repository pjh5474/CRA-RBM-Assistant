# Scenario-based Synthetic Dataset

## Purpose

CRA-RBM Assistant does not use real patient data, real subject data, confidential sponsor protocol, or real site performance data.

Instead, it uses **scenario-based synthetic operational data** to demonstrate CRA monitoring review logic after a public registry study is imported into the internal workspace.

Public registry metadata and synthetic operational data are intentionally separated.

```text
ClinicalTrials.gov-derived Registry Data
              ↓
        Imported Study
              ↓
Synthetic Operational Scenario
              ↓
CRA Review / Risk / Follow-up
```

The synthetic scenario is not intended to represent the actual operational status or risk of the imported ClinicalTrials.gov study.

---

## Scenario Design Principles

- reflect common CRA review areas
- use controlled synthetic issues
- keep scenarios reproducible
- map each issue to a review workflow
- avoid real patient / site / sponsor data
- support dashboards, risk review, and report drafts
- never present synthetic findings as public registry facts

---

## Why Deterministic Scenarios Are Used

Imported studies are assigned a deterministic scenario profile based on `studyId`.

This is intentionally different from fully random demo-data generation.

Deterministic profiles provide:

- reproducible demo data
- stable screenshots
- consistent interview explanations
- repeatable testing
- different review patterns across imported studies
- predictable downstream report output

Conceptually:

```text
scenario_profile =
    profile_list[
        sum(character codes of studyId)
        % number_of_profiles
    ]
```

This method is used only for portfolio demonstration.

It is not a risk-prediction algorithm.

---

## Scenario Examples

| Scenario                   | Synthetic Data Design                                     | CRA Review Purpose                       |
| -------------------------- | --------------------------------------------------------- | ---------------------------------------- |
| Outdated ICF version       | Subject signed ICF v1.0 after v2.0 became effective       | Consent version consistency review       |
| Visit window deviation     | Visit occurred outside the expected visit window          | Protocol compliance review               |
| Missing essential document | Delegation Log or IP Accountability Log marked missing    | Site file readiness review               |
| Expired GCP certificate    | GCP certificate marked expired                            | Training / qualification evidence review |
| SAE reporting delay        | Synthetic delay signal and related deviation              | Safety reporting follow-up               |
| Delegation before training | Protocol or GCP training completed after delegation start | Delegation / training consistency review |
| Query aging                | Open query remains unresolved beyond scenario threshold   | Data-cleaning follow-up                  |
| Multiple concurrent issues | Several indicators are triggered in one site              | Integrated risk-based review             |

---

## Scenario Profiles

| Scenario Profile           | Main Review Focus              | Example Signals                                                       |
| -------------------------- | ------------------------------ | --------------------------------------------------------------------- |
| `DOCUMENT_READINESS_RISK`  | Essential document readiness   | Missing Delegation Log, expired GCP certificate, pending Approved ICF |
| `PROTOCOL_DEVIATION_RISK`  | Protocol compliance            | Visit-window deviation, missing assessment, open major deviation      |
| `ICF_VERSION_RISK`         | Informed consent consistency   | Outdated ICF used after newer version became effective                |
| `DELEGATION_TRAINING_RISK` | Delegation / training evidence | Training after delegation start, missing GCP evidence                 |
| `BALANCED_HIGH_RISK`       | Multiple operational areas     | Query aging, safety delay, missing documents, deviation, ICF issue    |

---

## Delegation and Training Scenario

This scenario demonstrates whether synthetic site staff completed required training before delegated study tasks began.

Controlled issues may include:

- protocol training completed after delegation start
- missing GCP training evidence
- Training Log pending
- Delegation Log missing or pending

The purpose is to demonstrate cross-record date and evidence consistency checks.

---

## How Profiles Affect Generated Data

A profile can influence:

- monitoring metrics
- essential document records
- protocol deviation records
- ICF versions
- subject consent records
- delegation records
- training records
- risk factors
- Site Review Hub summary
- CRA follow-up actions
- Monitoring Report Draft findings

This allows one imported public study to be reused across multiple CRA-RBM workflows without implying that the public study actually has those operational issues.

---

## Registry Data vs Synthetic Data

This distinction is fundamental.

### Registry Facts

Examples:

- NCT ID
- title
- phase
- status
- conditions
- interventions
- outcomes
- eligibility criteria
- study locations

These come from the ClinicalTrials.gov-derived data platform.

### Synthetic Operational Data

Examples:

- high-risk site classification
- query aging
- SAE delay
- missing essential document
- outdated ICF use
- training inconsistency
- CRA action item

These are generated by the portfolio application.

The Agent and documentation are designed to keep these sources separate.

---

## Important Limitation

The scenario profile does **not** predict or describe the real-world risk of a ClinicalTrials.gov study.

It only controls which synthetic operational scenario is generated after import.

Therefore, a statement such as:

> "This study is high risk according to ClinicalTrials.gov."

would be incorrect.

The intended interpretation is:

> "This imported study is being used as the study-level context for a synthetic CRA monitoring scenario generated by the portfolio application."

---

## Intended Use

The synthetic dataset is used for:

- application development
- dashboard demonstrations
- consistency-check logic
- risk-scoring demonstration
- screenshot generation
- monitoring-report draft generation
- interview / portfolio explanation
- repeatable testing

It is not intended for:

- real clinical-trial decision-making
- site risk prediction
- patient or subject assessment
- regulatory submission
- sponsor oversight
- production monitoring operations
