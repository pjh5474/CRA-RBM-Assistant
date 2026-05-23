from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_deviation(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "deviationId": row["deviation_id"],
        "studyId": row["study_id"],
        "siteId": row["site_id"],
        "subjectCode": row.get("subject_code"),
        "category": row["category"],
        "severity": row["severity"],
        "status": row["status"],
        "description": row["description"],
        "detectedDate": row["detected_date"],
        "rootCause": row.get("root_cause"),
        "correctiveAction": row.get("corrective_action"),
        "preventiveAction": row.get("preventive_action"),
    }


def get_protocol_deviations_by_site_from_supabase(
    study_id: str,
    site_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("protocol_deviations")
        .select("*")
        .eq("study_id", study_id)
        .eq("site_id", site_id)
        .order("detected_date", desc=True)
        .execute()
    )

    return [to_camel_case_deviation(row) for row in response.data]


def upsert_protocol_deviations_to_supabase(
    deviations: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not deviations:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "deviation_id": deviation["deviationId"],
            "study_id": deviation["studyId"],
            "site_id": deviation["siteId"],
            "subject_code": deviation.get("subjectCode"),
            "category": deviation["category"],
            "severity": deviation["severity"],
            "status": deviation["status"],
            "description": deviation["description"],
            "detected_date": deviation["detectedDate"],
            "root_cause": deviation.get("rootCause"),
            "corrective_action": deviation.get("correctiveAction"),
            "preventive_action": deviation.get("preventiveAction"),
        }
        for deviation in deviations
    ]

    response = (
        supabase.table("protocol_deviations")
        .upsert(rows, on_conflict="deviation_id")
        .execute()
    )

    return [to_camel_case_deviation(row) for row in response.data]
