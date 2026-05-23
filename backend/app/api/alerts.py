from typing import List

from fastapi import APIRouter

from app.schemas.alert_schema import HighRiskSiteAlertResponse
from app.services.alert_service import get_high_risk_site_alerts

router = APIRouter(prefix="/api/alerts", tags=["alerts"])


@router.get("/high-risk-sites", response_model=List[HighRiskSiteAlertResponse])
def get_high_risk_site_alert_list(include_medium: bool = True):
    return get_high_risk_site_alerts(include_medium=include_medium)
