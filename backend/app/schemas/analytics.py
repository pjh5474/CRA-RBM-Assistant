from pydantic import BaseModel


class TrialOverviewResponse(BaseModel):
    total_trials: int
    interventional_trials: int
    observational_trials: int
    other_trials: int
    latest_year: int | None


class YearlyTrialItem(BaseModel):
    study_year: int
    trial_count: int


class CountryTrialItem(BaseModel):
    country: str
    trial_count: int


class ConditionTrendItem(BaseModel):
    condition: str
    study_year: int
    trial_count: int
    interventional_count: int
    observational_count: int
