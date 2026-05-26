from datetime import date
from typing import Any, Dict, List, Optional

from fastapi import HTTPException

from app.repositories.delegation_training_repository import (
    get_delegation_training_records_by_site_from_supabase,
    get_site_staff_by_site_from_supabase,
)
from app.services.study_service import get_risk_sites_by_study_id


def get_site_name_from_risk_sites(study_id: str, site_id: str) -> str:
    risk_sites = get_risk_sites_by_study_id(study_id)

    for site in risk_sites:
        if site["siteId"] == site_id:
            return site["siteName"]

    raise HTTPException(
        status_code=404,
        detail=f"Site not found for study {study_id}: {site_id}",
    )


def parse_optional_date(value: Optional[str]) -> Optional[date]:
    if not value:
        return None

    return date.fromisoformat(value)


def build_issue_response(
    record: Dict[str, Any],
    issue_type: str,
    message: str,
) -> Dict[str, Any]:
    return {
        "recordId": record["recordId"],
        "staffId": record["staffId"],
        "staffName": record.get("staffName") or "Unknown staff",
        "role": record.get("role") or "Unknown role",
        "delegatedTask": record["delegatedTask"],
        "delegationStartDate": record["delegationStartDate"],
        "gcpTrainingDate": record.get("gcpTrainingDate"),
        "protocolTrainingDate": record.get("protocolTrainingDate"),
        "trainingStatus": record["trainingStatus"],
        "status": "Issue",
        "issueType": issue_type,
        "message": message,
    }


def check_delegation_training_record(
    record: Dict[str, Any],
) -> Dict[str, Any]:
    delegation_start_date = date.fromisoformat(record["delegationStartDate"])
    gcp_training_date = parse_optional_date(record.get("gcpTrainingDate"))
    protocol_training_date = parse_optional_date(record.get("protocolTrainingDate"))

    if not gcp_training_date and not protocol_training_date:
        return build_issue_response(
            record=record,
            issue_type="Missing GCP and Protocol Training",
            message=(
                "Both GCP training date and protocol training date are missing "
                "for this delegated task."
            ),
        )

    if not gcp_training_date:
        return build_issue_response(
            record=record,
            issue_type="Missing GCP Training",
            message="GCP training date is missing for this delegated task.",
        )

    if not protocol_training_date:
        return build_issue_response(
            record=record,
            issue_type="Missing Protocol Training",
            message="Protocol training date is missing for this delegated task.",
        )

    if gcp_training_date > delegation_start_date:
        return build_issue_response(
            record=record,
            issue_type="GCP Training After Delegation",
            message=(
                "GCP training was completed after the delegation start date. "
                "CRA should review training evidence and delegation timing."
            ),
        )

    if protocol_training_date > delegation_start_date:
        return build_issue_response(
            record=record,
            issue_type="Protocol Training After Delegation",
            message=(
                "Protocol training was completed after the delegation start date. "
                "CRA should review whether task delegation occurred before required training."
            ),
        )

    return {
        "recordId": record["recordId"],
        "staffId": record["staffId"],
        "staffName": record.get("staffName") or "Unknown staff",
        "role": record.get("role") or "Unknown role",
        "delegatedTask": record["delegatedTask"],
        "delegationStartDate": record["delegationStartDate"],
        "gcpTrainingDate": record.get("gcpTrainingDate"),
        "protocolTrainingDate": record.get("protocolTrainingDate"),
        "trainingStatus": record["trainingStatus"],
        "status": "Valid",
        "issueType": None,
        "message": (
            "GCP and protocol training dates are consistent with the delegation "
            "start date."
        ),
    }


def get_delegation_training_check(
    study_id: str,
    site_id: str,
) -> Dict[str, Any]:
    site_name = get_site_name_from_risk_sites(study_id, site_id)

    staff = get_site_staff_by_site_from_supabase(
        study_id=study_id,
        site_id=site_id,
    )

    records = get_delegation_training_records_by_site_from_supabase(
        study_id=study_id,
        site_id=site_id,
    )

    checks = [check_delegation_training_record(record) for record in records]

    issue_records = [check for check in checks if check["status"] == "Issue"]

    missing_training_records = [
        check
        for check in issue_records
        if check["issueType"]
        in [
            "Missing GCP and Protocol Training",
            "Missing GCP Training",
            "Missing Protocol Training",
        ]
    ]

    training_after_delegation_records = [
        check
        for check in issue_records
        if check["issueType"]
        in [
            "GCP Training After Delegation",
            "Protocol Training After Delegation",
        ]
    ]

    return {
        "studyId": study_id,
        "siteId": site_id,
        "siteName": site_name,
        "totalRecords": len(records),
        "validRecords": len(records) - len(issue_records),
        "issueRecords": len(issue_records),
        "missingTrainingRecords": len(missing_training_records),
        "trainingAfterDelegationRecords": len(training_after_delegation_records),
        "staff": staff,
        "records": records,
        "checks": checks,
    }
