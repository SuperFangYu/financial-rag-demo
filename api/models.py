from pydantic import BaseModel

class AskRequest(BaseModel):
    company_name: str
    question: str

class AskResponse(BaseModel):
    answer: str

