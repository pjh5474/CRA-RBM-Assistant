export interface MonitoringReportFinding {
	category: string;
	finding: string;
	recommendedAction: string;
}

export interface MonitoringReportRiskSummary {
	riskScore: number;
	riskLevel: "Low" | "Medium" | "High";
	riskFactors: string[];
}

export interface MonitoringReportEssentialDocumentSummary {
	readinessScore: number;
	totalDocuments: number;
	readyDocuments: number;
	missingDocuments: number;
	pendingDocuments: number;
	expiredDocuments: number;
}

export interface MonitoringReportProtocolDeviationSummary {
	totalDeviations: number;
	openDeviations: number;
	inReviewDeviations: number;
	resolvedDeviations: number;
	majorDeviations: number;
	criticalDeviations: number;
}

export interface MonitoringReportIcfSummary {
	totalConsents: number;
	validConsents: number;
	issueConsents: number;
}

export interface MonitoringReportFollowUpAction {
	category: string;
	action: string;
	priority: "High" | "Medium" | "Low";
}

export interface MonitoringReportDraft {
	studyId: string;
	studyTitle: string;
	siteId: string;
	siteName: string;
	principalInvestigator: string;
	visitType: string;
	riskScore: number;
	riskLevel: "Low" | "Medium" | "High";
	summary: string;
	riskSummary: MonitoringReportRiskSummary;
	essentialDocumentSummary: MonitoringReportEssentialDocumentSummary;
	protocolDeviationSummary: MonitoringReportProtocolDeviationSummary;
	icfSummary: MonitoringReportIcfSummary;
	findings: MonitoringReportFinding[];
	followUpActions: MonitoringReportFollowUpAction[];
	limitations: string[];
}
