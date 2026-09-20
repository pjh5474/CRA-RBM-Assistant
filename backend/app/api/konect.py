import httpx
from fastapi import APIRouter

router = APIRouter(prefix="/api/konect", tags=["konect"])

@router.get("/probe")
async def konect_probe():
    url = "https://lms.konect.or.kr/web/index.do"

    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/153.0.0.0 Safari/537.36",
        "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":
            "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer":
            "https://lms.konect.or.kr/web/index.do",
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