from typing import Any, Dict, List

from fastapi import HTTPException

from app.services.risk_scoring_service import get_all_site_risks
from app.utils.data_loader import load_json_file


def get_all_studies() -> List[Dict[str, Any]]:
    studies = load_json_file("data/sample-studies.json")

    return [
        {
            "studyId": study["studyId"],
            "title": study["title"],
            "phase": study["phase"],
            "indication": study["indication"],
            "sponsor": study["sponsor"],
        }
        for study in studies
    ]


def get_study_by_id(study_id: str) -> Dict[str, Any]:
    studies = load_json_file("data/sample-studies.json")

    for study in studies:
        if study["studyId"] == study_id:
            return study

    raise HTTPException(status_code=404, detail=f"Study not found: {study_id}")


def get_sites_by_study_id(study_id: str) -> List[Dict[str, Any]]:
    get_study_by_id(study_id)

    sites = load_json_file("data/synthetic-sites.json")

    return [site for site in sites if site["studyId"] == study_id]


def get_risk_sites_by_study_id(study_id: str) -> List[Dict[str, Any]]:
    """
    Returns site information combined with calculated risk score for a specific study.
    This endpoint is designed for the frontend Site Risk Dashboard.
    """
    sites = get_sites_by_study_id(study_id)
    site_risks = get_all_site_risks()

    risk_by_site_id = {
        risk["siteId"]: risk for risk in site_risks if risk["studyId"] == study_id
    }

    risk_sites: List[Dict[str, Any]] = []

    for site in sites:
        risk = risk_by_site_id.get(site["siteId"])

        risk_sites.append(
            {
                **site,
                "riskScore": risk["riskScore"] if risk else 0,
                "riskLevel": risk["riskLevel"] if risk else "Low",
                "riskFactors": risk["riskFactors"] if risk else [],
            }
        )

    return risk_sites
