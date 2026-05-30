from fastapi import APIRouter, HTTPException

from models.schemas import ConvertRequest, ConvertResponse
from services.tone_converter import convert_tone

router = APIRouter()


@router.post("/convert", response_model=ConvertResponse)
async def convert(request: ConvertRequest):
    try:
        converted = convert_tone(request.text, request.target_audience)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="LLM API 호출 중 오류가 발생했습니다.")

    return ConvertResponse(
        converted_text=converted,
        target_audience=request.target_audience,
        original_text=request.text,
    )
