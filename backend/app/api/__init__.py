from fastapi import APIRouter

from app.api import (
    alerts,
    audit_logs,
    checklists,
    clinical_trials,
    health,
    risk,
    site_monitoring,
    studies,
)

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(studies.router)
api_router.include_router(risk.router)
api_router.include_router(site_monitoring.router)
api_router.include_router(checklists.router)
api_router.include_router(clinical_trials.router)
api_router.include_router(audit_logs.router)
api_router.include_router(alerts.router)
