from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.database import SessionLocal
from ..models import models
from ..schemas import schemas

router = APIRouter(prefix="/history", tags=["history"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.History])
async def get_history(db: Session = Depends(get_db)):
    return db.query(models.History).all()
