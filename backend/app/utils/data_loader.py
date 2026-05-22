import json
from pathlib import Path
from typing import Any


def get_project_root() -> Path:
    """
    Returns the project root directory.

    Current file path:
    backend/app/utils/data_loader.py

    Project root:
    cra-rbm-assistant/
    """
    return Path(__file__).resolve().parents[3]


def load_json_file(relative_path: str) -> Any:
    """
    Load a JSON file from the project root.

    Example:
        load_json_file("data/monitoring-metrics.json")
    """
    file_path = get_project_root() / relative_path

    if not file_path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
