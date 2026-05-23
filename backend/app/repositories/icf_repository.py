from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_icf_version(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "icfVersionId": row["icf_version_id"],
        "studyId": row["study_id"],
        "version": row["version"],
        "irbApprovalDate": row["irb_approval_date"],
        "effectiveDate": row["effective_date"],
        "status": row["status"],
    }


def to_camel_case_subject_consent(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "consentId": row["consent_id"],
        "studyId": row["study_id"],
        "siteId": row["site_id"],
        "subjectCode": row["subject_code"],
        "signedIcfVersion": row["signed_icf_version"],
        "consentDate": row["consent_date"],
        "consentProcessNote": row.get("consent_process_note"),
    }


def get_icf_versions_by_study_from_supabase(
    study_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("icf_versions")
        .select("*")
        .eq("study_id", study_id)
        .order("effective_date")
        .execute()
    )

    return [to_camel_case_icf_version(row) for row in response.data]


def get_subject_consents_by_site_from_supabase(
    study_id: str,
    site_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("subject_consents")
        .select("*")
        .eq("study_id", study_id)
        .eq("site_id", site_id)
        .order("consent_date")
        .execute()
    )

    return [to_camel_case_subject_consent(row) for row in response.data]


def upsert_icf_versions_to_supabase(
    icf_versions: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not icf_versions:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "icf_version_id": item["icfVersionId"],
            "study_id": item["studyId"],
            "version": item["version"],
            "irb_approval_date": item["irbApprovalDate"],
            "effective_date": item["effectiveDate"],
            "status": item["status"],
        }
        for item in icf_versions
    ]

    response = (
        supabase.table("icf_versions")
        .upsert(rows, on_conflict="icf_version_id")
        .execute()
    )

    return [to_camel_case_icf_version(row) for row in response.data]


def upsert_subject_consents_to_supabase(
    consents: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not consents:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "consent_id": item["consentId"],
            "study_id": item["studyId"],
            "site_id": item["siteId"],
            "subject_code": item["subjectCode"],
            "signed_icf_version": item["signedIcfVersion"],
            "consent_date": item["consentDate"],
            "consent_process_note": item.get("consentProcessNote"),
        }
        for item in consents
    ]

    response = (
        supabase.table("subject_consents")
        .upsert(rows, on_conflict="consent_id")
        .execute()
    )

    return [to_camel_case_subject_consent(row) for row in response.data]
