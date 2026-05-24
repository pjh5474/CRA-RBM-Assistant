from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.api import api_router

frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")


app = FastAPI(
    title="CRA-RBM Assistant API",
    description="Backend API for CRA risk-based monitoring assistant prototype",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        frontend_origin,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
