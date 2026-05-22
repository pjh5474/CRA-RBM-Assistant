import os

from app.repositories.monitoring_metric_repository import (
    get_all_monitoring_metrics_from_supabase,
)

from typing import Dict, List, Any

from app.utils.data_loader import load_json_file

DATA_SOURCE = os.getenv("DATA_SOURCE", "json")


def calculate_open_query_score(open_queries: int) -> int:
    if open_queries <= 5:
        return 0
    if open_queries <= 10:
        return 1
    return 2


def calculate_query_aging_score(query_aging_days: int) -> int:
    if query_aging_days <= 7:
        return 0
    if query_aging_days <= 14:
        return 1
    return 2


def calculate_protocol_deviation_score(protocol_deviations: int) -> int:
    if protocol_deviations <= 1:
        return 0
    if protocol_deviations <= 3:
        return 1
    return 2


def calculate_sae_reporting_delay_score(sae_reporting_delay_count: int) -> int:
    if sae_reporting_delay_count <= 0:
        return 0
    return 3


def calculate_missing_document_score(missing_essential_documents: int) -> int:
    if missing_essential_documents <= 0:
        return 0
    return 2


def calculate_ip_accountability_score(ip_accountability_issues: int) -> int:
    if ip_accountability_issues <= 0:
        return 0
    return 2


def calculate_icf_issue_score(icf_issues: int) -> int:
    if icf_issues <= 0:
        return 0
    return 3


def classify_risk_level(risk_score: int) -> str:
    if risk_score <= 2:
        return "Low"
    if risk_score <= 5:
        return "Medium"
    return "High"


def extract_risk_factors(metric: Dict[str, Any]) -> List[str]:
    risk_factors: List[str] = []

    if metric.get("openQueries", 0) >= 11:
        risk_factors.append("High open query count")
    elif metric.get("openQueries", 0) >= 6:
        risk_factors.append("Moderate open query count")

    if metric.get("queryAgingDays", 0) >= 15:
        risk_factors.append("Long query aging")
    elif metric.get("queryAgingDays", 0) >= 8:
        risk_factors.append("Moderate query aging")

    if metric.get("protocolDeviations", 0) >= 4:
        risk_factors.append("Multiple protocol deviations")
    elif metric.get("protocolDeviations", 0) >= 2:
        risk_factors.append("Protocol deviation trend")

    if metric.get("saeReportingDelayCount", 0) >= 1:
        risk_factors.append("SAE reporting delay")

    if metric.get("missingEssentialDocuments", 0) >= 1:
        risk_factors.append("Missing essential documents")

    if metric.get("ipAccountabilityIssues", 0) >= 1:
        risk_factors.append("IP accountability issue")

    if metric.get("icfIssues", 0) >= 1:
        risk_factors.append("ICF issue")

    return risk_factors


def calculate_site_risk(metric: Dict[str, Any]) -> Dict[str, Any]:
    open_query_score = calculate_open_query_score(metric.get("openQueries", 0))
    query_aging_score = calculate_query_aging_score(metric.get("queryAgingDays", 0))
    deviation_score = calculate_protocol_deviation_score(
        metric.get("protocolDeviations", 0)
    )
    sae_score = calculate_sae_reporting_delay_score(
        metric.get("saeReportingDelayCount", 0)
    )
    document_score = calculate_missing_document_score(
        metric.get("missingEssentialDocuments", 0)
    )
    ip_score = calculate_ip_accountability_score(
        metric.get("ipAccountabilityIssues", 0)
    )
    icf_score = calculate_icf_issue_score(metric.get("icfIssues", 0))

    risk_score = (
        open_query_score
        + query_aging_score
        + deviation_score
        + sae_score
        + document_score
        + ip_score
        + icf_score
    )

    return {
        "siteId": metric["siteId"],
        "studyId": metric["studyId"],
        "riskScore": risk_score,
        "riskLevel": classify_risk_level(risk_score),
        "riskFactors": extract_risk_factors(metric),
    }


def get_all_site_risks() -> List[Dict[str, Any]]:
    if DATA_SOURCE == "supabase":
        monitoring_metrics = get_all_monitoring_metrics_from_supabase()
    else:
        monitoring_metrics = load_json_file("data/monitoring-metrics.json")

    return [calculate_site_risk(metric) for metric in monitoring_metrics]
