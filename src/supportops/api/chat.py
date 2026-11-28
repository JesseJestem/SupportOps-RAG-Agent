from typing import Annotated

from fastapi import APIRouter, Depends

from supportops.api.dependencies import get_chat_service
from supportops.schemas import ChatRequest, ChatResponse
from supportops.services.chat import ChatService

router = APIRouter(
    tags=["Chat"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest, chat_service: Annotated[ChatService, Depends(get_chat_service)]
) -> ChatResponse:
    response = chat_service.generate_answer(request)
    return response
