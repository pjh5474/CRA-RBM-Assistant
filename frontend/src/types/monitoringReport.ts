export interface MonitoringReportFinding {
	category: string;
	finding: string;
	recommendedAction: string;
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
	findings: MonitoringReportFinding[];
	limitations: string[];
}
