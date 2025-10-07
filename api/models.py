from pydantic import BaseModel
from typing import Literal

class AskRequest(BaseModel):
    company_name: str
    question: str

class AskResponse(BaseModel):
    answer: str
    #source: Literal["financial", "news"]
