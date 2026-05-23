from typing import Any, Dict, List

from app.repositories.monitoring_metric_repository import (
    upsert_monitoring_metrics_to_supabase,
)
from app.repositories.site_repository import upsert_sites_to_supabase
from app.repositories.essential_document_repository import (
    upsert_essential_documents_to_supabase,
)
from app.repositories.protocol_deviation_repository import (
    upsert_protocol_deviations_to_supabase,
)


def build_demo_sites_for_imported_study(study: Dict[str, Any]) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    return [
        {
            "siteId": f"{study_id}-SITE-001",
            "studyId": study_id,
            "siteName": "Imported Study Demo Site 01",
            "principalInvestigator": "Dr. Demo Kim",
            "country": "Korea",
            "status": "Active",
            "activationDate": "2026-05-01",
            "targetEnrollment": 12,
            "currentEnrollment": 8,
        },
        {
            "siteId": f"{study_id}-SITE-002",
            "studyId": study_id,
            "siteName": "Imported Study Demo Site 02",
            "principalInvestigator": "Dr. Demo Lee",
            "country": "Korea",
            "status": "Active",
            "activationDate": "2026-05-03",
            "targetEnrollment": 10,
            "currentEnrollment": 4,
        },
        {
            "siteId": f"{study_id}-SITE-003",
            "studyId": study_id,
            "siteName": "Imported Study Demo Site 03",
            "principalInvestigator": "Dr. Demo Park",
            "country": "Korea",
            "status": "Active",
            "activationDate": "2026-05-05",
            "targetEnrollment": 15,
            "currentEnrollment": 13,
        },
    ]


