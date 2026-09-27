from fastapi import APIRouter, Query

from app.schemas.registry_study_schema import (
    RegistryStudyDetailResponse,
    RegistryStudySearchResponse,
)

from app.services.registry_study_service import (
    get_study_detail,
    search_studies,
)


router = APIRouter(
    prefix="/api/registry/studies",
    tags=["registry-studies"],
)


@router.get(
    "",
    response_model=RegistryStudySearchResponse,
)
def search_registry_studies_endpoint(
    query: str | None = None,
    status: str | None = None,
    phase: str | None = None,
    country: str | None = None,
    page: int = Query(
        default=1,
        ge=1,
    ),
    page_size: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
):
    return search_studies(
        query=query,
        status=status,
        phase=phase,
        country=country,
        page=page,
        page_size=page_size,
    )


@router.get(
    "/{nct_id}",
    response_model=RegistryStudyDetailResponse,
)
def get_registry_study_endpoint(
    nct_id: str,
):
    return get_study_detail(nct_id.upper())
