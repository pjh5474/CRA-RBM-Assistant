from typing import List

from fastapi import APIRouter

from app.schemas.action_item_schema import SiteActionItemsResponse
from app.schemas.study_schema import (
    SiteResponse,
    StudyDetailResponse,
    StudyRiskSiteResponse,
    StudySummaryResponse,
)
from app.services.action_item_service import get_action_items_by_study_id
from app.services.study_service import (
    get_all_studies,
    get_risk_sites_by_study_id,
    get_sites_by_study_id,
    get_study_by_id,
)

router = APIRouter(prefix="/api/studies", tags=["studies"])


@router.get("", response_model=List[StudySummaryResponse])
def get_studies():
    return get_all_studies()


@router.get("/{study_id}", response_model=StudyDetailResponse)
def get_study_detail(study_id: str):
    return get_study_by_id(study_id)


@router.get("/{study_id}/sites", response_model=List[SiteResponse])
def get_study_sites(study_id: str):
    return get_sites_by_study_id(study_id)


@router.get("/{study_id}/risk-sites", response_model=List[StudyRiskSiteResponse])
def get_study_risk_sites(study_id: str):
    return get_risk_sites_by_study_id(study_id)


@router.get("/{study_id}/action-items", response_model=List[SiteActionItemsResponse])
def get_study_action_items(study_id: str):
    return get_action_items_by_study_id(study_id)
