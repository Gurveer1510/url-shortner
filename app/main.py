from fastapi import FastAPI, status, HTTPException, Depends, Query
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import engine, get_db
from typing import Dict
import random
import string
from . import models

app = FastAPI()

models.Base.metadata.create_all(engine)


app = FastAPI()

def generate_random_key():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(6))


@app.post("/input/", status_code=status.HTTP_201_CREATED)
def get_url(long_url: str = Query(...), db: Session = Depends(get_db)):
    # print(generate_random_key())
    short_key = generate_random_key()
    new_entry = models.Url(original_url=long_url, short_url=short_key)
    db.add(new_entry)
    db.commit()

    return {"short_url": short_key}


@app.get("/find/")
def redirect(url: str = Query(...), db: Session = Depends(get_db)):

    url = db.query(models.Url).filter(models.Url.short_url == url).first()

    if url:
        destination_url = url.original_url
        print(destination_url)
        return {"url" : url.original_url}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
