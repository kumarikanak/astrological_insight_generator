from pydantic import BaseModel

class BirthInput(BaseModel):
    name: str
    birth_date: str   # YYYY-MM-DD
    birth_time: str   # HH:MM
    birth_place: str
    language: str = "en"

class InsightOutput(BaseModel):
    zodiac: str
    insight: str
    language: str
