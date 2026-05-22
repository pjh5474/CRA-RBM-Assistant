from typing import Any, Dict, List
from pydantic import BaseModel


class StudySummaryResponse(BaseModel):
    studyId: str
    title: str
    phase: str
    indication: str
    sponsor: str


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
    eligibilityCriteria: Dict[str, List[str]]
    visitSchedule: List[Dict[str, Any]]
    safetyReporting: Dict[str, Any]
    craFocusAreas: List[str]


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
