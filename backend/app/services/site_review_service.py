from typing import Any, Dict, List

from fastapi import HTTPException

from app.services.essential_document_service import get_essential_document_readiness
from app.services.icf_service import get_icf_version_check
from app.services.monitoring_report_service import get_monitoring_report_draft
from app.services.protocol_deviation_service import get_protocol_deviation_summary
from app.services.study_service import get_risk_sites_by_study_id, get_study_by_id


def get_site_risk_summary(study_id: str, site_id: str) -> Dict[str, Any]:
    risk_sites = get_risk_sites_by_study_id(study_id)

    for site in risk_sites:
        if site["siteId"] == site_id:
            return site

    raise HTTPException(
        status_code=404,
        detail=f"Site not found for study {study_id}: {site_id}",
    )


def build_site_review_modules(
    study_id: str,
    site_id: str,
    essential_documents: Dict[str, Any],
    protocol_deviations: Dict[str, Any],
    icf_version_check: Dict[str, Any],
    monitoring_report_draft: Dict[str, Any],
) -> List[Dict[str, str]]:
    return [
        {
            "title": "Monitoring Report Draft",
            "description": "Review generated IMV-style monitoring report draft based on site risk and findings.",
            "href": f"/studies/{study_id}/sites/{site_id}/monitoring-report",
            "statusLabel": f"{monitoring_report_draft['riskLevel']} risk",
        },
        {
            "title": "Essential Document Readiness",
            "description": "Check missing, pending, expired, and ready essential site documents.",
            "href": f"/studies/{study_id}/sites/{site_id}/essential-documents",
            "statusLabel": f"{essential_documents['readinessScore']}% ready",
        },
        {
            "title": "Protocol Deviation Tracker",
            "description": "Review deviation category, severity, status, root cause, corrective action, and preventive action.",
            "href": f"/studies/{study_id}/sites/{site_id}/protocol-deviations",
            "statusLabel": f"{protocol_deviations['openDeviations']} open",
        },
        {
            "title": "ICF Version Control Check",
            "description": "Verify whether subject consent records match the effective ICF version on consent date.",
            "href": f"/studies/{study_id}/sites/{site_id}/icf-version-check",
            "statusLabel": f"{icf_version_check['issueConsents']} issue(s)",
        },
    ]


def get_site_review_summary(study_id: str, site_id: str) -> Dict[str, Any]:
    study = get_study_by_id(study_id)
    site = get_site_risk_summary(study_id, site_id)

    essential_documents = get_essential_document_readiness(study_id, site_id)
    protocol_deviations = get_protocol_deviation_summary(study_id, site_id)
    icf_version_check = get_icf_version_check(study_id, site_id)
    monitoring_report_draft = get_monitoring_report_draft(study_id, site_id)

    return {
        "study": {
            "studyId": study["studyId"],
            "title": study["title"],
            "phase": study["phase"],
            "indication": study["indication"],
            "sponsor": study["sponsor"],
        },
        "site": site,
        "essentialDocuments": essential_documents,
        "protocolDeviations": protocol_deviations,
        "icfVersionCheck": icf_version_check,
        "monitoringReportDraft": monitoring_report_draft,
        "modules": build_site_review_modules(
            study_id=study_id,
            site_id=site_id,
            essential_documents=essential_documents,
            protocol_deviations=protocol_deviations,
            icf_version_check=icf_version_check,
            monitoring_report_draft=monitoring_report_draft,
        ),
    }
