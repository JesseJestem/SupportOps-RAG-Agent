import pytest
from fastapi.testclient import TestClient

from supportops.api.dependencies import get_chat_service
from supportops.main import app
from supportops.schemas import ChatRequest, ChatResponse
from supportops.services.chat import ChatService


class StubChatService(ChatService):
    def generate_answer(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(answer=f"Test answer: {request.message}", sources=["test-document.md"])


@pytest.mark.parametrize(
    "payload,expected_status",
    [
        ({"message": "Hello"}, 200),
        ({"message": "Hello", "top_k": 1}, 200),
        ({"message": "Hello", "top_k": 20}, 200),
        ({"message": ""}, 422),
        ({"message": None}, 422),
        ({"message": "   "}, 422),
        ({"message": 123}, 422),
        ({"message": "A" * 2001}, 422),
        ({"message": "Hello", "top_k": 0}, 422),
        ({"message": "Hello", "top_k": 21}, 422),
        ({"message": "Hello", "top_k": "5"}, 422),
        ({"message": "Hello", "top_k": True}, 422),
        ({}, 422),
        ({"message": "A"}, 200),
        ({"message": "A" * 2000}, 200),
    ],
)
def test_chat_status_code(
    client: TestClient, payload: dict[str, object], expected_status: int
) -> None:
    response = client.post("/chat", json=payload)
    assert response.status_code == expected_status


def test_chat_response(client: TestClient) -> None:
    response = client.post("/chat", json={"message": "Hello", "top_k": 1})
    assert response.status_code == 200
    assert response.json() == {"answer": "Chat is not implemented yet.", "sources": []}


def test_chat_request_default_top_k() -> None:
    request = ChatRequest(message="Hello")
    assert request.top_k == 5


def test_chat_request_strip_whitespace() -> None:
    request = ChatRequest(message="   Hello World   ")
    assert request.message == "Hello World"


def test_chat_dependency_override(client: TestClient) -> None:
    def get_stub_chat_service() -> ChatService:
        return StubChatService()

    try:
        app.dependency_overrides[get_chat_service] = get_stub_chat_service
        response = client.post("/chat", json={"message": "   Hello   ", "top_k": 3})

        assert response.status_code == 200
        assert response.json() == {"answer": "Test answer: Hello", "sources": ["test-document.md"]}

    finally:
        app.dependency_overrides.pop(get_chat_service, None)
