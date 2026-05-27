from app.utils.supabase_client import get_supabase_client


def delete_existing_demo_operational_data_by_study_id(study_id: str) -> None:
    supabase = get_supabase_client()

    # Child tables first
    (supabase.table("monitoring_metrics").delete().eq("study_id", study_id).execute())

    (supabase.table("essential_documents").delete().eq("study_id", study_id).execute())

    (supabase.table("protocol_deviations").delete().eq("study_id", study_id).execute())

    (supabase.table("subject_consents").delete().eq("study_id", study_id).execute())

    (supabase.table("icf_versions").delete().eq("study_id", study_id).execute())

    (
        supabase.table("delegation_training_records")
        .delete()
        .eq("study_id", study_id)
        .execute()
    )

    (supabase.table("site_staff").delete().eq("study_id", study_id).execute())

    # Parent operational table last
    (supabase.table("sites").delete().eq("study_id", study_id).execute())
