import json
import os
from typing import Any

from app.utils.databricks_sql import (
    get_databricks_connection,
)


CATALOG = os.getenv("DATABRICKS_CATALOG")
SCHEMA = os.getenv(
    "DATABRICKS_SCHEMA",
    "clinical_trials",
)


def _table(name: str) -> str:
    if not CATALOG:
        raise RuntimeError("DATABRICKS_CATALOG is not configured.")

    return f"{CATALOG}.{SCHEMA}.{name}"


def _fetch_all(
    query: str,
    parameters: list[Any] | None = None,
) -> list[dict[str, Any]]:
    with get_databricks_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                query,
                parameters or [],
            )

            columns = [column[0] for column in cursor.description]

            return [dict(zip(columns, row)) for row in cursor.fetchall()]


def _json_array(value):
    if value is None:
        return []

    if isinstance(value, list):
        return value

    return json.loads(value)


def search_registry_studies(
    query_text: str | None = None,
    status: str | None = None,
    phase: str | None = None,
    country: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> dict[str, Any]:

    conditions = ["1 = 1"]
    parameters: list[Any] = []

    if query_text:
        pattern = f"%{query_text.lower()}%"

        conditions.append(
            """
            (
                LOWER(nct_id) LIKE ?
                OR LOWER(brief_title) LIKE ?
                OR EXISTS(
                    conditions,
                    c -> LOWER(c) LIKE ?
                )
            )
            """
        )

        parameters.extend(
            [
                pattern,
                pattern,
                pattern,
            ]
        )

    if status:
        conditions.append("overall_status = ?")
        parameters.append(status)

    if phase:
        conditions.append("array_contains(phases, ?)")
        parameters.append(phase)

    if country:
        conditions.append("array_contains(countries, ?)")
        parameters.append(country)

    # hasNext를 계산하기 위해 한 건 더 조회
    fetch_size = page_size + 1
    offset = (page - 1) * page_size

    sql_query = f"""
        SELECT
            nct_id,
            brief_title,
            study_type,
            TO_JSON(phases) AS phases_json,
            overall_status,
            enrollment_count,
            start_date,
            last_update_date,
            completion_date,
            TO_JSON(conditions) AS conditions_json,
            TO_JSON(countries) AS countries_json,
            TO_JSON(intervention_names) AS intervention_names_json,
            has_results
        FROM {_table("serving_study_search")}
        WHERE {" AND ".join(conditions)}
        ORDER BY
            last_update_date DESC NULLS LAST,
            nct_id DESC
        LIMIT {fetch_size}
        OFFSET {offset}
    """

    rows = _fetch_all(
        sql_query,
        parameters,
    )

    has_next = len(rows) > page_size

    rows = rows[:page_size]

    items = [
        {
            "nctId": row["nct_id"],
            "title": row["brief_title"],
            "studyType": row["study_type"],
            "phases": _json_array(row["phases_json"]),
            "status": row["overall_status"],
            "enrollmentCount": row["enrollment_count"],
            "startDate": row["start_date"],
            "lastUpdateDate": row["last_update_date"],
            "completionDate": row["completion_date"],
            "conditions": _json_array(row["conditions_json"]),
            "countries": _json_array(row["countries_json"]),
            "interventionNames": _json_array(row["intervention_names_json"]),
            "hasResults": row["has_results"],
        }
        for row in rows
    ]

    return {
        "items": items,
        "page": page,
        "pageSize": page_size,
        "hasNext": has_next,
    }


def get_registry_study_detail(
    nct_id: str,
) -> dict[str, Any] | None:

    query = f"""
        SELECT
            nct_id,
            brief_title,
            official_title,
            study_type,
            TO_JSON(phases) AS phases_json,
            overall_status,

            brief_summary,
            TO_JSON(who_masked) AS who_masked_json,
            eligibility_criteria,

            enrollment_count,
            enrollment_type,
            allocation,
            intervention_model,
            primary_purpose,
            masking,
            start_date,
            completion_date,
            has_results,

            TO_JSON(conditions)
                AS conditions_json,

            TO_JSON(
                array_sort(
                    array_distinct(
                        filter(
                            transform(
                                locations,
                                x -> x.country
                            ),
                            x -> x IS NOT NULL
                        )
                    )
                )
            ) AS countries_json,

            TO_JSON(interventions)
                AS interventions_json,

            TO_JSON(outcomes)
                AS outcomes_json,

            TO_JSON(locations)
                AS locations_json

        FROM {_table("serving_study_detail")}

        WHERE nct_id = ?

        LIMIT 1
    """

    rows = _fetch_all(
        query,
        [nct_id],
    )

    if not rows:
        return None

    row = rows[0]

    return {
        "nctId": row["nct_id"],
        "title": row["brief_title"],
        "officialTitle": row["official_title"],
        "studyType": row["study_type"],
        "phases": _json_array(row["phases_json"]),
        "status": row["overall_status"],
        "briefSummary": row["brief_summary"],
        "whoMasked": _json_array(row["who_masked_json"]),
        "eligibilityCriteria": row["eligibility_criteria"],
        "enrollmentCount": row["enrollment_count"],
        "enrollmentType": row["enrollment_type"],
        "allocation": row["allocation"],
        "interventionModel": row["intervention_model"],
        "primaryPurpose": row["primary_purpose"],
        "masking": row["masking"],
        "startDate": row["start_date"],
        "completionDate": row["completion_date"],
        "hasResults": row["has_results"],
        "conditions": _json_array(row["conditions_json"]),
        "countries": _json_array(row["countries_json"]),
        "interventions": _json_array(row["interventions_json"]),
        "outcomes": _json_array(row["outcomes_json"]),
        "locations": _json_array(row["locations_json"]),
    }
