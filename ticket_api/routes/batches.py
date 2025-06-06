from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import SessionLocal
from ..models import models
from ..schemas import schemas
from ..auth.auth import check_scope

router = APIRouter(prefix="/batches", tags=["batches"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Batch, dependencies=[Depends(check_scope("internal"))])
async def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    db_batch = models.Batch(description=batch.description)
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch

@router.patch("/{batch_id}", response_model=schemas.Batch, dependencies=[Depends(check_scope("internal"))])
async def update_batch(batch_id: int, batch: schemas.BatchUpdate, db: Session = Depends(get_db)):
    db_batch = db.get(models.Batch, batch_id)
    if not db_batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    for key, value in batch.dict(exclude_unset=True).items():
        setattr(db_batch, key, value)
    db.commit()
    db.refresh(db_batch)
    return db_batch
