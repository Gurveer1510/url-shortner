from fastapi import FastAPI
from .database import engine
from .routers import input
from . import models

app = FastAPI()

models.Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(input)


