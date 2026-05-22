import os
from typing import Any, Dict, List

from app.repositories.checklist_repository import (
    get_all_checklists_from_supabase,
    get_checklist_by_type_from_supabase,
)
from app.utils.data_loader import load_json_file

DATA_SOURCE = os.getenv("DATA_SOURCE", "json")


def get_all_checklists() -> Dict[str, List[Dict[str, Any]]]:
    if DATA_SOURCE == "supabase":
        return get_all_checklists_from_supabase()

    return load_json_file("data/checklist-templates.json")


def get_siv_checklist() -> List[Dict[str, Any]]:
    if DATA_SOURCE == "supabase":
        return get_checklist_by_type_from_supabase("siv")

    checklists = get_all_checklists()
    return checklists["sivChecklist"]


def get_imv_checklist() -> List[Dict[str, Any]]:
    if DATA_SOURCE == "supabase":
        return get_checklist_by_type_from_supabase("imv")

    checklists = get_all_checklists()
    return checklists["imvChecklist"]
