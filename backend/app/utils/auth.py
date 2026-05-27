from typing import Any, Dict, Optional

from fastapi import Header, HTTPException

from app.utils.supabase_client import get_supabase_client


def get_bearer_token(authorization: str | None) -> str:
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header is required",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Authorization header must use Bearer token",
        )

    return authorization.replace("Bearer ", "", 1).strip()


def require_authenticated_user(
    authorization: str | None = Header(default=None),
) -> Dict[str, Any]:
    token = get_bearer_token(authorization)
    supabase = get_supabase_client()

    try:
        response = supabase.auth.get_user(token)
    except Exception as exc:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token",
        ) from exc

    user = getattr(response, "user", None)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token",
        )

    return {
        "id": user.id,
        "email": user.email,
    }


def get_optional_authenticated_user(
    authorization: str | None = Header(default=None),
) -> Optional[Dict[str, Any]]:
    if not authorization:
        return None

    if not authorization.startswith("Bearer "):
        return None

    token = authorization.replace("Bearer ", "", 1).strip()
    supabase = get_supabase_client()

    try:
        response = supabase.auth.get_user(token)
    except Exception:
        return None

    user = getattr(response, "user", None)

    if not user:
        return None

    return {
        "id": user.id,
        "email": user.email,
    }
