from typing import List
from pydantic import BaseModel


class ActionItemResponse(BaseModel):
    riskFactor: str
    recommendedAction: str


class SiteActionItemsResponse(BaseModel):
    siteId: str
    studyId: str
    siteName: str
    riskScore: int
    riskLevel: str
    actionItems: List[ActionItemResponse]
