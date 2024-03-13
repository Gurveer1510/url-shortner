from fastapi import APIRouter, Query, Depends, status, HTTPException

from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter(tags=['redirect'])

@router.get("/find/")
def redirect(url: str = Query(...), db: Session = Depends(get_db)):

    url = db.query(models.Url).filter(models.Url.short_url == url).first()

    if url:
        destination_url = url.original_url
        print(destination_url)
        return {"url" : url.original_url}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
