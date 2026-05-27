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
        "ownerUserId": row.get("owner_user_id"),
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


def upsert_sites_to_supabase(sites: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not sites:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "site_id": site["siteId"],
            "study_id": site["studyId"],
            "site_name": site["siteName"],
            "principal_investigator": site["principalInvestigator"],
            "country": site["country"],
            "status": site["status"],
            "activation_date": site["activationDate"],
            "target_enrollment": site["targetEnrollment"],
            "current_enrollment": site["currentEnrollment"],
            "owner_user_id": site.get("ownerUserId"),
        }
        for site in sites
    ]

    response = supabase.table("sites").upsert(rows, on_conflict="site_id").execute()

    return [to_camel_case_site(row) for row in response.data]
