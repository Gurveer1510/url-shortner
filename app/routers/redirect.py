from fastapi import APIRouter, Query, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .. import models
from fastapi import Body
from ..database import get_db

router = APIRouter(tags=['redirect'])

@router.get("/{url}")
async def redirect(url, db: Session = Depends(get_db)):

    url = db.query(models.Url).filter(models.Url.short_url == url).first()

    if url:
        destination_url = url.original_url
        return RedirectResponse(destination_url)
        

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
