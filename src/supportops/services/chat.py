from supportops.schemas import ChatRequest, ChatResponse


class ChatService:
    def generate_answer(self, request: ChatRequest) -> ChatResponse:
        response = ChatResponse(answer="Chat is not implemented yet.", sources=[])
        return response
