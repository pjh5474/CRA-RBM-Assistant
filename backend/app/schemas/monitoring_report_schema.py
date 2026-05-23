from typing import List
from pydantic import BaseModel


class MonitoringReportFindingResponse(BaseModel):
    category: str
    finding: str
    recommendedAction: str


class MonitoringReportDraftResponse(BaseModel):
    studyId: str
    studyTitle: str
    siteId: str
    siteName: str
    principalInvestigator: str
    visitType: str
    riskScore: int
    riskLevel: str
    summary: str
    findings: List[MonitoringReportFindingResponse]
    limitations: List[str]
