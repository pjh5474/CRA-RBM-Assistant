from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BACKEND_ROOT = PROJECT_ROOT / "backend"

sys.path.append(str(BACKEND_ROOT))

from app.utils.supabase_client import get_supabase_client  # noqa: E402


def load_json(relative_path: str):
    file_path = PROJECT_ROOT / relative_path

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def seed_studies():
    supabase = get_supabase_client()
    studies = load_json("data/sample-studies.json")

    rows = []
    for study in studies:
        rows.append(
            {
                "study_id": study["studyId"],
                "title": study["title"],
                "phase": study["phase"],
                "indication": study["indication"],
                "sponsor": study["sponsor"],
                "study_design": study["studyDesign"],
                "intervention": study["intervention"],
                "population": study["population"],
                "endpoints": study["endpoints"],
                "eligibility_criteria": study["eligibilityCriteria"],
                "visit_schedule": study["visitSchedule"],
                "safety_reporting": study["safetyReporting"],
                "cra_focus_areas": study["craFocusAreas"],
            }
        )

    supabase.table("studies").upsert(rows).execute()
    print(f"Seeded studies: {len(rows)}")


def seed_sites():
    supabase = get_supabase_client()
    sites = load_json("data/synthetic-sites.json")

    rows = []
    for site in sites:
        rows.append(
            {
                "site_id": site["siteId"],
                "study_id": site["studyId"],
                "site_name": site["siteName"],
                "principal_investigator": site["principalInvestigator"],
                "country": site["country"],
                "status": site["status"],
                "activation_date": site["activationDate"],
                "target_enrollment": site["targetEnrollment"],
                "current_enrollment": site["currentEnrollment"],
            }
        )

    supabase.table("sites").upsert(rows).execute()
    print(f"Seeded sites: {len(rows)}")


def seed_monitoring_metrics():
    supabase = get_supabase_client()
    metrics = load_json("data/monitoring-metrics.json")

    rows = []
    for metric in metrics:
        rows.append(
            {
                "metric_id": metric["metricId"],
                "site_id": metric["siteId"],
                "study_id": metric["studyId"],
                "open_queries": metric["openQueries"],
                "query_aging_days": metric["queryAgingDays"],
                "protocol_deviations": metric["protocolDeviations"],
                "sae_reporting_delay_count": metric["saeReportingDelayCount"],
                "missing_essential_documents": metric["missingEssentialDocuments"],
                "ip_accountability_issues": metric["ipAccountabilityIssues"],
                "icf_issues": metric["icfIssues"],
                "last_monitoring_visit_date": metric["lastMonitoringVisitDate"],
            }
        )

    supabase.table("monitoring_metrics").upsert(rows).execute()
    print(f"Seeded monitoring metrics: {len(rows)}")


def seed_checklist_templates():
    supabase = get_supabase_client()
    checklists = load_json("data/checklist-templates.json")

    rows = []

    for index, item in enumerate(checklists["sivChecklist"], start=1):
        rows.append(
            {
                "checklist_type": "siv",
                "category": item["category"],
                "item": item["item"],
                "rationale": item["rationale"],
                "display_order": index,
            }
        )

    for index, item in enumerate(checklists["imvChecklist"], start=1):
        rows.append(
            {
                "checklist_type": "imv",
                "category": item["category"],
                "item": item["item"],
                "rationale": item["rationale"],
                "display_order": index,
            }
        )

    # checklist_templates는 identity PK라 upsert 기준이 애매합니다.
    # 초기 seed 전에는 Supabase SQL Editor에서 truncate 후 실행하는 방식을 권장합니다.
    supabase.table("checklist_templates").insert(rows).execute()
    print(f"Seeded checklist templates: {len(rows)}")


def main():
    seed_studies()
    seed_sites()
    seed_monitoring_metrics()
    seed_checklist_templates()


if __name__ == "__main__":
    main()
