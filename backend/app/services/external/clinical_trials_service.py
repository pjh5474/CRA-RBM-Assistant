from typing import Any, Dict, List

import httpx
from fastapi import HTTPException

from app.repositories.study_repository import (
    study_exists_in_supabase,
    upsert_study_to_supabase,
)
from app.services.demo_data_service import (
    create_demo_operational_data_for_imported_study,
)

CLINICAL_TRIALS_API_BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

CLINICAL_TRIALS_API_HEADERS = {
    "User-Agent": "CRA-RBM-Assistant/1.0 (portfolio project; contact: warwarsn@gmail.com)",
    "Accept": "application/json",
}


def _get_nested(data: Dict[str, Any], path: List[str], default=None):
    current = data

    for key in path:
        if not isinstance(current, dict):
            return default

        current = current.get(key)

        if current is None:
            return default

    return current


def _extract_intervention_names(study: Dict[str, Any]) -> List[str]:
    interventions = _get_nested(
        study,
        ["protocolSection", "armsInterventionsModule", "interventions"],
        [],
    )

    return [
        intervention.get("name")
        for intervention in interventions
        if intervention.get("name")
    ]


def _extract_outcome_measures(study: Dict[str, Any], outcome_type: str) -> List[str]:
    outcomes = _get_nested(
        study,
        ["protocolSection", "outcomesModule", outcome_type],
        [],
    )

    return [outcome.get("measure") for outcome in outcomes if outcome.get("measure")]


def _extract_design_value(study: Dict[str, Any], key: str):
    return _get_nested(
        study,
        ["protocolSection", "designModule", "designInfo", key],
        None,
    )


def _extract_masking(study: Dict[str, Any]) -> str | None:
    masking_info = _extract_design_value(study, "maskingInfo")

    if not isinstance(masking_info, dict):
        return None

    return masking_info.get("masking")


def _extract_who_masked(study: Dict[str, Any]) -> List[str]:
    masking_info = _extract_design_value(study, "maskingInfo")

    if not isinstance(masking_info, dict):
        return []

    who_masked = masking_info.get("whoMasked", [])

    if not isinstance(who_masked, list):
        return []

    return who_masked


def _map_search_item(study: Dict[str, Any]) -> Dict[str, Any]:
    identification = _get_nested(study, ["protocolSection", "identificationModule"], {})
    status = _get_nested(study, ["protocolSection", "statusModule"], {})
    design = _get_nested(study, ["protocolSection", "designModule"], {})
    conditions = _get_nested(
        study, ["protocolSection", "conditionsModule", "conditions"], []
    )

    nct_id = identification.get("nctId") or ""
    title = (
        identification.get("briefTitle")
        or identification.get("officialTitle")
        or "Untitled clinical trial"
    )

    return {
        "nctId": nct_id,
        "title": title,
        "status": status.get("overallStatus"),
        "phases": design.get("phases", []),
        "conditions": conditions,
        "interventions": _extract_intervention_names(study),
    }


def _map_detail(study: Dict[str, Any]) -> Dict[str, Any]:
    identification = _get_nested(study, ["protocolSection", "identificationModule"], {})
    description = _get_nested(study, ["protocolSection", "descriptionModule"], {})
    status = _get_nested(study, ["protocolSection", "statusModule"], {})
    design = _get_nested(study, ["protocolSection", "designModule"], {})
    conditions = _get_nested(
        study, ["protocolSection", "conditionsModule", "conditions"], []
    )
    eligibility = _get_nested(study, ["protocolSection", "eligibilityModule"], {})

    nct_id = identification.get("nctId") or ""
    title = (
        identification.get("officialTitle")
        or identification.get("briefTitle")
        or "Untitled clinical trial"
    )

    return {
        "nctId": nct_id,
        "title": title,
        "briefSummary": description.get("briefSummary"),
        "status": status.get("overallStatus"),
        "phases": design.get("phases", []),
        "conditions": conditions,
        "interventions": _extract_intervention_names(study),
        "studyType": design.get("studyType"),
        "allocation": _extract_design_value(study, "allocation"),
        "masking": _extract_masking(study),
        "whoMasked": _extract_who_masked(study),
        "primaryOutcomes": _extract_outcome_measures(study, "primaryOutcomes"),
        "secondaryOutcomes": _extract_outcome_measures(study, "secondaryOutcomes"),
        "eligibilityCriteria": eligibility.get("eligibilityCriteria"),
    }


