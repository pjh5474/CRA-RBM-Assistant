from typing import List, Optional

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
from app.schemas.action_item_schema import SiteActionItemsResponse
from app.schemas.clinical_trials_schema import (
    ClinicalTrialDetailResponse,
    ClinicalTrialSearchResponse,
    ImportClinicalTrialResponse,
)
from app.schemas.audit_log_schema import AuditLogResponse
from app.schemas.alert_schema import HighRiskSiteAlertResponse
from app.schemas.monitoring_report_schema import MonitoringReportDraftResponse
from app.schemas.essential_document_schema import (
    EssentialDocumentReadinessResponse,
)


from app.services.essential_document_service import (
    get_essential_document_readiness,
)
from app.services.monitoring_report_service import get_monitoring_report_draft
from app.services.alert_service import get_high_risk_site_alerts
from app.services.audit_log_service import get_audit_logs
from app.services.action_item_service import get_action_items_by_study_id
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

from app.services.external.clinical_trials_service import (
    get_clinical_trial_detail,
    search_clinical_trials,
)
from app.services.external.clinical_trials_service import (
    get_clinical_trial_detail,
    import_clinical_trial_to_supabase,
    search_clinical_trials,
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


@app.get(
    "/api/studies/{study_id}/action-items",
    response_model=List[SiteActionItemsResponse],
)
def get_study_action_items(study_id: str):
    return get_action_items_by_study_id(study_id)


@app.get(
    "/api/studies/{study_id}/sites/{site_id}/monitoring-report-draft",
    response_model=MonitoringReportDraftResponse,
)
def get_site_monitoring_report_draft(study_id: str, site_id: str):
    return get_monitoring_report_draft(study_id=study_id, site_id=site_id)


@app.get("/api/checklists", response_model=ChecklistResponse)
def get_checklists():
    return get_all_checklists()


@app.get("/api/checklists/siv", response_model=List[ChecklistItemResponse])
def get_siv_checklists():
    return get_siv_checklist()


@app.get("/api/checklists/imv", response_model=List[ChecklistItemResponse])
def get_imv_checklists():
    return get_imv_checklist()


@app.get(
    "/api/external/clinical-trials/search",
    response_model=ClinicalTrialSearchResponse,
)
async def search_external_clinical_trials(query: str, page_size: int = 10):
    return await search_clinical_trials(query=query, page_size=page_size)


@app.get(
    "/api/external/clinical-trials/{nct_id}",
    response_model=ClinicalTrialDetailResponse,
)
async def get_external_clinical_trial_detail(nct_id: str):
    return await get_clinical_trial_detail(nct_id)


@app.post(
    "/api/external/clinical-trials/{nct_id}/import",
    response_model=ImportClinicalTrialResponse,
)
async def import_external_clinical_trial(nct_id: str):
    return await import_clinical_trial_to_supabase(nct_id)


@app.get("/api/audit-logs", response_model=List[AuditLogResponse])
def get_audit_log_list(
    limit: int = 50,
    table_name: Optional[str] = None,
    action: Optional[str] = None,
):
    return get_audit_logs(
        limit=limit,
        table_name=table_name,
        action=action,
    )


@app.get(
    "/api/alerts/high-risk-sites",
    response_model=List[HighRiskSiteAlertResponse],
)
def get_high_risk_site_alert_list(include_medium: bool = True):
    return get_high_risk_site_alerts(include_medium=include_medium)


@app.get(
    "/api/studies/{study_id}/sites/{site_id}/essential-documents",
    response_model=EssentialDocumentReadinessResponse,
)
def get_site_essential_document_readiness(study_id: str, site_id: str):
    return get_essential_document_readiness(
        study_id=study_id,
        site_id=site_id,
    )
