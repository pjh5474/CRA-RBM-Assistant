from fastapi import APIRouter

from app.schemas.essential_document_schema import EssentialDocumentReadinessResponse
from app.schemas.icf_schema import IcfVersionCheckResponse
from app.schemas.monitoring_report_schema import MonitoringReportDraftResponse
from app.schemas.protocol_deviation_schema import ProtocolDeviationSummaryResponse
from app.services.essential_document_service import get_essential_document_readiness
from app.services.icf_service import get_icf_version_check
from app.services.monitoring_report_service import get_monitoring_report_draft
from app.services.protocol_deviation_service import get_protocol_deviation_summary

router = APIRouter(
    prefix="/api/studies/{study_id}/sites/{site_id}",
    tags=["site-monitoring"],
)


@router.get(
    "/monitoring-report-draft",
    response_model=MonitoringReportDraftResponse,
)
def get_site_monitoring_report_draft(study_id: str, site_id: str):
    return get_monitoring_report_draft(study_id=study_id, site_id=site_id)


@router.get(
    "/essential-documents",
    response_model=EssentialDocumentReadinessResponse,
)
def get_site_essential_document_readiness(study_id: str, site_id: str):
    return get_essential_document_readiness(
        study_id=study_id,
        site_id=site_id,
    )


@router.get(
    "/protocol-deviations",
    response_model=ProtocolDeviationSummaryResponse,
)
def get_site_protocol_deviation_summary(study_id: str, site_id: str):
    return get_protocol_deviation_summary(
        study_id=study_id,
        site_id=site_id,
    )


@router.get(
    "/icf-version-check",
    response_model=IcfVersionCheckResponse,
)
def get_site_icf_version_check(study_id: str, site_id: str):
    return get_icf_version_check(
        study_id=study_id,
        site_id=site_id,
    )
