from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints


class ChatRequest(BaseModel):
    message: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=1,
            max_length=2000,
        ),
    ]
    top_k: int = Field(default=5, ge=1, le=20, strict=True)


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
