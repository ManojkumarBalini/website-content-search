from pydantic import BaseModel

class SearchResult(BaseModel):
    content: str
    match_score: float
    path: str