from typing import Any, Dict, List

from fastapi import HTTPException

from app.utils.data_loader import load_json_file


def get_all_studies() -> List[Dict[str, Any]]:
    studies = load_json_file("data/sample-studies.json")

    return [
        {
            "studyId": study["studyId"],
            "title": study["title"],
            "phase": study["phase"],
            "indication": study["indication"],
            "sponsor": study["sponsor"],
        }
        for study in studies
    ]


def get_study_by_id(study_id: str) -> Dict[str, Any]:
    studies = load_json_file("data/sample-studies.json")

    for study in studies:
        if study["studyId"] == study_id:
            return study

    raise HTTPException(status_code=404, detail=f"Study not found: {study_id}")


def get_sites_by_study_id(study_id: str) -> List[Dict[str, Any]]:
    # study 존재 여부를 먼저 확인해서 잘못된 studyId 요청을 구분합니다.
    get_study_by_id(study_id)

    sites = load_json_file("data/synthetic-sites.json")

    return [site for site in sites if site["studyId"] == study_id]
