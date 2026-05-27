from typing import Any, Dict, List

from fastapi import HTTPException

from app.services.action_item_service import generate_action_items_for_risk_factors
from app.services.essential_document_service import get_essential_document_readiness
from app.services.icf_service import get_icf_version_check
from app.services.protocol_deviation_service import get_protocol_deviation_summary
from app.services.study_service import get_risk_sites_by_study_id, get_study_by_id
from app.services.delegation_training_service import get_delegation_training_check


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


def build_risk_factor_findings(risk_factors: List[str]) -> List[Dict[str, str]]:
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


def build_essential_document_findings(
    essential_documents: Dict[str, Any],
) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []

    if essential_documents["missingDocuments"] > 0:
        findings.append(
            {
                "category": "Essential Documents",
                "finding": (
                    f"{essential_documents['missingDocuments']} missing essential "
                    "document(s) were identified during site readiness review."
                ),
                "recommendedAction": (
                    "Request site file reconciliation and confirm that missing "
                    "essential documents are collected, filed, and tracked to completion."
                ),
            }
        )

    if essential_documents["expiredDocuments"] > 0:
        findings.append(
            {
                "category": "Essential Documents",
                "finding": (
                    f"{essential_documents['expiredDocuments']} expired essential "
                    "document(s) were identified."
                ),
                "recommendedAction": (
                    "Request updated document evidence and confirm whether retraining "
                    "or updated qualification documentation is required."
                ),
            }
        )

    if essential_documents["pendingDocuments"] > 0:
        findings.append(
            {
                "category": "Essential Documents",
                "finding": (
                    f"{essential_documents['pendingDocuments']} pending essential "
                    "document(s) require confirmation."
                ),
                "recommendedAction": (
                    "Follow up with site staff to confirm pending document status and "
                    "expected completion timeline."
                ),
            }
        )

    return findings


def build_protocol_deviation_findings(
    protocol_deviations: Dict[str, Any],
) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []

    if protocol_deviations["criticalDeviations"] > 0:
        findings.append(
            {
                "category": "Protocol Compliance",
                "finding": (
                    f"{protocol_deviations['criticalDeviations']} critical protocol "
                    "deviation(s) were identified."
                ),
                "recommendedAction": (
                    "Review critical deviation(s), confirm escalation requirements, "
                    "and assess whether immediate corrective and preventive actions are needed."
                ),
            }
        )

    if protocol_deviations["majorDeviations"] > 0:
        findings.append(
            {
                "category": "Protocol Compliance",
                "finding": (
                    f"{protocol_deviations['majorDeviations']} major protocol "
                    "deviation(s) were identified."
                ),
                "recommendedAction": (
                    "Review root cause, corrective action, and preventive action with "
                    "site staff, and track open items until resolution."
                ),
            }
        )

    if protocol_deviations["openDeviations"] > 0:
        findings.append(
            {
                "category": "Protocol Compliance",
                "finding": (
                    f"{protocol_deviations['openDeviations']} protocol deviation(s) "
                    "remain open."
                ),
                "recommendedAction": (
                    "Confirm owner, due date, and documentation status for each open "
                    "deviation."
                ),
            }
        )

    return findings


def build_icf_findings(
    icf_version_check: Dict[str, Any],
) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []

    if icf_version_check["issueConsents"] > 0:
        findings.append(
            {
                "category": "Informed Consent",
                "finding": (
                    f"{icf_version_check['issueConsents']} informed consent version "
                    "issue(s) were identified."
                ),
                "recommendedAction": (
                    "Review ICF version history, consent date, and source documentation. "
                    "Confirm whether outdated ICF version use requires documentation correction, "
                    "site retraining, or escalation."
                ),
            }
        )

    return findings


def build_delegation_training_findings(
    delegation_training_check: Dict[str, Any],
) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []

    if delegation_training_check["missingTrainingRecords"] > 0:
        findings.append(
            {
                "category": "Delegation and Training",
                "finding": (
                    f"{delegation_training_check['missingTrainingRecords']} "
                    "delegation/training record(s) have missing GCP or protocol "
                    "training evidence."
                ),
                "recommendedAction": (
                    "Review delegation log and training evidence with site staff. "
                    "Confirm whether missing training documentation should be filed "
                    "or whether retraining is required."
                ),
            }
        )

    if delegation_training_check["trainingAfterDelegationRecords"] > 0:
        findings.append(
            {
                "category": "Delegation and Training",
                "finding": (
                    f"{delegation_training_check['trainingAfterDelegationRecords']} "
                    "record(s) show training completed after delegation start date."
                ),
                "recommendedAction": (
                    "Reconcile delegation start date against GCP/protocol training "
                    "completion dates and determine whether delegation timing requires "
                    "documentation correction or site retraining."
                ),
            }
        )

    return findings


