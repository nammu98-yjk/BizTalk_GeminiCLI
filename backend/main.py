from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import convert

app = FastAPI(title="업무 말투 변환기 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(convert.router, prefix="/api")


@app.get("/health")
async def health():
    return {"status": "ok"}
