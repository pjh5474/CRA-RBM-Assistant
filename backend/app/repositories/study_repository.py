from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_study(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "studyId": row["study_id"],
        "title": row["title"],
        "phase": row["phase"],
        "indication": row["indication"],
        "sponsor": row["sponsor"],
        "studyDesign": row.get("study_design"),
        "intervention": row.get("intervention"),
        "population": row.get("population"),
        "endpoints": row.get("endpoints"),
        "eligibilityCriteria": row.get("eligibility_criteria"),
        "visitSchedule": row.get("visit_schedule"),
        "safetyReporting": row.get("safety_reporting"),
        "craFocusAreas": row.get("cra_focus_areas"),
        "ownerUserId": row.get("owner_user_id"),
        "isPublicDemo": row.get("is_public_demo", False),
    }


def get_accessible_studies_from_supabase(
    owner_user_id: str | None = None,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    public_response = (
        supabase.table("studies")
        .select("*")
        .eq("is_public_demo", True)
        .order("study_id")
        .execute()
    )

    studies_by_id = {row["study_id"]: row for row in public_response.data}

    if owner_user_id:
        owned_response = (
            supabase.table("studies")
            .select("*")
            .eq("owner_user_id", owner_user_id)
            .order("study_id")
            .execute()
        )

        for row in owned_response.data:
            studies_by_id[row["study_id"]] = row

    return [to_camel_case_study(row) for row in studies_by_id.values()]


def get_all_studies_from_supabase() -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("studies")
        .select("study_id,title,phase,indication,sponsor")
        .order("study_id")
        .execute()
    )

    return [
        {
            "studyId": row["study_id"],
            "title": row["title"],
            "phase": row["phase"],
            "indication": row["indication"],
            "sponsor": row["sponsor"],
        }
        for row in response.data
    ]


def get_study_by_id_from_supabase(study_id: str) -> Dict[str, Any] | None:
    supabase = get_supabase_client()

    response = (
        supabase.table("studies")
        .select("*")
        .eq("study_id", study_id)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return to_camel_case_study(response.data[0])


def study_exists_in_supabase(study_id: str) -> bool:
    supabase = get_supabase_client()

    response = (
        supabase.table("studies")
        .select("study_id")
        .eq("study_id", study_id)
        .limit(1)
        .execute()
    )

    return bool(response.data)


def upsert_study_to_supabase(study: Dict[str, Any]) -> Dict[str, Any]:
    """
    Upsert one internal study object into Supabase studies table.
    Input uses frontend/backend camelCase format.
    Output returns camelCase study object.
    """
    supabase = get_supabase_client()

    row = {
        "study_id": study["studyId"],
        "title": study["title"],
        "phase": study["phase"],
        "indication": study["indication"],
        "sponsor": study["sponsor"],
        "study_design": study.get("studyDesign"),
        "intervention": study.get("intervention"),
        "population": study.get("population"),
        "endpoints": study.get("endpoints"),
        "eligibility_criteria": study.get("eligibilityCriteria"),
        "visit_schedule": study.get("visitSchedule"),
        "safety_reporting": study.get("safetyReporting"),
        "cra_focus_areas": study.get("craFocusAreas"),
        "owner_user_id": study.get("ownerUserId"),
        "is_public_demo": study.get("isPublicDemo", False),
    }

    response = supabase.table("studies").upsert(row, on_conflict="study_id").execute()

    if not response.data:
        return study

    return to_camel_case_study(response.data[0])
