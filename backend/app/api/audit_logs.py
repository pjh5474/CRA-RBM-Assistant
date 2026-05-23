from typing import List, Optional

from fastapi import APIRouter

from app.schemas.audit_log_schema import AuditLogResponse
from app.services.audit_log_service import get_audit_logs

router = APIRouter(prefix="/api/audit-logs", tags=["audit-logs"])


@router.get("", response_model=List[AuditLogResponse])
def get_audit_log_list(
    limit: int = 50,
    table_name: Optional[str] = None,
    action: Optional[str] = None,
):
    return get_audit_logs(
        limit=limit,
        table_name=table_name,
        action=action,
    )
