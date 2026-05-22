from typing import List
from pydantic import BaseModel


class ChecklistItemResponse(BaseModel):
    category: str
    item: str
    rationale: str


class ChecklistResponse(BaseModel):
    sivChecklist: List[ChecklistItemResponse]
    imvChecklist: List[ChecklistItemResponse]
