from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_camel_case_document(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "documentId": row["document_id"],
        "studyId": row["study_id"],
        "siteId": row["site_id"],
        "documentType": row["document_type"],
        "required": row["required"],
        "status": row["status"],
        "version": row.get("version"),
        "documentDate": row.get("document_date"),
        "expiryDate": row.get("expiry_date"),
        "comment": row.get("comment"),
        "ownerUserId": row.get("owner_user_id"),
    }


def get_essential_documents_by_site_from_supabase(
    study_id: str,
    site_id: str,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("essential_documents")
        .select("*")
        .eq("study_id", study_id)
        .eq("site_id", site_id)
        .order("document_type")
        .execute()
    )

    return [to_camel_case_document(row) for row in response.data]


def upsert_essential_documents_to_supabase(
    documents: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not documents:
        return []

    supabase = get_supabase_client()

    rows = [
        {
            "document_id": document["documentId"],
            "study_id": document["studyId"],
            "site_id": document["siteId"],
            "document_type": document["documentType"],
            "required": document["required"],
            "status": document["status"],
            "version": document.get("version"),
            "document_date": document.get("documentDate"),
            "expiry_date": document.get("expiryDate"),
            "comment": document.get("comment"),
            "owner_user_id": document.get("ownerUserId"),
        }
        for document in documents
    ]

    response = (
        supabase.table("essential_documents")
        .upsert(rows, on_conflict="document_id")
        .execute()
    )

    return [to_camel_case_document(row) for row in response.data]
