import httpx
import os
from fastapi import APIRouter, HTTPException, Header
from fastapi.responses import Response

router = APIRouter(prefix="/api/konect", tags=["konect"])

KONECT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/153.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://lms.konect.or.kr/web/index.do",
}

KONECT_FALLBACK_TOKEN = os.getenv("KONECT_FALLBACK_TOKEN")


@router.get("/probe")
async def konect_probe():
    url = "https://lms.konect.or.kr/web/index.do"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://lms.konect.or.kr/web/index.do",
    }

    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=15.0,
    ) as client:
        response = await client.get(
            url,
            headers=headers,
        )

    return {
        "status": response.status_code,
        "finalUrl": str(response.url),
        "bodyPreview": response.text[:300],
    }


@router.get("/fetch")
async def fetch_konect(
    url: str,
    x_internal_token: str | None = Header(default=None),
):
    if x_internal_token != KONECT_FALLBACK_TOKEN:
        raise HTTPException(status_code=401)

    if not url.startswith("https://lms.konect.or.kr/"):
        raise HTTPException(
            status_code=400,
            detail="Invalid target URL",
        )

    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=20.0,
    ) as client:
        response = await client.get(
            url,
            headers=KONECT_HEADERS,
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get(
            "content-type",
            "text/html",
        ),
    )
