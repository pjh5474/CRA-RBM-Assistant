from typing import List

from fastapi import APIRouter

from app.schemas.checklist_schema import ChecklistItemResponse, ChecklistResponse
from app.services.checklist_service import (
    get_all_checklists,
    get_imv_checklist,
    get_siv_checklist,
)

router = APIRouter(prefix="/api/checklists", tags=["checklists"])


@router.get("", response_model=ChecklistResponse)
def get_checklists():
    return get_all_checklists()


@router.get("/siv", response_model=List[ChecklistItemResponse])
def get_siv_checklists():
    return get_siv_checklist()


@router.get("/imv", response_model=List[ChecklistItemResponse])
def get_imv_checklists():
    return get_imv_checklist()
