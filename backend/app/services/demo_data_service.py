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
from app.repositories.icf_repository import (
    upsert_icf_versions_to_supabase,
    upsert_subject_consents_to_supabase,
)
from app.repositories.delegation_training_repository import (
    upsert_delegation_training_records_to_supabase,
    upsert_site_staff_to_supabase,
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
    create_demo_icf_data_for_imported_study(study)
    create_demo_delegation_training_data_for_imported_study(study)

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


def build_demo_icf_versions_for_imported_study(
    study: Dict[str, Any],
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    return [
        {
            "icfVersionId": f"{study_id}-ICF-V1",
            "studyId": study_id,
            "version": "1.0",
            "irbApprovalDate": "2026-04-01",
            "effectiveDate": "2026-04-05",
            "status": "Superseded",
        },
        {
            "icfVersionId": f"{study_id}-ICF-V2",
            "studyId": study_id,
            "version": "2.0",
            "irbApprovalDate": "2026-05-01",
            "effectiveDate": "2026-05-05",
            "status": "Active",
        },
    ]


def build_demo_subject_consents_for_imported_study(
    study: Dict[str, Any],
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    return [
        {
            "consentId": f"{study_id}-SITE-001-CONSENT-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-001",
            "subjectCode": "SUBJ-001-001",
            "signedIcfVersion": "2.0",
            "consentDate": "2026-05-10",
            "consentProcessNote": "Consent version is consistent with active ICF.",
        },
        {
            "consentId": f"{study_id}-SITE-002-CONSENT-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "subjectCode": "SUBJ-002-001",
            "signedIcfVersion": "1.0",
            "consentDate": "2026-05-10",
            "consentProcessNote": "Subject signed outdated ICF version after v2.0 became effective.",
        },
        {
            "consentId": f"{study_id}-SITE-002-CONSENT-002",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "subjectCode": "SUBJ-002-002",
            "signedIcfVersion": "2.0",
            "consentDate": "2026-05-12",
            "consentProcessNote": "Consent version is consistent with active ICF.",
        },
        {
            "consentId": f"{study_id}-SITE-003-CONSENT-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-003",
            "subjectCode": "SUBJ-003-001",
            "signedIcfVersion": "1.0",
            "consentDate": "2026-04-20",
            "consentProcessNote": "Consent version was valid before v2.0 effective date.",
        },
    ]


def create_demo_icf_data_for_imported_study(study: Dict[str, Any]) -> bool:
    icf_versions = build_demo_icf_versions_for_imported_study(study)
    consents = build_demo_subject_consents_for_imported_study(study)

    upsert_icf_versions_to_supabase(icf_versions)
    upsert_subject_consents_to_supabase(consents)

    return True


def build_demo_site_staff_for_imported_study(
    study: Dict[str, Any],
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    staff_members: List[Dict[str, Any]] = []

    for site_index in range(1, 4):
        site_id = f"{study_id}-SITE-{site_index:03d}"

        staff_members.extend(
            [
                {
                    "staffId": f"{site_id}-STAFF-001",
                    "studyId": study_id,
                    "siteId": site_id,
                    "staffName": f"CRC Demo Staff {site_index}-01",
                    "role": "Study Coordinator",
                    "isActive": True,
                },
                {
                    "staffId": f"{site_id}-STAFF-002",
                    "studyId": study_id,
                    "siteId": site_id,
                    "staffName": f"Sub-I Demo Staff {site_index}-02",
                    "role": "Sub-Investigator",
                    "isActive": True,
                },
            ]
        )

    return staff_members


def build_demo_delegation_training_records_for_imported_study(
    study: Dict[str, Any],
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    return [
        {
            "recordId": f"{study_id}-SITE-001-DTR-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-001",
            "staffId": f"{study_id}-SITE-001-STAFF-001",
            "delegatedTask": "Informed Consent Process",
            "delegationStartDate": "2026-05-10",
            "delegationEndDate": None,
            "gcpTrainingDate": "2026-04-20",
            "protocolTrainingDate": "2026-05-01",
            "trainingStatus": "Complete",
            "comment": "Training completed before delegation start date.",
        },
        {
            "recordId": f"{study_id}-SITE-002-DTR-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "staffId": f"{study_id}-SITE-002-STAFF-001",
            "delegatedTask": "Investigational Product Accountability",
            "delegationStartDate": "2026-05-01",
            "delegationEndDate": None,
            "gcpTrainingDate": "2026-04-15",
            "protocolTrainingDate": "2026-05-03",
            "trainingStatus": "Complete",
            "comment": "Protocol training completed after delegation start date.",
        },
        {
            "recordId": f"{study_id}-SITE-002-DTR-002",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-002",
            "staffId": f"{study_id}-SITE-002-STAFF-002",
            "delegatedTask": "Safety Reporting",
            "delegationStartDate": "2026-05-02",
            "delegationEndDate": None,
            "gcpTrainingDate": None,
            "protocolTrainingDate": "2026-04-28",
            "trainingStatus": "Missing",
            "comment": "GCP training evidence is missing.",
        },
        {
            "recordId": f"{study_id}-SITE-003-DTR-001",
            "studyId": study_id,
            "siteId": f"{study_id}-SITE-003",
            "staffId": f"{study_id}-SITE-003-STAFF-001",
            "delegatedTask": "Source Data Entry",
            "delegationStartDate": "2026-05-08",
            "delegationEndDate": None,
            "gcpTrainingDate": "2026-04-10",
            "protocolTrainingDate": "2026-04-25",
            "trainingStatus": "Complete",
            "comment": "Training dates are consistent with delegation start date.",
        },
    ]


def create_demo_delegation_training_data_for_imported_study(
    study: Dict[str, Any],
) -> bool:
    staff_members = build_demo_site_staff_for_imported_study(study)
    records = build_demo_delegation_training_records_for_imported_study(study)

    upsert_site_staff_to_supabase(staff_members)
    upsert_delegation_training_records_to_supabase(records)

    return True
