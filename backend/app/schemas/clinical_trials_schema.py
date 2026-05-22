from typing import List, Optional
from pydantic import BaseModel


class ClinicalTrialSearchItem(BaseModel):
    nctId: str
    title: str
    status: Optional[str] = None
    phases: List[str] = []
    conditions: List[str] = []
    interventions: List[str] = []


class ClinicalTrialSearchResponse(BaseModel):
    query: str
    count: int
    results: List[ClinicalTrialSearchItem]


class ClinicalTrialDetailResponse(BaseModel):
    nctId: str
    title: str
    briefSummary: Optional[str] = None
    status: Optional[str] = None
    phases: List[str] = []
    conditions: List[str] = []
    interventions: List[str] = []
    studyType: Optional[str] = None
    allocation: Optional[str] = None
    masking: Optional[str] = None
    whoMasked: List[str] = []
    primaryOutcomes: List[str] = []
    secondaryOutcomes: List[str] = []
    eligibilityCriteria: Optional[str] = None
