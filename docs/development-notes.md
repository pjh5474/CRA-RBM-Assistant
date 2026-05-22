# Development Notes

## Why FastAPI

FastAPI was selected because this project requires API development, risk scoring logic, future ClinicalTrials.gov API integration, and potential LLM-based document processing.

## Why Supabase PostgreSQL

Supabase PostgreSQL was selected to move from a JSON-based prototype to a managed relational database while keeping MVP development and deployment simple.

## Why Risk Scoring

The risk scoring logic was designed to demonstrate how CRA monitoring data can be prioritized based on query aging, protocol deviations, SAE reporting delays, missing essential documents, IP accountability issues, and ICF issues.

## Current Limitation

This project is a portfolio prototype and does not implement validated clinical system requirements such as audit trail, electronic signature, system validation, or Part 11 compliance.
