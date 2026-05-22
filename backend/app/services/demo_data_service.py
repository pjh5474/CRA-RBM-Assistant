from typing import Any, Dict, List

from app.repositories.monitoring_metric_repository import (
    upsert_monitoring_metrics_to_supabase,
)
from app.repositories.site_repository import upsert_sites_to_supabase


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
    """
    Create synthetic demo sites and monitoring metrics for imported public study.

    This data is not real site performance data.
    It is generated only to demonstrate the CRA-RBM dashboard workflow.
    """
    demo_sites = build_demo_sites_for_imported_study(study)
    demo_metrics = build_demo_monitoring_metrics_for_imported_study(study)

    upsert_sites_to_supabase(demo_sites)
    upsert_monitoring_metrics_to_supabase(demo_metrics)

    return True
