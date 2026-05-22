from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_metric(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "metricId": row["metric_id"],
        "siteId": row["site_id"],
        "studyId": row["study_id"],
        "openQueries": row["open_queries"],
        "queryAgingDays": row["query_aging_days"],
        "protocolDeviations": row["protocol_deviations"],
        "saeReportingDelayCount": row["sae_reporting_delay_count"],
        "missingEssentialDocuments": row["missing_essential_documents"],
        "ipAccountabilityIssues": row["ip_accountability_issues"],
        "icfIssues": row["icf_issues"],
        "lastMonitoringVisitDate": row["last_monitoring_visit_date"],
    }


def get_all_monitoring_metrics_from_supabase() -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("monitoring_metrics").select("*").order("metric_id").execute()
    )

    return [to_camel_case_metric(row) for row in response.data]


def get_monitoring_metrics_by_study_id_from_supabase(
    study_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("monitoring_metrics")
        .select("*")
        .eq("study_id", study_id)
        .order("metric_id")
        .execute()
    )

    return [to_camel_case_metric(row) for row in response.data]
