from typing import Any, Dict, List

from app.services.study_service import get_risk_sites_by_study_id


ACTION_RECOMMENDATIONS = {
    "High open query count": "Follow up with site staff to prioritize open query resolution and confirm the expected resolution timeline.",
    "Moderate open query count": "Review open query status with site staff and monitor whether additional support is needed.",
    "Long query aging": "Identify aged queries and request site response or clarification for delayed items.",
    "Moderate query aging": "Monitor query aging trend and remind site staff of timely query response expectations.",
    "Multiple protocol deviations": "Review deviation root causes and assess whether corrective and preventive actions are required.",
    "Protocol deviation trend": "Discuss recurring deviation patterns with site staff and consider targeted retraining.",
    "SAE reporting delay": "Review SAE reporting process with site staff and confirm whether safety reporting retraining is required.",
    "Missing essential documents": "Request essential document reconciliation and confirm site file readiness.",
    "IP accountability issue": "Review IP dispensing, return, storage, and accountability records with the site.",
    "ICF issue": "Review informed consent process, ICF version control, and signature date documentation.",
}


def generate_action_items_for_risk_factors(
    risk_factors: List[str],
) -> List[Dict[str, str]]:
    action_items: List[Dict[str, str]] = []

    for risk_factor in risk_factors:
        recommended_action = ACTION_RECOMMENDATIONS.get(
            risk_factor,
            "Review this risk factor with the site and determine appropriate follow-up actions.",
        )

        action_items.append(
            {
                "riskFactor": risk_factor,
                "recommendedAction": recommended_action,
            }
        )

    return action_items


def get_action_items_by_study_id(study_id: str) -> List[Dict[str, Any]]:
    risk_sites = get_risk_sites_by_study_id(study_id)

    site_action_items: List[Dict[str, Any]] = []

    for site in risk_sites:
        # Low risk site는 action item을 생성하지 않고 제외합니다.
        if site["riskLevel"] == "Low":
            continue

        site_action_items.append(
            {
                "siteId": site["siteId"],
                "studyId": site["studyId"],
                "siteName": site["siteName"],
                "riskScore": site["riskScore"],
                "riskLevel": site["riskLevel"],
                "actionItems": generate_action_items_for_risk_factors(
                    site["riskFactors"]
                ),
            }
        )

    return site_action_items
