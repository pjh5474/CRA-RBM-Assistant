export interface SiteStaff {
	staffId: string;
	studyId: string;
	siteId: string;
	staffName: string;
	role: string;
	isActive: boolean;
}

export interface DelegationTrainingRecord {
	recordId: string;
	studyId: string;
	siteId: string;
	staffId: string;
	staffName?: string | null;
	role?: string | null;
	isActive?: boolean | null;
	delegatedTask: string;
	delegationStartDate: string;
	delegationEndDate?: string | null;
	gcpTrainingDate?: string | null;
	protocolTrainingDate?: string | null;
	trainingStatus: "Complete" | "Missing" | "Expired" | "Pending";
	comment?: string | null;
}

export interface DelegationTrainingCheckItem {
	recordId: string;
	staffId: string;
	staffName: string;
	role: string;
	delegatedTask: string;
	delegationStartDate: string;
	gcpTrainingDate?: string | null;
	protocolTrainingDate?: string | null;
	trainingStatus: string;
	status: "Valid" | "Issue";
	issueType?: string | null;
	message: string;
}

export interface DelegationTrainingCheck {
	studyId: string;
	siteId: string;
	siteName: string;
	totalRecords: number;
	validRecords: number;
	issueRecords: number;
	missingTrainingRecords: number;
	trainingAfterDelegationRecords: number;
	staff: SiteStaff[];
	records: DelegationTrainingRecord[];
	checks: DelegationTrainingCheckItem[];
}
