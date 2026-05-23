from typing import List
from pydantic import BaseModel

from app.schemas.essential_document_schema import EssentialDocumentReadinessResponse
from app.schemas.icf_schema import IcfVersionCheckResponse
from app.schemas.monitoring_report_schema import MonitoringReportDraftResponse
from app.schemas.protocol_deviation_schema import ProtocolDeviationSummaryResponse


class SiteReviewRiskSummaryResponse(BaseModel):
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


class SiteReviewStudySummaryResponse(BaseModel):
    studyId: str
    title: str
    phase: str
    indication: str
    sponsor: str


class SiteReviewModuleResponse(BaseModel):
    title: str
    description: str
    href: str
    statusLabel: str


class SiteReviewSummaryResponse(BaseModel):
    study: SiteReviewStudySummaryResponse
    site: SiteReviewRiskSummaryResponse
    essentialDocuments: EssentialDocumentReadinessResponse
    protocolDeviations: ProtocolDeviationSummaryResponse
    icfVersionCheck: IcfVersionCheckResponse
    monitoringReportDraft: MonitoringReportDraftResponse
    modules: List[SiteReviewModuleResponse]