def build_report_summary(
    study: Dict[str, Any],
    site: Dict[str, Any],
    essential_documents: Dict[str, Any],
    protocol_deviations: Dict[str, Any],
    icf_version_check: Dict[str, Any],
    delegation_training_check: Dict[str, Any],
) -> str:
    return (
        f"Site {site['siteName']} was classified as {site['riskLevel']} risk "
        f"with a risk score of {site['riskScore']} for study {study['studyId']}. "
        f"Essential document readiness was {essential_documents['readinessScore']}%. "
        f"The site has {protocol_deviations['openDeviations']} open protocol deviation(s), "
        f"{icf_version_check['issueConsents']} informed consent version issue(s), "
        f"and {delegation_training_check['issueRecords']} delegation/training issue(s). "
        "This monitoring report draft summarizes key CRA follow-up considerations "
        "based on synthetic monitoring, document readiness, deviation, and consent data."
    )


def build_follow_up_actions(
    findings: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    follow_up_actions: List[Dict[str, str]] = []

    high_priority_categories = {
        "Safety Reporting",
        "Informed Consent",
        "Protocol Compliance",
        "Delegation and Training",
    }

    for finding in findings:
        category = finding["category"]
        priority = "High" if category in high_priority_categories else "Medium"

        follow_up_actions.append(
            {
                "category": category,
                "action": finding["recommendedAction"],
                "priority": priority,
            }
        )

    return follow_up_actions


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

    essential_documents = get_essential_document_readiness(study_id, site_id)
    protocol_deviations = get_protocol_deviation_summary(study_id, site_id)
    icf_version_check = get_icf_version_check(study_id, site_id)
    delegation_training_check = get_delegation_training_check(study_id, site_id)

    findings = (
        build_risk_factor_findings(target_site["riskFactors"])
        + build_essential_document_findings(essential_documents)
        + build_protocol_deviation_findings(protocol_deviations)
        + build_icf_findings(icf_version_check)
        + build_delegation_training_findings(delegation_training_check)
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
        "summary": build_report_summary(
            study=study,
            site=target_site,
            essential_documents=essential_documents,
            protocol_deviations=protocol_deviations,
            icf_version_check=icf_version_check,
            delegation_training_check=delegation_training_check,
        ),
        "riskSummary": {
            "riskScore": target_site["riskScore"],
            "riskLevel": target_site["riskLevel"],
            "riskFactors": target_site["riskFactors"],
        },
        "essentialDocumentSummary": {
            "readinessScore": essential_documents["readinessScore"],
            "totalDocuments": essential_documents["totalDocuments"],
            "readyDocuments": essential_documents["readyDocuments"],
            "missingDocuments": essential_documents["missingDocuments"],
            "pendingDocuments": essential_documents["pendingDocuments"],
            "expiredDocuments": essential_documents["expiredDocuments"],
        },
        "protocolDeviationSummary": {
            "totalDeviations": protocol_deviations["totalDeviations"],
            "openDeviations": protocol_deviations["openDeviations"],
            "inReviewDeviations": protocol_deviations["inReviewDeviations"],
            "resolvedDeviations": protocol_deviations["resolvedDeviations"],
            "majorDeviations": protocol_deviations["majorDeviations"],
            "criticalDeviations": protocol_deviations["criticalDeviations"],
        },
        "icfSummary": {
            "totalConsents": icf_version_check["totalConsents"],
            "validConsents": icf_version_check["validConsents"],
            "issueConsents": icf_version_check["issueConsents"],
        },
        "delegationTrainingSummary": {
            "totalRecords": delegation_training_check["totalRecords"],
            "validRecords": delegation_training_check["validRecords"],
            "issueRecords": delegation_training_check["issueRecords"],
            "missingTrainingRecords": delegation_training_check[
                "missingTrainingRecords"
            ],
            "trainingAfterDelegationRecords": delegation_training_check[
                "trainingAfterDelegationRecords"
            ],
        },
        "findings": findings,
        "followUpActions": build_follow_up_actions(findings),
        "limitations": [
            "This report is generated from synthetic monitoring and site review data.",
            "This draft does not replace CRA judgment or sponsor-approved monitoring report templates.",
            "This report is not intended for regulatory submission or real clinical trial operation.",
            "This project demonstrates data structuring and CRA workflow understanding for portfolio purposes.",
        ],
    }
