from typing import Any, Dict, List

from app.utils.supabase_client import get_supabase_client


def to_checklist_item(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "category": row["category"],
        "item": row["item"],
        "rationale": row["rationale"],
    }


def get_checklist_by_type_from_supabase(checklist_type: str) -> List[Dict[str, Any]]:
    supabase = get_supabase_client()

    response = (
        supabase.table("checklist_templates")
        .select("category,item,rationale,display_order")
        .eq("checklist_type", checklist_type)
        .order("display_order")
        .execute()
    )

    return [to_checklist_item(row) for row in response.data]


def get_all_checklists_from_supabase() -> Dict[str, List[Dict[str, Any]]]:
    return {
        "sivChecklist": get_checklist_by_type_from_supabase("siv"),
        "imvChecklist": get_checklist_by_type_from_supabase("imv"),
    }
