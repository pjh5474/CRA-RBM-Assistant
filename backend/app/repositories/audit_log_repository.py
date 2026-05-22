from typing import Any, Dict, List, Optional

from app.utils.supabase_client import get_supabase_client


def to_camel_case_audit_log(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": row["id"],
        "actorUserId": row.get("actorUserId"),
        "tableName": row["tableName"],
        "action": row["action"],
        "recordId": row["recordId"],
        "oldData": row.get("oldData"),
        "newData": row.get("newData"),
        "createdAt": row["createdAt"],
    }


def get_audit_logs_from_supabase(
    limit: int = 50,
    table_name: Optional[str] = None,
    action: Optional[str] = None,
) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    query = (
        supabase.table("audit_logs")
        .select("*")
        .order("createdAt", desc=True)
        .limit(limit)
    )

    if table_name:
        query = query.eq("tableName", table_name)

    if action:
        query = query.eq("action", action)

    response = query.execute()

    return [to_camel_case_audit_log(row) for row in response.data]
