from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_study(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "studyId": row["study_id"],
        "title": row["title"],
        "phase": row["phase"],
        "indication": row["indication"],
        "sponsor": row["sponsor"],
        "studyDesign": row["study_design"],
        "intervention": row["intervention"],
        "population": row["population"],
        "endpoints": row["endpoints"],
        "eligibilityCriteria": row["eligibility_criteria"],
        "visitSchedule": row["visit_schedule"],
        "safetyReporting": row["safety_reporting"],
        "craFocusAreas": row["cra_focus_areas"],
    }


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
        "study_design": study["studyDesign"],
        "intervention": study["intervention"],
        "population": study["population"],
        "endpoints": study["endpoints"],
        "eligibility_criteria": study["eligibilityCriteria"],
        "visit_schedule": study["visitSchedule"],
        "safety_reporting": study["safetyReporting"],
        "cra_focus_areas": study["craFocusAreas"],
    }

    response = supabase.table("studies").upsert(row, on_conflict="study_id").execute()

    if not response.data:
        return study

    return to_camel_case_study(response.data[0])
