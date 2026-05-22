export interface ClinicalTrialSearchItem {
	nctId: string;
	title: string;
	status?: string | null;
	phases: string[];
	conditions: string[];
	interventions: string[];
}

export interface ClinicalTrialSearchResponse {
	query: string;
	count: number;
	results: ClinicalTrialSearchItem[];
}

export interface ClinicalTrialDetail {
	nctId: string;
	title: string;
	briefSummary?: string | null;
	status?: string | null;
	phases: string[];
	conditions: string[];
	interventions: string[];
	studyType?: string | null;
	allocation?: string | null;
	masking?: string | null;
	whoMasked: string[];
	primaryOutcomes: string[];
	secondaryOutcomes: string[];
	eligibilityCriteria?: string | null;
}
