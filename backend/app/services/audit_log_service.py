from typing import Any, Dict, List, Optional

from app.repositories.audit_log_repository import get_audit_logs_from_supabase


def get_audit_logs(
    limit: int = 50,
    table_name: Optional[str] = None,
    action: Optional[str] = None,
) -> List[Dict[str, Any]]:
    safe_limit = min(max(limit, 1), 100)

    return get_audit_logs_from_supabase(
        limit=safe_limit,
        table_name=table_name,
        action=action,
    )
