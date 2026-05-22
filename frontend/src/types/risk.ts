export interface RiskSite {
	siteId: string;
	studyId: string;
	siteName: string;
	principalInvestigator: string;
	country: string;
	status: string;
	activationDate: string;
	targetEnrollment: number;
	currentEnrollment: number;
	riskScore: number;
	riskLevel: "Low" | "Medium" | "High";
	riskFactors: string[];
}
