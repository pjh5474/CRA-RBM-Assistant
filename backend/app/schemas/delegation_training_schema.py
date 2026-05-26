from typing import List, Optional
from pydantic import BaseModel


class SiteStaffResponse(BaseModel):
    staffId: str
    studyId: str
    siteId: str
    staffName: str
    role: str
    isActive: bool


class DelegationTrainingRecordResponse(BaseModel):
    recordId: str
    studyId: str
    siteId: str
    staffId: str
    staffName: Optional[str] = None
    role: Optional[str] = None
    isActive: Optional[bool] = None
    delegatedTask: str
    delegationStartDate: str
    delegationEndDate: Optional[str] = None
    gcpTrainingDate: Optional[str] = None
    protocolTrainingDate: Optional[str] = None
    trainingStatus: str
    comment: Optional[str] = None


class DelegationTrainingCheckItemResponse(BaseModel):
    recordId: str
    staffId: str
    staffName: str
    role: str
    delegatedTask: str
    delegationStartDate: str
    gcpTrainingDate: Optional[str] = None
    protocolTrainingDate: Optional[str] = None
    trainingStatus: str
    status: str
    issueType: Optional[str] = None
    message: str


class DelegationTrainingCheckResponse(BaseModel):
    studyId: str
    siteId: str
    siteName: str
    totalRecords: int
    validRecords: int
    issueRecords: int
    missingTrainingRecords: int
    trainingAfterDelegationRecords: int
    staff: List[SiteStaffResponse]
    records: List[DelegationTrainingRecordResponse]
    checks: List[DelegationTrainingCheckItemResponse]
