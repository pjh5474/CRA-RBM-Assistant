from typing import Any, Dict, List

from fastapi import HTTPException

from app.repositories.protocol_deviation_repository import (
    get_protocol_deviations_by_site_from_supabase,
)
from app.services.study_service import get_risk_sites_by_study_id


def count_by_field(
    deviations: List[Dict[str, Any]],
    field: str,
    value: str,
) -> int:
    return sum(1 for deviation in deviations if deviation[field] == value)


def get_site_name_from_risk_sites(study_id: str, site_id: str) -> str:
    risk_sites = get_risk_sites_by_study_id(study_id)

    for site in risk_sites:
        if site["siteId"] == site_id:
            return site["siteName"]

    raise HTTPException(
        status_code=404,
        detail=f"Site not found for study {study_id}: {site_id}",
    )


def get_protocol_deviation_summary(
    study_id: str,
    site_id: str,
) -> Dict[str, Any]:
    site_name = get_site_name_from_risk_sites(study_id, site_id)

    deviations = get_protocol_deviations_by_site_from_supabase(
        study_id=study_id,
        site_id=site_id,
    )

    return {
        "studyId": study_id,
        "siteId": site_id,
        "siteName": site_name,
        "totalDeviations": len(deviations),
        "openDeviations": count_by_field(deviations, "status", "Open"),
        "inReviewDeviations": count_by_field(deviations, "status", "In Review"),
        "resolvedDeviations": count_by_field(deviations, "status", "Resolved"),
        "minorDeviations": count_by_field(deviations, "severity", "Minor"),
        "majorDeviations": count_by_field(deviations, "severity", "Major"),
        "criticalDeviations": count_by_field(deviations, "severity", "Critical"),
        "deviations": deviations,
    }
