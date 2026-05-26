from typing import Any, Dict


def build_profile_metric(
    study_id: str,
    site_index: int,
    open_queries: int,
    query_aging_days: int,
    protocol_deviations: int,
    sae_reporting_delay_count: int,
    missing_essential_documents: int,
    ip_accountability_issues: int,
    icf_issues: int,
) -> Dict[str, Any]:
    site_id = f"{study_id}-SITE-{site_index:03d}"

    return {
        "metricId": f"{site_id}-METRIC-001",
        "studyId": study_id,
        "siteId": site_id,
        "openQueries": open_queries,
        "queryAgingDays": query_aging_days,
        "protocolDeviations": protocol_deviations,
        "saeReportingDelayCount": sae_reporting_delay_count,
        "missingEssentialDocuments": missing_essential_documents,
        "ipAccountabilityIssues": ip_accountability_issues,
        "icfIssues": icf_issues,
        "lastMonitoringVisitDate": "2026-05-15",
    }
