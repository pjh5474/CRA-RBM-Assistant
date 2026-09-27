import os

from databricks import sql


def get_databricks_connection():
    server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
    http_path = os.getenv("DATABRICKS_HTTP_PATH")
    access_token = os.getenv("DATABRICKS_TOKEN")

    if not server_hostname:
        raise RuntimeError("DATABRICKS_SERVER_HOSTNAME is not configured.")

    if not http_path:
        raise RuntimeError("DATABRICKS_HTTP_PATH is not configured.")

    if not access_token:
        raise RuntimeError("DATABRICKS_TOKEN is not configured.")

    return sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token,
    )
