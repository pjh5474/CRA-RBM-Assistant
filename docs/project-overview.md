# Project Overview

## CRA-RBM Assistant

CRA-RBM Assistant is a portfolio prototype designed to support Clinical Research Associate monitoring preparation by connecting clinical study information, synthetic site monitoring metrics, risk scoring logic, and CRA follow-up action items.

## Purpose

The purpose of this project is to demonstrate how backend development and data quality management experience can be applied to CRA-related workflows such as:

- Protocol review
- Site Initiation Visit preparation
- Interim Monitoring Visit preparation
- Query and deviation follow-up
- Essential document readiness
- Risk-based monitoring

## MVP Workflow

The MVP workflow is:

Sample Study Data
↓
Study Overview
↓
Generated CRA Checklist
↓
Synthetic Site Monitoring Data
↓
Risk Score Calculation
↓
CRA Follow-up Action Items

Key Concept:

This project does not aim to replace CRA judgment.
Instead, it demonstrates how clinical trial information and monitoring data can be structured to support CRA review, prioritization, and follow-up planning.

Data Policy:

This project does not use real patient data, real subject data, or confidential sponsor documents.

All site-level data is synthetic and created only for portfolio and educational purposes.

Planned MVP Features :

- Display sample clinical study information
- Display synthetic site monitoring data
- Calculate site-level risk score
- Classify site risk level as Low, Medium, or High
- Generate CRA-oriented follow-up action items
- Generate SIV and IMV checklist items

Future Extensions :

- ClinicalTrials.gov API integration
- Protocol PDF upload and parsing
- Protocol amendment comparison
- ICF version control check
- Delegation log and training log consistency check
- n8n-based high-risk site alert workflow
- LLM-assisted protocol summarization and checklist generation
