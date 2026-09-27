from datetime import date
from typing import Any

from pydantic import BaseModel, Field


class RegistryStudySummaryResponse(BaseModel):
    nctId: str
    title: str

    studyType: str | None = None
    phases: list[str] = Field(default_factory=list)
    status: str | None = None

    enrollmentCount: int | None = None

    startDate: date | None = None
    completionDate: date | None = None

    conditions: list[str] = Field(default_factory=list)
    countries: list[str] = Field(default_factory=list)

    hasResults: bool = False


class RegistryStudySearchResponse(BaseModel):
    items: list[RegistryStudySummaryResponse]

    page: int
    pageSize: int
    hasNext: bool


class RegistryStudyDetailResponse(RegistryStudySummaryResponse):
    officialTitle: str | None = None

    enrollmentType: str | None = None

    allocation: str | None = None
    interventionModel: str | None = None
    primaryPurpose: str | None = None
    masking: str | None = None

    interventions: list[dict[str, Any]] = Field(default_factory=list)

    outcomes: list[dict[str, Any]] = Field(default_factory=list)

    locations: list[dict[str, Any]] = Field(default_factory=list)
