from typing import Any, Dict, List

from app.services.action_item_service import generate_action_items_for_risk_factors
from app.services.study_service import get_all_studies, get_risk_sites_by_study_id


def get_high_risk_site_alerts(
    include_medium: bool = True,
) -> List[Dict[str, Any]]:
    """
    Returns medium/high risk site alerts for n8n or external automation workflows.
    """
    studies = get_all_studies()
    alerts: List[Dict[str, Any]] = []

    target_risk_levels = ["High", "Medium"] if include_medium else ["High"]

    for study in studies:
        study_id = study["studyId"]
        study_title = study["title"]

        risk_sites = get_risk_sites_by_study_id(study_id)

        for site in risk_sites:
            if site["riskLevel"] not in target_risk_levels:
                continue

            action_items = generate_action_items_for_risk_factors(site["riskFactors"])

            alerts.append(
                {
                    "studyId": study_id,
                    "studyTitle": study_title,
                    "siteId": site["siteId"],
                    "siteName": site["siteName"],
                    "riskScore": site["riskScore"],
                    "riskLevel": site["riskLevel"],
                    "riskFactors": site["riskFactors"],
                    "recommendedActions": [
                        item["recommendedAction"] for item in action_items
                    ],
                }
            )

    return alerts
