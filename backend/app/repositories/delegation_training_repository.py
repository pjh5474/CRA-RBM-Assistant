from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_site_staff(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "staffId": row["staff_id"],
        "studyId": row["study_id"],
        "siteId": row["site_id"],
        "staffName": row["staff_name"],
        "role": row["role"],
        "isActive": row["is_active"],
    }


def to_camel_case_delegation_training_record(row: Dict[str, Any]) -> Dict[str, Any]:
    staff = row.get("site_staff")

    return {
        "recordId": row["record_id"],
        "studyId": row["study_id"],
        "siteId": row["site_id"],
        "staffId": row["staff_id"],
        "staffName": staff.get("staff_name") if staff else row.get("staff_name"),
        "role": staff.get("role") if staff else row.get("role"),
        "isActive": staff.get("is_active") if staff else row.get("is_active"),
        "delegatedTask": row["delegated_task"],
        "delegationStartDate": row["delegation_start_date"],
        "delegationEndDate": row.get("delegation_end_date"),
        "gcpTrainingDate": row.get("gcp_training_date"),
        "protocolTrainingDate": row.get("protocol_training_date"),
        "trainingStatus": row["training_status"],
        "comment": row.get("comment"),
    }


def get_site_staff_by_site_from_supabase(
    study_id: str,
    site_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("site_staff")
        .select("*")
        .eq("study_id", study_id)
        .eq("site_id", site_id)
        .order("staff_name")
        .execute()
    )

    return [to_camel_case_site_staff(row) for row in response.data]


def get_delegation_training_records_by_site_from_supabase(
    study_id: str,
    site_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("delegation_training_records")
        .select(
            "*, site_staff(staff_name, role, is_active)"
        )
        .eq("study_id", study_id)
        .eq("site_id", site_id)
        .order("delegation_start_date")
        .execute()
    )

    return [to_camel_case_delegation_training_record(row) for row in response.data]


def upsert_site_staff_to_supabase(
    staff_members: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not staff_members:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "staff_id": staff["staffId"],
            "study_id": staff["studyId"],
            "site_id": staff["siteId"],
            "staff_name": staff["staffName"],
            "role": staff["role"],
            "is_active": staff["isActive"],
        }
        for staff in staff_members
    ]

    response = (
        supabase.table("site_staff")
        .upsert(rows, on_conflict="staff_id")
        .execute()
    )

    return [to_camel_case_site_staff(row) for row in response.data]


def upsert_delegation_training_records_to_supabase(
    records: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not records:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "record_id": record["recordId"],
            "study_id": record["studyId"],
            "site_id": record["siteId"],
            "staff_id": record["staffId"],
            "delegated_task": record["delegatedTask"],
            "delegation_start_date": record["delegationStartDate"],
            "delegation_end_date": record.get("delegationEndDate"),
            "gcp_training_date": record.get("gcpTrainingDate"),
            "protocol_training_date": record.get("protocolTrainingDate"),
            "training_status": record["trainingStatus"],
            "comment": record.get("comment"),
        }
        for record in records
    ]

    response = (
        supabase.table("delegation_training_records")
        .upsert(rows, on_conflict="record_id")
        .execute()
    )

    return [to_camel_case_delegation_training_record(row) for row in response.data]