from fastapi import HTTPException

from app.repositories.registry_study_repository import (
    get_registry_study_detail,
    search_registry_studies,
)


def search_studies(
    query: str | None,
    status: str | None,
    phase: str | None,
    country: str | None,
    page: int,
    page_size: int,
):
    return search_registry_studies(
        query_text=query,
        status=status,
        phase=phase,
        country=country,
        page=page,
        page_size=page_size,
    )


def get_study_detail(
    nct_id: str,
):
    study = get_registry_study_detail(nct_id)

    if not study:
        raise HTTPException(
            status_code=404,
            detail=f"Registry study not found: {nct_id}",
        )

    return study
