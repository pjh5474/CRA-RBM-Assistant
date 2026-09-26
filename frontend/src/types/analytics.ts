export type TrialOverview = {
	total_trials: number;
	interventional_trials: number;
	observational_trials: number;
	other_trials: number;
	latest_year: number | null;
};

export type YearlyTrial = {
	study_year: number;
	trial_count: number;
};

export type CountryTrial = {
	country: string;
	trial_count: number;
};

export type ConditionTrend = {
	condition: string;
	study_year: number;
	trial_count: number;
	interventional_count: number;
	observational_count: number;
};
