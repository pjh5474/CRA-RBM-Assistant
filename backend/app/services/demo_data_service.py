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
from app.utils.profile_metric_builder import build_profile_metric
from app.repositories.demo_data_repository import (
    delete_existing_demo_operational_data_by_study_id,
)

SCENARIO_PROFILE_DOCUMENT_READINESS = "DOCUMENT_READINESS_RISK"
SCENARIO_PROFILE_PROTOCOL_DEVIATION = "PROTOCOL_DEVIATION_RISK"
SCENARIO_PROFILE_ICF_VERSION = "ICF_VERSION_RISK"
SCENARIO_PROFILE_DELEGATION_TRAINING = "DELEGATION_TRAINING_RISK"
SCENARIO_PROFILE_BALANCED_HIGH_RISK = "BALANCED_HIGH_RISK"

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


def select_scenario_profile(study_id: str) -> str:
    profiles = [
        SCENARIO_PROFILE_DOCUMENT_READINESS,
        SCENARIO_PROFILE_PROTOCOL_DEVIATION,
        SCENARIO_PROFILE_ICF_VERSION,
        SCENARIO_PROFILE_DELEGATION_TRAINING,
        SCENARIO_PROFILE_BALANCED_HIGH_RISK,
    ]

    index = sum(ord(char) for char in study_id) % len(profiles)

    return profiles[index]


