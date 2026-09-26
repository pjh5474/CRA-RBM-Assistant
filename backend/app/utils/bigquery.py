import json
import os
from functools import lru_cache

from google.cloud import bigquery
from google.oauth2 import service_account


@lru_cache
def get_bigquery_client() -> bigquery.Client:
    project_id = os.getenv("GCP_PROJECT_ID")
    service_account_file = os.getenv("GCP_SERVICE_ACCOUNT_FILE")
    service_account_json = os.getenv("GCP_SERVICE_ACCOUNT_JSON")

    if not project_id:
        raise RuntimeError("GCP_PROJECT_ID is not configured.")

    # Local development: JSON key file
    if service_account_file:
        credentials = service_account.Credentials.from_service_account_file(
            service_account_file
        )

    # Deployment: JSON stored in environment variable
    elif service_account_json:
        service_account_info = json.loads(service_account_json)

        credentials = service_account.Credentials.from_service_account_info(
            service_account_info
        )

    else:
        raise RuntimeError(
            "GCP_SERVICE_ACCOUNT_FILE or "
            "GCP_SERVICE_ACCOUNT_JSON must be configured."
        )

    return bigquery.Client(
        project=project_id,
        credentials=credentials,
    )
