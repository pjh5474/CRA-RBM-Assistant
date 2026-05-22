from fastapi import FastAPI
from typing import List

from app.schemas.risk_schema import SiteRiskResponse
from app.services.risk_scoring_service import get_all_site_risks

app = FastAPI(
    title="CRA-RBM Assistant API",
    description="Backend API for CRA risk-based monitoring assistant prototype",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "CRA-RBM Assistant API",
    }


@app.get("/api/risk/sites", response_model=List[SiteRiskResponse])
def get_site_risks():
    return get_all_site_risks()
