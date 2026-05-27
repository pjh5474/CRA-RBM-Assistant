export interface StudySummary {
	studyId: string;
	title: string;
	phase: string;
	indication: string;
	sponsor: string;
	ownerUserId?: string | null;
	isPublicDemo?: boolean;
}

export interface StudyDetail {
	studyId: string;
	title: string;
	phase: string;
	indication: string;
	sponsor: string;
	studyDesign: Record<string, unknown>;
	intervention: Record<string, unknown>;
	population: Record<string, unknown>;
	endpoints: Record<string, unknown>;
	eligibilityCriteria: {
		inclusion: string[];
		exclusion: string[];
	};
	visitSchedule: Array<Record<string, unknown>>;
	safetyReporting: Record<string, unknown>;
	craFocusAreas: string[];
}