async def search_clinical_trials(query: str, page_size: int = 10) -> Dict[str, Any]:
    params = {
        "query.term": query,
        "pageSize": page_size,
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(
            CLINICAL_TRIALS_API_BASE_URL,
            params=params,
            headers=CLINICAL_TRIALS_API_HEADERS,
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail={
                "message": "ClinicalTrials.gov API request failed",
                "statusCode": response.status_code,
                "response": response.text[:500],
            },
        )

    data = response.json()
    studies = data.get("studies", [])

    results = [
        _map_search_item(study)
        for study in studies
        if _map_search_item(study).get("nctId")
    ]

    return {
        "query": query,
        "count": len(results),
        "results": results,
    }


async def get_clinical_trial_detail(nct_id: str) -> Dict[str, Any]:
    url = f"{CLINICAL_TRIALS_API_BASE_URL}/{nct_id}"

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(
            url,
            headers=CLINICAL_TRIALS_API_HEADERS,
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Clinical trial not found: {nct_id}",
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail={
                "message": "ClinicalTrials.gov API request failed",
                "statusCode": response.status_code,
                "response": response.text[:500],
            },
        )

    data = response.json()
    return _map_detail(data)


def _join_or_default(values: List[str], default: str = "Not specified") -> str:
    if not values:
        return default

    return ", ".join(values)


def convert_clinical_trial_to_internal_study(
    clinical_trial: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Convert ClinicalTrials.gov detail response into internal Study format.

    This mapping is intentionally simplified for CRA-RBM Assistant MVP.
    Some fields are stored as placeholders because public registry data
    does not always contain protocol-level operational details.
    """
    nct_id = clinical_trial["nctId"]

    phases = clinical_trial.get("phases", [])
    conditions = clinical_trial.get("conditions", [])
    interventions = clinical_trial.get("interventions", [])
    primary_outcomes = clinical_trial.get("primaryOutcomes", [])
    secondary_outcomes = clinical_trial.get("secondaryOutcomes", [])

    return {
        "studyId": nct_id,
        "title": clinical_trial.get("title") or "Untitled clinical trial",
        "phase": _join_or_default(phases),
        "indication": _join_or_default(conditions),
        "sponsor": "ClinicalTrials.gov Public Registry",
        "studyDesign": {
            "type": clinical_trial.get("studyType"),
            "allocation": clinical_trial.get("allocation"),
            "masking": clinical_trial.get("masking"),
            "whoMasked": clinical_trial.get("whoMasked", []),
            "registryStatus": clinical_trial.get("status"),
            "source": "ClinicalTrials.gov",
        },
        "intervention": {
            "interventions": interventions,
            "investigationalProduct": interventions[0] if interventions else None,
            "comparator": None,
            "route": None,
            "dose": None,
            "treatmentDuration": None,
        },
        "population": {
            "targetPopulation": _join_or_default(conditions),
            "plannedEnrollment": None,
            "ageRange": None,
        },
        "endpoints": {
            "primaryEndpoint": (
                primary_outcomes[0] if primary_outcomes else "Not specified"
            ),
            "primaryEndpoints": primary_outcomes,
            "secondaryEndpoints": secondary_outcomes,
        },
        "eligibilityCriteria": {
            "rawText": clinical_trial.get("eligibilityCriteria"),
            "inclusion": [],
            "exclusion": [],
        },
        "visitSchedule": [],
        "safetyReporting": {
            "aeCollectionPeriod": "Not specified in imported registry preview",
            "saeReportingTimeline": "Not specified in imported registry preview",
            "pregnancyReportingRequired": None,
        },
        "craFocusAreas": [
            "Review registry information against protocol source document",
            "Confirm eligibility criteria from approved protocol",
            "Confirm endpoint-related source data requirements",
            "Confirm safety reporting process from protocol and study manual",
            "Confirm essential document readiness before site initiation",
        ],
    }


async def import_clinical_trial_to_supabase(nct_id: str) -> Dict[str, Any]:
    """
    Fetch ClinicalTrials.gov detail, convert it into internal Study format,
    upsert it into Supabase, and create synthetic demo operational data.
    """
    existed_before_import = study_exists_in_supabase(nct_id)

    clinical_trial = await get_clinical_trial_detail(nct_id)
    internal_study = convert_clinical_trial_to_internal_study(clinical_trial)

    imported_study = upsert_study_to_supabase(internal_study)

    demo_data_created = create_demo_operational_data_for_imported_study(imported_study)

    status = "updated" if existed_before_import else "created"

    message = (
        "Study already existed and was updated with demo operational data."
        if existed_before_import
        else "Study imported successfully with demo operational data."
    )

    return {
        "status": status,
        "message": message,
        "demoDataCreated": demo_data_created,
        "study": imported_study,
    }
