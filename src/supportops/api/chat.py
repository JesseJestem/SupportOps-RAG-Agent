from fastapi import APIRouter

from supportops.schemas import ChatRequest, ChatResponse
from supportops.services.chat import ChatService

router = APIRouter(
    tags=["Chat"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    chat_service = ChatService()
    response = chat_service.generate_answer(request)
    return response