def replace_demo_operational_data_for_imported_study(
    study: Dict[str, Any],
) -> bool:
    study_id = study["studyId"]
    scenario_profile = select_scenario_profile(study_id)

    delete_existing_demo_operational_data_by_study_id(study_id)

    demo_sites = build_demo_sites_for_imported_study(study)
    demo_metrics = build_demo_monitoring_metrics_for_imported_study(
        study,
        scenario_profile,
    )

    upsert_sites_to_supabase(demo_sites)
    upsert_monitoring_metrics_to_supabase(demo_metrics)

    create_demo_essential_documents_for_imported_study(
        study,
        scenario_profile,
    )
    create_demo_protocol_deviations_for_imported_study(
        study,
        scenario_profile,
    )
    create_demo_icf_data_for_imported_study(
        study,
        scenario_profile,
    )
    create_demo_delegation_training_data_for_imported_study(
        study,
        scenario_profile,
    )

    return True


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
    scenario_profile: str,
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    if scenario_profile == SCENARIO_PROFILE_DOCUMENT_READINESS:
        return [
            build_profile_metric(
                study_id=study_id,
                site_index=1,
                open_queries=3,
                query_aging_days=5,
                protocol_deviations=0,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=2,
                open_queries=6,
                query_aging_days=9,
                protocol_deviations=1,
                sae_reporting_delay_count=0,
                missing_essential_documents=4,
                ip_accountability_issues=1,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=3,
                open_queries=2,
                query_aging_days=4,
                protocol_deviations=0,
                sae_reporting_delay_count=0,
                missing_essential_documents=1,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
        ]

    if scenario_profile == SCENARIO_PROFILE_PROTOCOL_DEVIATION:
        return [
            build_profile_metric(
                study_id=study_id,
                site_index=1,
                open_queries=4,
                query_aging_days=6,
                protocol_deviations=1,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=2,
                open_queries=9,
                query_aging_days=12,
                protocol_deviations=5,
                sae_reporting_delay_count=0,
                missing_essential_documents=1,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=3,
                open_queries=5,
                query_aging_days=8,
                protocol_deviations=2,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
        ]

    if scenario_profile == SCENARIO_PROFILE_ICF_VERSION:
        return [
            build_profile_metric(
                study_id=study_id,
                site_index=1,
                open_queries=2,
                query_aging_days=4,
                protocol_deviations=0,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=2,
                open_queries=5,
                query_aging_days=8,
                protocol_deviations=1,
                sae_reporting_delay_count=0,
                missing_essential_documents=1,
                ip_accountability_issues=0,
                icf_issues=2,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=3,
                open_queries=3,
                query_aging_days=5,
                protocol_deviations=0,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=1,
            ),
        ]

    if scenario_profile == SCENARIO_PROFILE_DELEGATION_TRAINING:
        return [
            build_profile_metric(
                study_id=study_id,
                site_index=1,
                open_queries=3,
                query_aging_days=6,
                protocol_deviations=0,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=2,
                open_queries=6,
                query_aging_days=10,
                protocol_deviations=1,
                sae_reporting_delay_count=0,
                missing_essential_documents=2,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=3,
                open_queries=4,
                query_aging_days=7,
                protocol_deviations=1,
                sae_reporting_delay_count=0,
                missing_essential_documents=1,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
        ]

    if scenario_profile == SCENARIO_PROFILE_BALANCED_HIGH_RISK:
        return [
            build_profile_metric(
                study_id=study_id,
                site_index=1,
                open_queries=5,
                query_aging_days=7,
                protocol_deviations=1,
                sae_reporting_delay_count=0,
                missing_essential_documents=0,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=2,
                open_queries=16,
                query_aging_days=15,
                protocol_deviations=4,
                sae_reporting_delay_count=1,
                missing_essential_documents=2,
                ip_accountability_issues=1,
                icf_issues=1,
            ),
            build_profile_metric(
                study_id=study_id,
                site_index=3,
                open_queries=8,
                query_aging_days=11,
                protocol_deviations=2,
                sae_reporting_delay_count=0,
                missing_essential_documents=1,
                ip_accountability_issues=0,
                icf_issues=0,
            ),
        ]

    return [
        build_profile_metric(
            study_id=study_id,
            site_index=1,
            open_queries=3,
            query_aging_days=5,
            protocol_deviations=0,
            sae_reporting_delay_count=0,
            missing_essential_documents=0,
            ip_accountability_issues=0,
            icf_issues=0,
        ),
        build_profile_metric(
            study_id=study_id,
            site_index=2,
            open_queries=12,
            query_aging_days=16,
            protocol_deviations=3,
            sae_reporting_delay_count=1,
            missing_essential_documents=2,
            ip_accountability_issues=1,
            icf_issues=1,
        ),
        build_profile_metric(
            study_id=study_id,
            site_index=3,
            open_queries=6,
            query_aging_days=9,
            protocol_deviations=1,
            sae_reporting_delay_count=0,
            missing_essential_documents=1,
            ip_accountability_issues=0,
            icf_issues=0,
        ),
    ]


def get_document_status_for_profile(
    scenario_profile: str,
    site_index: int,
    document_type: str,
) -> tuple[str, str]:
    status = "Ready"
    comment = "Document confirmed as available for demo readiness review."

    if scenario_profile == SCENARIO_PROFILE_DOCUMENT_READINESS:
        if site_index == 2 and document_type in [
            "Delegation Log",
            "Training Log",
            "IP Accountability Log",
        ]:
            return (
                "Missing",
                "Document is missing and requires CRA follow-up for site file readiness.",
            )

        if site_index == 2 and document_type == "GCP Certificate":
            return (
                "Expired",
                "GCP certificate is expired and requires updated training evidence.",
            )

        if site_index == 3 and document_type == "Approved ICF":
            return (
                "Pending",
                "Approved ICF filing status is pending confirmation.",
            )

    if scenario_profile == SCENARIO_PROFILE_PROTOCOL_DEVIATION:
        if site_index == 2 and document_type == "Delegation Log":
            return (
                "Pending",
                "Delegation log requires confirmation due to protocol deviation follow-up.",
            )

    if scenario_profile == SCENARIO_PROFILE_ICF_VERSION:
        if site_index == 2 and document_type == "Approved ICF":
            return (
                "Pending",
                "Approved ICF version filing requires confirmation due to consent version issue.",
            )

        if site_index == 3 and document_type == "Approved ICF":
            return (
                "Expired",
                "Approved ICF document appears outdated and requires version reconciliation.",
            )

    if scenario_profile == SCENARIO_PROFILE_DELEGATION_TRAINING:
        if site_index == 2 and document_type == "Training Log":
            return (
                "Pending",
                "Training log is pending confirmation for delegated site staff.",
            )

        if site_index == 2 and document_type == "Delegation Log":
            return (
                "Missing",
                "Delegation log is missing and requires CRA review.",
            )

        if site_index == 3 and document_type == "GCP Certificate":
            return (
                "Expired",
                "GCP certificate is expired and should be reconciled with staff delegation records.",
            )

    if scenario_profile == SCENARIO_PROFILE_BALANCED_HIGH_RISK:
        if site_index == 2 and document_type in [
            "Delegation Log",
            "IP Accountability Log",
        ]:
            return (
                "Missing",
                "Document is missing in a high-risk site scenario.",
            )

        if site_index == 2 and document_type in [
            "GCP Certificate",
            "Approved ICF",
        ]:
            return (
                "Expired",
                "Document is expired and requires updated evidence.",
            )

        if site_index == 3 and document_type == "Training Log":
            return (
                "Pending",
                "Training log is pending final confirmation.",
            )

    return status, comment


def build_demo_essential_documents_for_site(
    study_id: str,
    site_id: str,
    site_index: int,
    scenario_profile: str,
) -> List[Dict[str, Any]]:
    documents: List[Dict[str, Any]] = []

    for index, document_type in enumerate(ESSENTIAL_DOCUMENT_TYPES, start=1):
        status, comment = get_document_status_for_profile(
            scenario_profile=scenario_profile,
            site_index=site_index,
            document_type=document_type,
        )

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
    scenario_profile: str,
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
                scenario_profile=scenario_profile,
            )
        )

    upsert_essential_documents_to_supabase(all_documents)

    return True


def build_demo_protocol_deviations_for_imported_study(
    study: Dict[str, Any],
    scenario_profile: str,
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    if scenario_profile == SCENARIO_PROFILE_DOCUMENT_READINESS:
        return [
            {
                "deviationId": f"{study_id}-SITE-002-DEV-001",
                "studyId": study_id,
                "siteId": f"{study_id}-SITE-002",
                "subjectCode": "SUBJ-002-001",
                "category": "Documentation Process Issue",
                "severity": "Minor",
                "status": "In Review",
                "description": "Site file documentation inconsistency was identified during readiness review.",
                "detectedDate": "2026-05-12",
                "rootCause": "Site file reconciliation was not completed before monitoring review.",
                "correctiveAction": "Site is reconciling missing and pending essential documents.",
                "preventiveAction": "Site staff should maintain a document readiness checklist before monitoring visits.",
            }
        ]

    if scenario_profile == SCENARIO_PROFILE_PROTOCOL_DEVIATION:
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
                "severity": "Major",
                "status": "Open",
                "description": "A protocol-required assessment was not completed at the scheduled visit.",
                "detectedDate": "2026-05-13",
                "rootCause": "Assessment checklist was not reviewed before the visit.",
                "correctiveAction": "Site is reviewing source documentation to confirm whether assessment can be completed or documented as missed.",
                "preventiveAction": "Site staff should use the visit checklist before each subject visit.",
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

    if scenario_profile == SCENARIO_PROFILE_ICF_VERSION:
        return [
            {
                "deviationId": f"{study_id}-SITE-002-DEV-001",
                "studyId": study_id,
                "siteId": f"{study_id}-SITE-002",
                "subjectCode": "SUBJ-002-001",
                "category": "Informed Consent Process Issue",
                "severity": "Major",
                "status": "Open",
                "description": "Subject consent documentation requires review due to potential ICF version inconsistency.",
                "detectedDate": "2026-05-10",
                "rootCause": "Site may have used an outdated ICF version after a newer version became effective.",
                "correctiveAction": "CRA should review consent source documentation and ICF version history.",
                "preventiveAction": "Site staff should confirm active ICF version before obtaining consent.",
            }
        ]

    if scenario_profile == SCENARIO_PROFILE_DELEGATION_TRAINING:
        return [
            {
                "deviationId": f"{study_id}-SITE-002-DEV-001",
                "studyId": study_id,
                "siteId": f"{study_id}-SITE-002",
                "subjectCode": None,
                "category": "Delegation and Training Process Issue",
                "severity": "Major",
                "status": "Open",
                "description": "Delegated task timing requires review because training evidence was completed after delegation start date.",
                "detectedDate": "2026-05-03",
                "rootCause": "Delegation log was updated before protocol training evidence was completed.",
                "correctiveAction": "CRA should reconcile delegation log and training records.",
                "preventiveAction": "Site should confirm required training evidence before delegating study tasks.",
            }
        ]

    if scenario_profile == SCENARIO_PROFILE_BALANCED_HIGH_RISK:
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

    return []


def create_demo_protocol_deviations_for_imported_study(
    study: Dict[str, Any],
    scenario_profile: str,
) -> bool:
    demo_deviations = build_demo_protocol_deviations_for_imported_study(
        study,
        scenario_profile,
    )
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
    scenario_profile: str,
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    if scenario_profile == SCENARIO_PROFILE_ICF_VERSION:
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
                "signedIcfVersion": "1.0",
                "consentDate": "2026-05-12",
                "consentProcessNote": "Second outdated ICF version scenario for consent consistency review.",
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

    if scenario_profile == SCENARIO_PROFILE_BALANCED_HIGH_RISK:
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
            "signedIcfVersion": "2.0",
            "consentDate": "2026-05-10",
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


def create_demo_icf_data_for_imported_study(
    study: Dict[str, Any],
    scenario_profile: str,
) -> bool:
    icf_versions = build_demo_icf_versions_for_imported_study(study)
    consents = build_demo_subject_consents_for_imported_study(
        study,
        scenario_profile,
    )

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
    scenario_profile: str,
) -> List[Dict[str, Any]]:
    study_id = study["studyId"]

    if scenario_profile == SCENARIO_PROFILE_DELEGATION_TRAINING:
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

    if scenario_profile == SCENARIO_PROFILE_BALANCED_HIGH_RISK:
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
        ]

    if scenario_profile == SCENARIO_PROFILE_DOCUMENT_READINESS:
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
                "delegatedTask": "Site File Maintenance",
                "delegationStartDate": "2026-05-01",
                "delegationEndDate": None,
                "gcpTrainingDate": "2026-04-15",
                "protocolTrainingDate": None,
                "trainingStatus": "Missing",
                "comment": "Protocol training evidence is missing for site file maintenance responsibility.",
            },
        ]

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
    scenario_profile: str,
) -> bool:
    staff_members = build_demo_site_staff_for_imported_study(study)
    records = build_demo_delegation_training_records_for_imported_study(
        study,
        scenario_profile,
    )

    upsert_site_staff_to_supabase(staff_members)
    upsert_delegation_training_records_to_supabase(records)

    return True
