from typing import Any, Dict, List

import httpx
from fastapi import HTTPException

CLINICAL_TRIALS_API_BASE_URL = "https://clinicaltrials.gov/api/v2/studies"


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
        response = await client.get(CLINICAL_TRIALS_API_BASE_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="ClinicalTrials.gov API request failed",
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
        response = await client.get(url)

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Clinical trial not found: {nct_id}",
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="ClinicalTrials.gov API request failed",
        )

    data = response.json()
    return _map_detail(data)
