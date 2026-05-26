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

## Scenario Profile Assignment

Each imported public study is assigned a deterministic scenario profile based on its study ID.

This keeps synthetic data reproducible while allowing different imported studies to demonstrate different CRA monitoring risk scenarios.

| Scenario Profile         | Main Review Focus                                               |
| ------------------------ | --------------------------------------------------------------- |
| DOCUMENT_READINESS_RISK  | Essential document missing/expired/pending issues               |
| PROTOCOL_DEVIATION_RISK  | Visit window, missing assessment, protocol compliance follow-up |
| ICF_VERSION_RISK         | Consent date and ICF version consistency                        |
| DELEGATION_TRAINING_RISK | Training completion and delegation timing consistency           |
| BALANCED_HIGH_RISK       | Multiple risk signals across site operations                    |
