from typing import List
from pydantic import BaseModel


class HighRiskSiteAlertResponse(BaseModel):
    studyId: str
    studyTitle: str
    siteId: str
    siteName: str
    riskScore: int
    riskLevel: str
    riskFactors: List[str]
    recommendedActions: List[str]