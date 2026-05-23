from typing import List, Optional
from pydantic import BaseModel


class IcfVersionResponse(BaseModel):
    icfVersionId: str
    studyId: str
    version: str
    irbApprovalDate: str
    effectiveDate: str
    status: str


class SubjectConsentResponse(BaseModel):
    consentId: str
    studyId: str
    siteId: str
    subjectCode: str
    signedIcfVersion: str
    consentDate: str
    consentProcessNote: Optional[str] = None


class IcfVersionCheckItemResponse(BaseModel):
    consentId: str
    subjectCode: str
    signedIcfVersion: str
    consentDate: str
    expectedIcfVersion: Optional[str] = None
    status: str
    issueType: Optional[str] = None
    message: str


class IcfVersionCheckResponse(BaseModel):
    studyId: str
    siteId: str
    siteName: str
    totalConsents: int
    validConsents: int
    issueConsents: int
    icfVersions: List[IcfVersionResponse]
    consents: List[SubjectConsentResponse]
    checks: List[IcfVersionCheckItemResponse]
