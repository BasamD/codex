from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from ..database.database import SessionLocal
from ..models import models
from ..schemas import schemas
from ..auth.auth import check_scope, get_current_token

router = APIRouter(prefix="/tickets", tags=["tickets"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Ticket])
async def list_tickets(db: Session = Depends(get_db), token=Depends(get_current_token)):
    query = db.query(models.Ticket)
    if 'external' in token['scopes']:
        query = query.filter(models.Ticket.customer_id == token.get('customer_id'))
    return query.all()

@router.post("/", response_model=schemas.Ticket)
async def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    db_ticket = models.Ticket(guid=str(uuid4()), **ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/{guid}", response_model=schemas.Ticket)
async def get_ticket(guid: str, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter_by(guid=guid).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.patch("/{guid}", response_model=schemas.Ticket)
async def update_ticket(guid: str, ticket: schemas.TicketUpdate, db: Session = Depends(get_db)):
    db_ticket = db.query(models.Ticket).filter_by(guid=guid).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    for key, value in ticket.dict(exclude_unset=True).items():
        setattr(db_ticket, key, value)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
