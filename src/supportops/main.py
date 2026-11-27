from fastapi import FastAPI

from supportops.api.chat import router as chat_router
from supportops.api.health import router as health_router

app = FastAPI(
    title="SupportOps RAG Agent",
)


app.include_router(health_router)
app.include_router(chat_router)
