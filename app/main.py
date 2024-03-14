from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .routers import input, redirect
from . import models

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)


app = FastAPI()

@app.get("/")
def greet():
    return {
        "message" : "hello user"
    }

app.include_router(input.router)
app.include_router(redirect.router)


