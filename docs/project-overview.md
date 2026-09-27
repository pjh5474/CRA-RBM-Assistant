# Project Overview

## CRA-RBM Assistant

CRA-RBM Assistant is a clinical trial monitoring support prototype that connects:

- public ClinicalTrials.gov registry data
- a cloud data engineering pipeline
- application-level study search / detail / import
- synthetic CRA operational scenarios
- risk-based monitoring workflows
- clinical trial analytics
- external AI Agent tools

The project demonstrates how structured data can be transformed into CRA-oriented application workflows without using real patient or confidential sponsor data.

---

## Purpose

The project has two connected purposes.

### 1. CRA Workflow Modeling

Demonstrate how CRA monitoring concepts can be translated into structured software workflows such as:

- Study Overview
- SIV / IMV checklist views
- site risk review
- query / deviation follow-up
- essential document readiness
- ICF version consistency
- delegation / training consistency
- monitoring report draft generation
- CRA follow-up action items

### 2. Data-to-Application Integration

Demonstrate how a cloud data platform can feed a real application.

```text
ClinicalTrials.gov
      ↓
Databricks / Spark / Delta
      ↓
Gold + Serving
      ↓
BigQuery / dbt + FastAPI
      ↓
CRA-RBM Assistant
      ↓
CRA Assistant Agent
```

---

## Current Workflow

### Registry and Import Flow

```text
ClinicalTrials.gov
      ↓
Clinical Trials Data Platform
      ↓
Databricks Serving Layer
      ↓
FastAPI Registry API
      ↓
Study Search / Preview
      ↓
Authenticated Import
      ↓
Supabase Internal Study
      ↓
Synthetic Operational Data
      ↓
CRA Monitoring Workflow
```

### Analytics Flow

```text
Databricks Gold
      ↓
BigQuery
      ↓
dbt Analytics Mart
      ↓
FastAPI
      ↓
Clinical Trial Analytics Dashboard
```

### Agent Flow

```text
CRA Assistant Agent
      ↓
searchRegistryStudies / getRegistryStudyDetail
      ↓
CRA-RBM FastAPI
      ↓
Databricks Serving
```

---

## Core Features

### Public Registry Search and Detail

- keyword / condition search
- NCT ID lookup
- phase / status / country filtering
- recently updated study ordering
- study design fields
- interventions
- outcomes
- locations
- masking / who-masked
- brief summary
- eligibility criteria

### Study Import

- authenticated import
- registry → internal Study mapping
- Supabase persistence
- deterministic synthetic scenario generation
- reuse of existing Study Overview and monitoring workflows

### Clinical Trial Analytics

- trial overview
- study-type distribution
- yearly trends
- country summaries
- condition trends

### CRA Monitoring Workflows

- SIV / IMV checklist views
- Risk Dashboard
- Site Review Hub
- CRA Action Items
- Essential Document Readiness
- Protocol Deviation Tracker
- ICF Version Control Check
- Delegation & Training Check
- Monitoring Report Draft
- Audit-like Logs

---

## Data Policy

The project separates three data categories.

### Public Registry Data

ClinicalTrials.gov-derived study metadata such as:

- NCT ID
- title
- phase
- status
- conditions
- interventions
- outcomes
- eligibility criteria
- locations

### Internal Application Data

Supabase-backed study and workflow state used by CRA-RBM.

### Synthetic Operational Data

Controlled demo data used to illustrate CRA monitoring scenarios.

No real:

- patient data
- subject data
- site performance data
- sponsor-confidential protocol
- proprietary clinical trial document

is used.

---

## Key Design Principle

The project does not aim to replace CRA judgement.

Instead, it demonstrates how data and software can support:

- review
- prioritization
- consistency checking
- follow-up planning
- monitoring preparation

Unknown protocol-level operational details are not fabricated from public registry data.

---

## Current Status

Implemented:

- [x] ClinicalTrials.gov full-registry data platform integration
- [x] Databricks Serving-based Study Search
- [x] Databricks Serving-based Study Detail
- [x] Study Import into Supabase
- [x] Synthetic operational scenario generation
- [x] Study Overview
- [x] SIV / IMV checklist views
- [x] Site Risk Dashboard
- [x] Site Review Hub
- [x] CRA Action Items
- [x] Essential Document Readiness
- [x] Protocol Deviation Tracker
- [x] ICF Version Control Check
- [x] Delegation & Training Check
- [x] Monitoring Report Draft
- [x] Audit-like Logs
- [x] Clinical Trial Analytics Dashboard
- [x] BigQuery / dbt analytics integration
- [x] CRA Assistant Agent Registry Search / Detail tools

---

## Related Projects

```text
Clinical Trials Data Platform
        ↓
CRA-RBM Assistant
        ↓
CRA Assistant Agent
```

Together, the projects demonstrate:

> **Public Data → Data Engineering → Application Serving → Domain Workflow → AI Tool Integration**
