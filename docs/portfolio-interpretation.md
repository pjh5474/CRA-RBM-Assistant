# Portfolio Interpretation

## 1. Project Context

CRA-RBM Assistant is a portfolio project that demonstrates how data engineering, backend development, and data quality experience can be applied to clinical trial monitoring workflows.

The project initially focused on translating CRA monitoring activities into structured software workflows. It has since been extended to consume a separate cloud data engineering pipeline built on ClinicalTrials.gov public registry data.

The current project therefore demonstrates two connected capabilities:

1. **Clinical domain workflow design**
   - risk-based monitoring support
   - essential document readiness
   - protocol deviation tracking
   - ICF version consistency checks
   - delegation / training consistency checks
   - monitoring report draft generation

2. **Data-to-application integration**
   - Databricks Serving Layer integration
   - FastAPI registry APIs
   - BigQuery / dbt analytics integration
   - study import into Supabase
   - AI Agent tool integration through stable APIs

---

## 2. Core Portfolio Message

The main message of this project is:

> **Structured data becomes valuable when it is connected to actual application workflows.**

CRA-RBM Assistant does not stop at storing or visualizing data.

It connects:

```text
ClinicalTrials.gov Public Registry
        ↓
Cloud Data Engineering Pipeline
        ↓
Databricks Serving / BigQuery Analytics
        ↓
FastAPI
        ↓
CRA-RBM Application
        ↓
CRA Assistant Agent
```

This demonstrates how data can move from raw public source data into:

- analytical datasets
- application-ready serving models
- end-user workflows
- AI tool interfaces

---

## 3. Strengths Demonstrated

### Data Modeling and Data Quality

- separation of registry data and synthetic operational data
- explicit application-facing data contracts
- date / version consistency validation
- status-based tracking
- issue categorization
- audit-like change traceability

### Data Engineering Integration

- Databricks Serving Layer consumption
- BigQuery analytics consumption
- dbt analytics mart integration
- FastAPI as a service boundary between the data platform and application
- preservation of stable frontend contracts while replacing the underlying data source

### Backend and API Design

- registry search / detail APIs
- compatibility APIs for existing import workflows
- analytics APIs
- study / site / monitoring APIs
- authenticated write operations
- separation of application database responsibilities and external registry data

### Workflow Design

- study import
- site risk review
- essential document readiness
- protocol deviation review
- ICF consistency checks
- delegation / training checks
- monitoring report draft generation
- CRA follow-up action generation

### AI Integration

- registry search tool
- registry detail tool
- reuse of FastAPI instead of direct Databricks access
- clear separation between factual registry data and synthetic CRA operational data

---

## 4. Feature-to-Engineering Mapping

| Feature                     | Domain / Workflow               | Engineering Strength Demonstrated              |
| --------------------------- | ------------------------------- | ---------------------------------------------- |
| Registry Search             | Public clinical trial discovery | Application-oriented Serving model consumption |
| Registry Study Detail       | Structured study inspection     | Nested data delivery through API contracts     |
| Study Import                | Registry → internal workspace   | Data mapping and compatibility-layer design    |
| Clinical Trial Analytics    | Trial trends / distributions    | BigQuery + dbt analytics mart consumption      |
| Risk Dashboard              | Site risk prioritization        | Indicator modeling and dashboard integration   |
| Essential Document Tracker  | Site file readiness             | Status-based data management                   |
| Protocol Deviation Tracker  | Deviation follow-up             | Issue categorization and structured follow-up  |
| ICF Version Check           | Consent version review          | Date / version consistency validation          |
| Delegation & Training Check | Staff readiness review          | Cross-record consistency validation            |
| Monitoring Report Draft     | Monitoring documentation        | Structured data-to-document workflow           |
| Audit-like Logs             | Change traceability             | Trigger-based history tracking                 |
| Auth-gated Import           | Controlled write operation      | Authentication-aware service design            |
| Agent Registry Tools        | AI-assisted registry lookup     | API reuse and tool-based AI integration        |

---

## 5. Data Platform Integration

The application is connected to a separate `clinical-trials-data-platform` project.

The data platform provides:

```text
ClinicalTrials.gov
        ↓
Bronze
        ↓
Silver
        ↓
Quality
        ↓
Gold / Serving
```

