from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.engine import engine
from src.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