def build_demo_monitoring_metrics_for_imported_study(
    study: Dict[str, Any],
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    return [
        {
            "metricId": f"{study_id}-METRIC-001",
            "siteId": f"{study_id}-SITE-001",
            "studyId": study_id,
            "openQueries": 5,
            "queryAgingDays": 4,
            "protocolDeviations": 1,
            "saeReportingDelayCount": 0,
            "missingEssentialDocuments": 0,
            "ipAccountabilityIssues": 0,
            "icfIssues": 0,
            "lastMonitoringVisitDate": "2026-05-10",
        },
        {
            "metricId": f"{study_id}-METRIC-002",
            "siteId": f"{study_id}-SITE-002",
            "studyId": study_id,
            "openQueries": 14,
            "queryAgingDays": 16,
            "protocolDeviations": 4,
            "saeReportingDelayCount": 1,
            "missingEssentialDocuments": 2,
            "ipAccountabilityIssues": 1,
            "icfIssues": 1,
            "lastMonitoringVisitDate": "2026-05-09",
        },
        {
            "metricId": f"{study_id}-METRIC-003",
            "siteId": f"{study_id}-SITE-003",
            "studyId": study_id,
            "openQueries": 8,
            "queryAgingDays": 9,
            "protocolDeviations": 2,
            "saeReportingDelayCount": 0,
            "missingEssentialDocuments": 1,
            "ipAccountabilityIssues": 0,
            "icfIssues": 0,
            "lastMonitoringVisitDate": "2026-05-11",
        },
    ]


def create_demo_operational_data_for_imported_study(
    study: Dict[str, Any],
) -> bool:
    demo_sites = build_demo_sites_for_imported_study(study)
    demo_metrics = build_demo_monitoring_metrics_for_imported_study(study)

    upsert_sites_to_supabase(demo_sites)
    upsert_monitoring_metrics_to_supabase(demo_metrics)
    create_demo_essential_documents_for_imported_study(study)
    create_demo_protocol_deviations_for_imported_study(study)

    return True


ESSENTIAL_DOCUMENT_TYPES = [
    "IRB Approval Letter",
    "Approved Protocol",
    "Approved ICF",
    "Investigator CV",
    "GCP Certificate",
    "Delegation Log",
    "Training Log",
    "IP Accountability Log",
]


def build_demo_essential_documents_for_site(
    study_id: str,
    site_id: str,
    site_index: int,
) -> List[Dict[str, Any]]:
    documents: List[Dict[str, Any]] = []

    for index, document_type in enumerate(ESSENTIAL_DOCUMENT_TYPES, start=1):
        status = "Ready"
        comment = "Document confirmed as available for demo readiness review."

        if site_index == 2 and document_type in [
            "Delegation Log",
            "IP Accountability Log",
        ]:
            status = "Missing"
            comment = "Document is missing and requires CRA follow-up."

        if site_index == 2 and document_type == "GCP Certificate":
            status = "Expired"
            comment = (
                "GCP certificate is expired and requires updated training evidence."
            )

        if site_index == 3 and document_type == "Training Log":
            status = "Pending"
            comment = "Training log is pending final confirmation."

        document_id = f"{site_id}-DOC-{index:03d}"

        documents.append(
            {
                "documentId": document_id,
                "studyId": study_id,
                "siteId": site_id,
                "documentType": document_type,
                "required": True,
                "status": status,
                "version": "1.0" if status != "Missing" else None,
                "documentDate": "2026-05-01" if status != "Missing" else None,
                "expiryDate": "2026-05-15" if status == "Expired" else None,
                "comment": comment,
            }
        )

    return documents


def create_demo_essential_documents_for_imported_study(
    study: Dict[str, Any],
) -> bool:
    study_id = study["studyId"]

    all_documents: List[Dict[str, Any]] = []

    for site_index in range(1, 4):
        site_id = f"{study_id}-SITE-{site_index:03d}"
        all_documents.extend(
            build_demo_essential_documents_for_site(
                study_id=study_id,
                site_id=site_id,
                site_index=site_index,
            )
        )

    upsert_essential_documents_to_supabase(all_documents)

    return True


def build_demo_protocol_deviations_for_imported_study(
    study: Dict[str, Any],
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    return [
        {
            "deviationId": f"{study_id}-SITE-002-DEV-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "subjectCode": "SUBJ-002-001",
            "category": "Visit Window Deviation",
            "severity": "Major",
            "status": "Open",
            "description": "The Week 12 visit was performed outside the allowed visit window.",
            "detectedDate": "2026-05-12",
            "rootCause": "Subject scheduling delay",
            "correctiveAction": "Site documented the reason for the delayed visit and notified the CRA.",
            "preventiveAction": "Site staff should review visit window requirements before scheduling future visits.",
        },
        {
            "deviationId": f"{study_id}-SITE-002-DEV-002",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "subjectCode": "SUBJ-002-002",
            "category": "Missing Assessment",
            "severity": "Minor",
            "status": "In Review",
            "description": "A protocol-required assessment was not completed at the scheduled visit.",
            "detectedDate": "2026-05-13",
            "rootCause": "Assessment checklist was not reviewed before the visit.",
            "correctiveAction": "Site is reviewing source documentation to confirm whether assessment can be completed or documented as missed.",
            "preventiveAction": "Site staff should use the visit checklist before each subject visit.",
        },
        {
            "deviationId": f"{study_id}-SITE-002-DEV-003",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "subjectCode": "SUBJ-002-003",
            "category": "SAE Reporting Delay",
            "severity": "Critical",
            "status": "Open",
            "description": "SAE reporting was delayed beyond the expected reporting timeline.",
            "detectedDate": "2026-05-14",
            "rootCause": "Site staff were unclear on immediate SAE reporting escalation process.",
            "correctiveAction": "CRA should review SAE reporting process with site staff and confirm escalation contact information.",
            "preventiveAction": "Safety reporting retraining should be considered for delegated site staff.",
        },
        {
            "deviationId": f"{study_id}-SITE-003-DEV-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-003",
            "subjectCode": "SUBJ-003-001",
            "category": "Protocol Deviation Trend",
            "severity": "Minor",
            "status": "Resolved",
            "description": "Minor documentation inconsistency was identified and resolved during monitoring review.",
            "detectedDate": "2026-05-11",
            "rootCause": "Source note template was inconsistently completed.",
            "correctiveAction": "Site corrected the source note and filed clarification.",
            "preventiveAction": "Site staff were reminded to complete source templates consistently.",
        },
    ]


def create_demo_protocol_deviations_for_imported_study(
    study: Dict[str, Any],
) -> bool:
    demo_deviations = build_demo_protocol_deviations_for_imported_study(study)
    upsert_protocol_deviations_to_supabase(demo_deviations)

    return True
