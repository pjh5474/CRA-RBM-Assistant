from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_site(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "siteId": row["site_id"],
        "studyId": row["study_id"],
        "siteName": row["site_name"],
        "principalInvestigator": row["principal_investigator"],
        "country": row["country"],
        "status": row["status"],
        "activationDate": row["activation_date"],
        "targetEnrollment": row["target_enrollment"],
        "currentEnrollment": row["current_enrollment"],
    }


def get_sites_by_study_id_from_supabase(study_id: str) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("sites")
        .select("*")
        .eq("study_id", study_id)
        .order("site_id")
        .execute()
    )

    return [to_camel_case_site(row) for row in response.data]
