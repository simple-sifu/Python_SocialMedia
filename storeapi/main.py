from contextlib import asynccontextmanager

from fastapi import FastAPI

from storeapi.database import database
from storeapi.routers.post import router as post_router


# a context manager is a function that does setup and teardown
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    # doesnt run until application terminates
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
  
app.include_router(post_router)