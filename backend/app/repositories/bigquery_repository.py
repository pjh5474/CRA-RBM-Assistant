import os

from google.cloud import bigquery

from app.utils.bigquery import get_bigquery_client


PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = os.getenv("BQ_DATASET_ID", "clinical_trials")


def _table(table_name: str) -> str:
    return f"`{PROJECT_ID}.{DATASET_ID}.{table_name}`"


class BigQueryRepository:
    def __init__(self):
        self.client = get_bigquery_client()

    def get_overview(self) -> dict:
        query = f"""
        SELECT
            SUM(study_count) AS total_trials,

            SUM(
                CASE
                    WHEN study_type = 'INTERVENTIONAL'
                    THEN study_count
                    ELSE 0
                END
            ) AS interventional_trials,

            SUM(
                CASE
                    WHEN study_type = 'OBSERVATIONAL'
                    THEN study_count
                    ELSE 0
                END
            ) AS observational_trials,

            SUM(
                CASE
                    WHEN study_type NOT IN (
                        'INTERVENTIONAL',
                        'OBSERVATIONAL'
                    )
                    THEN study_count
                    ELSE 0
                END
            ) AS other_trials,

            MAX(
                CASE
                    WHEN study_year <= EXTRACT(YEAR FROM CURRENT_DATE())
                    THEN study_year
                END
            ) AS latest_year

        FROM {_table("gold_yearly_summary")}
        WHERE study_year IS NOT NULL
        """

        row = next(iter(self.client.query(query).result()))

        return dict(row.items())

    def get_yearly(self) -> list[dict]:
        query = f"""
        SELECT
            study_year,
            SUM(study_count) AS trial_count
        FROM {_table("gold_yearly_summary")}
        WHERE study_year IS NOT NULL
        GROUP BY study_year
        ORDER BY study_year
        """

        rows = self.client.query(query).result()

        return [dict(row.items()) for row in rows]

    def get_countries(
        self,
        limit: int = 20,
    ) -> list[dict]:
        query = f"""
        SELECT
            country,
            SUM(trial_count) AS trial_count
        FROM {_table("gold_country_summary")}
        WHERE country IS NOT NULL
        GROUP BY country
        ORDER BY trial_count DESC
        LIMIT @limit
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter(
                    "limit",
                    "INT64",
                    limit,
                )
            ]
        )

        rows = self.client.query(
            query,
            job_config=job_config,
        ).result()

        return [dict(row.items()) for row in rows]

    def get_condition_trend(
        self,
        condition: str,
    ) -> list[dict]:
        query = f"""
        SELECT
            condition,
            study_year,
            study_count AS trial_count,
            interventional_count,
            observational_count
        FROM {_table("gold_condition_trends")}
        WHERE
            study_year IS NOT NULL
            AND study_year <= EXTRACT(YEAR FROM CURRENT_DATE())
            AND LOWER(condition) = LOWER(@condition)
        ORDER BY study_year
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter(
                    "condition",
                    "STRING",
                    condition,
                )
            ]
        )

        rows = self.client.query(
            query,
            job_config=job_config,
        ).result()

        return [dict(row.items()) for row in rows]
