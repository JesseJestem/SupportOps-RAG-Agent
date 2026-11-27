from supportops.schemas import ChatRequest, ChatResponse
from supportops.services.chat import ChatService


def test_generate_answer() -> None:
    chat_service = ChatService()
    request = ChatRequest(message="Hello")
    response = chat_service.generate_answer(request)

    assert isinstance(response, ChatResponse)
    assert response.answer == "Chat is not implemented yet."
    assert response.sources == []
