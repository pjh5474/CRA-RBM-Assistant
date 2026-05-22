from pydantic import BaseModel
from typing import List


class SiteRiskResponse(BaseModel):
    siteId: str
    studyId: str
    riskScore: int
    riskLevel: str
    riskFactors: List[str]
