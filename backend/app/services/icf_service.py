from datetime import date
from typing import Any, Dict, List, Optional

from fastapi import HTTPException

from app.repositories.icf_repository import (
    get_icf_versions_by_study_from_supabase,
    get_subject_consents_by_site_from_supabase,
)
from app.services.study_service import get_risk_sites_by_study_id


def get_site_name_from_risk_sites(study_id: str, site_id: str) -> str:
    risk_sites = get_risk_sites_by_study_id(study_id)

    for site in risk_sites:
        if site["siteId"] == site_id:
            return site["siteName"]

    raise HTTPException(
        status_code=404,
        detail=f"Site not found for study {study_id}: {site_id}",
    )


def parse_date(value: str) -> date:
    return date.fromisoformat(value)


def find_expected_icf_version(
    icf_versions: List[Dict[str, Any]],
    consent_date: str,
) -> Optional[Dict[str, Any]]:
    consent_dt = parse_date(consent_date)

    eligible_versions = [
        version
        for version in icf_versions
        if parse_date(version["effectiveDate"]) <= consent_dt
    ]

    if not eligible_versions:
        return None

    return sorted(
        eligible_versions,
        key=lambda item: parse_date(item["effectiveDate"]),
        reverse=True,
    )[0]


def check_subject_consent(
    consent: Dict[str, Any],
    icf_versions: List[Dict[str, Any]],
) -> Dict[str, Any]:
    expected_version = find_expected_icf_version(
        icf_versions=icf_versions,
        consent_date=consent["consentDate"],
    )

    if expected_version is None:
        return {
            "consentId": consent["consentId"],
            "subjectCode": consent["subjectCode"],
            "signedIcfVersion": consent["signedIcfVersion"],
            "consentDate": consent["consentDate"],
            "expectedIcfVersion": None,
            "status": "Issue",
            "issueType": "Consent Before Effective ICF",
            "message": "No approved ICF version was effective on the consent date.",
        }

    expected_version_value = expected_version["version"]

    if consent["signedIcfVersion"] != expected_version_value:
        return {
            "consentId": consent["consentId"],
            "subjectCode": consent["subjectCode"],
            "signedIcfVersion": consent["signedIcfVersion"],
            "consentDate": consent["consentDate"],
            "expectedIcfVersion": expected_version_value,
            "status": "Issue",
            "issueType": "Outdated ICF Version",
            "message": (
                f"Subject signed ICF v{consent['signedIcfVersion']}, "
                f"but expected ICF v{expected_version_value} was effective "
                f"on the consent date."
            ),
        }

    return {
        "consentId": consent["consentId"],
        "subjectCode": consent["subjectCode"],
        "signedIcfVersion": consent["signedIcfVersion"],
        "consentDate": consent["consentDate"],
        "expectedIcfVersion": expected_version_value,
        "status": "Valid",
        "issueType": None,
        "message": "Subject consent version is consistent with the effective ICF version.",
    }


def get_icf_version_check(
    study_id: str,
    site_id: str,
) -> Dict[str, Any]:
    site_name = get_site_name_from_risk_sites(study_id, site_id)

    icf_versions = get_icf_versions_by_study_from_supabase(study_id)
    consents = get_subject_consents_by_site_from_supabase(
        study_id=study_id,
        site_id=site_id,
    )

    checks = [check_subject_consent(consent, icf_versions) for consent in consents]

    issue_count = sum(1 for check in checks if check["status"] == "Issue")

    return {
        "studyId": study_id,
        "siteId": site_id,
        "siteName": site_name,
        "totalConsents": len(consents),
        "validConsents": len(consents) - issue_count,
        "issueConsents": issue_count,
        "icfVersions": icf_versions,
        "consents": consents,
        "checks": checks,
    }
