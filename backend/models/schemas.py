from pydantic import BaseModel, field_validator


class ConvertRequest(BaseModel):
    text: str
    target_audience: str  # boss / colleague / client / team

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("text 필드는 필수입니다.")
        return v

    @field_validator("target_audience")
    @classmethod
    def audience_must_be_valid(cls, v: str) -> str:
        allowed = {"boss", "colleague", "client", "team"}
        if v not in allowed:
            raise ValueError(f"target_audience는 {allowed} 중 하나여야 합니다.")
        return v


class ConvertResponse(BaseModel):
    converted_text: str
    target_audience: str
    original_text: str
