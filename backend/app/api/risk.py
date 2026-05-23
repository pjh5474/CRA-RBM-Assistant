from typing import List

from fastapi import APIRouter

from app.schemas.risk_schema import SiteRiskResponse
from app.services.risk_scoring_service import get_all_site_risks

router = APIRouter(prefix="/api/risk", tags=["risk"])


@router.get("/sites", response_model=List[SiteRiskResponse])
def get_site_risks():
    return get_all_site_risks()
