from fastapi import FastAPI
from datetime import datetime
from app.pydantic_models import BirthInput, InsightOutput
from app.get_zodiac_sign import get_zodiac, get_daily_rule
from app.zodiac_insight_generator import LLMClient
from app.cache import make_cache_key, get_cached, set_cache

app = FastAPI(title="Astrological Insight Generator")
llm = LLMClient()

@app.post("/insight", response_model=InsightOutput)
def get_insight(data: BirthInput):
    dt = datetime.strptime(data.birth_date, "%Y-%m-%d")
    sign = get_zodiac(dt.month, dt.day)

    cache_key = make_cache_key(data.name, data.birth_date, sign, data.language)
    cached = get_cached(cache_key)
    if cached:
        return InsightOutput(zodiac=sign, insight=cached, language=data.language)

    base_rule = get_daily_rule(sign)
    generated_insight = llm.generate(sign, base_rule, language=data.language)

    set_cache(cache_key, generated_insight)
    return InsightOutput(zodiac=sign, insight=generated_insight, language=data.language)
