from typing import Any, Dict, Optional
from pydantic import BaseModel


class AuditLogResponse(BaseModel):
    id: int
    actorUserId: Optional[str] = None
    tableName: str
    action: str
    recordId: str
    oldData: Optional[Dict[str, Any]] = None
    newData: Optional[Dict[str, Any]] = None
    createdAt: str
