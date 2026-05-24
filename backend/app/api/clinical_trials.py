from fastapi import APIRouter, Depends
from app.utils.auth import require_authenticated_user

from app.schemas.clinical_trials_schema import (
    ClinicalTrialDetailResponse,
    ClinicalTrialSearchResponse,
    ImportClinicalTrialResponse,
)
from app.services.external.clinical_trials_service import (
    get_clinical_trial_detail,
    import_clinical_trial_to_supabase,
    search_clinical_trials,
)

router = APIRouter(
    prefix="/api/external/clinical-trials",
    tags=["clinical-trials"],
)


@router.get("/search", response_model=ClinicalTrialSearchResponse)
async def search_external_clinical_trials(query: str, page_size: int = 10):
    return await search_clinical_trials(query=query, page_size=page_size)


@router.get("/{nct_id}", response_model=ClinicalTrialDetailResponse)
async def get_external_clinical_trial_detail(nct_id: str):
    return await get_clinical_trial_detail(nct_id)


@router.post(
    "/{nct_id}/import",
    response_model=ImportClinicalTrialResponse,
)
async def import_external_clinical_trial(
    nct_id: str,
    current_user=Depends(require_authenticated_user),
):
    return await import_clinical_trial_to_supabase(nct_id)
