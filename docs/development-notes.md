# Development Notes

## Why FastAPI

FastAPI is used as the application/service boundary between the frontend, Supabase-backed CRA workflows, Databricks Serving Layer, BigQuery/dbt analytics, and external Agent tools.

It was selected because the project requires:

- REST API development
- synchronous data-source integration
- registry search / detail APIs
- study import and mapping logic
- CRA workflow services
- analytics API delivery
- integration with external AI tools

A key design goal is to keep the frontend and external Agent independent from physical Databricks and warehouse table structures.

```text
Frontend / Agent
      ↓
    FastAPI
      ↓
Databricks / BigQuery / Supabase
```

This allows the underlying data platform to evolve while preserving stable application contracts.

---

## Why Supabase PostgreSQL

Supabase PostgreSQL is used as the application database for internal CRA-RBM workspace data.

It stores application-oriented entities such as:

- imported studies
- sites
- monitoring metrics
- essential documents
- protocol deviations
- ICF versions
- subject consent records
- delegation / training records
- audit-like logs

Supabase Auth is also used to protect write operations such as study import.

Public ClinicalTrials.gov registry data is not treated as the same data domain as CRA-RBM operational data.

```text
Databricks Serving
→ public registry facts

Supabase
→ internal application / synthetic operational state
```

---

## Why Separate Gold and Serving

The upstream data platform uses different downstream models for different access patterns.

### Gold

Gold datasets are optimized for analytics.

Examples:

- yearly trial trends
- country summaries
- condition trends

Gold is exported to BigQuery and further modeled with dbt.

### Serving

Serving datasets are optimized for application access.

Examples:

- study search
- study detail

This separation avoids forcing analytical aggregate models to also act as application read models.

---

## Why Keep the Existing Import Contract

The original Study Import UI already had a stable frontend contract.

Instead of redesigning the UI, the underlying data source was replaced:

```text
Before
Frontend
  ↓
FastAPI
  ↓
ClinicalTrials.gov API

After
Frontend
  ↓
FastAPI
  ↓
Databricks Serving Layer
```

The compatibility API layer allows the existing UI and TypeScript models to remain largely unchanged while the backend source changes.

This demonstrates backward-compatible integration and reduced frontend coupling.

---

## Why Risk Scoring

The risk scoring logic is designed to demonstrate how CRA monitoring data can be prioritized using synthetic operational indicators such as:

- query aging
- protocol deviations
- SAE reporting delay signals
- missing essential documents
- IP accountability issues
- ICF issues

The score is intentionally simplified and is not intended to represent a validated clinical risk model.

Its purpose is to demonstrate:

- indicator-based prioritization
- rule-driven review logic
- dashboard integration
- CRA follow-up workflow design

---

## Why Scenario-based Synthetic Data

The project does not use real patient, subject, site-performance, or sponsor-confidential data.

Synthetic operational scenarios are used to demonstrate CRA review logic in a reproducible way.

Scenario generation is deterministic by study ID so that:

- the same imported study produces the same scenario
- screenshots remain stable
- testing is reproducible
- different studies can demonstrate different review patterns

Synthetic scenarios are explicitly separated from public registry facts.

---

## Why Audit-like Logs

Selected Supabase tables use PostgreSQL triggers to record insert, update, and delete history with old/new JSONB snapshots.

The goal is to demonstrate change traceability concepts.

This is intentionally described as **audit-like logging** because the project does not implement validated audit-trail requirements such as:

- formal computerized system validation
- electronic signature controls
- validated user identity / attribution
- immutable regulatory audit-trail guarantees
- 21 CFR Part 11 compliance

---

## Why Agent Tools Use FastAPI

The CRA Assistant Agent does not query Databricks directly.

Instead:

```text
CRA Assistant Agent
      ↓
Registry Tool
      ↓
FastAPI
      ↓
Databricks Serving
```

This keeps AI logic independent from physical storage and allows application APIs to be reused across frontend and Agent consumers.

---

## Current Limitations

This project is a portfolio prototype.

Current limitations include:

- no real patient or subject data
- synthetic site-level operational scenarios
- simplified risk scoring
- no validated audit trail
- no electronic signature
- no formal system validation
- no 21 CFR Part 11 compliance claim
- registry data is a stored platform snapshot rather than a live ClinicalTrials.gov lookup at response time
- imported public registry metadata does not contain every protocol-level operational field
- current authorization is not a production-grade multi-tenant access-control design
- Databricks SQL Warehouse startup / query latency can affect registry API response time

The project is designed to demonstrate architecture, data flow, domain modeling, and integration rather than production clinical-system validation.
