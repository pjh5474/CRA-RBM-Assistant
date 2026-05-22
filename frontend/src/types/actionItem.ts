export interface ActionItem {
	riskFactor: string;
	recommendedAction: string;
}

export interface SiteActionItems {
	siteId: string;
	studyId: string;
	siteName: string;
	riskScore: number;
	riskLevel: "Low" | "Medium" | "High";
	actionItems: ActionItem[];
}
