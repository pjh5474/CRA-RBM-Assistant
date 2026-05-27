from typing import List
from pydantic import BaseModel


class MonitoringReportFindingResponse(BaseModel):
    category: str
    finding: str
    recommendedAction: str


class MonitoringReportRiskSummaryResponse(BaseModel):
    riskScore: int
    riskLevel: str
    riskFactors: List[str]


class MonitoringReportEssentialDocumentSummaryResponse(BaseModel):
    readinessScore: int
    totalDocuments: int
    readyDocuments: int
    missingDocuments: int
    pendingDocuments: int
    expiredDocuments: int


class MonitoringReportProtocolDeviationSummaryResponse(BaseModel):
    totalDeviations: int
    openDeviations: int
    inReviewDeviations: int
    resolvedDeviations: int
    majorDeviations: int
    criticalDeviations: int


class MonitoringReportIcfSummaryResponse(BaseModel):
    totalConsents: int
    validConsents: int
    issueConsents: int


class MonitoringReportDelegationTrainingSummaryResponse(BaseModel):
    totalRecords: int
    validRecords: int
    issueRecords: int
    missingTrainingRecords: int
    trainingAfterDelegationRecords: int


class MonitoringReportFollowUpActionResponse(BaseModel):
    category: str
    action: str
    priority: str


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
    riskSummary: MonitoringReportRiskSummaryResponse
    essentialDocumentSummary: MonitoringReportEssentialDocumentSummaryResponse
    protocolDeviationSummary: MonitoringReportProtocolDeviationSummaryResponse
    icfSummary: MonitoringReportIcfSummaryResponse
    delegationTrainingSummary: MonitoringReportDelegationTrainingSummaryResponse
    findings: List[MonitoringReportFindingResponse]
    followUpActions: List[MonitoringReportFollowUpActionResponse]
    limitations: List[str]
