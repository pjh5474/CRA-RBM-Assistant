from fastapi import APIRouter, Query

from app.schemas.analytics import (
    TrialOverviewResponse,
    YearlyTrialItem,
    CountryTrialItem,
    ConditionTrendItem,
)
from app.services.analytics_service import AnalyticsService


router = APIRouter(
    prefix="/api/analytics",
    tags=["analytics"],
)

service = AnalyticsService()


@router.get(
    "/overview",
    response_model=TrialOverviewResponse,
)
def get_overview():
    return service.get_overview()


@router.get(
    "/yearly",
    response_model=list[YearlyTrialItem],
)
def get_yearly():
    return service.get_yearly()


@router.get(
    "/countries",
    response_model=list[CountryTrialItem],
)
def get_countries(
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
    )
):
    return service.get_countries(limit)


@router.get(
    "/conditions",
    response_model=list[ConditionTrendItem],
)
def get_condition_trend(
    condition: str = Query(
        ...,
        min_length=1,
    )
):
    return service.get_condition_trend(condition)
