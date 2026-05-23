from typing import List, Optional
from pydantic import BaseModel


class ProtocolDeviationResponse(BaseModel):
    deviationId: str
    studyId: str
    siteId: str
    subjectCode: Optional[str] = None
    category: str
    severity: str
    status: str
    description: str
    detectedDate: str
    rootCause: Optional[str] = None
    correctiveAction: Optional[str] = None
    preventiveAction: Optional[str] = None


class ProtocolDeviationSummaryResponse(BaseModel):
    studyId: str
    siteId: str
    siteName: str
    totalDeviations: int
    openDeviations: int
    inReviewDeviations: int
    resolvedDeviations: int
    minorDeviations: int
    majorDeviations: int
    criticalDeviations: int
    deviations: List[ProtocolDeviationResponse]
