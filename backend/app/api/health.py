from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "CRA-RBM Assistant API",
        "version": "0.2.0",
    }
