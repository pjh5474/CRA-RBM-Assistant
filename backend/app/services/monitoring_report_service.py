from typing import Any, Dict, List

from fastapi import HTTPException

from app.services.action_item_service import generate_action_items_for_risk_factors
from app.services.study_service import get_risk_sites_by_study_id, get_study_by_id


RISK_FACTOR_CATEGORY_MAP = {
    "High open query count": "Query Management",
    "Moderate open query count": "Query Management",
    "Long query aging": "Query Management",
    "Moderate query aging": "Query Management",
    "Multiple protocol deviations": "Protocol Compliance",
    "Protocol deviation trend": "Protocol Compliance",
    "SAE reporting delay": "Safety Reporting",
    "Missing essential documents": "Essential Documents",
    "IP accountability issue": "Investigational Product",
    "ICF issue": "Informed Consent",
}


RISK_FACTOR_FINDING_MAP = {
    "High open query count": "A high number of open queries was identified at this site.",
    "Moderate open query count": "A moderate number of open queries was identified at this site.",
    "Long query aging": "Long query aging was identified, indicating delayed query resolution.",
    "Moderate query aging": "Moderate query aging was identified and should be monitored.",
    "Multiple protocol deviations": "Multiple protocol deviations were identified at this site.",
    "Protocol deviation trend": "A protocol deviation trend was identified and should be reviewed.",
    "SAE reporting delay": "A delayed SAE reporting case was identified.",
    "Missing essential documents": "One or more missing essential documents were identified.",
    "IP accountability issue": "An investigational product accountability issue was identified.",
    "ICF issue": "An informed consent-related issue was identified.",
}


def build_report_findings(risk_factors: List[str]) -> List[Dict[str, str]]:
    action_items = generate_action_items_for_risk_factors(risk_factors)

    action_by_factor = {
        item["riskFactor"]: item["recommendedAction"] for item in action_items
    }

    findings: List[Dict[str, str]] = []

    for risk_factor in risk_factors:
        findings.append(
            {
                "category": RISK_FACTOR_CATEGORY_MAP.get(
                    risk_factor,
                    "General Monitoring Finding",
                ),
                "finding": RISK_FACTOR_FINDING_MAP.get(
                    risk_factor,
                    f"{risk_factor} was identified and should be reviewed.",
                ),
                "recommendedAction": action_by_factor.get(
                    risk_factor,
                    "Review this issue with the site and determine appropriate follow-up actions.",
                ),
            }
        )

    return findings


def build_report_summary(
    study: Dict[str, Any],
    site: Dict[str, Any],
) -> str:
    risk_factors = site["riskFactors"]

    if risk_factors:
        factor_summary = ", ".join(risk_factors)
    else:
        factor_summary = "no major risk factors"

    return (
        f"Site {site['siteName']} was classified as {site['riskLevel']} risk "
        f"with a risk score of {site['riskScore']} for study {study['studyId']}. "
        f"The current monitoring review identified {factor_summary}. "
        "This draft summarizes key CRA follow-up considerations based on synthetic monitoring data."
    )


def get_monitoring_report_draft(
    study_id: str,
    site_id: str,
) -> Dict[str, Any]:
    study = get_study_by_id(study_id)
    risk_sites = get_risk_sites_by_study_id(study_id)

    target_site = None

    for site in risk_sites:
        if site["siteId"] == site_id:
            target_site = site
            break

    if not target_site:
        raise HTTPException(
            status_code=404,
            detail=f"Site not found for study {study_id}: {site_id}",
        )

    return {
        "studyId": study["studyId"],
        "studyTitle": study["title"],
        "siteId": target_site["siteId"],
        "siteName": target_site["siteName"],
        "principalInvestigator": target_site["principalInvestigator"],
        "visitType": "Interim Monitoring Visit",
        "riskScore": target_site["riskScore"],
        "riskLevel": target_site["riskLevel"],
        "summary": build_report_summary(study, target_site),
        "findings": build_report_findings(target_site["riskFactors"]),
        "limitations": [
            "This report is generated from synthetic monitoring data.",
            "This draft does not replace CRA judgment or sponsor-approved monitoring report templates.",
            "This report is not intended for regulatory submission or real clinical trial operation.",
        ],
    }
