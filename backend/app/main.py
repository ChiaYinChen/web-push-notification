"""Main app."""
from fastapi import FastAPI

from .config import settings
from .endpoint import router

app = FastAPI()
app.include_router(router, prefix=settings.API_PREFIX)
