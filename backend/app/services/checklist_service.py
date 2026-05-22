from typing import Any, Dict, List

from app.utils.data_loader import load_json_file


def get_all_checklists() -> Dict[str, List[Dict[str, Any]]]:
    return load_json_file("data/checklist-templates.json")


def get_siv_checklist() -> List[Dict[str, Any]]:
    checklists = get_all_checklists()
    return checklists["sivChecklist"]


def get_imv_checklist() -> List[Dict[str, Any]]:
    checklists = get_all_checklists()
    return checklists["imvChecklist"]
