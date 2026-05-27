from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class StudySummaryResponse(BaseModel):
    studyId: str
    title: str
    phase: str
    indication: str
    sponsor: str


class EligibilityCriteriaResponse(BaseModel):
    rawText: Optional[str] = None
    inclusion: List[str] = []
    exclusion: List[str] = []


class StudyDetailResponse(BaseModel):
    studyId: str
    title: str
    phase: str
    indication: str
    sponsor: str
    studyDesign: Dict[str, Any]
    intervention: Dict[str, Any]
    population: Dict[str, Any]
    endpoints: Dict[str, Any]
    eligibilityCriteria: EligibilityCriteriaResponse
    visitSchedule: List[Dict[str, Any]]
    safetyReporting: Dict[str, Any]
    craFocusAreas: List[str]
    ownerUserId: Optional[str] = None
    isPublicDemo: bool = False


class SiteResponse(BaseModel):
    siteId: str
    studyId: str
    siteName: str
    principalInvestigator: str
    country: str
    status: str
    activationDate: str
    targetEnrollment: int
    currentEnrollment: int


class StudyRiskSiteResponse(BaseModel):
    siteId: str
    studyId: str
    siteName: str
    principalInvestigator: str
    country: str
    status: str
    activationDate: str
    targetEnrollment: int
    currentEnrollment: int
    riskScore: int
    riskLevel: str
    riskFactors: List[str]
