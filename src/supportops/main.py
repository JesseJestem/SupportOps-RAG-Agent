from fastapi import FastAPI

from supportops.schemas import ChatRequest, ChatResponse

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    response = ChatResponse(answer="Chat is not implemented yet.", sources=[])
    return response
