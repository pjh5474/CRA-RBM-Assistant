from typing import Any, Dict, List

from fastapi import HTTPException

from app.repositories.essential_document_repository import (
    get_essential_documents_by_site_from_supabase,
)
from app.services.study_service import get_risk_sites_by_study_id


def calculate_readiness_score(documents: List[Dict[str, Any]]) -> int:
    required_documents = [document for document in documents if document["required"]]

    if not required_documents:
        return 100

    ready_count = sum(
        1 for document in required_documents if document["status"] == "Ready"
    )

    return round((ready_count / len(required_documents)) * 100)


def summarize_document_status(documents: List[Dict[str, Any]], status: str) -> int:
    return sum(1 for document in documents if document["status"] == status)


def get_site_name_from_risk_sites(study_id: str, site_id: str) -> str:
    risk_sites = get_risk_sites_by_study_id(study_id)

    for site in risk_sites:
        if site["siteId"] == site_id:
            return site["siteName"]

    raise HTTPException(
        status_code=404,
        detail=f"Site not found for study {study_id}: {site_id}",
    )


def get_essential_document_readiness(
    study_id: str,
    site_id: str,
) -> Dict[str, Any]:
    site_name = get_site_name_from_risk_sites(study_id, site_id)

    documents = get_essential_documents_by_site_from_supabase(
        study_id=study_id,
        site_id=site_id,
    )

    return {
        "studyId": study_id,
        "siteId": site_id,
        "siteName": site_name,
        "readinessScore": calculate_readiness_score(documents),
        "totalDocuments": len(documents),
        "readyDocuments": summarize_document_status(documents, "Ready"),
        "missingDocuments": summarize_document_status(documents, "Missing"),
        "pendingDocuments": summarize_document_status(documents, "Pending"),
        "expiredDocuments": summarize_document_status(documents, "Expired"),
        "documents": documents,
    }