CRA-RBM Assistant consumes two downstream paths.

### Application Serving Path

```text
Databricks Serving
        ↓
FastAPI Registry API
        ↓
Study Search / Detail / Import
```

### Analytics Path

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

This separation demonstrates the difference between:

- **analytical datasets**
- **application serving datasets**

and avoids forcing one data model to serve both purposes.

---

## 6. Application Integration Strategy

One important engineering decision was to preserve the existing frontend workflow while changing the underlying data source.

Previously:

```text
Frontend
    ↓
FastAPI
    ↓
ClinicalTrials.gov API
```

Current:

```text
Frontend
    ↓
FastAPI
    ↓
Databricks Serving Layer
```

The existing study import UI and frontend contracts were kept largely unchanged.

This demonstrates:

- backward-compatible API design
- reduced frontend coupling
- service-layer abstraction
- migration of a data source without redesigning the entire application

---

## 7. Data Boundary Design

The project intentionally distinguishes between:

### Public Registry Facts

Examples:

- NCT ID
- title
- phase
- status
- conditions
- interventions
- outcomes
- eligibility criteria

### Synthetic CRA Operational Data

Examples:

- site risk
- query aging
- protocol deviations
- essential document issues
- ICF inconsistencies
- follow-up actions

These two data categories are not presented as equivalent.

This boundary is important because public registry data does not contain all protocol-level or operational monitoring information.

Unknown operational information is not fabricated from registry data.

---

## 8. AI Agent Integration

The CRA Assistant Agent accesses registry data through CRA-RBM FastAPI.

```text
CRA Assistant Agent
        ↓
searchRegistryStudies
getRegistryStudyDetail
        ↓
FastAPI
        ↓
Databricks Serving
```

The Agent does not query Databricks directly.

This design demonstrates:

- tool-based AI integration
- reuse of application APIs
- reduced coupling between AI logic and physical data tables
- clear separation between factual registry data and synthetic demo data

---

## 9. Portfolio Positioning

This project can be presented differently depending on the target role.

### For Data Engineer Roles

Emphasize:

- data platform → application integration
- Serving Layer design
- analytical vs application data-model separation
- BigQuery / dbt consumption
- API-based data delivery
- stable application contracts
- data quality and consistency validation
- end-to-end data lifecycle

Suggested framing:

> I extended an existing clinical-trial workflow application so that public registry data was no longer consumed directly from the external API. Instead, the application now uses a Databricks-based Serving Layer through FastAPI, while analytical data is delivered through BigQuery and dbt. This allowed the same source data to support both application search/detail workflows and analytical dashboards with different data models.

### For CRA / Clinical Operations Roles

Emphasize:

- CRA monitoring workflow understanding
- risk-based review
- essential document readiness
- protocol deviation follow-up
- ICF consistency checks
- synthetic monitoring scenarios
- monitoring documentation support

---

## 10. What This Project Does Not Claim

This project does not claim to be:

- a validated clinical trial system
- a production CTMS
- a production EDC
- a validated audit trail
- a 21 CFR Part 11 compliant system
- a source of real patient or site performance data
- a replacement for CRA judgement
- a production-scale clinical data platform

It is a portfolio prototype designed to demonstrate:

- data workflow design
- application integration
- CRA-oriented domain modeling
- data quality logic
- cloud data engineering concepts
- AI tool integration

---

## 11. Overall Portfolio Narrative

The three related projects form one connected portfolio story.

```text
Clinical Trials Data Platform
        ↓
CRA-RBM Assistant
        ↓
CRA Assistant Agent
```

### Clinical Trials Data Platform

Demonstrates:

- ingestion
- transformation
- data quality
- incremental processing
- analytics modeling
- application serving

### CRA-RBM Assistant

Demonstrates:

- API integration
- application data consumption
- CRA workflow modeling
- dashboard / review workflows
- authenticated study import

### CRA Assistant Agent

Demonstrates:

- tool-based AI integration
- application API reuse
- source-aware retrieval
- registry search / detail assistance

Together, the portfolio demonstrates:

> **Public data → Data Engineering → Application Serving → Domain Workflow → AI Tool Integration**
