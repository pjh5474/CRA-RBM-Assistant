export interface ProtocolDeviation {
	deviationId: string;
	studyId: string;
	siteId: string;
	subjectCode?: string | null;
	category: string;
	severity: "Minor" | "Major" | "Critical";
	status: "Open" | "In Review" | "Resolved";
	description: string;
	detectedDate: string;
	rootCause?: string | null;
	correctiveAction?: string | null;
	preventiveAction?: string | null;
}

export interface ProtocolDeviationSummary {
	studyId: string;
	siteId: string;
	siteName: string;
	totalDeviations: number;
	openDeviations: number;
	inReviewDeviations: number;
	resolvedDeviations: number;
	minorDeviations: number;
	majorDeviations: number;
	criticalDeviations: number;
	deviations: ProtocolDeviation[];
}
