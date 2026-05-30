import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from prompts.templates import PROMPTS

load_dotenv(find_dotenv())

UPSTAGE_BASE_URL = "https://api.upstage.ai/v1"


def convert_tone(text: str, target_audience: str) -> str:
    api_key = os.getenv("UPSTAGE_API_KEY")
    if not api_key:
        raise RuntimeError("UPSTAGE_API_KEY가 설정되지 않았습니다.")

    client = OpenAI(api_key=api_key, base_url=UPSTAGE_BASE_URL)

    response = client.chat.completions.create(
        model="solar-pro2",
        messages=[
            {"role": "system", "content": PROMPTS[target_audience]},
            {"role": "user", "content": text},
        ],
    )

    return response.choices[0].message.content.strip()
