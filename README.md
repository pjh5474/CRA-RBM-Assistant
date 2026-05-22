# CRA-RBM Assistant

CRA-RBM Assistant is a prototype web application designed to support Clinical Research Associate (CRA) monitoring preparation by structuring public clinical trial information and synthetic site monitoring data.

This project connects backend development, data quality management, and clinical research operations by implementing core workflows related to protocol review, site monitoring preparation, query/deviation follow-up, and risk-based monitoring.

## 1. Project Background

Clinical Research Associates are responsible for supporting clinical trial quality by monitoring protocol compliance, subject safety, data integrity, essential document readiness, investigational product accountability, and site performance.

As clinical trials become more data-driven and risk-based, CRAs are increasingly expected to understand not only documents and regulations, but also data flow, system usage, query management, and risk indicators across trial sites.

This project was developed as a portfolio project to demonstrate how software engineering and data management experience can be applied to CRA-related workflows.

## 2. Project Goal

The goal of this project is to build a CRA-oriented monitoring support prototype that can:

- Import or define clinical study information
- Extract key protocol-related elements
- Generate SIV and IMV checklist items
- Manage synthetic site monitoring data
- Calculate site-level risk scores
- Suggest CRA follow-up action items for high-risk sites

This application does not use real patient data or confidential clinical trial documents. All site-level data is synthetic and created only for portfolio and educational purposes.

## 3. Main Features

### Study Overview

Displays structured study information such as:

- Study title
- Phase
- Indication
- Study design
- Intervention
- Comparator
- Primary endpoint
- Secondary endpoint
- Inclusion criteria
- Exclusion criteria

### CRA Checklist Generator

Generates CRA-oriented checklist items for:

- Site Initiation Visit, SIV
- Interim Monitoring Visit, IMV
- Essential document review
- Informed consent review
- Eligibility review
- Safety reporting process
- Investigational product accountability
- Source data and eCRF consistency

### Site Risk Dashboard

Visualizes site-level risk indicators using synthetic monitoring data:

- Enrollment status
- Open query count
- Query aging
- Protocol deviation count
- SAE reporting delay
- Missing essential documents
- Risk score
- Risk level

### CRA Follow-up Action Items

Suggests follow-up actions based on detected site risks, such as:

- Query resolution follow-up
- Protocol deviation root cause review
- SAE reporting process retraining
- Essential document reconciliation
- Site staff retraining consideration

## 4. System Architecture

Initial MVP architecture:

Frontend
↓
Backend API
↓
Study Data / Site Monitoring Data
↓
Risk Scoring Engine
↓
Checklist Generator
↓
CRA Dashboard

Planned Architecture:
Next.js Frontend
↓
FastAPI Backend
↓
MySQL Database
↓
Risk Scoring Service
↓
n8n Workflow Automation

## 5. Data Sources

This project uses:

- Manually created sample study data
- Synthetic site monitoring data
- Public clinical trial registry data in future versions

## 6. MVP Scope

The first MVP includes:

- Sample study data display
- Study overview page
- SIV/IMV checklist generation
- Synthetic site monitoring data display
- Site risk score calculation
- Recommended CRA action items

## 7. Risk Scoring Logic

Site risk is calculated based on the following indicators:

- Open query count
- Query aging days
- Protocol deviation count
- SAE reporting delay count
- Missing essential document count
- Enrollment delay

Risk level:

- 0 to 2 points : Low
- 3 to 5 points : Medium
- 6 points or higher : High

Detailed logic is descirbed in docs/risk-scoring-logic.md

## 8. Tech Stack

Planned stack:

- Frontend : Next.js
- Backend : FastAPI
- Database : Supabase PostgreSQL
- Automation : n8n
- Deployment: Docker, AWS or Vercel
- Future AI Integration : LLM-based protocol summurization and checklist generation

FastAPI is selected for rapid API development, clinical trial registry API integration, risk scoring logic, and future LLM-based document processing.

Supabase PostgreSQL is selected to provide a managed relational database for study, site, checklist, and monitoring metric data while supporting fast MVP development and deployment.

## 9. Project Limitations

This project is a prototype and has the following limitations

- It does not replace CRA judgement.
- It does not provide regulatory or medical adivce.
- It does not use real clinical trial subject data.
- Risk scoring logic is simplified for demonstration.
- Checklist generation is based on predefined rules and tmeplates in the MVP version.
- This project is a portfolio prototype and does not implement validated clinical trial system requirements such as audit trail, electronic signature, system validation, or Part 11 compliance.

## 10. Future Improvements

Planned improvements include:

- ClinicalTrials.gov API integration
- Protocol PDF upload and parsing
- Protocal amendment comparison
- ICF version control check
- Delegation log and training log consistency check
- n8n-based high-risk site alert workflow
- LLM-assisted CRA action item generation
