from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.checklist_schema import ChecklistItemResponse, ChecklistResponse
from app.schemas.risk_schema import SiteRiskResponse
from app.schemas.study_schema import (
    SiteResponse,
    StudyDetailResponse,
    StudyRiskSiteResponse,
    StudySummaryResponse,
)
from app.services.checklist_service import (
    get_all_checklists,
    get_imv_checklist,
    get_siv_checklist,
)
from app.services.risk_scoring_service import get_all_site_risks
from app.services.study_service import (
    get_all_studies,
    get_sites_by_study_id,
    get_study_by_id,
    get_risk_sites_by_study_id,
)

app = FastAPI(
    title="CRA-RBM Assistant API",
    description="Backend API for CRA risk-based monitoring assistant prototype",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "CRA-RBM Assistant API",
        "version": "0.2.0",
    }


@app.get("/api/studies", response_model=List[StudySummaryResponse])
def get_studies():
    return get_all_studies()


@app.get("/api/studies/{study_id}", response_model=StudyDetailResponse)
def get_study_detail(study_id: str):
    return get_study_by_id(study_id)


@app.get("/api/studies/{study_id}/sites", response_model=List[SiteResponse])
def get_study_sites(study_id: str):
    return get_sites_by_study_id(study_id)


@app.get("/api/risk/sites", response_model=List[SiteRiskResponse])
def get_site_risks():
    return get_all_site_risks()


@app.get(
    "/api/studies/{study_id}/risk-sites", response_model=List[StudyRiskSiteResponse]
)
def get_study_risk_sites(study_id: str):
    return get_risk_sites_by_study_id(study_id)


@app.get("/api/checklists", response_model=ChecklistResponse)
def get_checklists():
    return get_all_checklists()


@app.get("/api/checklists/siv", response_model=List[ChecklistItemResponse])
def get_siv_checklists():
    return get_siv_checklist()


@app.get("/api/checklists/imv", response_model=List[ChecklistItemResponse])
def get_imv_checklists():
    return get_imv_checklist()
