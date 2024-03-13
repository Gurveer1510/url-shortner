from fastapi import APIRouter, Query, Depends, status
from ..utilities.generate_random_string import generate_random_key
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db


router = APIRouter(tags=['input'])

@router.post("/input/", status_code=status.HTTP_201_CREATED)
def get_url(long_url: str = Query(...), db: Session = Depends(get_db)):
    # print(generate_random_key())
    short_key = generate_random_key()
    new_entry = models.Url(original_url=long_url, short_url=short_key)
    db.add(new_entry)
    db.commit()

    return {"short_url": short_key}

